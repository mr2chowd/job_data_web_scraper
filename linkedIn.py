from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_linkedin_url(position, location):

    url = "https://www.linkedin.com/jobs/search/?keywords={}&location={}&refresh=true"
    position = position.replace(' ', '+')
    location = location.replace(' ', '+')
    lurl = url.format(position, location)
    return lurl

def linkedin_data(position, location ):
    lurl = get_linkedin_url(position,location)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get(lurl)
    result =driver.find_element(By.CLASS_NAME,'results-context-header__job-count').text
    result = result.replace(',',"")
    result = result.replace('+',"")
    search_result = pd.to_numeric(result)
    print("Search result of Linkedin: ", search_result)

    i = 0
    while True: 
        no_more =driver.find_element(By.CLASS_NAME,"leading-regular").text
        if no_more ==  "You've viewed all jobs for this search":
            print("No more results to show !!")
            break
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        try:
            send=driver.find_element(By.CLASS_NAME,'infinite-scroller__show-more-button')
            if send.text == "See more jobs":
                driver.execute_script("arguments[0].click();", send) 
                time.sleep(3)
        except:
            pass
            time.sleep(5)

    companyname= []
    jobtitle = []

    try:
        for i in range(search_result):
            company=driver.find_elements(By.CLASS_NAME,'base-search-card__subtitle')[i].text
            title=driver.find_elements(By.CLASS_NAME,'base-search-card__title')[i].text
            companyname.append(company)
            jobtitle.append(title)
    
    except:
        print("done!")
    companydf=pd.DataFrame(companyname,columns=["company"])
    jobtitledf=pd.DataFrame(jobtitle,columns=["job title"])

    jobposting_linkedin = companydf.join(jobtitledf)
    return jobposting_linkedin

