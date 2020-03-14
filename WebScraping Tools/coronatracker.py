from bs4 import BeautifulSoup as bs
import requests as req
import smtplib

URL = "https://www.worldometers.info/coronavirus/"
r = req.get(URL)
soup = bs(r.content, 'html.parser')
numbers = soup.find_all('div', attrs={'class':'maincounter-number'})
tables = soup.find_all('td')
print("COVID-19 Statistics Tracker \n\n")
print("Number of infected cases: {}".format(numbers[0].text))
print("Number of death cases: {}".format(numbers[1].text))
print("Number of recovery cases: {}".format(numbers[2].text))
deaths = numbers[1].text.strip(' ')
deaths_n = deaths.replace(',', '')
recovery_num = numbers[2].text.strip(' ')
rec_n = recovery_num.replace(',', '')
ratio = int(rec_n)/int(deaths_n)
victims_nepal = tables[1135].text.strip(' ')
v_n_strip = victims_nepal.replace(',', '')

print("Recovery to Death ratio is "+str(round(ratio))+":1")
print("Victims in "+str(tables[1134].text.strip(' '))+": {}".format(victims_nepal))
print("\nSource: Worldometers")

if int(deaths_n) > 6200:
    gmail_user = 'my_email'
    gmail_password = 'my_gmail_password'

    sent_from = gmail_user
    to = ['shashankdutt7@gmail.com', 'rohanu25@gmail.com']
    subject = 'COVID-19 Death Toll crossed 6000!'
    body = 'More than 6000 people died of coronavirus!'
    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print ('Email sent!')
    except:
        print ('Something went wrong...')
if int(v_n_strip) > 1:
    gmail_user = 'rohaniam777@gmail.com'
    gmail_password = 'silicosis'

    sent_from = gmail_user
    to = ['shashankdutt7@gmail.com', 'rohanu25@gmail.com']
    subject = 'COVID-19 - New victim in Nepal'
    body = 'New victim of Coronavirus found in Nepal. Stay safe!'
    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print ('Email sent!')
    except:
        print ('Something went wrong...')


input()
