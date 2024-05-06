import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import getNumbersFromString

from selenium import webdriver
from bs4 import BeautifulSoup

# Given a job at a company, return the HTML content of the page
def get_job_page_soup(company_job_url):
    # Set up WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(company_job_url)

    try:
        show_more_button = driver.find_element(By.CLASS_NAME, "show-more-less-html__button--more")
        show_more_button.click()  # click on the "See More" information button to access the rest of the HTML content

        html_content = driver.page_source
        job_page_soup = BeautifulSoup(html_content, 'html.parser')
    finally:
        driver.quit()
    return job_page_soup


# Given a job page soup, return the job description text
def get_job_page_description_text(job_page_soup):
    result = ""
    elements = job_page_soup.find_all(class_="show-more-less-html__markup relative overflow-hidden")
    texts = [element.get_text(separator=" ", strip=True) for element in elements]

    # Output or process the text data
    for text in texts:
        result += text
    return result


# Given a job page soup, return the job name
def get_job_name(job_page_soup):
    element = job_page_soup.select_one(
        'h1.top-card-layout__title.font-sans.text-lg.papabear\\:text-xl.font-bold.leading-open.text-color-text.mb-0.topcard__title')
    name = element.text if element else 'Element not found'
    return name


# Given a job page soup, return the job location
def get_job_location(job_page_soup):
    element = job_page_soup.select_one('span.topcard__flavor.topcard__flavor--bullet')
    location = element.text if element else 'Element not found'
    return location.strip()


# Given a job page soup, return the string that contains the salary range
def get_job_salary_string(job_page_soup):
    job_salary_string = "NA"
    salary_div = job_page_soup.find('div', class_='salary compensation__salary')
    if salary_div:
        job_salary_string = salary_div.text.strip()
    else:
        text = get_job_page_description_text(job_page_soup)
        start_index = 0
        while True:
            dollar_index = text.find('$', start_index)  # salaries start with a $ sign
            if dollar_index == -1:
                break  # No more dollar signs found
            # Check if 'm' is within the next 4 characters of the dollar sign or if '.' is within three characters of the dollar sign -
            # this guards against $70m (amount raised from funding) and $20.00/hr (usually yearly compensation is given after this)
            if 'm' in text[dollar_index + 1:dollar_index + 5] or '.' in text[dollar_index + 1:dollar_index+4]:
                start_index = dollar_index + 1  # Move start index just past this dollar sign
                continue  # Skip to the next dollar sign

            # If 'm' is not found, process this valid dollar sign
            end_index = min(dollar_index + 21, len(text))  # obtain a chunk of text right after the desired '$' sign
            job_salary_string = text[dollar_index:end_index]
            break  # Exit after processing the first valid dollar sign

    return job_salary_string

# Given a string that contains the salary, parse the string to return the salary value
def get_job_salary_value(job_salary_string):
    if job_salary_string != "NA":
        job_salary_value = getNumbersFromString.extract_numbers(job_salary_string)  # extract the salary range from the string
        if len(job_salary_value) == 1:
            job_salary_value = job_salary_value[0]
            if job_salary_value < 10000:  # if the salary is less than $10000 (generally a legitmate salary will be more than $1000)
                job_salary_value = "NA"
                return job_salary_value
            else:
                return job_salary_value
        elif len(job_salary_value) == 2:  # if the salary has two values (i.e. a range)
            job_salary_value = (job_salary_value[0] + job_salary_value[1]) / 2  # find the average of the two numbers
            print(job_salary_value)
            if job_salary_value < 10000:
                job_salary_value = "NA"
                return job_salary_value
            else:
                return job_salary_value
        return job_salary_string
    else:
        return job_salary_string


if __name__ == '__main__':
    #url = "https://www.linkedin.com/jobs/view/sales-development-representative-at-runwise-3720966634?position=1&pageNum=0&refId=NlA7XPgUwUIh3cmiGCgRpA%3D%3D&trackingId=PklYAUgESSwMHk5mLYduCA%3D%3D&trk=public_jobs_jserp-result_search-card"
    #url = "https://www.linkedin.com/jobs/view/sales-development-representative-at-flowhub-3837578556?position=1&pageNum=0&refId=%2FquFMxaDHyanbqEW2XlB1g%3D%3D&trackingId=l7ze%2FJlr2lpnFFNNndxM0A%3D%3D&trk=public_jobs_jserp-result_search-card"
    url = "https://www.linkedin.com/jobs/view/sales-development-representative-at-assembled-3825239866?position=1&pageNum=0&refId=urzzSd1hxuOQTMRSMVRf7Q%3D%3D&trackingId=kVcld%2FdV3ltWiaCYlxvI6w%3D%3D&trk=public_jobs_jserp-result_search-card"
    soup = get_job_page_soup(url)
    name = get_job_name(soup)
    print(name)
    #location = get_job_location(soup)
    #print(location)
    salary_string = get_job_salary_string(soup)
    print(salary_string)
    salary_value = get_job_salary_value(salary_string)
    print("Salary Value: ", salary_value)
    #description = get_job_page_description_text(soup)
    #print(description)