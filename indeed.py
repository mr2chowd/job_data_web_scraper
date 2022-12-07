
from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
def get_indeed_url(position, location):
   
    url = 'https://www.indeed.com/jobs?q={}&l={}'
    urlo = "https://www.indeed.com/jobs?q=IT&l=Utica&vjk=401002068bdd57ff"
   
    position = position.replace(' ', '+')
    location = location.replace(' ', '+')
    url = url.format(position, location)
    print(url)
    return url

def indeed_data(position, location):

    companyname= []
    jobtitle = []
    url = get_indeed_url(position, location)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get(url)
    result =driver.find_element(By.CLASS_NAME,'jobsearch-JobCountAndSortPane-jobCount').text
    result = result.replace(',',"")
    result = result.replace(' jobs',"")
    search_result = pd.to_numeric(result)
    print("Search result of indeed: ", search_result)
    
    n = 0
    next_flag = False
    while True:
        nexturl = url + '&start=' + str(n)
        driver.get(nexturl)

        n = n + 10
        company_name = driver.find_elements(By.CLASS_NAME,"companyName")
        job_title = driver.find_elements(By.CLASS_NAME,"jobTitle")
        for c in company_name:
            companyname.append(c.text)
        for j in job_title:
            jobtitle.append(j.text)
        e = driver.find_elements(By.CLASS_NAME,"css-cy0uue")
        prev_next = len(e)
        if(prev_next==2):
            next_flag = True

        if next_flag == True and prev_next == 1:
            print("No more urls")
            break
        time.sleep(5)

    companydf=pd.DataFrame(companyname,columns=["company"])
    jobtitledf=pd.DataFrame(jobtitle,columns=["job title"])
    jobposting_indeed = companydf.join(jobtitledf) 
    return jobposting_indeed

            
