# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 11:10:20 2018

@author: Administrator
"""

#作业第一题
description=[16,19,21,17,18,19,23]
print(description)
o=description[3]
str(o)
print("星期三的温度是"+str(o))

#作业第二题
ice={'周日':{'气温':'24','天气情况':'小雨','最高气温':'25'},'周一':{'气温':'12','天气情况':'暴雨','最高气温':'13'},
   '周二':{'气温':'24','天气情况':'晴','最高气温':'28'},'周三':{'气温':'18','天气情况':'多云','最高气温':'20'},
   '周四':{'气温':'30','天气情况':'晴','最高气温':'33'},'周五':{'气温':'17','天气情况':'阴天','最高气温':'19'},
   '周六':{'气温':'35','天气情况':'晴','最高气温':'36'}}
print(ice['周三']['气温'],ice['周三']['天气情况'])

p=ice['周三']['最高气温']
str(p)
print("今天的最高气度是"+str(p))

#作业第三题
import urllib.request as r
url='http://api.openweathermap.org/data/2.5/weather?q=chongqing&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
data=r.urlopen(url).read().decode('utf-8')
import json
data=json.loads(data)

print(data["main"]['temp'])
print(data["weather"][0]['description'])
print(data["main"]['pressure'])



#第四题
#中文
time=data['list'][0]['dt_txt']
data1=time[8:10]
time=time[12:16]
city=data['city']['name']
description=data['list'][0]['weather'][0]['description']
temp=data['list'][0]['main']['temp']
temp_max=data['list'][0]['main']['temp_max']
temp_min=data['list'][0]['main']['temp_min']
pressure=data['list'][0]['main']['pressure']
print('{}日{}的{}天气情况{},温度：{} 最高温度:{} 最低温度:{} 气压:{}'.format(data1,time,city,
      description,temp,temp_max,temp_min,pressure))

#英文
time=data['list'][0]['dt_txt']
data1=time[8:10]
time=time[11:16]
city=data['city']['name']
description=data['list'][0]['weather'][0]['main']
temp=data['list'][0]['main']['temp']
temp_max=data['list'][0]['main']['temp_max']
temp_min=data['list'][0]['main']['temp_min']
pressure=data['list'][0]['main']['pressure']
print('The weather at {} in {} in June {}st is {},temp：{} temp_max:{} temp_min:{} pressure:{}'.format(time,
      city,data1,description,temp,temp_max,temp_min,pressure))

#The weather at 9 in Chongqing in June 21st is rain
time=data['list'][8]['dt_txt']
data1=time[8:10]
time=time[11:13]
description=data['list'][8]['weather'][0]['main']
print('The weather at {} in Chongqing in June {}st is {}'.format(time,data1,description))


time=data['list'][0]['dt_txt']
city=data['city']['name']
description=data['list'][0]['weather'][0]['main']
temp=data['list'][0]['main']['temp']
temp_max=data['list'][0]['main']['temp_max']
temp_min=data['list'][0]['main']['temp_min']
pressure=data['list'][0]['main']['pressure']
print('{},The weather in {} is {},temp：{} temp_max:{} temp_min:{} pressure:{}'.format(time,
      city,description,temp,temp_max,temp_min,pressure))




#图形
for i in range(11):
    print('*'*(i+1),'^',' '*(18-i-2),'天气预报',' '*(18-i-2),'^','*'*(i+1))

#第七题天气提示
import urllib.request as r
url='http://api.openweathermap.org/data/2.5/forecast?q=chongqing,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
import json
data=json.loads(data)

def ice(n):
    time=data['list'][n]['dt_txt']
    data1=time[8:10]
    time=time[11:16]
    city=data['city']['name']
    description=data['list'][n]['weather'][0]['description']
    temp=data['list'][n]['main']['temp']
    temp_max=data['list'][n]['main']['temp_max']
    temp_min=data['list'][n]['main']['temp_min']
    pressure=data['list'][n]['main']['pressure']
    print('{}日{}的{}天气情况{},温度：{} 最高温度:{} 最低温度:{} 气压:{}'.format(data1,time,city,
          description,temp,temp_max,temp_min,pressure))
for i in range(37):
    ice(i)



def ice(n):
    time1=data['list'][n]['dt_txt']
    time=time1[11:13]
    time=int(time)
    if time>20:
        print('现在时间是{}天黑了，请勿出门'.format(time1))
    elif time>5:
        data1=time1[8:10]
        time=time1[11:16]
        city=data['city']['name']
        description=data['list'][n]['weather'][0]['description']
        temp=data['list'][n]['main']['temp']
        temp_max=data['list'][n]['main']['temp_max']
        temp_min=data['list'][n]['main']['temp_min']
        pressure=data['list'][n]['main']['pressure']
        if description==('小雨'):
            print('提示:现在外面是小雨请备伞     {}日{}的{}温度：{} 最高温度:{} 最低温度:{} 气压:{}'.format(data1,time,city,
                  temp,temp_max,temp_min,pressure))
        elif description==('中雨'):
            print('提示:现在外面是中雨请备伞，不要穿太单薄的衣物    {}日{}的{}温度：{} 最高温度:{} 最低温度:{} 气压:{}'.format(data1,time,city,
                  temp,temp_max,temp_min,pressure))
        elif description==('多云'):
            print('提示:外面天气多云，可以外出锻炼   {}日{}的{}温度：{} 最高温度:{} 最低温度:{} 气压:{}'.format(data1,time,city,
                  temp,temp_max,temp_min,pressure))
        print('提示:外面晴空万里，适合一家人出去游玩  {}日{}的{}温度：{} 最高温度:{} 最低温度:{} 气压:{}'.format(data1,time,city,temp,temp_max,temp_min,pressure))
    else:
        print('现在时间是{}天黑了，请不要出门'.format(time1))
for i in range(37):
    ice(i)   



def ice(n):
    time1=data['list'][n]['dt_txt']
    time=time1[11:13]
    time=int(time)
    if time>20:
        print('现在时间是{}天黑了，请勿出门'.format(time1))
    elif time>5:
        data1=time1[8:10]
        time=time1[11:16]
        city=data['city']['name']
        description=data['list'][n]['weather'][0]['description']
        temp=data['list'][n]['main']['temp']
        temp_max=data['list'][n]['main']['temp_max']
        temp_min=data['list'][n]['main']['temp_min']
        pressure=data['list'][n]['main']['pressure']
        if description==('小雨'):
            print('提示:现在外面是小雨请备伞 ','\n','{}日{}的{}温度：{} 最高温度:{} 最低温度:{} 气压:{}'.format(data1,time,city,
                  temp,temp_max,temp_min,pressure))
        elif description==('中雨'):
            print('提示:现在外面是中雨请备伞，不要穿太单薄的衣物 ','\n','{}日{}的{}温度：{} 最高温度:{} 最低温度:{} 气压:{}'.format(data1,time,city,
                  temp,temp_max,temp_min,pressure))
        elif description==('多云'):
            print('提示:外面天气多云，可以外出锻炼','\n','{}日{}的{}温度：{} 最高温度:{} 最低温度:{} 气压:{}'.format(data1,time,city,
                  temp,temp_max,temp_min,pressure))
        print('提示:外面晴空万里，适合一家人出去游玩','\n','{}日{}的{}温度：{} 最高温度:{} 最低温度:{} 气压:{}'.format(data1,time,city,temp,temp_max,temp_min,pressure))
    else:
        print('现在时间是{}天黑了，请不要出门'.format(time1))
for i in range(37):
    ice(i) 




#第十题火车票
def ice_a(s):
    ls=open('./火车站编码.csv','r',encoding='utf-8').readlines()
    abc=''
    for i in ls:
        if s==i.split(',')[0]:
            abc=i.split(',')[1]
            break
    return abc

import urllib.request as r
date=input('请输入年月日')
from_station=input('出发站')
from_station=ice_a(from_station)
to_station=input('到达站')
to_station=ice_a(to_station)
print(date,from_station,to_station)
url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'
url=url.format(date,from_station,to_station).replace('\n','')
print(url)
data=r.urlopen(url).read().decode('utf-8')
import json
data1=json.loads(data)
data=data1['data']['result']

p= ' '
len([p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p])
b='车次{}出发站{}到达站{}出发时间{}到达时间{}历时{}商务座/特等座{}一等座{}二等座{}高级软卧{}软卧{}动卧{}硬卧{}软座{}硬座{}无座{}其他{}能否预定{}'.format(p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p)
b=b.split(p)
for t in b:
    print(t.center(10),end='')
print('\t')
def ice(n):
    a=data[n]
    a=a.split('|')
    a[6]=data1['data']['map'].get('{}'.format(a[6]))
    a[7]=data1['data']['map'].get('{}'.format(a[7]))
    a=[a[3],a[6],a[7],a[8],a[9],a[10],a[32],a[31],a[30],'-','-','-','-','-','-','-',a[11]]
    for i in a:
        print(str(i).center(13),end='')
    print('\t')
m=[]
for i in range(len(data)):
    a=data[i]
    a=a.split('|')
    c=('{}-{}'.format(a[8],a[3]))
    m.append(c)
    ice(i)
m.sorted(m)
print(m)



#第十一题

import urllib.request as r#导入联网工具包，命令为r
url='http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&ch=1&tn=78040160_26_pg&wd=%E6%A1%83%E5%AD%90&oq=%25E6%25A9%2598%25E5%25AD%2590&rsv_pq=9485189d0003ebe5&rsv_t=888a52sKt4YAfxLBcOoz%2B1tRgJyBiMfXuAht9uXHGh%2BABeSyUNsnARzNTcM7tWRoN4Y1mLU&rqlang=cn&rsv_enter=1&inputT=1205&rsv_sug3=12&rsv_sug1=6&rsv_sug7=100&rsv_sug2=0&rsv_sug4=1206'
data=r.urlopen(url).read().decode('utf-8')
import re
ls1=re.compile('"title":"(.*?)"').findall(data)
ls2=re.compile('<div class="c-abstract">(.*?)</div>').findall(data)
ls3=re.compile('"url":"(.*?)"').findall(data)

ice=[]
for i in range(len(ls1)):
    print(ls1[i],'\n')
    print(ls2[i],'\n')
    print(ls3[i],'\n')
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')


import urllib.request as r
pat='<div class="content">(.*?)</div>'
pat1='<h2>(.*?)</h2>'
import re

f=open('./糗事百科.txt','w',encoding='utf-8')
for x in range(1,14):
    url='https://www.qiushibaike.com/8hr/page/{}/ '.format(x)
    req=r.Request(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'})
    myurl=r.urlopen(req)
    data=myurl.read().decode('utf-8')
    ls=re.compile(pat,re.S).findall(data)
    ls1=re.compile(pat1,re.S).findall(data)

    for i in range(len(ls)):
        f.write('{}\n{}\n'.format(ls1[i],ls[i].replace('\n','').replace('<span>','')))
f.close


#第十二题
import urllib.request as r
url='http://api.openweathermap.org/data/2.5/forecast?q=chongqing,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
import re
ls=re.compile('"description":"(.*?)"').findall(data)
ls1=re.compile('"temp":(.*?),"').findall(data)
ls2=re.compile('"pressure":(.*?),"').findall(data)
ice=[]
for i in range(len(ls1)):
    print('天气情况：',ls[i],'\n')
    print('温度：',ls1[i],'\n')
    print('气压：',ls2[i],'\n')
    print('++++++++++++++++++++')



#十四题
#获取全国城市的编号
import urllib.request as r
req=r.Request('http://www.gaokaopai.com/daxue-0-0-0-0-0-0-0.html',headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'})
myurl=r.urlopen(req)
print(myurl.getcode())
data=myurl.read().decode('utf-8')
import re
s3=re.compile('<span><a href="http://www.gaokaopai.com/daxue-(.*?)-0-0-0-0-0-0.html">(.*?)</a></span>').findall(data)
print(s3)
s1=re.compile('<span><a href="http://www.gaokaopai.com/daxue-(.*?)-0-0-0-0-0-0.html">').findall(data)
s2=re.compile('<span><a href="http://www.gaokaopai.com/daxue-..-0-0-0-0-0-0.html">(.*?)</a></span>').findall(data)



#循环下载数据
m=[]
import urllib.request as r    
for i in range(100):
    url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
    data='id={}&type=2&city=34&state=1'.format(s1[i])
    data=data.encode()
    req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
    p=r.urlopen(req).read().decode('utf-8','ignore')
    m.append(p)
    a=i
    print('输出{}次'.format(a))


#自动修改代码
for i in range(2300):
    a=m[i]
    if a.startswith('<!DOCTYPE html>'):
        print('第{}存在错误'.format(i))
        url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
        data='id={}&type=2&city=34&state=1'.format(s1[i])
        data=data.encode()
        req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
        p=r.urlopen(req).read().decode('utf-8','ignore')
        m[i]=p
    else:
        continue

#最终版
f=open('./all_school.txt','r',encoding='utf-8')
s=f.read()
import re
s1=re.compile('http://www.gaokaopai.com/daxue-jianjie-(.*?).html',re.S).findall(s)
f.close()    
m=[]
import urllib.request as r    
for i in range(2300):
    url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
    data='id={}&type=1&city=31&state=1'.format(s1[i])
    data=data.encode()
    req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
    p=r.urlopen(req).read().decode('utf-8','ignore')
    m.append(p)
    a=m[i]
    if a.startswith('<!DOCTYPE html>'):
        print('第{}存在错误'.format(i))
        url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
        data='id={}&type=1&city=31&state=1'.format(s1[i])
        data=data.encode()
        req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
        p=r.urlopen(req).read().decode('utf-8','ignore')
        m[i]=p
    else:
        a=i
        print('{}次输出成功'.format(a))

#再次检验是否有错
for i in range(2300):
    a=m[i]
    if a.startswith('<!DOCTYPE html>'):
        print('第{}存在错误'.format(i))
        url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
        data='id={}&type=1&city=31&state=1'.format(s1[i])
        data=data.encode()
        req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
        p=r.urlopen(req).read().decode('utf-8','ignore')
        m[i]=p
    else:
        a=i
        print('{}次输出成功'.format(a))

f=open('./上海文科.txt','w',encoding='utf-8')
for i in range(len(m)):
    p=m[i]
    f.write(p+"\n")
f.close()    



#十五题
class Weather:
    def __init__(self,description,temp,pre):
        self.description=description
        self.temp=temp
        self.pre=pre
    def msg(self):
        print("{},温度:{},气压:{}".format(self.description,self.temp,self.pre))

s1=Weather('晴天','13','8023')
s2=Weather('晴天','14','1314')
s3=Weather('晴天','20','5200')


s1.msg()
s2.msg()
s3.msg()


#十六题
'''爬取一百页电影数据
'''
m=[]
import urllib.request as r    
for i in range(1,101):
    url='http://dianying.2345.com/list/-------{}.html'.format(i)
    req=r.Request(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'})
    p=r.urlopen(req).read().decode('gbk','ignore')
    print('第{}页获取结束'.format(i))
    m.append(p)

'''找出每部电影唯一指代的数字代码
'''
import re
n=[]
for i in range(len(m)):
    ls=re.compile('<li media="(.*?)".*').findall(m[i])
    n.append(ls)
a=[]
for i in range(len(n)):
    for j in range(35):
        b=n[i][j]
        a.append(b)

'''通过之前的电影相关数字编码，在网站上爬取每部电影的详细数据
'''

s=[]
for k in range(len(a)):
    url='http://dianying.2345.com/detail/{}.html '.format(a[k])
    req=r.Request(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'})
    data=r.urlopen(url).read().decode('gbk')
    print('成功{}'.format(k))
    s.append(data)

'''整理出我们需要的电影数据，并保存为TXT的文本
'''
f=open('./dianying1.txt','w')
import re
for y in range(len(s)):
    name=re.compile('<h1>(.*?)</h1>',re.S).findall(s[y])
    pinfen=re.compile('<em class="emScore">(.*?)</em>',re.S).findall(s[y])
    jianjie=re.compile('<span class="sAll">(.*?)</span>',re.S).findall(s[y])
    diqu=re.compile('<a title="(.*?)" data-ajax83="ys_dy_2015_detail_diq').findall(s[y])
    zhuyan=re.compile('<a data-ajax83="ys_dy_2015_detail_zhy_." title="(.*?)" href',re.S).findall(s[y])
    shichang=re.compile('<em class="emTit">时长：</em>\n\s*<em>(.*?)</em>',re.S).findall(s[y])
    niandai=re.compile('<em class="emTit">年代：</em>\n\s*<em>(.*?)</em>',re.S).findall(s[y])
    print('{}数据已录取'.format(y))
    f.write('电影名：{},豆瓣评分:{},地区:{},年代:{},时长:{},主演:{},电影简介:{}\n'.format(name,pinfen,diqu,niandai,shichang,zhuyan,jianjie))
f.close()

'''读取之前的文本数据，并整理为用户查询时需要的格式
'''
m=[]
import urllib.request as r
url='file:./dianying.txt'
data=r.urlopen(url).read().decode('gbk')
data1=data.split('\n')
ls1=[]
ls2=[]
ls3=[]
for i in range(len(data1)):#电影名,时长，简介.
    if i%3==0:
        ls1.append(data1[i])
    if i%3==1:
        ls2.append(data1[i])
    if i%3==2:
        ls3.append(data1[i])

'''用户查询的相关代码
'''

import re
dy=re.compile("电影名：..(.*?)..,").findall(data)
p='yes'
o='no'
def ice(b):
    for i in range(len(dy)):
        a=dy[i]
        try:
            a.index(b)
            print('{}\n{}\n{}\n'.format(ls1[i],ls2[i],ls3[i]))
        except Exception as r:
            pass

b=input('请输入电影名称：') 
ice(b)
c=input('查询结束,是否继续查询：yes或者no')
while c==p:
    b=input('请输入电影名称：') 
    ice(b)
    c=input('查询结束,是否继续查询：yes或者no')
    continue 
else:
    input('输入任意退出')

