import companyDetails
import scrapingURLS
import jobDetails
import allCompanyJobsURLS
import showingResults
import mostUsedWord
import sched
import time

if __name__ == '__main__':
    while True:
        desired_scraped_jobs = 100  # this number is dynamic
        ceiling = 25 * (desired_scraped_jobs // 10)
        list_company_homepage_all_urls = []  # list containing the 100 company homepage urls
        rough_df = showingResults.create_empty_rough_dataframe()
        for start in range(0, ceiling, 25):  # making sure the desired number of elements are scraped
            url = f"https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?currentJobId=3878876505&f_I=104%2C137&f_TPR=r2592000&geoId=103644278&keywords=sales%20development%20representative&location=United%20States&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R&start={start}"
            jobs_search_soup = scrapingURLS.linkedin_url_to_HTML_soup(url)
            jobs_list = scrapingURLS.scrape_linkedin_job_listings(jobs_search_soup)
            list_company_homepage_urls = scrapingURLS.scraped_jobs_to_company_homepage_urls(jobs_list)
            list_company_homepage_all_urls.extend(list_company_homepage_urls)
        #print(list_company_homepage_all_urls)
        #print(len(list_company_homepage_all_urls))
        for list_company_homepage_url in list_company_homepage_all_urls:  # for each company in the 100 companies
            company_page_soup = companyDetails.get_company_page_soup(list_company_homepage_url)
            company_name = companyDetails.get_company_name(company_page_soup)  # extract company name
            company_description = companyDetails.get_company_description(company_page_soup)  # extract company description
            company_jobs_page_url = companyDetails.company_page_soup_to_all_company_jobs_url(company_page_soup)
            company_jobs_urls = allCompanyJobsURLS.company_jobs_page_to_company_jobs_urls(company_jobs_page_url)  # extracts the URLs of all jobs offered by the company
            for company_job_url in company_jobs_urls:  # for each job offered by the company
                job_page_soup = jobDetails.get_job_page_soup(company_job_url)
                job_name = jobDetails.get_job_name(job_page_soup)
                job_location = jobDetails.get_job_location(job_page_soup)
                job_salary_string = jobDetails.get_job_salary_string(job_page_soup)  # extract the rough string containing the salary information
                job_salary_value = jobDetails.get_job_salary_value(job_salary_string)  # process the rough string to obtain the salary value
                job_description = jobDetails.get_job_page_description_text(job_page_soup)
                rough_df = showingResults.add_job_details_as_new_row_in_rough(rough_df, company_name, company_description, job_name, job_salary_value, job_location, job_description)  # add the job information as a new row in rough_df
                print(rough_df)
        final_df = showingResults.create_empty_final_dataframe()  # create the final_df where the results will be displayed
        final_df = showingResults.get_final_dataframe(rough_df, final_df)  # transfer all job information into desried information that is shown in final_df
        print(final_df)
        time.sleep(60)  # schedule every minute inside the while loop

