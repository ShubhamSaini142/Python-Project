from bs4 import BeautifulSoup
import requests
import time

print('Enter some skill you are not familiar with')
unfamiliar_skill = input('>')
print('Filtering Out', unfamiliar_skill)
# program start


def find_jobs():
    url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='
    reponse = requests.get(url)
    html_text = reponse.content
    soup = BeautifulSoup(html_text, "lxml")
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text
            skills = job.find(
                'span', class_='srp-skills').text.replace(' ', '')
            More_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'push/{index}.txt', 'w') as f:
                    f.write(f"Company Name : {company_name.strip()}\n")
                    f.write(f"Required Skills : {skills.strip()}\n")
                    f.write(f"More Info : {More_info}\n")
                print("File Saved", index)


if __name__ == '__main__':
    while True:
        find_jobs()
        wait_time = 5
        print("Waiting for", wait_time*60, "minutes...")
        time.sleep(wait_time*60)
