from bs4 import BeautifulSoup
import re
import requests as rq
import csv
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties

school=[]              # 宣告school為空list
fi=open("schools.txt","r")      # find schools.txt and is read mode存到fi
m=fi.read()            # fi read後 存到m
k=m.split('\n')        # 讀取學校後存成k list
school.extend(k)       # k list 存入 school list
school_list=[]
school_num=[]
state_num=[]

# creating class
class State:
    def __init__(self, state_name, lontitude, latitude):
        self.state_name = state_name
        self.lontitude = lontitude
        self.latitude = latitude

california = State('California', -120.092522, 36.593516 )
Illinois = State('California', -89.639413, 40.200705 )
Indiana = State('Indiana', -86.081059, 40.199605)
Michigan = State('Michigan', -84.913973, 43.829168)
Minnesota = State('Minnesota', -93.166219, 45.081207)
Massachusetts = State('Massachusetts', -72.022514, 42.340703)
New_York = State('New York', -75.536305, 42.783398)
Texas = State('Texas', -98.993774, 31.603828)
North_Carolina = State('North Carolina', -79.009322, 35.57369)
Missouri = State('Missouri', -92.061038, 38.324025)
London = State('London', -0.112721, 51.542689)
Goettingen = State('Goettingen', 9.937336, 51.540792)
Aachen = State('Aachen', 6.065724, 50.781614)
Munich = State('Munich', 11.550037, 48.158233)
Hamburg = State('Hamburg', 9.969572, 53.463551)
Stuttgart = State('Stuttgart', 9.193388, 48.785312)
Dortmund = State('Dortmund', 7.414254, 51.484394)
Dresden = State('Dresden', 13.735818, 51.028479)
UofT = State('UofT', -79.395506, 43.663093)
McGill = State('McGill', -73.576287, 45.50504)
Singapore = State('Singapore', 103.890882, 1.352426)

final_list=[]
for i in range(len(school)):    # 知道幾間學校後，跑幾次迴圈
    url="https://www.ptt.cc/bbs/studyabroad/search?&q="+school[i]
    school_list.append(url)


for i in range(len(school_list)):
    response = rq.get(school_list[i])
    soup = BeautifulSoup(response.text, "html.parser")  # 指定parser 作為解析器
    # print(soup.prettify())                 # 把排版後的 html 印出來

    sel = soup.select("div.title a")  # 取HTML標中的 <div class="title"></div> 中的<a>標籤存入sel
    num = 1
    print(type(sel))
    while rq.get(url):


        for s in sel:
             print(num, ".  ")
             print(s.text)
             print("https://www.ptt.cc/" + s["href"])
             print("---------------------------------------")
             num += 1
        print("-----------------換頁-------------------")
        try:
            next_page1 = soup.select("div.btn-group.btn-group-paging a")
            url = "https://www.ptt.cc" + next_page1[1]["href"]

            response = rq.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            sel = soup.select("div.title a")
        except:
            pass
            break
    school_num.append(num)
      # print(school_num)
    print('各大學的查詢熱度',school[i],': ',num)


# state的list希望可以以更簡潔扼要的方式去寫
state_num.append(school_num[0]+school_num[1]+school_num[2]+school_num[3]+\
                 school_num[4]+school_num[5]+school_num[6]+school_num[7]+school_num[8])
state_num.append(school_num[9]+school_num[10]+school_num[11])
state_num.append(school_num[12]+school_num[13])
state_num.append(school_num[14]+school_num[15]+school_num[16])
state_num.append(school_num[17]+school_num[18]+school_num[19])
state_num.append(school_num[20]+school_num[21]+school_num[22])
state_num.append(school_num[23]+school_num[24]+school_num[25]+\
                 school_num[26]+school_num[27])
state_num.append(school_num[28]+school_num[29]+school_num[30])
state_num.append(school_num[31])
state_num.append(school_num[32])
state_num.append(school_num[33]+school_num[34]+school_num[35]+school_num[36]+school_num[37]+\
                 school_num[38]+school_num[39]+school_num[40])
state_num.append(school_num[41]+school_num[42]+school_num[43])
state_num.append(school_num[44]+school_num[45+school_num[46]])
state_num.append(school_num[47]+school_num[48]+school_num[49]+school_num[50]+school_num[51])
state_num.append(school_num[52]+school_num[53])
state_num.append(school_num[54]+school_num[55])
state_num.append(school_num[56])
state_num.append(school_num[57])
state_num.append(school_num[58])
state_num.append(school_num[59])
state_num.append(school_num[60]+school_num[61]+school_num[62])

print(state_num)
    #import pandas as pd

    #result=[school[i],num]
    #with open('result.csv','r')as f:
     # writer=csv.writer(f)
      #writer.writerow(result)
    #list=[[school[i],num]]
    #test=pd.DataFrame(data=list)
    #df.loc[] = '3'
    #print(test)
    #test.to_csv('result.csv',encoding='gbk',header=0,index=0)





for i in range(len(area_list)):      #匯出txt
    #print(str(area_list[i])+','+str(state_num[i])+','+str(coordinate_x[i])+','+str(coordinate_y[i]))
    file1=open("final.txt","a")
    file1.write(str(area_list[i])+','+str(state_num[i])+','+str(coordinate_x[i])+','+str(coordinate_y[i])+'\n')
    file1.close()


    '''final_list.append(str(area_list[i]))
    final_list.append(str(state_num[i]))
    final_list.append(str(coordinate_x[i]))
    final_list.append(str(coordinate_y[i]))'''

'''file1=open("final.txt","a")
file1.write(final_list)
file1.close()'''