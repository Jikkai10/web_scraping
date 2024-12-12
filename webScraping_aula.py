from bs4 import BeautifulSoup

 
with open('home.html', 'r') as html_file: #abre o arquivo para leitura
    content = html_file.read() #guarda as informações do arquivo
    
    soup = BeautifulSoup(content, 'lxml') #separa as informações
    courses_cards = soup.find_all('div', class_='card') #procura todas as divs da classe card
    # escreve os preços dos cursos
    for course in courses_cards:
        course_name = course.h5.text #pega a tag h5 dentro das divs
        course_price = course.a.text.split()[-1] #pega o ultimo elemento da tag a das divs
        
        print(f'{course_name} costs {course_price}')
   


