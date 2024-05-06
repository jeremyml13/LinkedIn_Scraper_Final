import pandas as pd
import mostUsedWord


# Create an empty dataframe to store individual job information
def create_empty_rough_dataframe():
    columns = ["Company Name", "Company Description", "Job Name", "Job Salary", "Job Location", "Job Description"]
    rough_df = pd.DataFrame(columns=columns)
    return rough_df

# Update the rough dataframe by adding a row of information corresponding to the job information
def add_job_details_as_new_row_in_rough(rough_df, company_name, company_description, job_name, job_salary_value, job_location, job_description):
    new_row = pd.DataFrame([{"Company Name": company_name, "Company Description": company_description, "Job Name": job_name, "Job Salary": job_salary_value, "Job Location": job_location, "Job Description": job_description}])
    rough_df = pd.concat([rough_df, new_row], ignore_index=True)
    return rough_df

# Create an empty dataframe to store final company information
def create_empty_final_dataframe():
    columns = ["Company Name", "Company Description", "Average Salary", "Median Salary", "Standard Deviation Salaries", "Highest Paid Role", "Location Distribution", "Most Used Word in Job Descriptions"]
    final_df = pd.DataFrame(columns=columns)
    return final_df

# Update the final dataframe by adding a row of information corresponding to the company information
def add_job_details_as_new_row_in_final(final_df, company_name, company_description, average_salary, median_salary, std_dev_salary, highest_paid_role_with_salary, location_distribution, most_used_word):
    new_row = pd.DataFrame([{"Company Name": company_name, "Company Description": company_description, "Average Salary": average_salary, "Median Salary": median_salary, "Standard Deviation Salaries": std_dev_salary,
                             "Highest Paid Role": highest_paid_role_with_salary, "Location Distribution": location_distribution, "Most Used Word in Job Descriptions": most_used_word}])
    final_df = pd.concat([final_df, new_row], ignore_index=True)
    return final_df

# Given a rough_df and an empty final_df, return the populated final_df with the desired information from the rough_df
def get_final_dataframe(rough_df, final_df):
    unique_companies = rough_df["Company Name"].unique()  # find unique companies in rough_df
    for company in unique_companies:
        company_data = rough_df[rough_df["Company Name"] == company]  # filter the rough_df by company name
        company_name = company_data["Company Name"].iloc[0]  # obtain company name
        company_description = company_data["Company Description"].iloc[0]  # obtain company description
        company_data["Job Salary"] = pd.to_numeric(company_data["Job Salary"], errors='coerce')  # Convert salary information to numeric values, where values that are "NA" will ultimately be ignored in the calculations
        average_salary = company_data["Job Salary"].mean()  # obtain company average salary
        median_salary = company_data["Job Salary"].median()  # obtain company median salary
        std_dev_salary = company_data["Job Salary"].std()  # obtain standard deviation of salaries within company
        # if statement to find the highest paying role
        if company_data['Job Salary'].notna().any():
            max_salary_index = company_data['Job Salary'].idxmax()  # find index of max salary
            highest_paid_role = company_data.loc[max_salary_index, 'Job Name']  # find corresponding job name of max salary
            highest_paid_salary = company_data.loc[max_salary_index, 'Job Salary']  # find corresponding salary of max salary
            highest_paid_role_with_salary = f"{highest_paid_role}: (${highest_paid_salary})"
        else:
            highest_paid_role_with_salary = "No valid salary data available"
        location_distribution = company_data['Job Location'].value_counts()  # obtain location distribution of roles for the company
        location_distribution_string = '  '.join([f"{loc}: {count}" for loc, count in location_distribution.items()])  # separate these dictionaries spaces and format them nicely
        #print(location_distribution)
        job_descriptions = company_data["Job Description"]  # obtain job description
        all_descriptions = ''.join(job_descriptions)  # concatenate all job descriptions
        most_used_word = mostUsedWord.most_used_word(all_descriptions)  # find the most used word in the descriptions that is not a stopword
        final_df = add_job_details_as_new_row_in_final(final_df, company_name, company_description, average_salary, median_salary, std_dev_salary, highest_paid_role_with_salary, location_distribution_string, most_used_word)  # update the final_df by adding a new row with the found information
    return final_df




if __name__ == '__main__':
    data = {
        "Company Name": ["Runwise", "Runwise", "Runwise", "Runwise", "Assembled", "Assembled", "Assembled", "Assembled", "Assembled", "Assembled", "Flowhub", "Flowhub"],
        "Company Description": ["Runwise is the first end-to-end boiler and heating solutions provider.",
                                "Runwise is the first end-to-end boiler and heating solutions provider.",
                                "Runwise is the first end-to-end boiler and heating solutions provider.",
                                "Runwise is the first end-to-end boiler and heating solutions provider.",
                                "At Assembled, we’re on a mission to create a sustainable future.",
                                "At Assembled, we’re on a mission to create a sustainable future.",
                                "At Assembled, we’re on a mission to create a sustainable future.",
                                "At Assembled, we’re on a mission to create a sustainable future.",
                                "At Assembled, we’re on a mission to create a sustainable future.",
                                "At Assembled, we’re on a mission to create a sustainable future.",
                                "At Flowhub, we’re on a mission to make safe ca...",
                                "At Flowhub, we’re on a mission to make safe ca..."],
        "Job Name": ["Collections Specialist", "Sales Development Representative", "Account Executive", "Lead Field Service Technician", "Sales Development Representative", "Technical Support", "Talent Sourcer", "Sales Engineer", "Customer Success Manager", "Implementation Manager", "Sales Development Representative", "Product Marketing Manager"],
        "Job Salary": ["52500.0", "92500.0", "187500.0", "NA", "87500.0", "97500.0", "100000.0", "NA", "150000.0", "107500.0", "61000.0", "115000.0"],
        "Job Location": ["New York, NY", "New York, NY", "New York, NY", "New York, NY", "San Francisco Bay Area", "San Francisco, CA", "San Francisco, CA", "San Francisco, CA", "San Francisco, CA", "San Francisco, CA", "United States", "United States"],
        "Job Description": ["Runwise is seeking a highly motivated, results...", "Runwise is looking for a growth-minded Sales D...", "Runwise is looking for an Account Executive to...", "About The Company Runwise is a premier industr...", "Assembled is building software to transform an...", "Assembled is building software to transform an...", "Assembled is building software to transform an...", "Assembled is building software to transform an...", "Assembled is building software to transform an...", "Assembled is building software to transform an...", "As a Sales Development Representative (SDR), y...", "To help accelerate our industry leadership as ..."]
    }
    rough_df = pd.DataFrame(data)
    print(rough_df)
    final_df = create_empty_final_dataframe()
    final_df = get_final_dataframe(rough_df, final_df)
    pd.set_option('display.max_columns', None)  # Ensure all columns are shown
    pd.set_option('display.width', 1000)  # Set the display width for showing more characters
    pd.set_option('display.max_colwidth', None)
    print(final_df)



    """
    rough_df = create_empty_rough_dataframe()
    company_name = "Runwise"
    company_description = "Blah Blah Blah"
    job_name = "Sales Associate"
    job_salary_value = 100000
    job_location = "New York City"
    job_description = "Fuck this shit"
    rough_df = add_job_details_as_new_row(rough_df, company_name, company_description, job_name, job_salary_value, job_location, job_description)
    print(rough_df)
    """

