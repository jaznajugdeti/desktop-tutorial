# Напишите функцию-генератор all_variants(text), которая принимает строку text
# и возвращает объект-генератор, при каждой итерации которого будет возвращаться
# подпоследовательности переданной строки.
def all_variants(text):
    for x in range(len(text)):
        for y in range(x + 1, len(text) + 1):
            yield text[x:y]


a = all_variants("abc")
for i in a:
    print(i)


    # for l in range(len(text)):
    #     for r in range(l, len(text)):
    #         yield text[l:r + 1]
    # for j in text:
    #     yield j
# так выводят подпоследовательность но только по буквам а не по всем вариантам


# а еще так !!!!!!!!!
# x = 0
#     y = 0
#     for x in range(len(text)):
#         for y in range(x + 1, len(text) + 1):
#             yield text[x:y]
# Пункты задачи:
# Напишите функцию-генератор all_variants(text).
# Опишите логику работы внутри функции all_variants.
# Вызовите функцию all_variants и выполните итерации.
# Пример результата выполнения программы:
# Пример работы функции:
# a = all_variants("abc")
# for i in a:
# print(i)
# Вывод на консоль:
# a
# b
# c
# ab
# bc
# abc
#
# Примечания:
# Для функции генератора используйте оператор yield.
