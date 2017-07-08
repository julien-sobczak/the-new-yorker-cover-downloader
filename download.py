#!/bin/env python3

import datetime
import requests
import sys
import shutil


def print_link(date):  
    link = "http://images.archives.newyorker.com/rvimageserver/Conde%20Nast/New%20Yorker/" + date.strftime("%Y_%m_%d") + "/page0000001.jpg?type=1&width=4880&quality=70"
    print('<a href="%s" target="_tab">Issue %s</a><br/>' % (link, date.strftime("%Y-%m-%d")))


def download_link(date):
    filename = 'cover-' + date.strftime("%Y-%m-%d") + '.jpg'
    print(filename)
    url = "http://images.archives.newyorker.com/rvimageserver/Conde%20Nast/New%20Yorker/" + date.strftime("%Y_%m_%d") + "/page0000001.jpg?type=1&width=4880&quality=70"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "fr-FR,fr;q=0.8,en-US;q=0.6,en;q=0.4",
       # "Connection": "keep-alive",
        "Cookie": "AMCVS_F7093025512D2B690A490D44%40AdobeOrg=1; s_vi=[CS]v1|2CABD74D05310C16-40000109800031EB[CE]; AMCV_F7093025512D2B690A490D44%40AdobeOrg=102365995%7CMCIDTS%7C17349%7CMCMID%7C41442994571598590553272366333680048503%7CMCAAMLH-1499523349%7C6%7CMCAAMB-1499523352%7CNRX38WO0n5BH8Th-nqAG_A%7CMCOPTOUT-1498925749s%7CNONE%7CMCAID%7C2CABD74D05310C16-40000109800031EB%7CMCSYNCSOP%7C411-17356%7CvVersion%7C2.2.0; __ibxl=1; _dr=https%3A%2F%2Fwww.google.fr%2F; timeSpent=1498918661798; s_cc=true; s_nr=1498918668966-New; v30=google.fr; v39=google.fr; s_sq=conde-newyorker%3D%2526c.%2526a.%2526activitymap.%2526page%253Darchive%2526link%253DBROWSE%252520ALL%252520ISSUES%2526region%253Dapp-root%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Darchive%2526pidt%253D1%2526oid%253Dhttp%25253A%25252F%25252Farchives.newyorker.com%25252F%2526ot%253DA; _parsely_slot_click={%22url%22:%22http://www.newyorker.com/archive%22%2C%22x%22:701%2C%22y%22:390%2C%22xpath%22:%22//*[@id=%5C%22app-root%5C%22]/div[2]/main[1]/section[1]/div[2]/nav[1]/a[1]%22%2C%22href%22:%22http://archives.newyorker.com/%22}; _parsely_visitor={%22id%22:%2227598b2d-25e0-404c-b731-a11c3fb8034e%22%2C%22session_count%22:1%2C%22last_session_ts%22:1498918553985}; SID=web01; OSID=web01; computerid=5e974520-c882-4002-bc9d-391fd29fb1ff; zezzion=0; RVKernel.User.UserGUID=5C045A75-AFF1-6BA5-D23C-EFC1B03BFDE5; dummy_test_cookie=OK; __utma=26165485.234499121.1498918671.1498918671.1498918671.1; __utmc=26165485; __utmz=26165485.1498918671.1.1.utmcsr=newyorker.com|utmccn=(referral)|utmcmd=referral|utmcct=/archive; zezzionTimeout=Jul 02 2017 16:29:42 GMT",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    }
    response = requests.get(url, headers=headers, stream=True)
    with open('downloads/' + filename, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response

def main():

    cur_date = datetime.datetime(1925, 2, 21)  # TODO 
    mid_date = datetime.datetime(1973, 7, 2)
    end_date = datetime.datetime.now()

    while cur_date < mid_date - datetime.timedelta(days=7): 
        download_link(cur_date)
        cur_date += datetime.timedelta(days=7)
    
    cur_date = mid_date
    print("=======================================")
    while cur_date < end_date:
        download_link(cur_date)
        cur_date += datetime.timedelta(days=7)


if __name__ == "__main__":
    main()
