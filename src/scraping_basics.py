from bs4 import BeautifulSoup


def run_scrapping_basics():

    with open("src/home.html", "r") as html_file:
        content = html_file.read()

        soup = BeautifulSoup(content, 'lxml')

        def ex1():
            courses_html_tags = soup.find_all('h5')
            courses = [course_tag.text for course_tag in courses_html_tags]
            print(courses)

        # ex1()

        def ex2():
            course_cards = soup.find_all('div', class_='card')
            for course_card in course_cards:
                course_name = course_card.h5.text
                course_price = course_card.a.text.split()[-1]
                print(f'"{course_name}" costs {course_price}')

        # ex2()

        def ex3():
            card = soup.find('div', id='card-python-web-development')
            print(card)
        ex3()


if __name__ == '__main__':
    run_scrapping_basics()
