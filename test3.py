#https://stackoverflow.com/questions/6690367/parse-extract-table-data-using-python
import HTMLParser
data = '''
<html> 
<table border="1px"> 
<tr>
<td>yes</td>
<td>no</td>
</tr>
</table>
</html>
'''
class TableParser(HTMLParser.HTMLParser):
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        self.in_td = False

    def handle_starttag(self, tag, attrs):
        if tag == 'td':
            self.in_td = True

    def handle_data(self, data):
        if self.in_td:
        print data

    def handle_endtag(self, tag):
        self.in_td = False

p = TableParser()
p.feed(data)
