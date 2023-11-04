from bs4 import BeautifulSoup
import requests

def find_jobs():
    html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text

    soup = BeautifulSoup(html_text, "lxml")


    job_cards = soup.find_all("li", class_ = "clearfix job-bx wht-shd-bx")
    job_count = 0

    for job_card in job_cards:
        company_name = job_card.header.h3.text.strip()
        job_location = job_card.find("ul", class_ = "top-jd-dtl clearfix").span.text
        job_experience = job_card.find("ul", class_ = "top-jd-dtl clearfix").li.find(string=True, recursive=False)
        skills = set(job_card.find("span", class_ = "srp-skills").text.strip().replace(" ","").split(","))
        if unknown_skill not in skills:
            job_count += 1
            print(f'Company: {company_name}')
            print(f'Location: {job_location}')
            print(f'Experience: {job_experience}')
            print(f'Skills: {skills}')
            print('\n')
    print(f'No. of jobs found: {job_count}')

if __name__ == "__main__":
    print("Python developer jobs from Times Jobs")
    unknown_skill = str(input("Enter skill you're not familiar with > ")).strip().lower()
    print("Filtering out jobs..")
    print('\n')

    find_jobs()
