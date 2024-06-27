import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker


class JoinOurTeamTest:
    def __init__(self):
        # Initialize the WebDriver and Faker instance
        self.driver = webdriver.Chrome()
        self.url = "https://naxa.com.np/contact/joinourteam"
        self.fake = Faker()

    def navigate_to_page(self):
        # Navigate to the specified URL and maximize the browser window
        print("Navigating to the page...")
        self.driver.get(self.url)
        self.driver.maximize_window()

    def highlight_element(self, element):
        # Highlight an element by adding a red border around it (for debugging purposes)
        self.driver.execute_script("arguments[0].style.border='3px solid red'", element)
        time.sleep(1)

    def reset_element_style(self, element):
        # Reset the element style to remove the highlight
        self.driver.execute_script("arguments[0].style.border=''", element)
        time.sleep(1)

    def click_join_our_team(self):
        # Locate and click the 'Join Our Team' link on the page
        print("Clicking 'Join Our Team'...")
        join_team_locator = (By.CSS_SELECTOR, "[href='/contact/joinourteam'] span")
        join_team_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(join_team_locator)
        )
        self.highlight_element(join_team_element)
        join_team_element.click()
        self.reset_element_style(join_team_element)

    def select_random_job_option(self):
        # Select a random job option from the dropdown menu, skipping the first option
        print("Selecting random job option...")
        dropdown_locator = (By.CSS_SELECTOR, ".naxatw-w-72.naxatw-py-4.naxatw-flex.naxatw-flex-col select")
        options_locator = (By.CSS_SELECTOR, ".naxatw-w-72.naxatw-py-4.naxatw-flex.naxatw-flex-col select option")

        dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(dropdown_locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)
        self.highlight_element(dropdown)
        dropdown.click()

        options = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(options_locator)
        )

        random_option = random.choice(options[1:])  # Skip the first option
        self.driver.execute_script("arguments[0].scrollIntoView(true);", random_option)
        random_option.click()
        self.reset_element_style(dropdown)
        time.sleep(1)

    def select_random_gender_option(self):
        # Select a random gender option from the dropdown menu, skipping the first option
        print("Selecting random gender option...")
        try:
            gender_label_locator = (By.CSS_SELECTOR, "div:nth-of-type(8) > label")
            gender_label_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(gender_label_locator)
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", gender_label_element)
            time.sleep(1)

            gender_dropdown_locator = (By.CSS_SELECTOR,
                                       ".md\\:naxatw-p-\\[0\\.9rem\\].naxatw-bg-\\[\\#F4F4F4\\].naxatw-border.naxatw-outline-none.naxatw-rounded")
            gender_dropdown = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(gender_dropdown_locator)
            )
            self.highlight_element(gender_dropdown)
            gender_dropdown.click()
            time.sleep(1)

            options_locator = (By.CSS_SELECTOR,
                               ".md\\:naxatw-p-\\[0\\.9rem\\].naxatw-bg-\\[\\#F4F4F4\\].naxatw-border.naxatw-outline-none.naxatw-rounded option")
            options = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_all_elements_located(options_locator)
            )
            random_option = random.choice(options[1:])  # Skip the first option
            random_option.click()
            self.reset_element_style(gender_dropdown)
            time.sleep(1)
        except Exception as e:
            print(f"Error selecting gender: {str(e)}")

    def select_random_source_option(self):
        # Select a random source option from the dropdown menu, skipping the first option
        print("Selecting random source option...")
        try:
            source_dropdown_locator = (By.CSS_SELECTOR,
                                       "div:nth-of-type(2) > .naxatw-bg-\[\#F4F4F4\].naxatw-border.naxatw-outline-none.naxatw-p-3.naxatw-rounded")
            source_dropdown = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(source_dropdown_locator)
            )
            self.highlight_element(source_dropdown)
            source_dropdown.click()
            time.sleep(1)

            options_locator = (By.CSS_SELECTOR,
                               "div:nth-of-type(2) > .naxatw-bg-\[\#F4F4F4\].naxatw-border.naxatw-outline-none.naxatw-p-3.naxatw-rounded > option")
            options = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_all_elements_located(options_locator)
            )
            random_option = random.choice(options[1:])  # Skip the first option
            random_option.click()

            self.reset_element_style(source_dropdown)
            time.sleep(1)
        except Exception as e:
            print(f"Error selecting source: {str(e)}")

    def select_random_experience_option(self):
        # Select a random experience option from the dropdown menu, skipping the first option
        print("Selecting random experience option...")
        try:
            experience_dropdown_locator = (By.CSS_SELECTOR,
                                           "div:nth-of-type(9) > .form-group.naxatw-flex.naxatw-flex-col > .naxatw-bg-\[\#F4F4F4\].naxatw-border.naxatw-outline-none.naxatw-p-3.naxatw-rounded")
            experience_dropdown = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(experience_dropdown_locator)
            )
            self.highlight_element(experience_dropdown)
            experience_dropdown.click()
            time.sleep(1)

            options_locator = (By.CSS_SELECTOR,
                               "div:nth-of-type(9) > .form-group.naxatw-flex.naxatw-flex-col > .naxatw-bg-\[\#F4F4F4\].naxatw-border.naxatw-outline-none.naxatw-p-3.naxatw-rounded > option")
            options = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_all_elements_located(options_locator)
            )
            random_option = random.choice(options[1:])  # Skip the first option
            random_option.click()
            self.reset_element_style(experience_dropdown)
            time.sleep(1)
        except Exception as e:
            print(f"Error selecting experience: {str(e)}")

    def fill_form(self):
        # Fill out the form with random data generated by Faker
        print("Filling out the form with random data...")
        first_name_locator = (By.NAME, "first_name")
        middle_name_locator = (By.CSS_SELECTOR, "[placeholder='Middle Name']")
        last_name_locator = (By.CSS_SELECTOR, "[placeholder='Last Name']")
        permanent_address_locator = (By.CSS_SELECTOR, "[placeholder='Permanent Address']")
        city_locator = (By.CSS_SELECTOR, "[placeholder='City/District']")
        province_locator = (By.CSS_SELECTOR, "[placeholder='Province/State']")
        email_locator = (By.CSS_SELECTOR, ".team_form [placeholder='Email']")
        contact_num_locator = (By.CSS_SELECTOR, "div:nth-of-type(7) > div:nth-of-type(2) > .form-control")
        expected_salary_locator = (By.CSS_SELECTOR, "div:nth-of-type(9) > .form-group > .form-control")
        skills_locator = (By.CSS_SELECTOR, "[placeholder='Write down your skills']")
        qualification_locator = (By.CSS_SELECTOR, "[placeholder='Academic Qualifications']")
        current_org_locator = (By.CSS_SELECTOR, "[placeholder='Current Organization']")
        current_designation_locator = (By.CSS_SELECTOR, "[placeholder='Current Designation']")
        reference_name_locator = (By.CSS_SELECTOR, "[placeholder='Reference Name']")
        reference_position_locator = (By.CSS_SELECTOR, "[placeholder='Reference Position']")
        reference_num_locator = (By.CSS_SELECTOR, "[placeholder='Reference Contact Number']")

        # Wait until the first name field is present
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(first_name_locator)
        )

        # Generate a 10-digit contact number
        contact_number = ''.join(random.choices('0123456789', k=10))

        # Fill in each form field with random data
        self.driver.find_element(*first_name_locator).send_keys("TestTest")
        self.driver.find_element(*middle_name_locator).send_keys("Testtest")
        self.driver.find_element(*last_name_locator).send_keys("TestTest")
        self.driver.find_element(*permanent_address_locator).send_keys("kathmandu")
        self.driver.find_element(*city_locator).send_keys(self.fake.city())
        self.driver.find_element(*province_locator).send_keys(self.fake.state())
        self.driver.find_element(*email_locator).send_keys(self.fake.email())
        self.driver.find_element(*contact_num_locator).send_keys(contact_number)
        self.driver.find_element(*expected_salary_locator).send_keys("1")
        self.driver.find_element(*skills_locator).send_keys(self.fake.sentence())
        self.driver.find_element(*qualification_locator).send_keys("MBA")
        self.driver.find_element(*current_org_locator).send_keys(self.fake.word())
        self.driver.find_element(*current_designation_locator).send_keys(self.fake.word())
        self.driver.find_element(*reference_name_locator).send_keys(self.fake.name())
        self.driver.find_element(*reference_position_locator).send_keys(self.fake.word())
        self.driver.find_element(*reference_num_locator).send_keys(contact_number)

    def upload_file(self, locator, file_path):
        # Upload a file by sending the file path to the input element
        try:
            upload_locator = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locator)
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", upload_locator)
            self.highlight_element(upload_locator)
            upload_locator.send_keys(file_path)
            time.sleep(5)
            self.reset_element_style(upload_locator)
        except Exception as e:
            print(f"Error uploading file: {str(e)}")

    def upload_cv(self, file_path):
        # Upload the CV file
        cv_locator = (By.ID, "selectCVFile")
        self.upload_file(cv_locator, file_path)

    def upload_cover_letter(self, file_path):
        # Upload the cover letter file
        cover_letter_locator = (By.CSS_SELECTOR, "input#selectCoverLetterFile")
        self.upload_file(cover_letter_locator, file_path)

    def submit_form(self):
        # Click the 'Apply Now' button to submit the form
        print("Clicking 'Apply Now' button to submit the form...")
        try:
            apply_now_locator = (By.CSS_SELECTOR, ".team_form [class='buttons mb-0'] span")
            apply_now_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(apply_now_locator)
            )
            # self.driver.execute_script("arguments[0].scrollIntoView(true);", apply_now_button)
            self.highlight_element(apply_now_button)
            apply_now_button.click()
            self.reset_element_style(apply_now_button)
            print("Form submitted successfully!")
        except Exception as e:
            print(f"Error submitting form: {str(e)}")

    def verify_submission(self):
        # Verify if the submission was successful by checking for the success message
        print("Verifying form submission...")
        try:
            success_message_locator = (By.CSS_SELECTOR, ".status-content h2")
            success_message_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(success_message_locator)
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", success_message_element)
            assert "Submission Complete!" in success_message_element.text
            print("Submission verification successful!")
        except Exception as e:
            print(f"Submission verification failed: {str(e)}")

    def close_driver(self):
        # Close the browser
        print("Closing the browser...")
        self.driver.quit()


if __name__ == "__main__":
    test = JoinOurTeamTest()
    cv_path = "/home/tilak/Desktop/Test.pdf"
    cover_letter_path = "/home/tilak/Desktop/Test.pdf"
    try:
        test.navigate_to_page()
        test.click_join_our_team()
        time.sleep(2)
        test.select_random_job_option()
        time.sleep(2)
        test.fill_form()
        time.sleep(3)
        test.select_random_gender_option()
        time.sleep(2)
        test.select_random_source_option()
        time.sleep(2)
        test.select_random_experience_option()
        time.sleep(2)
        test.upload_cv(cv_path)
        time.sleep(4)
        test.upload_cover_letter(cover_letter_path)
        time.sleep(3)
        # test.submit_form()
        # time.sleep(5)
        # test.verify_submission()
    finally:
        test.close_driver()
