import html.parser
import sys

#https://docs.python.org/3/library/html.parser.html

testdata = '''
<html> 
<table border="1px"> 
<tr>
<td>yes</td>
<td>no</td>
</tr>
</table>
</html>
'''
testdata2 = """<table>
  <tr><th>Event</th><th>Start Date</th><th>End Date</th></tr>
  <tr><td>a</td><td>b</td><td>c</td></tr>
  <tr><td>d</td><td>e</td><td>f</td></tr>
  <tr><td>g</td><td>h</td><td>i</td></tr>
</table>
"""
#table = etree.HTML(s).find("body/table")
class TableParser(html.parser.HTMLParser):
    def __init__(self):
        html.parser.HTMLParser.__init__(self)
        self.in_td = False

    def handle_starttag(self, tag, attrs):
        if tag == 'td':
            self.in_td = True

    def handle_data(self, data):
        if self.in_td:
            print(data)

    def handle_endtag(self, tag):
        self.in_td = False
    
    def unknown_decl(self, data):
        print('[-] WARNING: Unknown declaration! Aborting for debug purposes :) ')
        sys.exit(1)

p = TableParser()
#p.feed(testdata2)
#p.feed('junematch.html')
htmlfile = 'junematch.html'
#htmlfile = '../../CZ3QFP/VINparse/testpage.html'
with open(htmlfile, 'r') as infile:
    p.feed(infile.read())
