from urllib2 import urlopen

goog_url='http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=11&e=30&f=2015&g=d&a=2&b=27&c=2014&ignore=.csv'

def download_google_stock_data(csv_url):
    response = urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dst_url = r'googw.csv'
    fx = open(dst_url, 'w')
    for line in lines:
        fx.write(line + "\n")

    fx.close()
download_google_stock_data(goog_url)