from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import re

def get_data(url, case) -> list:
    browser_options = ChromeOptions()
    browser_options.headless = False
    browser_options.add_experimental_option("detach", True)

    driver = Chrome(options=browser_options)
    driver.get(url)

    login_link = driver.find_element(By.ID, 'HeadLoginView_loginLink')
    login_link.click()

    username = driver.find_element(By.ID, "MainContent_Login1_UserName")
    password = driver.find_element(By.ID, "MainContent_Login1_Password")

    # Enter login credentials
    username.send_keys("mastercuong70@gmail.com")
    password.send_keys("gemcy6-xycvik-kacnUm")

    password.send_keys(Keys.ENTER)

    link = driver.find_element(By.ID, 'MasterMainMenuLink14')
    link.click()

    # Change between exams!
    exam_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'MainContent_modalRepeater_ModalMenu_14_subheadingGroupRepeaterNew_14_subheadingRepeaterNew_0_linkRepeater_1_link_3'))
        )
    exam_link.click()

    options_cleaned = []
    options = []
    i = 1

    count = driver.find_element(By.ID, "MainContent_NarrativeDisplay_lblQuestionCount")
    
    text = count.text

    # print(text)

    # Step 4: Use a regular expression to find the number
    match = re.search(r'/(\d+)', text)

    if match:
        total_questions = int(match.group(1))
        print(f"Total questions: {total_questions}")

    # Going till the end
    while i < total_questions + 1:
        try:
            # Check for the confirm button first
            confirm_button = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.ID, 'MainContent_NarrativeDisplay_btnSectionSummaryConfirm'))
            )
            if confirm_button:
                confirm_button.click()
        except:
            # If the confirm button is not found, then click the next button

            # Extract options
            options_elements = driver.find_element(By.CSS_SELECTOR, 'table.radioButtonList')
            labels = options_elements.find_elements(By.TAG_NAME, 'label')

            # Extract the text and format it as a list of options
            options_cleaned = [label.text.strip() for label in labels]
            options = options + (options_cleaned)

            # Print the list of options
            # print(options)
            
            next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'MainContent_NarrativeDisplay_btnNext'))
            )
            next_button.click()

            i += 1

    print(len(options))
    
    confirm_button = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.ID, 'MainContent_NarrativeDisplay_btnSectionSummaryConfirm'))
            )
    if confirm_button:
        confirm_button.click()

    narrative_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'MainContent_NarrativeDisplay_btnFinalNext'))
    )
    narrative_button.click()
    
    questions = []

    question_number = 1

    while question_number < total_questions + 1:    
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, 'MainContent_NarrativeDisplay_pnlInitBackgroundContainer'))
        )

        # Get all the text from the element
        pt = element.text
        pt = pt.replace('\n', ' ')

        # print("PT: ", pt)
        print("#: ",question_number)

        question_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, 'MainContent_NarrativeDisplay_lblResultQuestion'))
        )
        # Get the text from the element
        question_text = question_element.text
        
        print("Q: ",question_text)

        correct_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, 'MainContent_NarrativeDisplay_lblCorrectAnswer'))
        )
        # Get the text from the element
        correct_answer = correct_element.text

        print("A: ",correct_answer)

        explain_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, 'MainContent_NarrativeDisplay_lblCorrectExplain'))
        )
        # Get the text from the element
        explanation = explain_element.text

        print("E: ",explanation)
        
        question_data = {
                "Source": "counselingexam.com",
                "Exam Name": "NCMHCE Narrative Exam 4",
                "Question #": question_number,
                # "Case Study #": case_study_number,
                # "Patient Demographic": patient_demographic,
                # "General Information": general_information,
                # "Presenting Problem": presenting_problem,
                # "Mental Status Exam": mental_status_exam,
                "Content": pt,
                "Question": question_text,
                "Choice A": options[4 * (question_number-1)],
                "Choice B": options[4 * (question_number-1) + 1],
                "Choice C": options[4 * (question_number-1) + 2],
                "Choice D": options[4 * (question_number-1) + 3],
                "Correct Answer": correct_answer,
                "Explanation for correct answer": explanation
            }
        
        questions.append(question_data)

        next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'MainContent_NarrativeDisplay_btnResultNext'))
        )

        next_button.click()
        # Wait for the page to refresh by checking for a specific element to ensure new content is loaded
        WebDriverWait(driver, 20).until(
            EC.staleness_of(element)  # Wait until the old element is no longer attached to the DOM
        )
        question_number = question_number + 1
    
    driver.quit()

    return questions

    # 
    # return data

def main():
    data = get_data("https://counselingexam.com/free-practice-exam", 0)
    # data = get_data("https://counselingexam.com/free-practice-exam", 1)
    df = pd.DataFrame(data)
    df.to_csv('/Users/hongdong-wan/Documents/Georgia Tech 2024 Spring/Undergraduate Research/counseling_exam_4_questions.csv', index=False)
    print("Data has been saved to CSV.")

if __name__ == '__main__':
    main()
