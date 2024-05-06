# This is unused code

"""
def parse_scraped_jobs_name_and_ids(jobs_list):
    list_job_ids = []
    for job in jobs_list:
        base_card_division = job.find("div", {"class": "base-card"})
        job_id_pos = base_card_division.get("data-entity-urn")
        job_id = job_id_pos.split(":")[3]
        list_job_ids.append(job_id)
    return list_job_ids
"""

"""
def parse_scraped_jobs_list_to_job_page_urls(jobs_list):
    list_job_page_urls = []
    for job in jobs_list:
        job_page_division = job.find("a", {"class": "base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2]"})
        job_page_url = job_page_division.get("href")
        list_job_page_urls.append(job_page_url)
    return list_job_page_urls
"""


"""
def company_page_to_company_jobs_page(list_company_page_urls):
    list_company_jobs_urls = []
    for company in list_company_page_urls:
        soup = linkedin_url_to_HTML_text(company)
        company_page_metadata = soup.find('a')
        print(company_page_metadata)
        company_jobs_division = company_page_metadata.find("a", {"class": "top-card-layout__cta"})
        print(company_jobs_division)
        company_jobs_url = company_jobs_division.get("href")
        list_company_jobs_urls.append(company_jobs_url)
    return list_company_jobs_urls
"""

"""
def get_job_salary(text):
    # Load the question answering pipeline
    qa_pipeline = pipeline("question-answering")

    # Provide context (the text) and ask a question
    context = text

    question = "What is this location for this job?"

    # Use the QA pipeline to get the answer
    answer = qa_pipeline(question=question, context=context)

    # Print the answer
    return answer["answer"]
"""

"""
job_salary_string = "NA"
    salary_div = job_page_soup.find('div', class_='salary compensation__salary')
    if salary_div:
        job_salary_string = salary_div.text.strip()
    else:
        text = get_job_page_description_text(job_page_soup)
        dollar_index = text.find('$')
        if dollar_index != -1:
            end_index = min(dollar_index + 21, len(text))
            job_salary_string = text[dollar_index:end_index]
    return job_salary_string
"""

"""
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

# Ensure necessary components are downloaded
nltk.download()


def most_used_word(text):
    # Tokenize the text
    words = word_tokenize(text.lower())

    # Filter out stopwords
    filtered_words = [word for word in words if word not in stopwords.words('english') and word.isalpha()]

    # Count word frequencies
    word_counts = Counter(filtered_words)

    # Find the word with the highest frequency
    most_used = word_counts.most_common(1)
    if most_used:
        return most_used[0][0]  # Return the word
    else:
        return None  # Return None if no suitable word is found


# Example usage
text = "Hello world! Welcome to the world of programming. Programming is fun."
print(most_used_word(text))
"""
