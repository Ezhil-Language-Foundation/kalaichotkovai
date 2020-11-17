import os
import codecs
from collections import OrderedDict
import tamil

class WordList:
    def __init__(self):
        self.uniq_phrases=OrderedDict()

    def process(self,filename):
        print('Processing: ',filename)
        with codecs.open(filename,'r','utf-8') as fp:
            for line in fp.readlines():
                line = line.strip()
                try:
                    en_part,ta_part = line.split('|')
                    if not tamil.utf8.has_english(en_part):
                        en_part, ta_part=ta_part, en_part
                    self.uniq_phrases[en_part.strip()] = ta_part.strip()
                except ValueError:
                    pass

def main():
    uniq_collector=WordList()
    for path,subdirs,files in os.walk('./sorkal'):
        for fname in files:
            if not fname.endswith('.words'): continue
            uniq_collector.process(os.path.join(path,fname))
    keys=sorted(uniq_collector.uniq_phrases,key=lambda c:c)
    print('Size: ',len(uniq_collector.uniq_phrases))
    with codecs.open('demo.list','w','utf-8') as fp:
        for k in keys:#uniq_collector.uniq_phrases.items():
            v=uniq_collector.uniq_phrases[k]
            fp.write('{0}|{1}\n'.format(k,v))

if __name__ == "__main__":
    main()
