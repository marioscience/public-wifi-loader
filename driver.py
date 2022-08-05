import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By

# VERNON
login_url = "https://n402.network-auth.com/splash/?mac=E0%3A55%3A3D%3AF3%3AE3%3A48&real_ip=10.240.247.242&client_ip=10.240.247.242&client_mac=34:02:86:A0:C4:9A&vap=2&a=cb7a1d775e800fd1ee4049f7dca9e041eb9ba083&b=2928449&auth_version=5&key=dfae05a025f92c9627e9ce7b1c4cef18e97e8b66&acl_ver=P12438273V2&continue_url=http%3A%2F%2Fwww.gstatic.com%2Fgenerate_204"

# FRANKLIN
    #login_url = "https://n402.network-auth.com/splash/?mac=34%3A56%3AFE%3AA0%3ABE%3A93&real_ip=10.240.247.242&client_ip=10.240.247.242&client_mac=34:02:86:A0:C4:9A&vap=2&a=12c6fc06c99a462375eeb3f43dfd832b08ca9e17&b=5835129&auth_version=5&key=32bd3d05ce669e97f10cf3b0e2e0dfb029be0699&acl_ver=P12262010V2&continue_url=http%3A%2F%2Fwww.gstatic.com%2Fgenerate_204"

checkbox_element = "input type='checkbox' class='largerCheckbox'"
button_element = "input id='button' name='mode_login' type='submit'"


def authenticate_wifi(login_url, checkbox_class, submit_id):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("window-size=700,300")

    driver = webdriver.Chrome(options=options)

    driver.get(login_url)

    driver.implicitly_wait(0.5)

    checkbox = driver.find_element(By.CLASS_NAME, checkbox_class)
    button = driver.find_element(By.ID, submit_id)

    checkbox.click()
    driver.implicitly_wait(0.1)
    button.click()

    time.sleep(2)
    driver.quit()

# sequence of events:
# 1. Load URL
# 2. check checkbox
# 3. Click button


if __name__ == "__main__":
    # when file is run directly execute main steps. place those in a function
    # that can be used in both here and for automated checking of internet.
    start_time = None
    while(True):
        authenticate_wifi(login_url, 'largerCheckbox', 'button')
        start_t = 300
        end_t = 460
        variable_t = random.randint(start_t, end_t)
        if start_time:
            elapsed = time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time))
            print(f"Took: {elapsed}")
        start_time = time.time()
        print("====== STARTING ======")
        current_t = time.strftime("%Y-%m-%d %H:%M:%S")
        print(current_t)
        minute_t = variable_t/60
        print("Time to wait: {minute_t:.2f} minutes.".format(minute_t=minute_t))
        time.sleep(variable_t)
        print("====== ENDING ======")