import os
from os.path import basename
from subprocess import call

process = True

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
        if (process):
            call([mscoreexe, filepath, "-o", "images/"+ filename +".png", "-T", "10", "-r", "72" ])
            call([mscoreexe, filepath, "-o", "sound/"+ filename +".mp3" ])
            # no ogg for the moment
            #call([mscoreexe, filepath, "-o", "sound/"+ filename +".ogg" ])
        outfile.write('<h4>Example '+ str(int(filename)) +'</h4>\n')
        outfile.write('    <p>\n')
        outfile.write('        <audio preload="none" controls="controls">\n'
#'           <source src="sound/'+ filename +'.ogg" />\n'
'           <source src="sound/'+ filename +'.mp3" />\n'
'           Your browser does not support the audio tag.'
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
