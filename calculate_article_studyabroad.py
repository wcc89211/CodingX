from bs4 import BeautifulSoup
import requests as rq

school = []
school_file = open("C:/Users/oscar/Desktop/codingx_practice/CodingX/schools.txt","r")  # find schools.txt and is read mode存到fi
school_file_content = school_file.read()  # read the file and extract the content
school_name = school_file_content.split('\n')  #split the content and seperate with \n
school.extend(school_name)  # save the school name into list (school)

state_file = open('C:/Users/oscar/Desktop/codingx_practice/Refactoring/state_detail.txt',"r") 
state_file_content = state_file.read()
state_detail = state_file_content.split('\n')

for i in range(len(state_detail)):
    state_detail[i] = state_detail[i].split(',')
    for j in range(1,5):
        state_detail[i][j] = eval(state_detail[i][j])

class State:
    def __init__(self, state_name, lontitude, latitude, range_lower, range_upper):
        self.state_name = state_name
        self.lontitude = lontitude
        self.latitude = latitude
        self.range = range(range_lower,range_upper)

state_list = []
for i in range(0,21):
    state_list.append( State(state_detail[i][0], state_detail[i][1], state_detail[i][2], state_detail[i][3], state_detail[i][4]) )

school_list = []
for i in range(len(school)):    # 知道幾間學校後，跑幾次迴圈
    url = "https://www.ptt.cc/bbs/studyabroad/search?&q="+school[i]
    school_list.append(url)

school_num = []
for i in range(len(school_list)):
    response = rq.get(school_list[i])
    soup = BeautifulSoup(response.text, "html.parser")  # 指定parser 作為解析器
    title = soup.select("div.title a")  # 取HTML標中的 <div class="title"></div> 中的<a>標籤存入title
    num = 1
    while rq.get(url):
        for s in title:
             num += 1
        try:
            next_page1 = soup.select("div.btn-group.btn-group-paging a")
            url = "https://www.ptt.cc" + next_page1[1]["href"]
            response = rq.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            title = soup.select("div.title a")
        except:
            pass
            break
    school_num.append(num)
    print('各大學的查詢熱度',school[i],': ',num)

state_num = []
for i in range(len(state_list)):
    total_num = 0
    for j in state_list[i].range:
        total_num = total_num + school_num[j]
    state_num.append(total_num)

for i in range(len(state_list)):  #export the result into file1 (final.txt)
    file1=open("C:/Users/oscar/Desktop/codingx_practice/Refactoring/final.txt","a")
    file1.write(str(state_list[i].state_name)+','+str(state_num[i])+','+str(state_list[i].lontitude)+','+str(state_list[i].latitude)+'\n')
    file1.close()