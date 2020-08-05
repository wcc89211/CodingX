from bs4 import BeautifulSoup
import requests as rq

school = []
file = open("C:/Users/oscar/Desktop/codingx_practice/CodingX/schools.txt","r")  # find schools.txt and is read mode存到fi
file_content = file.read()  # read the file and extract the content
school_name = file_content.split('\n')  #split the content and seperate with \n
school.extend(school_name)  # save the school name into list (school)

# creating class
class State:
    def __init__(self, state_name, lontitude, latitude, range_lower, range_upper):
        self.state_name = state_name
        self.lontitude = lontitude
        self.latitude = latitude
        self.range = range(range_lower,range_upper)

state_list = []  # append the state attribute to the state_list
state_list.append( State('California', -120.092522, 36.593516, 0, 9) )
state_list.append( State('Illinios', -89.639413, 40.200705, 9, 12) )
state_list.append( State('Indiana', -86.081059, 40.199605, 12, 14) )
state_list.append( State('Michigan', -84.913973, 43.829168, 14, 17) )
state_list.append( State('Minnesota', -93.166219, 45.081207, 17, 20) )
state_list.append( State('Massachusetts', -72.022514, 42.340703, 20, 23) )
state_list.append( State('New York', -75.536305, 42.783398, 23, 28) )
state_list.append( State('Texas', -98.993774, 31.603828, 28, 31) )
state_list.append( State('North Carolina', -79.009322, 35.57369, 31, 32) )
state_list.append( State('Missouri', -92.061038, 38.324025, 32, 33) )
state_list.append( State('London', -0.112721, 51.542689, 33, 41) )
state_list.append( State('Goettingen', 9.937336, 51.540792, 41, 44) )
state_list.append( State('Aachen', 6.065724, 50.781614, 44, 47) )
state_list.append( State('Munich', 11.550037, 48.158233, 47, 52) )
state_list.append( State('Hamburg', 9.969572, 53.463551, 52, 54) )
state_list.append( State('Stuttgart', 9.193388, 48.785312, 54, 56) )
state_list.append( State('Dortmund', 7.414254, 51.484394, 56, 57) )
state_list.append( State('Dresden', 13.735818, 51.028479, 57, 58) )
state_list.append( State('UofT', -79.395506, 43.663093, 58, 59) )
state_list.append( State('McGill', -73.576287, 45.50504, 59, 60) )
state_list.append( State('Singapore', 103.890882, 1.352426, 60, 63) )

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
    file1=open("C:/Users/oscar/Desktop/codingx_practice/reconstruction_prac/final.txt","a")
    file1.write(str(state_list[i].state_name)+','+str(state_num[i])+','+str(state_list[i].lontitude)+','+str(state_list[i].latitude)+'\n')
    file1.close()