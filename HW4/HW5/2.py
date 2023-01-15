#  Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах.
# Алгоритм RLE

# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'

# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ

# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ

# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q



import re


def compression(inform):
    compres_inform = ''
    i = 0
    while i <= len(inform)-1:
        if inform[i] != '\n':
            count_simbol = 1
            for j in range(i+1, len(inform)):
                if inform[j] == inform[i]:
                    count_simbol += 1
                else:
                    break
            compres_inform += str(count_simbol) + inform[i]
            i = i + int(count_simbol)
        else:
            compres_inform += '\n'
            break
    return compres_inform


def decompression(inform):
    decompres_inform = ''
    cal = re.findall(r'\d+', inform)
    for i in range(len(cal)):
        num_str = inform.find(cal[i])
        n = len(cal[i])
        for j in range(0, int(cal[i])):
            decompres_inform += inform[num_str+n]
    decompres_inform += '\n'
    return decompres_inform


# Архивация данных из одного файла , запись в архивный файл
with open('text_start.txt', "r") as f1:
    some_text = f1.readlines()
    compress_text = []
    for i in range(len(some_text)):
        compress_text.append(compression(some_text[i]))
with open("text_compres.txt", "w") as f2:
    f2.writelines(compress_text)


# Разархивация архивного файла текста в новый разорхивированный файл
with open("text_compres.txt", "r") as f3:
    some_detext = f3.readlines()
    decompress_text = []
    for i in range(len(some_detext)):
        decompress_text.append(decompression(some_detext[i]))
with open("text_decompress.txt", "w") as f4:
    f4.writelines(decompress_text)