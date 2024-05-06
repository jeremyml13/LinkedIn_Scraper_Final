from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import requests

# Given a company jobs page url, return all the URLS of the jobs offered by that company
def company_jobs_page_to_company_jobs_urls(company_jobs_page_url):
    response = requests.get(company_jobs_page_url)
    html_content = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all <a> tags with the specified class
    links = soup.find_all('a', class_="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2]")

    # Extract the href attributes from each link
    company_jobs_urls = [link['href'] for link in links if 'href' in link.attrs]

    return company_jobs_urls


if __name__ == '__main__':
    url = "https://www.linkedin.com/jobs/runwise-jobs-worldwide?f_C=4367317&trk=top-card_top-card-primary-button-top-card-primary-cta&position=1&pageNum=0"
    all_links = company_jobs_page_to_company_jobs_urls(url)
    print(all_links)