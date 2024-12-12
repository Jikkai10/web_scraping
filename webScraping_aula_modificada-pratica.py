from bs4 import BeautifulSoup
import requests
import time


print('Put some skill that you are not familiar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
    #pega as informações do site
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=Python&txtLocation=').text

    #separa as informações
    soup = BeautifulSoup(html_text, 'lxml')

    #encontra os cards de trabalhos
    #estão dentro da tag li de classe 'clearfix job-bx wht-shd-bx'
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

    #itera sobre cada trrabalho
    for index, job in enumerate(jobs):
        #pega a data de publicação
        published_date = job.find('span', class_ = 'sim-posted').span.text
        #só mostra trabalhos publicados a poucos dias
        if 'few' in published_date:
            #pega o nome da companhia
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '').replace('\n', '').replace('	', '')

            #pega as habilidades requeridas
            skills = job.find('div', class_ = 'more-skills-sections')
            skills_name = skills.find_all('span')
            
            #pega o link de mais informações
            more_info = job.a['href']
            x = 0
            
            #procura se tem a habilidade não familiar
            #se tiver vai para o proximo trabalho
            for name in skills_name:
                if unfamiliar_skill in name.text:
                    x = 1
            if x == 1:
                x = 0
                continue
            
            #abrre o arquivo para escrever
            with open(f'posts/{index}.txt', 'w') as f:
                f.write(f'Company name: {company_name.strip()}, \n') 
                f.write('Required Skills: ')
                #itera sobre cada habilidade
                for name in skills_name:
                    f.write(name.text.replace(" ", '').replace('\n', '').replace('	', '').strip())
                    f.write(', ')
                f.write(f'\nMore info: {more_info}')
                print(f'File saved: {index}')


#função é chamada caso arquivo seja executado como main
if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait*60)