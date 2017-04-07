import sys


if len(sys.argv) != 2:
    print "Error."
    sys.exit()

chord_number = sys.argv[1]
fret_offset = 1

if len(chord_number) != 6:
    print "Error. Input must be 6 characters long."
    sys.exit()

print "    e A D G B E"
print "   ------------"

for i in range(5):
    fret_notes = ""
    for j in range(6):
        #print chord_number[j], "\t", fret_offset+i
        if int(chord_number[j]) == int(fret_offset + i):
            fret_notes += "X "
        else:
            fret_notes += ". "
    print "{0} | {1}".format(fret_offset+i, fret_notes)
