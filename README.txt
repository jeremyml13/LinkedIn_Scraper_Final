This Python algorithm is capable of scraping the first X (in this case 100) results from the public LinkedIn job board containing "Sales Development Representative" roles in the United States.

After scraping these results, the script then looks at each company for each of those 100 roles, and finds all roles offered by that company on LinkedIn. For each role found, the company
name, the company description, the job name, the job description, the job location, and the job salary (if the scraped salary was a range, the average was taken to find the salary value)
were recorded. This information is recorded in a DataFrame called rough_df. Using all of this information, for each company, the following was found: company name, company description, average salary,
median salary, standard deviation of salaries, highest paid role, location distribution, and the most used word in all the job descriptions by that company. These results are displayed
in a DataFrame called final_df.

In most cases, the public job page did not have a salary range embedded in the web-page for easy access. In this case,
salaries were scraped from the job description text by searching for "$" in the text, and making sure that what followed the "$" was actually a salary range. For example, in the description of a
job at Assembled, the term "$70m" was used, before the salary was mentioned. Using some simple checks, like making sure an "m" is not in the near vicinity of the "$" index, as well as making sure
the salary was not referring to an hourly wage by checking for periods in the very near vicinity of the found "$", the salary range was scraped from the job description.
The salary string scraped from the job description was cleaned and the salary extracted using regular languages.
Some companies, like Assembled, did not even put the salary in the job description. If a salary was not able to be scraped from the job description, it was given a value of "NA".
If given more time, more stress cases for scraping the salary from job description would be accounted for.

The script takes some time to run, as Requests was not able to scrape off the information on most of the LinkedIn pages, as it was dynamic content. This means that Selenium, which is slow, was
heavily utilized to obtain the HTML content. Additionally, Selenium had to be opened and quit after every scrape, as it "got caught" if it was left open and tried to scrape too many things in a row.
If given more time, I would find a way to optimize the use of Selenium and Requests so that the program runs as optimally as possible. Sometimes, the script glitches and does not
properly the first time. Running it again solves this problem that sometimes arises. If given more time, I would figure out why this occurs. 

The script can be run executing in Terminal:
python3 main.py

The smaller parts of the scraper found in the different Python files will also successfully run if used as an argument in Terminal:
For example, executing:
showingResults.py
will successfully showing the results of a rough_df in a final_df
*Note: in order to run getNumbersFromString.py and mostUsedWord.py, there is no main argument, so commenting out the test cases at the
bottom of the page and then running will successfully execute the script.