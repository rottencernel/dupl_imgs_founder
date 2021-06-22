import os
import cv2
import imghdr
import numpy as np


def compare_images(directory, show_images=True, similarrity='high', compression=50):
    # Список, куда  добавляются дублирующие/похожие изображения
    duplicates = []
    global lower_res
    lower_res = []

    imgs_matrix = create_imgs_matrix(directory, compression)

    # ищем похожие изображения
    if similarrity == 'low':
        ref = 1000
    # Ищем изображения дублирующие друг друга 1в1
    else:
        ref = 200

    main_img = 0
    compared_img = 1
    nrows, ncols = compression, compression
    srow_A = 0
    erow_A = nrows
    srow_B = erow_A
    erow_B = srow_B + nrows

    while erow_B <= imgs_matrix.shape[0]:
        while compared_img < (len(image_files)):
            # Выбераем два изображения из imgs_matrix
            imgA = imgs_matrix[srow_A : erow_A, # ряды
                                0     : ncols]  # колонны
            imgB = imgs_matrix[srow_B : erow_B, # ряды
                                0     : ncols]  # колонны

            # Сравниваем изображения
            rotation = 0
            while image_files[main_img] not in duplicates and rotation <= 3:
                if rotation != 0:
                    imgB = rotate_img(imgB)
                err = mse(imgA, imgB)
                if err < ref:
                    if show_images == True:
                        show_file_info(compared_img, main_img)
                        add_to_delllist(image_files[main_img], duplicates)
                        check_img_quality(directory, image_files[main_img], image_files[compared_img], lower_res)
                rotation += 1
            srow_B += nrows
            erow_B += nrows
            compared_img += 1
        
        srow_A += nrows
        erow_A += nrows
        srow_B = erow_A
        erow_B = srow_B + nrows
        main_img += 1
        compared_img = main_img + 1
        
    global msg
    msg = 'Готово друг, найдено' + ' ' + str(len(duplicates)) + ' пар дубликатов из ' + str(len(image_files)) + '!'

    return set(lower_res)


# Ищет изображение в папке и создает тензор
def create_imgs_matrix(directory, compression):
    global image_files
    image_files = []
    # Создаем список всех файлов в папке
    folder_files = [filename for filename in os.listdir(directory)]

    # Создаем матрицу изображения
    counter = 0
    for filename in folder_files:
        # Проверяем доступен ли файл и является ли он изображением
        if not os.path.isdir(directory + filename) and imghdr.what(directory + filename):
            # Декодируем изображение и создаем матрицу
            img = cv2.imdecode(np.fromfile(directory + filename, dtype = np.uint8), cv2.IMREAD_UNCHANGED)
            if type(img) == np.ndarray:
                img = img[..., 0:3]
                # Меняем размер изображения на основе задонной в аргументе функции компрессии
                img = cv2.resize(img, dsize=(compression, compression), interpolation=cv2.INTER_CUBIC)
                if counter == 0:
                    imgs_matrix = img
                    image_files.append(filename)
                    counter += 1
                else:
                    imgs_matrix = np.concatenate((imgs_matrix, img))
                    image_files.append(filename)
        
    return imgs_matrix

# Считаем среднеквадратичное откланение(MSE) между матрицами двух изображений
def mse(imageA, imageB):
    err = np.sum((imageA.astype('float') - imageB.astype('float')) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    return err


# Разворачиваем изображение на 90 градусов
def rotate_img(image):
    image = np.rot90(image, k=1, axes=(0, 1))
    return image


def show_file_info(compared_img, main_img):
    return f'Дублирующие файлы: { image_files[main_img] }  и  {image_files[compared_img]}'


# Добавляем элемент в список для удаления
def add_to_delllist(filename, list):
    list.append(filename)


# Проверяем качество изображения сравниваемых изображенийю.
#  Файл меньшего размера будет добавлен в отдельный список
def check_img_quality(directory, imageA, imageB, list):
    size_imgA = os.stat(directory + imageA).st_size
    size_imgB = os.stat(directory + imageB).st_size

    if size_imgA > size_imgB:
        add_to_delllist(imageB, list)
    else:
        add_to_delllist(imageA, list)
