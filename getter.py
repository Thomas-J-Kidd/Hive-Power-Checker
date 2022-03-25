import updater_mod
import multiprocessing
import time
import schedule
import smtplib, ssl

#100%_hivepower_0%


# object armoredbanana

user1 = updater_mod.Hive_power_tracker(username = "armoredbanana")
user1.get_user_data()
check_backc_time_user_1 = user1.get_time()
print(user1)

# object trostparadox
user2 = updater_mod.Hive_power_tracker(username = "trostparadox")
user2.get_user_data()
user2.get_time()
print(user2)

# object bhanutejap
user3 = updater_mod.Hive_power_tracker(username = "bhanutejap")
user3.get_user_data()
user3.get_time()
print(user3)

# # email things
# port = 465  # For SSL
# smtp_server = "smtp.gmail.com"
# sender_email = "hivepower100@gmail.com"  # Enter your address
# receiver_email = "thomas.kidd@okstate.edu"  # Enter receiver address
# password = "100%_hivepower_0%"
# message =  "Hello there\n\nYour hive power is full"

# # checkback

# def check_back_user_1():
#     print("\nCheckback")
#     user1.get_user_data()
#     check_backc_time_user_1 = user1.get_time()
#     print(user1)
#     schedule.every(check_backc_time_user_1).seconds.do(check_back_user_1)
#     # Create a secure SSL context
#     context = ssl.create_default_context()
#     with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
#         server.login(sender_email, password)
#         server.sendmail(sender_email, receiver_email, message)

# schedule.every(check_backc_time_user_1).minutes.do(check_back_user_1)

# while 1:
#     schedule.run_pending()
#     time.sleep(5)
#     if check_backc_time_user_1 == 0:
#         break



