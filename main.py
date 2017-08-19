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
        self.in_tr = False
        self.rowlist = []
        self.datalist = []

    def handle_starttag(self, tag, attrs):
        if tag == 'tr':
            self.in_tr = True
        if tag == 'td':
            self.in_td = True

    def handle_data(self, data):
#        if self.in_td:
#            print(data)
        if self.in_td:
            self.datalist.append(data)


    def handle_endtag(self, tag):
        self.in_td = False
        self.in_tr = False
        if tag == 'tr':
            self.rowlist.append(self.datalist)
            self.datalist = [] # Reset the datalist
    
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
q = p.rowlist # This is the table in pythonic form!

name = input('Enter shooter name:\n')

##############################################################################
######## parse lists, analyze match statistics
# Remove empty last element in table
del q[-1]
# Remove first element of list because we don't need it 
del q[0]

''' 
46 ppl
14 in enh
'''

# Counters for each division
Service = 0
Enhanced = 0
Open = 0
i = 0 # Overall counter
shooter_found = 0
for rows in q:
    i += 1 # increment here vs end is simplest way to achieve right count
    if rows[1] == 'Service':
        Service += 1
    elif rows[1] == 'Enhanced':
        Enhanced += 1
    elif rows[1] == 'Open':
        Open += 1
    else:
        print('[-] WARNING: unknown division detected! Submit an issue on Github please!')

    if rows[0] == name:
#        print(name + ' came in ' + str(i) + ' place overall!') # For debug
        place = i
        division = rows[1]
        # Use string as a variable that already exists
        div_place = globals()[rows[1]] 
        shooter_found = 1

if shooter_found == 0:
    sys.exit('Failure: Shooter \'' + name + '\' not found! Exiting')

print('Match statistics:')
print('Shooter name: ' + name)
print('Place Overall: ' + str(place) + '/' + str(i))
print('Place Division(' + division + '): ' + str(div_place) + '/' + str(globals()[division]))

''' Resources:
https://stackoverflow.com/questions/19122345/to-convert-string-to-variable-name
'''
