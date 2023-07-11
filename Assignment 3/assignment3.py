from selenium import webdriver
import time

# Launch the web browser and navigate to IMDb
driver = webdriver.Chrome()  # Set the path to your ChromeDriver executable
driver.get("https://www.imdb.com")

# Perform some actions on the IMDb page
# Action 1: Search for a movie and click on its title
search_input = driver.find_element("xpath","/html/body/div[2]/nav/div[2]/div[1]/form/div[2]/div/input")
search_input.send_keys("The Shawshank Redemption")
search_input.submit()

# Wait for the search results to load
time.sleep(5)

# Action 2: Click on the movie's title from the search results
movie_title = driver.find_element("xpath","/html/body/div[2]/main/div[2]/div[3]/section/div/div[1]/section[2]/div[2]/ul/li[1]/div[2]/div/a")
movie_title.click()

# Wait for the movie page to load
time.sleep(5)

# Action 3: Click on video thumbnail
video_element = driver.find_element("xpath","/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[3]/div[1]/div[3]/a[1]")
video_element.click();


# Action 4: click on official trailer video
trailer_element = driver.find_element("xpath","/html/body/div[2]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/ol/li[5]/div/a/img")
trailer_element.click();

time.sleep(8)

# Close the browser
driver.quit()
