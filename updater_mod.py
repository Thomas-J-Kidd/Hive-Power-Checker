from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
import time
import schedule

class Hive_power_tracker:

    def __init__(self, username):

        # getting drivers / webscraping working
        options = FirefoxOptions()
        options.add_argument("--headless")
        self.driver = webdriver.Firefox(executable_path = r'C:\Users\thoma\Documents\Blockchain\webscraping\geckodriver.exe', options=options) #this is the path where my geckodriver exists

        # getting data paramaters accessible for the whole class
        self.username = username
        self.vote_value_percentage = ''
        self.time_to_100 = ''
        self.effective_hive_power = ''
        self.hive_power = ''
        self.total_minute_value = 0
        

    # gets user data
    def get_user_data(self):

        hivestats_url = 'https://hivestats.io/@' + self.username
        self.driver.get(hivestats_url)
        time.sleep(3)
        self.vote_value_percentage = self.driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div/div[2]/section[1]/div[2]/div/div/span[1]/span[2]')
        self.time_to_100 = self.driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div/div[2]/section[3]/div[2]/table/tbody/tr[8]/td[2]')
        self.effective_hive_power = self.driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div/div[2]/section[3]/div[2]/table/tbody/tr[1]/td[2]/span')
        self.hive_power = self.driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div/div[2]/section[3]/div[2]/table/tbody/tr[2]/td[2]/span')

        
        
        return 0

            
    # prints out user data 
    def __repr__(self): 
        print("---------------","\nUser:", self.username, "\nVote Power:", self.vote_value_percentage.text, "\nTime untill full:", self.time_to_100.text, "\nEffective HP:", self.effective_hive_power.text, "\nActual HP:", self.hive_power.text, "\nFull Hive Power in: ", self.total_minute_value, " minutes")
        #return "User: % s Vote Power: % s Time untill full: % s Effective HP: % s Actual HP: % s" % (self.username, self.vote_value_percentage, self.time_to_100, self.effective_hive_power, self.hive_power) 
        return "---------------"

    # gets the number of minutes left for the user to have full hive power again
    def get_time(self):
        string = str(self.time_to_100.text)
        temp = string.replace(" ", "")
        self.total_minute_value = 0
        
        if (temp.find("Full") == 0):
            self.total_minute_value = 0

        # Getting the number of minutes remaining based on the day value
        if (temp.find("day") != -1):
            day_index = temp.find("day")
            day_value = int(temp[day_index-1])
            minute_day_value = day_value * 1440
            self.total_minute_value += minute_day_value

            # Getting the number of minutes remaining based on the hour value
        if (temp.find("hour") != -1):
            hour_index = temp.find("hour")
           
                
            if (temp[hour_index-2].isdigit()):
                hour_value = int(temp[hour_index-2] + temp[hour_index-1])
                minute_hour_value = hour_value * 60
                self.total_minute_value += minute_hour_value

            elif (temp[hour_index-1].isdigit()):
                hour_value = int(temp[hour_index-1])
                minute_hour_value = hour_value * 60
                self.total_minute_value += minute_hour_value

            # Getting the number of minutes remaining based on the minute value
        if (temp.find("minute") != -1):
            minute_index = temp.find("minute")
            if (temp[minute_index-2].isdigit()):
                minute_value = int(temp[minute_index-2] + temp[minute_index-1])
                self.total_minute_value += minute_value

            elif (temp[minute_index-1].isdigit()):
                minute_value = int(temp[minute_index-1])
                self.total_minute_value += minute_value

        return self.total_minute_value

# general outline 

# collect usernames in text file
# function that sets the usernames into the data collector
# function that sends messages / notifications (email,)
#           - update when the notification was sent to the user
#           - collect notification time for each user and store it in a dictionary 
# pay us a subscription fee of #hive per week/month/year or some timeframe

#-------------------------------
# phase 1
#-------------------------------
# flow
# user signs up for service
# once signed up we get that username into a text file
# take each user name from text file and pass it through the data function: then check hive power and time remaining to full charge

# initially test / store in google form 
# google collab notebook - execute our python scripts. 
# send a notification that they signed up and display their hive power % and time remaining until full
# send notification when hive power is at 99% or 100% 
# develop a formula for how often to check back based on persentage 
# after every 30 minutes we check 
#-------------------------------


#