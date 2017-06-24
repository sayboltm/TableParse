# thiis is first example, second will go in 'test3.py'
#https://stackoverflow.com/questions/20418807/python-parse-html-table-using-lxml

doc = """<TABLE>
<TR>
..     <TD><P>Name</P></TD>
..     <TD><P>Fees</P></TD>
..     <TD><P>Awards</P></TD>
..     <TD><P>Total</P></TD>
.. </TR>
.. <TR>
..     <TD><P>Tony</P></TD>
..     <TD >7,800</TD>
..     <TD >7</TD>
..     <TD>15,400</TD>
.. </TR>
.. <TR>
..     <TD><P>Paul</FONT></P></TD>
..     <TD >7,800</TD>
..     <TD >7</TD>
..     <TD>15,400</TD>
.. </TR>
.. <TR>
..     <TD><P>Richard</P></TD>
..     <TD >7,800</TD>
..     <TD >7</TD>
..     <TD>15,400</TD>
.. </TR>
.. 
.. </TR>
.. </TABLE>"""
>>> import lxml.html
>>> root = lxml.html.fromstring(doc)
>>> root.xpath('//tr/td//text()')
['Name', 'Fees', 'Awards', 'Total', 'Tony', '7,800', '7', '15,400', 'Paul',
'7,800', '7', '15,400', 'Richard', '7,800', '7', '15,400']
>>> 



#>>> doc = """<TABLE>
#... <TR>
#...     <TD><P>Name</P></TD>
#...     <TD><P>Fees</P></TD>
#...     <TD><P>Awards</P></TD>
#...     <TD><P>Total</P></TD>
#... </TR>
#... <TR>
#...     <TD><P>Tony</P></TD>
#...     <TD >7,800</TD>
#...     <TD >7</TD>
#...     <TD>15,400</TD>
#... </TR>
#... <TR>
#...     <TD><P>Paul</FONT></P></TD>
#...     <TD >7,800</TD>
#...     <TD >7</TD>
#...     <TD>15,400</TD>
#... </TR>
#... <TR>
#...     <TD><P>Richard</P></TD>
#...     <TD >7,800</TD>
#...     <TD >7</TD>
#...     <TD>15,400</TD>
#... </TR>
#... 
#... </TR>
#... </TABLE>"""
#>>> import lxml.html
#>>> root = lxml.html.fromstring(doc)
#>>> root.xpath('//tr/td//text()')
#['Name', 'Fees', 'Awards', 'Total', 'Tony', '7,800', '7', '15,400', 'Paul',
#'7,800', '7', '15,400', 'Richard', '7,800', '7', '15,400']
#>>> 
