# (C) 2020, Muthiah Annamalai
# This code is released to public domain.

import bs4
import sys
import codecs

def main(fname):
    with codecs.open(fname,"r","utf-8") as fp:
        bs = bs4.BeautifulSoup(fp.read(),features="html.parser")
    table=bs.find_all('table')[-1]
    rows=table.find_all('td')
    newfilename=        fname.replace('.html','.words')
    fp=codecs.open(newfilename,'w','utf-8')
    for i in range(len(rows)//2):
        en_row = rows[2*i]
        ta_row = rows[2*i+1]
        try:
            en_word = en_row.find('span').text.strip()
            ta_word = ta_row.find('span').text.strip()
            print('{0}=>{1}'.format(en_word,ta_word))
            fp.write(en_word+'|'+ta_word+'\n')
        except Exception as e:
            pass
    fp.close()
    print('Written {0}'.format(newfilename))
    return

if __name__ == "__main__":
    failed=[]
    for fname in sys.argv[1:]:
        try:
            main(fname)
        except Exception as e:
            failed.append(fname)
    print('Failed files',failed)

###
#Failed files ['.//kalaichotkovai.blogspot.com/2015/08/logical-fallacies_27.html',
#'.//kalaichotkovai.blogspot.com/2020/05/blog-post.html']
##

