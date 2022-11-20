from selenium import webdriver


def test_wikipedia():
    # creates a web driver for Chrome
    driver = webdriver.Chrome()
    # loads the Wikipedia home page
    driver.get("https://en.wikipedia.org")
    # finds and enters “wake tech” into the search bar and performs the search
    driver.find_element("id", "searchInput").send_keys("wake tech")
    driver.find_element("id", "searchButton").click()

    # checks if the title of the content article is “Wake Technical Community College”
    heading = driver.find_element("id", "firstHeading").text
    assert heading == "Wake Technical Community College"

    driver.quit()


test_wikipedia()
