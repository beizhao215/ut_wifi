import urllib2
from bs4 import BeautifulSoup
import re
import time
import sys
import mysql


class Spider:

    def __init__(self):
        self.name = "spider"
        self.mysql = mysql.Mysql()

    def main(self):
        current_time = time.strftime(('%Y-%m-%d %H:%M:%S'), time.localtime(time.time()))
        map_page = urllib2.urlopen('http://maps.wireless.utoronto.ca/stg/index.php?from=timeline&isappinstalled=0').read()
        map_page = BeautifulSoup(map_page, "html.parser")
        d = dict()
        for each in map_page.find_all('area'):
            alt = str(each.get('alt'))
            coords = str(each.get('coords'))
            d[alt] = coords

        for key, value in d.iteritems():

            item_dict = dict()

            content = urllib2.urlopen('http://maps.wireless.utoronto.ca/stg/popUp.php?name='+key).read()

            content = BeautifulSoup(content, "html.parser")

            bq_content = content.find_all("bq")    #get all content with bq tag

            text = str(bq_content[0].get_text())   #unicode to string

            nums = re.findall(r"[-+]?\d*\.\d+|\d+", str(text))

            item_dict["coords"] = value

            item_dict["num_connection"] = nums[0]

            if len(nums) == 1:
                nums.append('0')

            item_dict["num_active_access_points"] = nums[1]

            if len(nums) == 2:
                nums.append('0')

            item_dict["num_total_access_points"] = nums[2]

            if len(nums) == 3:
                nums.append('0')

            item_dict["num_conn_per_ap"] = nums[3]

            item_dict["name"] = str(content.find('center').contents[0])

            item_dict["alt"] = key

            item_dict["time"] = current_time

            self.mysql.insertData("utwifi", item_dict)

            f_handler = open('out.log', 'w')
            sys.stdout = f_handler
            print time

        #     item.append(nums)
        #     item.append(name)
        #     result[key] = item
        #
        # print result

spider = Spider()



spider.main()
