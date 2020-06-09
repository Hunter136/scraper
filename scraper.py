import requests, bs4, smtplib, time, urllib3
lyst = [] # for adding all project urls to list
#make a second class that inherits this one and just calls methods from this one so it looks clean, so you can do as many
#scrapes as you want
#perhaps look at the operator module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
#where to add selenium
#need to get url for each post in reddit page
#how to look for certain words and to get the urls for the project
#dealing with files as attributes, or making a file an atrribute or email login
class scraper():
    def __init__(self, driver, email="", url=None ): #file is where thing will be output to,
        self.url = url
        self.driver = driver
        self.email = email
    def setfile(self):#how do you make an email and add things to it???
        file2 = str(input("enter where you want this output to, then if you want an email or word doc of it, !!"))
        emailorword = input()
        if emailorword == "email" :
            password = str(input("what is your password for your email"))
            smtpobj = smtplib.SMTP('smtp.gmail.com', 587)# HAS TO BE A GMAIL
            self.email = file2
            print("Your logged into your email!")
            return smtpobj, file2, password
        else:
            file1 = open(file2, 'wb')
            print("you have a file ready to write the urls to!")#just a text file
            return file1
   # def setfilereader(self): #sets the file to be read and written for requests and to write the urls
        # to this class list
       # self.filereader = 'fileread.docx'
    def seturl(self):#sets object url
        self.url = str('https://www.reddit.com/')
    def getrequest(self):
        print("we are now requesting the website to be scraped")
        site = requests.get(self.url)# do we need to do something with the command line
    """def formatter(self,file):
        file = open(self.filereader, 'wb')
        def decorate(self, *args):
            r= 1
            for i in lyst:
                file.write("URL #%s" + i +" !" + '/n' % r)
                r+= 1
            return"it is written"
        file.close()
        """
    def selene(self):#this method goes to reddti page, goes to filter button types in arduino or whatever input
        #goes to r/arduino opens links of first 3 links with look what i did badge on it
        options = Options()
        options.headless = True#headless means the browser does work, but the windown doesnt open up on your screen
        self.driver = webdriver.Chrome(options=options, executable_path=r'')#need the rest for headless
        self.driver.get(self.url)
        elem = self.driver.find_elem_by_tag('button')
        elem.click()
        elem.send_keys("arduino")#should be chagned for any reddit page
        elem.send_keys(Keys.ENTER)
        time.sleep(2)
        for i in range(0,2):
            elem2 = self.driver.find_elem_by_id('a')# how to open links on a webpage
            # and to follow links to get new info
            self.driver.switch_to(elem2)#this may not be right
            word =  input("how long you wanna view the page in seconds please!")
            time.sleep(word)
        self.driver.quit()
    def soupIt(self,site):#this method gets all urls to the lyst list
        soup = bs4.BeautifulSoup(site.text, 'html.parser')
        for i in range(0,9):
            #else if soup.find() #if it has a look what i made button do it, or if it has the word project in it do it
            i = i +1
            domain = soup.find("a").attrs('href')
            time.sleep(2)
            if domain.contains('project') or domain.contains(soup.find("span", class_= '1jNP13YUk6zbpLWdjaJT1r')):
                lyst.append(domain)
        #this line looks up certain html characteristics of the title of each reddit post
        #keywords are going to be project, smart mirror, robot, led, coolness scale from in order is 5,8,8,4
    def writeToEmail(self, smtpobj, file2, password):#this method will write whatever is in lyst to email.
        #print(type(smtpobj))
        print(smtpobj.ehlo())  # 250 means success put first or else will fail code
        smtpobj.starttls()
        smtpobj.login(file2, password)
        print('writing to email now!')
        senderemail = input("input an email to send it to!")
        message = lyst
        smtpobj.sendmail(senderemail, self.email, message)#this line sends the email
def main():
    print('yes')
    object1 = scraper()
    object1.geturl()
    smtpobj, file2, password = object1.setfile()
    site = object1.getrequest()
    object1.selene()
    object1.soupit(site)
    object1.writeToEmail(smtpobj, file2, password)

if __name__ == "__main__":
    main()