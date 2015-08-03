outfile = open("index.html", 'w')

outfile.write('<html>\n'
'<head>\n'
'    <title>Theory of Harmony - Arnold Schoenberg</title>\n'
'</head>\n'
'<body>\n'
)

outfile.write('<ul>\n')
for i in range(1, 348):
    outfile.write('     <li><a class="link" href="book.html#ex' + str(i) + '">Example ' + str(i) +'</a></li>\n')
outfile.write('</ul>\n')

outfile.write('</body>\n'
'</html>')
outfile.close()