import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# Given a company homepage URL, return the HTML content of the homepage
def get_company_page_soup(company_homepage_url):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # Load the page
    driver.get(company_homepage_url)

    html_content = driver.page_source
    driver.quit()

    company_page_soup = BeautifulSoup(html_content, 'html.parser')

    return company_page_soup

# From a company page soup, return the company name
def get_company_name(company_page_soup):
    company_text = company_page_soup.select_one('#main-content > section:nth-of-type(1) > section > div > div:nth-of-type(2) > div:nth-of-type(1) > h1').text
    company_name = company_text.strip()
    return company_name

# From a company page soup, return the company description
def get_company_description(company_page_soup):
    company_description = company_page_soup.select_one('main > section:nth-of-type(1) > div > section:nth-of-type(1) > div > p').text
    return company_description

# From a company page soup, return the url to the page containing all company jobs
def company_page_soup_to_all_company_jobs_url(company_page_soup):
    # Using CSS selector to find the link
    company_jobs_url_element = company_page_soup.select_one(
        'main section > section > div > div:nth-of-type(2) > div:nth-of-type(1) > div > a:nth-of-type(1)')

    if company_jobs_url_element:
        company_jobs_url = company_jobs_url_element.get('href')
        return company_jobs_url
    else:
        error = "Job page not found"
        return error

if __name__ == '__main__':
    company_homepage_url = "https://www.linkedin.com/company/wearerunwise?trk=public_jobs_jserp-result_job-search-card-subtitle"
    company_page_soup = get_company_page_soup(company_homepage_url)
    company_name = get_company_name(company_page_soup)
    company_description = get_company_description(company_page_soup)
    print(company_name)
    print(company_description)