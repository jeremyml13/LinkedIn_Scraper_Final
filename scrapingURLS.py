import requests
from bs4 import BeautifulSoup
import time


# Given url to the LinkedIn job board containing "Sales Development Representative" roles, return the job board HTML content
def linkedin_url_to_HTML_soup(url):
    response = requests.get(url)
    list_data = response.text
    jobs_soup = BeautifulSoup(list_data, "html.parser")
    return jobs_soup


# Given a job board soup, locate all instances of where the URLs to the companies' homepages are located
def scrape_linkedin_job_listings(jobs_soup):
    jobs_list = jobs_soup.find_all("li")
    return jobs_list


# Given a jobs list in the HTML content, return the URLs to the companies' homepages
def scraped_jobs_to_company_homepage_urls(jobs_list):
    list_company_homepage_urls = []
    for job in jobs_list:
        job_page_division = job.find("a", {"class": "hidden-nested-link"})
        job_page_url = job_page_division.get("href")
        list_company_homepage_urls.append(job_page_url)
    return list_company_homepage_urls


if __name__ == '__main__':
    #driver = setup_driver()
    url = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=sales%2Bdevelopment%2Brepresentative&location=&geoId=&trk=public_jobs_jobs-search-bar_search-submit&start=0"
    jobs_soup = linkedin_url_to_HTML_soup(url)
    jobs_list = scrape_linkedin_job_listings(jobs_soup)
    list_company_homepage_urls = scraped_jobs_to_company_homepage_urls(jobs_list)
    #list_all_company_jobs_urls = company_homepage_urls_to_all_company_jobs_page_urls(list_company_homepage_urls)
    #print(list_all_company_jobs_urls)
    #driver.quit()  # Make sure to quit the driver after the scraping is done
