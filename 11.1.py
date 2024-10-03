# ыберите одну или несколько сторонних библиотек Python, например, requests, pandas, numpy, matplotlib, pillow.
# После выбора библиотек(-и) изучите документацию к ней(ним), ознакомьтесь с их основными возможностями и функциями.
# К каждой библиотеке дана ссылка на документацию ниже.
# Если вы выбрали:
# requests - запросить данные с сайта и вывести их в консоль.
# pandas - считать данные из файла, выполнить простой анализ данных (на своё усмотрение) и вывести результаты в консоль.
# numpy - создать массив чисел, выполнить математические операции с массивом и вывести результаты в консоль.
# matplotlib - визуализировать данные с помощью библиотеки любым удобным для вас инструментом из библиотеки.
# pillow - обработать изображение, например, изменить его размер, применить эффекты и сохранить в другой формат.
# В приложении к ссылке на GitHub напишите комментарий о возможностях, которые предоставила вам выбранная библиотека и
# как вы расширили возможности Python с её помощью.
import requests
# делает запрос
r = requests.get('https://api.github.com/events')
r.status_code
# сообщает статус в кодах, где 200 - выполнено, 404 - нет (есть и другие кода: 204 NO CONTENT и 304 NOT MODIFIED)
if r.status_code == 200:
    print('Success!')
elif r.status_code == 404:
    print('Not Found.')
# для автоматической отправки
re = requests.post('https://avatars.mds.yandex.net/i?id=4f7586d49edaa427e07a8819562fc284_l-5248434-images-thumbs&n=13')
print(re)
#возможность работы с куки-файлами
url = 'https://yandex.ru/images/search?img_url=https%3A%2F%2Fwww.tapeciarnia.pl%2Ftapety%2Fnormalne%2F253304_gory_jezioro_swierki_swiatlo_cien_odbicie.jpg&lr=213&pos=0&rpt=simage&source=serp&text=картинка'
cookies = {'visit': 'oktober'}
req = requests.get(url, cookies=cookies)
print(req)
