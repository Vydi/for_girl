def parser_fun():
    import requests
    from bs4 import BeautifulSoup

    url = 'https://mysekret.ru/komplimenty/korotkie-komplimenty-devushke-150-fraz-kotorye-mozhno-napisat-v-sms-pod-foto-v-kommentarii.html'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('ul', class_='subb')
    all_compliment = []
    for i in quotes:
        for p in i.findAll('li'):
            all_compliment.append(p.text)

    return all_compliment



