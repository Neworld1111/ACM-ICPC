import requests
from lxml import etree

def get_url(url):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62'
    }
    res = requests.get(url, headers=headers)
    html = res.content.decode("utf-8")
    # print(html)
    return html

def getResult(url):
    pass

if __name__ == "__main__":
    
    html = get_url('https://citel.bjtu.edu.cn/acm/contest/online')
    tree = etree.HTML(html)

    plat = []
    title = []
    link = []
    time = []
    for i in range(1,6):
        plat.append(tree.xpath('//*[@id="app"]/div[1]/div/div/div[2]/div/table/tbody/tr[{0}]/td[2]/text()'.format(i))[0])
        title.append(tree.xpath('//*[@id="app"]/div[1]/div/div/div[2]/div/table/tbody/tr[{0}]/td[3]/a/text()'.format(i))[0])
        link.append(tree.xpath('//*[@id="app"]/div[1]/div/div/div[2]/div/table/tbody/tr[{0}]/td[3]/a/@href'.format(i))[0])
        time.append(tree.xpath('//*[@id="app"]/div[1]/div/div/div[2]/div/table/tbody/tr[{0}]/td[4]/small/text()'.format(i))[0] )
    
    print('Upcoming Contest: ')
    for i in range(0,3):
        print('Contest{0} : '.format(i),title[i],'\r\n',link[i],'\r\n',time[i],'\r\n')
