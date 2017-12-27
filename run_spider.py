from scrapy import cmdline


cmdstr = " scrapy crawl Meinv"
# cmdstr += " -o item.csv -t csv  "
cmdline.execute(cmdstr.split())