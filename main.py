import requests
from bs4 import BeautifulSoup as BS
import csv

def get_html(url):
    response = requests.get(url)
    return response.text

def main():
    try:
        for i in range(1, 10000):

            BASE_URL = f'https://www.mashina.kg/search/all/{i}'
            html = get_html(BASE_URL)
            soup = get_soup(html)
            get_data(soup)
            
            
    except: 
        print('Конец. Это была послеедняя страница')

def get_soup(html):
    soup = BS(html, 'html.parser')
    return soup


def get_data(soup):
    

    catalog = soup.find('div', class_='search-results-table')
    cars = catalog.find_all('div', class_='list-item list-label')
    
    for car in cars:
        title = car.find('h2', class_='name').text.strip().replace('\n', '')
        

        price = car.find('div', class_='block price').text.replace(' ', '').replace('\n', '')
        
        image = car.find('img', class_='lazy-image').get('data-src').replace('\n', '')
        
        descriptoin = car.find('div', class_='block info-wrapper item-info-wrapper').text.replace(' ', '').replace('\n', '')
        
        
        
        write_csv({
            'title': title,
            'image': image,
            'price': price,
            'description': descriptoin
            })
             
        
def write_csv(data):
    with open('cars.csv', 'a') as file:
        names = ['title', 'price', 'image', 'description']
        write = csv.DictWriter(file, delimiter=',', fieldnames=names)
        write.writerow(data)


if __name__ == '__main__':
    main()
