import os
from os.path import basename
from subprocess import call


mscoreexe="/Applications/MuseScore 2.app/Contents/MacOS/mscore"

outfile = open("book2.html", 'w')

outfile.write('<html>\n'
'<head>\n'
'    <title>Theory of Harmony - Arnold Schoenberg</title>\n'
'</head>\n'
'<body>\n'
)





for file in os.listdir("mscz"):
    if file.endswith(".mscz"):
        print "Processing %s file..." % file
        filepath = "mscz/" + file
        filename = os.path.splitext(file)[0]
        call([mscoreexe, filepath, "-o", "images/"+ filename +".png", "-T", "10", "-r", "72" ])
        call([mscoreexe, filepath, "-o", "sound/"+ filename +".mp3" ])
        call([mscoreexe, filepath, "-o", "sound/"+ filename +".ogg" ])
        outfile.write('<h4>Example '+ filename +'</h4>\n')
        outfile.write('    <p>\n')
        outfile.write('        <audio controls="controls">\n'
'           <source src="sound/'+ filename +'.ogg" />\n'
'           <source src="sound/'+ filename +'.mp3" />\n'
'        </audio> \n')
        for png in os.listdir("images/"):
            if png.startswith(filename + "-") and png.endswith(".png"):
                outfile.write('        <figure>\n'
        '          <img src="images/'+ png +'">\n'
        '          <figcaption></figcaption>\n'
        '        </figure>\n')

        outfile.write('    </p>\n')


outfile.write('</body>\n'
'</html>')
outfile.close()
