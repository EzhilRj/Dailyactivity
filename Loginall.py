import logging
import os
import time
import unittest
import logging as L
import chromedriver_autoinstaller
import uiautomation
from selenium import webdriver
from selenium.webdriver.common.by import By
import configparser


class Test(unittest.TestCase):


    @classmethod
    def setUpClass(cls):

        log = L.getLogger()
        log.setLevel(logging.DEBUG)

        # Reading Properties
        config = configparser.RawConfigParser()
        config.read('Credentials.properties')

        options = webdriver.ChromeOptions()
        options.add_argument('user-data-dir=C:\\Path')  # Path to your chrome profile

        Screenshotsdirectorypath = r'C:\TestLogin\Screenshots'
        if not os.path.exists(Screenshotsdirectorypath):
            os.makedirs(Screenshotsdirectorypath)

        Errorscreenshotsdirectorypath = r'C:\TestLogin\LoginErrorScreenshots'
        if not os.path.exists(Errorscreenshotsdirectorypath):
            os.makedirs(Errorscreenshotsdirectorypath)

        LoginallLogsfolderpath = r'C:\TestLogin\Logs'
        if not os.path.exists(LoginallLogsfolderpath):
            os.makedirs(LoginallLogsfolderpath)
        f = open("C:\TestLogin\Logs\TestLogs.log", "w+")

        L.basicConfig(filename="C:/TestLogin/Logs/TestLogs.log",
                      format='%(asctime)s:%(levelname)s:%(message)s',
                      datefmt='%d-%m-%y %I:%M:%S %p')

        cls.driver = chromedriver_autoinstaller.install(False, 'C:\TestLogin')
        cls.driver = webdriver.Chrome(executable_path='C:/TestLogin/109/chromedriver.exe', chrome_options=options)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        L.info("Chrome is Opened Succesfully")


    def test_Loginall(self):

        global Redipaeimg, hrmsimg, Payrollimg, frameximg, vendoimg, bandhuimg, Redipaeerrorimg, hrmserrorimg, Payrollerrorimg, frameXerrimg, vendounerrimg, vendopwerrimg, bandhuerrimg, Redipaesayingmsg, bandhusayingmsg, Redipaewpmsg, HRMSWpmsg, Payrollwpmsg, framexwpmsg, vendowpmsg, bandhuwpmsg, HRMSurl, Hrmsuname, hrmsepword, HRMScomp, payrollurl, payrolluname, payrollepword, payrollcomp, Frameurl, Frameuname, Framepword, Framecomp, vendourl, Vendouname, vendopword

        # Reading Properties
        config = configparser.RawConfigParser()
        config.read('Credentials.properties')

        Redipaeurl = config.get('credentialsection', 'RedipaeBaseurl')
        Redipaeuname= config.get('credentialsection', 'Redipaeusername')
        Redipaepword = config.get('credentialsection', 'Redipaepassword')

        L.info("Redipae opened Successfully")
        self.driver.get(Redipaeurl)
        L.info("Redipae username Entered")

        self.driver.find_element(By.ID, "username").send_keys(Redipaeuname)
        L.info("Redipae password Entered")
        self.driver.find_element(By.ID, "password").send_keys(Redipaepword)
        L.info("Submit button is clicked")
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        L.info(Redipaeurl)
        L.info(Redipaeuname)
        L.info(Redipaepword)

        redipaeerr = ''
        Redipaesayingmsg = ''

        try:
            redipaeerr = self.driver.find_element(By.XPATH, "//span[@class='error']").text
            L.error(redipaeerr)
        except:
            L.info("Usermaster is clicked")
            self.driver.find_element(By.XPATH, "//*[text()='User Master']").click()
            L.info("Uploaduser is clicked")
            self.driver.find_element(By.XPATH, "//*[@href='http://redipae.in/User/UploadUser']").click()
            time.sleep(1)
            Redipaefolderpath = "C:\TestLogin\Screenshots\Redipaelogin"
            Redipaetimeformat = time.asctime().replace(":", "")
            Redipaeimg = Redipaefolderpath + Redipaetimeformat + ".png"
            L.info("Redipae screenshot is captured")
            self.driver.get_screenshot_as_file(Redipaeimg)
            Redipaesayingmsg = "Redipae Login successfully"
            print(Redipaesayingmsg)
            L.info(Redipaesayingmsg)

        if (redipaeerr == 'Please enter correct Username and Password. Please try again'):
            Redipaewpmsg = ('Redipae Says :: [' + redipaeerr + ']')
            print(Redipaewpmsg)
            time.sleep(0.5)
            Redipaeerrorfolderpath = "C:\TestLogin\LoginErrorScreenshots\Redipaeloginerror"
            Redipaetimeformat = time.asctime().replace(":", "")
            Redipaeerrorimg = Redipaeerrorfolderpath + Redipaetimeformat + ".jpg"
            self.driver.get_screenshot_as_file(Redipaeerrorimg)
            L.error(redipaeerr)


            #HRMS
        HRMSurl = config.get('credentialsection', 'HRMSBaseurl')
        Hrmsuname = config.get('credentialsection', 'HRMSusername')
        hrmsepword = config.get('credentialsection', 'HRMSPassword')
        HRMScomp = config.get('credentialsection', 'HRMScompany')


        L.info("Hrms is Opened")
        self.driver.get(HRMSurl)
        L.info("Username is Entered")
        self.driver.find_element(By.ID, "txtUsername").send_keys(Hrmsuname)
        L.info("Password is Entered")
        self.driver.find_element(By.ID, "txtPassword").send_keys(hrmsepword)
        L.info("Company id is Entered")
        self.driver.find_element(By.ID, "txtClient").send_keys(HRMScomp)
        L.info("Submit button is clicked")
        self.driver.find_element(By.ID, "btnLogin").click()
        L.info(HRMSurl)
        L.info(Hrmsuname)
        L.info(hrmsepword)
        L.info(HRMScomp)

        Hrmserr = ''
        hrmssayingmsg = ''

        try:
            Hrmserr = self.driver.find_element(By.ID, "lblError").text
            L.error(Hrmserr)

        except:

            L.info("Onboard is clicked")
            self.driver.find_element(By.XPATH, "//*[text()='OnBoard']").click()
            L.info("Add Ob Employee is clicked")
            self.driver.find_element(By.XPATH, "//*[text()='Add OB Employee']").click()
            time.sleep(1)
            HRMSfolderpath = "C:\TestLogin\Screenshots\HRMSLogin"
            HRMStimeformat = time.asctime().replace(":", "")
            hrmsimg = HRMSfolderpath + HRMStimeformat + ".png"
            L.info("HRMS Screenshot is Captured")
            self.driver.get_screenshot_as_file(hrmsimg)
            hrmssayingmsg = 'HRMS Login Successfully'
            print(hrmssayingmsg)
            L.info(hrmssayingmsg)


        if (Hrmserr == "Wrong Username or Password!"):
            HRMSWpmsg = ('HRMS Says:: [' + Hrmserr + ']')
            print(HRMSWpmsg)
            time.sleep(0.5)
            HRMSerrorfolderpath = "C:\TestLogin\LoginErrorScreenshots\HRMSLoginerror"
            HRMStimeformat = time.asctime().replace(":", "")
            hrmserrorimg = HRMSerrorfolderpath + HRMStimeformat + ".jpg"
            L.info("HRMS Failure Screen shot is captured")
            self.driver.get_screenshot_as_file(hrmserrorimg)
            L.error(Hrmserr)

            # Payroll
        # payrollurl = config.get('credentialsection', 'PayrollBaseurl')
        # payrolluname = config.get('credentialsection', 'Payrolluseranme')
        # payrollepword = config.get('credentialsection', 'Payrollpassword')
        # payrollcomp = config.get('credentialsection', 'Payrollcompany')
        #
        # L.info("Payroll is Opened")
        # self.driver.get(payrollurl)
        # L.info("Payroll USername is Entered")
        # self.driver.find_element(By.ID, "txtUsername").send_keys(payrolluname)
        # L.info("Payroll Password is Entered")
        # self.driver.find_element(By.ID, "txtPassword").send_keys(payrollepword)
        # L.info("Payroll Company is Entered")
        # self.driver.find_element(By.ID, "txtClient").send_keys(payrollcomp)
        # L.info("Submit button is Clicked")
        # self.driver.find_element(By.ID, "btnLogin").click()
        # L.info(payrollurl)
        # L.info(payrolluname)
        # L.info(payrollepword)
        # L.info(payrollcomp)
        #
        # Payrollerr = ''
        # payrollsayingmsg = ''
        #
        # try:
        #     Payrollerr = self.driver.find_element(By.ID, "lblError").text
        #     L.error(Payrollerr)
        #
        # except:
        #      L.info("FoRm is clicked")
        #      self.driver.find_element(By.XPATH, "//*[@id='aspnetForm']/div[4]/div[1]/div/div[2]/ul/li/a").click()
        #      L.info("Designation master is clicked")
        #      self.driver.find_element(By.XPATH, "//*[@href='DesignationMaster.aspx']").click()
        #      time.sleep(1)
        #      Payrollimgfolderpath = "C:\TestLogin\Screenshots\PayrollLogin"
        #      payrolltimeformat = time.asctime().replace(":", "")
        #      Payrollimg = Payrollimgfolderpath + payrolltimeformat + ".jpg"
        #      L.info("Payroll Screenshot captured Sucessfully")
        #      self.driver.get_screenshot_as_file(Payrollimg)
        #      payrollsayingmsg = "Payroll Login successfully"
        #      print(payrollsayingmsg)
        #      L.info(payrollsayingmsg)
        #
        # if (Payrollerr == "Wrong Username or Password!"):
        #     Payrollwpmsg = ("Payroll Says :: [" + Payrollerr + "]")
        #     print(Payrollwpmsg)
        #     time.sleep(0.5)
        #     Payrollerrorimgfolderpath = "C:\TestLogin\LoginErrorScreenshots\PayrollLoginerror"
        #     payrolltimeformat = time.asctime().replace(":", "")
        #     Payrollerrorimg = Payrollerrorimgfolderpath + payrolltimeformat + ".jpg"
        #     L.info("Payroll Failure screenshot is Captured")
        #     self.driver.get_screenshot_as_file(Payrollerrorimg)
        #     L.error(Payrollerr)

            # FrameX
        Frameurl = config.get('credentialsection', 'FramexBaseurl')
        Frameuname = config.get('credentialsection', 'FramexUsername')
        Framepword = config.get('credentialsection', 'FramexPassword')
        Framecomp = config.get('credentialsection', 'Framexcompany')

        L.info("Framex is Opened")
        self.driver.get(Frameurl)
        L.info("Username is Entered")
        self.driver.find_element(By.ID, "txtUserName").send_keys(Frameuname)
        L.info("Password is Entered")
        self.driver.find_element(By.ID, "txtPassword").send_keys(Framepword)
        L.info("company name is Entered")
        self.driver.find_element(By.ID, "txt_projectname").send_keys(Framecomp)
        self.driver.find_element(By.ID, "btnLogin").click()
        L.info(Frameurl)
        L.info(Frameuname)
        L.info(Framepword)
        L.info(Framecomp)

        frameerr = ''
        framesayingmsg = ''

        try:
            frameerr = self.driver.find_element(By.ID, 'lblmsg').text
            L.error(frameerr)

        except:

            L.info("Button is Clicked")
            self.driver.find_element(By.XPATH, "//*[@id='left-menu']/ul/li[1]/a/span").click()
            time.sleep(3)
            frameximgfolderpath = "C:\TestLogin\Screenshots\FrameLogin"
            frametimeformat = time.asctime().replace(":", "")
            frameximg = frameximgfolderpath + frametimeformat + ".png"
            L.info("Framex Screenshot is captured")
            self.driver.get_screenshot_as_file(frameximg)
            framesayingmsg = "Framex Login successfully"
            print(framesayingmsg)
            L.info(framesayingmsg)

        if (frameerr == 'The Username or Password you entered isn`t correct. Please try again.'):
            framexwpmsg = ("FrameX Says :: [" + frameerr + ']')
            print(framexwpmsg)
            time.sleep(0.5)
            framexerrorimgfolderpath = 'C:\TestLogin\LoginErrorScreenshots\FrameLoginerror'
            frametimeformat = time.asctime().replace(":", "")
            frameXerrimg = framexerrorimgfolderpath + frametimeformat + ".jpg"
            L.info("Framex Failure screenshot captured Successfully")
            self.driver.get_screenshot_as_file(frameXerrimg)
            L.error(frameerr)

            # Vendo
        vendourl = config.get('credentialsection', 'vendobaseurl')
        Vendouname = config.get('credentialsection', 'vendousername')
        vendopword = config.get('credentialsection', 'vendopassword')

        L.info("Vendo opened Successfully")
        self.driver.get(vendourl)
        L.info("Username is Entered")
        self.driver.find_element(By.NAME, "username").send_keys(Vendouname)
        L.info("Password is Entered")
        self.driver.find_element(By.NAME, "password").send_keys(vendopword)
        L.info("Submit is Clicked")
        self.driver.find_element(By.XPATH, "//*[@ng-click='login()']").click()
        time.sleep(1)
        L.info(vendourl)
        L.info(Vendouname)
        L.info(vendopword)


        vendoerr = ''
        vendosayingmsg = ''
        vendowpmsg = ''

        try:
            vendoerr = self.driver.find_element(By.XPATH,"//*[text()='Invalid Username.' or text()='Invalid Password.']").text
            L.error(vendoerr)

        except:
            L.info("Lookup is clicked")
            self.driver.find_element(By.XPATH, "//i[@class='zmdi zmdi-plus-circle-o-duplicate']").click()
            time.sleep(1)
            vendoimgfolderpath = "C:\TestLogin\Screenshots\Vendologin"
            vendotimeformat = time.asctime().replace(":", "")
            vendoimg = vendoimgfolderpath + vendotimeformat + ".png"
            L.info("Vendo Screenshot is Captured")
            self.driver.get_screenshot_as_file(vendoimg)
            vendosayingmsg = "Vendo login successfully"
            print(vendosayingmsg)
            L.info(vendosayingmsg)

        if (vendoerr == 'Invalid Username.'):
            vendowpmsg = ('Vendo Says :: [' + vendoerr + ']')
            print(vendowpmsg)
            time.sleep(0.5)
            vendoerrimgfolderpath = "C:\TestLogin\LoginErrorScreenshots\Vendologinerror"
            vendotimeformat = time.asctime().replace(":", "")
            vendounerrimg = vendoerrimgfolderpath + vendotimeformat + ".jpg"
            self.driver.get_screenshot_as_file(vendounerrimg)
            L.error(vendoerr)
        elif (vendoerr == 'Invalid Password.'):
            vendowpmsg = ('Vendo Says :: [' + vendoerr + ']')
            print(vendowpmsg)
            time.sleep(0.5)
            vendoerrimgfolderpath = "C:\TestLogin\LoginErrorScreenshots\Vendologinerror"
            vendotimeformat = time.asctime().replace(":", "")
            vendopwerrimg = vendoerrimgfolderpath + vendotimeformat + ".jpg"
            self.driver.get_screenshot_as_file(vendopwerrimg)
            L.error(vendoerr)

        # self.driver.get(Bandhubaseurl)
        # self.driver.find_element(By.ID, "username").send_keys(Bandhuusername)
        # self.driver.find_element(By.ID, "password").send_keys(Bandhupassword)
        # self.driver.find_element(By.ID, 'clientid').send_keys(Bandhucompany)
        # self.driver.find_element(By.ID, "BtnLogIn").click()
        # time.sleep(1)

        # bandhuerr = ''
        # bandhusayingmsg = ''

        # try:
        #  err = self.driver.switch_to.alert
        # bandhuerr = err.text

        # except:

        # self.driver.find_element(By.XPATH, "//*[text()='Onboard Approval']").click()
        # time.sleep(1)
        # bandhuimgfolderpath ="C:\TestLogin\Screenshots\BandhuHRlogin"
        # bandhutimeformat = time.asctime().replace(":","")
        # bandhuimg = bandhuimgfolderpath+bandhutimeformat+".jpg"
        # self.driver.get_screenshot_as_file(bandhuimg)
        # bandhusayingmsg = "BandhuHR login successfully"
        # print(bandhusayingmsg)
        # L.info(bandhusayingmsg)

        # if(bandhuerr=="UserName and Password isn't correct. Please try again"):
        #   bandhuwpmsg = ("Bandhu HR Says :: ["+bandhuerr+"]")
        #  print(bandhuwpmsg)
        # bandhuerrimgfolderpath = "C:\TestLogin\LoginErrorScreenshots\Bandhuerror1"
        # bandhutimeformat  = time.asctime().replace(":","")
        # bandhuerrimg = bandhuerrimgfolderpath+bandhutimeformat+".jpg"
        # self.driver.switch_to.alert.accept()

        # self.driver.get_screenshot_as_file(bandhuerrimg)
        # L.error(bandhuerr)



        # Entering Whatsapp

        WhatsappURl = config.get('credentialsection', 'WhatsappBaseurl')
        L.info("Whatsapp is Opened")
        self.driver.get(WhatsappURl)
        time.sleep(10)
        L.info("DevTeam Fieldlytics is clicked")
        #L.info(self.driver.find_element(By.XPATH,"//*[@title='Sandy']").click())
        #L.info(self.driver.find_element(By.XPATH, "//*[@title=\"Code Fieldlytics\"]").click())
        L.info(self.driver.find_element(By.XPATH, "//*[@title='DevTeam-Fieldlytics(PPMS)']").click())
        L.info("Add Button is clicked")
        L.info(self.driver.find_element(By.XPATH, " //*[@data-icon=\"clip\"]").click())
        time.sleep(2)
        L.info("Attach button is Clicked")
        self.driver.find_element(By.XPATH, " //*[@data-testid='attach-image']").click()

        if (Redipaesayingmsg == "Redipae Login successfully"):
            time.sleep(1)
            path = uiautomation.EditControl(Name="File name:")
            path.SetFocus()
            path.SendKeys(Redipaeimg)  # file=filepath
            btn = uiautomation.ButtonControl(Name="Open")
            btn.SetFocus()
            fil = uiautomation.EditControl(Name="File name:")
            fil.SetFocus()
            fil.SendKeys('{Enter}')
            self.driver.find_element(By.XPATH, "//*[@title='Type a message']").send_keys('Redipae Successfully Logged in')
            L.info('Redipae Successfully Logged in')

        else:

            time.sleep(1)
            path = uiautomation.EditControl(Name="File name:")
            path.SetFocus()
            path.SendKeys(Redipaeerrorimg)  # file=filepath
            btn = uiautomation.ButtonControl(Name="Open")
            btn.SetFocus()
            fil = uiautomation.EditControl(Name="File name:")
            fil.SetFocus()
            fil.SendKeys('{Enter}')
            self.driver.find_element(By.XPATH, "//*[@title='Type a message']").send_keys(Redipaewpmsg)
            L.error(Redipaewpmsg)

        # HRMS
        if (hrmssayingmsg == 'HRMS Login Successfully'):

            L.info(self.driver.find_element(By.XPATH, "//*[@data-testid='add-alt']").click())
            time.sleep(1)
            path = uiautomation.EditControl(Name="File name:")
            path.SetFocus()
            path.SendKeys(hrmsimg)  # file=filepath
            btn = uiautomation.ButtonControl(Name="Open")
            btn.SetFocus()
            fil = uiautomation.EditControl(Name="File name:")
            fil.SetFocus()
            fil.SendKeys('{Enter}')
            self.driver.find_element(By.XPATH, "//*[@title='Type a message']").send_keys('HRMS Successfully Logged in')
            L.info("HRMS Successfully Logged in")

        # HRMSError
        else:
            L.info(self.driver.find_element(By.XPATH, "//*[@data-testid='add-alt']").click())
            time.sleep(1)
            path = uiautomation.EditControl(Name="File name:")
            path.SetFocus()
            path.SendKeys(hrmserrorimg)  # file=filepath
            btn = uiautomation.ButtonControl(Name="Open")
            btn.SetFocus()
            fil = uiautomation.EditControl(Name="File name:")
            fil.SetFocus()
            fil.SendKeys('{Enter}')
            time.sleep(1)
            self.driver.find_element(By.XPATH, "//*[@title='Type a message']").send_keys(HRMSWpmsg)
            L.error(HRMSWpmsg)

        # Payroll
    #     if (payrollsayingmsg == "Payroll Login successfully"):
    #
    #         L.info(self.driver.find_element(By.XPATH, "//*[@data-testid='add-alt']").click())
    #         time.sleep(1)
    #         path = uiautomation.EditControl(Name="File name:")
    #         path.SetFocus()
    #         path.SendKeys(Payrollimg)  # file=filepath
    #         btn = uiautomation.ButtonControl(Name="Open")
    #         btn.SetFocus()
    #         fil = uiautomation.EditControl(Name="File name:")
    #         fil.SetFocus()
    #         fil.SendKeys('{Enter}')
    #         time.sleep(1)
    #         self.driver.find_element(By.XPATH,"//*[@id='app']/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[2]").send_keys('Payroll Successfully Logged in')
    #         L.info("Payroll Successfully Logged in")
    #
    # # PayrollError
    #     else:
    #
    #        L.info(self.driver.find_element(By.XPATH, "//*[@data-testid='add-alt']").click())
    #        time.sleep(1)
    #        path = uiautomation.EditControl(Name="File name:")
    #        path.SetFocus()
    #        path.SendKeys(Payrollerrorimg)  # file=filepath
    #        btn = uiautomation.ButtonControl(Name="Open")
    #        btn.SetFocus()
    #        fil = uiautomation.EditControl(Name="File name:")
    #        fil.SetFocus()
    #        fil.SendKeys('{Enter}')
    #        time.sleep(1)
    #        self.driver.find_element(By.XPATH,"//*[@id='app']/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[2]").send_keys(Payrollwpmsg)
    #        L.error(Payrollwpmsg)

    # Framex

        if (framesayingmsg == "Framex Login successfully"):
           L.info(self.driver.find_element(By.XPATH, "//*[@data-testid='add-alt']").click())
           time.sleep(1)
           path = uiautomation.EditControl(Name="File name:")
           path.SetFocus()
           path.SendKeys(frameximg)  # file=filepath
           btn = uiautomation.ButtonControl(Name="Open")
           btn.SetFocus()
           fil = uiautomation.EditControl(Name="File name:")
           fil.SetFocus()
           fil.SendKeys('{Enter}')
           self.driver.find_element(By.XPATH, "//*[@title='Type a message']").send_keys('Framex Successfully Logged in')
           L.info("Framex Successfully Logged in")

    # FramexError
        else:
           L.info(self.driver.find_element(By.XPATH, "//*[@data-testid='add-alt']").click())
           time.sleep(1)
           path = uiautomation.EditControl(Name="File name:")
           path.SetFocus()
           path.SendKeys(frameXerrimg)  # file=filepath
           btn = uiautomation.ButtonControl(Name="Open")
           btn.SetFocus()
           fil = uiautomation.EditControl(Name="File name:")
           fil.SetFocus()
           fil.SendKeys('{Enter}')
           time.sleep(1)
           self.driver.find_element(By.XPATH, "//*[@title='Type a message']").send_keys(framexwpmsg)
           L.error(framexwpmsg)

    # Vendo
        if (vendosayingmsg == "Vendo login successfully"):

           L.info(self.driver.find_element(By.XPATH, "//*[@data-testid='add-alt']").click())
           time.sleep(1)
           path = uiautomation.EditControl(Name="File name:")
           path.SetFocus()
           path.SendKeys(vendoimg)  # file=filepath
           btn = uiautomation.ButtonControl(Name="Open")
           btn.SetFocus()
           fil = uiautomation.EditControl(Name="File name:")
           fil.SetFocus()
           fil.SendKeys('{Enter}')
           self.driver.find_element(By.XPATH, "//*[@title='Type a message']").send_keys('Vendo Successfully Logged in')
           L.info("Vendo Successfully Logged in")


    # Vendo not a valid username Error
        elif (vendoerr == 'Invalid Username.'):

           time.sleep(1)
           L.info(self.driver.find_element(By.XPATH, "//*[@data-testid='add-alt']").click())
           time.sleep(1)
           path = uiautomation.EditControl(Name="File name:")
           path.SetFocus()
           path.SendKeys(vendounerrimg)  # file=filepath
           btn = uiautomation.ButtonControl(Name="Open")
           btn.SetFocus()
           fil = uiautomation.EditControl(Name="File name:")
           fil.SetFocus()
           fil.SendKeys('{Enter}')
           self.driver.find_element(By.XPATH, "//*[@title='Type a message']").send_keys(vendowpmsg)
           L.error(vendowpmsg)


    # Vendo not a valid password Error
        elif (vendoerr == 'Invalid Password.'):

           time.sleep(1)
           L.info(self.driver.find_element(By.XPATH, "//*[@data-testid='add-alt']").click())
           time.sleep(1)
           path = uiautomation.EditControl(Name="File name:")
           path.SetFocus()
           path.SendKeys(vendopwerrimg)  # file=filepath
           btn = uiautomation.ButtonControl(Name="Open")
           btn.SetFocus()
           fil = uiautomation.EditControl(Name="File name:")
           fil.SetFocus()
           fil.SendKeys('{Enter}')
           time.sleep(1)
           self.driver.find_element(By.XPATH, "//*[@title='Type a message']").send_keys(vendowpmsg)
           L.error(vendowpmsg)

    # Bandhu
    # if(bandhusayingmsg=="BandhuHR login successfully"):

    #   self.driver.find_element(By.XPATH, "//*[@data-testid='add-alt']").click()

    #  time.sleep(1)
    # path = uiautomation.EditControl(Name="File name:")
    # path.SetFocus()
    # path.SendKeys(bandhuimg)  # file=filepath
    # btn = uiautomation.ButtonControl(Name="Open")
    # btn.SetFocus()
    # fil = uiautomation.EditControl(Name="File name:")
    # fil.SetFocus()
    # fil.SendKeys('{Enter}')
    # time.sleep(1)
    # self.driver.find_element(By.XPATH, "//*[@id='app']/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[2]").send_keys('BandhuHR Successfully Logged in')
    # L.info("BandhuHR Successfully Logged in")

    # BandhuError

    # else:
    #   self.driver.find_element(By.XPATH, "//*[@data-testid='add-alt']").click()
    #  time.sleep(1)
    # path = uiautomation.EditControl(Name="File name:")
    # path.SetFocus()
    # path.SendKeys(bandhuerrimg)  # file=filepath
    # btn = uiautomation.ButtonControl(Name="Open")
    # btn.SetFocus()
    # fil = uiautomation.EditControl(Name="File name:")
    # fil.SetFocus()
    # fil.SendKeys('{Enter}')
    # self.driver.find_element(By.XPATH, "//*[@id='app']/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[2]").send_keys(bandhuwpmsg)
    # L.error(bandhuwpmsg)

    # self.driver.find_element(By.CSS_SELECTOR, "div[class='_1UWac Z2O8p oHEu9 focused'] div[role='textbox']").send_keys(Message)
        self.driver.find_element(By.CSS_SELECTOR, "span[data-testid='send']").click()
        L.info(print('Message sent successfully'))
        time.sleep(10)

    @classmethod
    def tearDownClass(cls):
        #cls.driver.close()
        print("Login Test is completed")


if __name__ == "__main__":
    unittest.main()