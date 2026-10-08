from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    # Open LAB search page
    driver.get("https://lab.fi/fi/haku")

    # Test 1: Check that the page opened
    assert "LAB" in driver.title
    print("PASS: LAB website opened successfully")
    print("Page title:", driver.title)

    # Find the visible search field
    search_box = wait.until(
        EC.visibility_of_element_located((By.ID, "edit-keywords--3"))
    )

    # Enter and submit the search term
    search_box.send_keys("erasmus")
    search_box.submit()

    # Test 2: Check that the search was completed
    wait.until(EC.url_contains("erasmus"))
    assert "erasmus" in driver.current_url.lower()

    print("PASS: Search for Erasmus completed successfully")
    print("Search URL:", driver.current_url)

    # Test 3: Check that Erasmus-related results are displayed
    wait.until(
        EC.text_to_be_present_in_element(
            (By.TAG_NAME, "body"), "Erasmus"
        )
    )

    assert "Erasmus" in driver.page_source

    print("PASS: Erasmus-related search results are displayed")

    # Test 4: Open the first Erasmus search result
    first_result = wait.until(
        EC.element_to_be_clickable(
            (By.PARTIAL_LINK_TEXT, "Erasmus Mundus")
        )
    )

    first_result.click()

    # Check that the linked page opened
    wait.until(EC.url_contains("erasmus-mundus-maisteriohjelmassa"))

    assert "erasmus-mundus-maisteriohjelmassa" in driver.current_url.lower()

    print("PASS: First Erasmus search result opened successfully")
    print("Result URL:", driver.current_url)

finally:
    driver.quit()