import bs4
import time
from gravador import gravador_csv
from selenium.common.exceptions import NoSuchElementException

posts = []
post = input('Insira os ID\'s das postagens: ')
posts.append(post)
while post != '':
    post = input('Mais um?: ')
    posts.append(post)

del posts[-1]

url_template = 'https://mbasic.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier={}'


def scraper_likers(driver):
    for p in posts:
        nomes = []
        links = []
        url = url_template.format(p)
        driver.get(url)
        while True:
            try:
                source = driver.page_source
                soup = bs4.BeautifulSoup(source, "lxml")
                limpa_link = ['/a/', '/ufi', '/story.php?', '/home.php?']
                for link in soup.findAll('a'):
                    if link.get('href').startswith(tuple(limpa_link)):
                        pass
                    else:
                        print('https://www.facebook.com{}'.format(link.get('href')), ';', link.string)
                        nomes.append(link.string)
                        links.append('https://www.facebook.com{}'.format(link.get('href')))
                time.sleep(3)
                driver.find_element_by_xpath("//*[contains(text(), 'Ver mais')]").click()
            except NoSuchElementException:
                print('\nAcabou a coleta!')
                col = "\n".join("{};{}".format(x, y) for x, y in zip(nomes, links))
                print(col)
                arquivo = input('Insira um nome para o arquivo: ')
                gravador_csv(col, arquivo)
                break
        time.sleep(5)




# TODO coletar as reações
'''
def scraper_likers(driver):
        for p in posts:
            
            url = url_template.format(p)
            driver.get(url)
            while True:
                try:
                    source = driver.page_source
                    soup = bs4.BeautifulSoup(source, "lxml")
                    print("\n".join([img['alt'] for img in soup.find_all('img', alt=True)]))
                    time.sleep(3)
                    driver.find_element_by_xpath("//*[contains(text(), 'Ver mais')]").click()
                except NoSuchElementException:
                    print('\nAcabou a coleta!')

                    break
            time.sleep(5)
'''