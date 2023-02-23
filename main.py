import requests
from bs4 import BeautifulSoup
import json
from fake_headers import Headers
from pprint import pprint




if __name__ in '__main__':
    headers = Headers(os= 'win', browser= 'chrome')

    page_number = 0
    main_url = f'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2&page={page_number}&disableBrowserCache=true'
    response = requests.get(main_url, headers= headers.generate())
    soup = BeautifulSoup(response.text, 'html.parser')
    vacancies_all = soup.find('div', id = 'a11y-main-content').find_all('div', class_='vacancy-serp-item__layout')
    # print(vacancies_all)

    needed_vacancies = []
    for vacancy in vacancies_all:
        vacancy_text = vacancy.find(('div'), class_ = 'g-user-content').text
        if ('django' or 'flask') in vacancy_text.lower():
            needed_vacancies.append(vacancy)

    # print(needed_vacancies)


    data ={}
    data['vacancy'] = []
    for vacancy in needed_vacancies:
        for town in vacancy:
            x = vacancy.find_all('div', class_='bloko-text')
        data['vacancy'].append({
            'link': vacancy.find('a', class_ = 'serp-item__title')['href'],
            'salary': vacancy.find('span', class_='bloko-header-section-3').text.replace(u"\u202F", " "),
            'company': vacancy.find('div', class_='vacancy-serp-item__meta-info-company').find('a').text,
            'town':x[1].text
            })

    with open('data.txt', 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile)

    with open('data.txt') as json_file:
        data = json.load(json_file)
        pprint(data)

