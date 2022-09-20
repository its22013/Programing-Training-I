import requests, json

""" input field """
""" 検索ワード入力 """
search = {
        'free' : 'フィッシャーズ', #free word
    'title' : '`',
    'publisher' : '',
    'subject' : '',
    'isbn' : '',
    'lccn' : '', #Library of Congress Control Number
    'oclc' : '', #Online Computer Library Center number
}
resurlt_num = 10
 
#検索件数、未入力なら10
""" 言語入力"""
lnaguage = '' #日本語なら'ja'入力
""" ソート入力"""
sort = 'newest' #新しい順なら'newest'を入力。デフォルト（未入力）はrelevance
""" input field 終了"""

def url_q():
    title_q = '' if search['title']=='' else 'intitle:'+search['title']
    publisher_q = '' if search['publisher']== '' else 'inpublisher:'+search['publisher']
    subject_q = '' if search['subject']== '' else 'subject:'+search['subject']
    isbn_q = '' if search['isbn']== '' else 'isbn:'+search['isbn']
    lccn_q = '' if search['lccn']== '' else 'lccn:'+search['lccn']
    oclc_q = '' if search['oclc']== '' else 'oclc:'+search['oclc']
    q_list = [search['free'], title_q, publisher_q, subject_q, isbn_q, lccn_q, oclc_q]
    q_list_none = list(filter(None, q_list))
    url_q = 'q=' + '+'.join(q_list_none) #q= と各検索項目を+でつなぐ
    return url_q

print(url_q())
def url_generation():
    base_url = 'https://www.googleapis.com/books/v1/volumes?'
    url_max = 'maxResults='+ str(resurlt_num)
    url_lnag = '' if lnaguage == '' else 'langRestrict='+lnaguage
    url_sort = '' if sort == '' else 'orderBy='+sort
    url_list = [url_q(), url_max, url_lnag, url_sort]
    url_list_none = list(filter(None, url_list))
    url = base_url + '&'.join(url_list_none)
    return url

print(url_generation())

def main(url, num):
    response = requests.get(url).json()
    totalitems = response['totalItems'] #件数
    print('件数：', totalitems)
    items_list = response['items'] #items リストデータ
    for i in range(num):
        items = items_list[i] #items
        info = items.get('volumeInfo')
       title = info.get('title')
        author = info.get('authors')
        publisher = info.get('publisher')
        publisheddate = info.get('publishedDate')
        pages = info.get('pageCount')
        printtype = info.get('printType')
        description = info.get('description') #要約
        language = info.get('language')
        print('タイトル：', title)
        print('著者：', author)
        print('出版社：', publisher)
        print('出版日：', publisheddate)
        print('ページ数：', pages)
        print('種別：', printtype)
        print('言語：', language)
        print('要約：', description)

url = url_generation()
main(url, resurlt_num)
