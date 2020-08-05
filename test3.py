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
area_list=['California', 'Illinois', 'Indiana', 'Michigan', 'Minnesota', 'Massachusetts', 'New York'\
    , 'Texas', 'North Carolina', 'Missouri', 'London', 'Goettingen', 'Aachen', 'Munich', 'Hamburg', 'Stuttgart'\
    ,'Dortmund','Dresden', 'UofT','McGill','Singapore']
coordinate_x = [-120.092522,-89.639413,-86.081059,-84.913973,-93.166219,-72.022514,\
                -75.536305,-98.993774,-79.009322,-92.061038,-0.112721,9.937336,6.065724,11.550037,\
              9.969572,9.193388,7.414254,13.735818,-79.395506,-73.576287,103.890882]
coordinate_y=[36.593516,40.200705,40.199605,43.829168,45.081207,42.340703,42.783398,\
              31.603828,35.57369,38.324025,51.542689,51.540792,50.781614,48.158233,53.463551,\
              48.785312,51.484394,51.028479,43.663093,45.50504,1.352426]
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