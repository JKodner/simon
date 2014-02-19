# Color Module is Copyright of 2012 Google Inc. Link to File: 
# https://github.com/GoogleCloudPlatform/titan/blob/master/titan/common/colors.py

import color as col
from os import system
from time import sleep
from random import choice

def reset():
	global board
	for i in ["l", "h", "s", "p"]:
		board = board.replace(i, col.format("<black>%s</black>" % i))
	return board

def change(*char):
	global board
	for i in char:
		board = board.replace(i, col.format("<%s>%s</%s>" % (cols[i], i, cols[i])))
	return board

board = """\n                    ooo OOO OOO ooo
              oOOllllllllll|hhhhhhhhOOo
           oOOlllllllllllll|hhhhhhhhhhhOOo
        oOOllllllllllllllll|hhhhhhhhhhhhhhOOo
      oOOllllllllllllllllll|hhhhhhhhhhhhhhhhOOo
    oOOllllllllllllllllllll|hhhhhhhhhhhhhhhhhOOo
   oOOlllllllllllllllllllll|hhhhhhhhhhhhhhhhhhhOOo
  oOOllllllllllllllllllllll|hhhhhhhhhhhhhhhhhhhhOOo
 oOOlllllllllllllllllllllll|hhhhhhhhhhhhhhhhhhhhhOOo
 oOOlllllllllllllllllllllll|hhhhhhhhhhhhhhhhhhhhhOOo
 oOO-----------------------|---------------------OOo
 oOOsssssssssssssssssssssss|pppppppppppppppppppppOOo
 oOOsssssssssssssssssssssss|pppppppppppppppppppppOOo
  oOOssssssssssssssssssssss|ppppppppppppppppppppOOo
   oOOsssssssssssssssssssss|pppppppppppppppppppOOo
    oOOssssssssssssssssssss|ppppppppppppppppppOOo
      oOOssssssssssssssssss|ppppppppppppppppOOo
        oOsssssssssssssssss|ppppppppppppppOOo
           oOOsssssssssssss|pppppppppppOOo
               oOOsssssssss|pppppppOOo
                   ooo OOO OOO ooo
"""

cols = {
	"l": "light_green",
	"h": "yellow",
	"s": "light_cyan",
	"p": "light_red"
}

colors = {
	"l": "g",
	"h": "y",
	"s": "b",
	"p": "r"
}

system('clear')
print "-" * 90
board = change("l", "h", "s", "p")
print board
print """Simon Game: The Circle Above will Show a Series of Colors. After, you will be required
to type in the order of colors you saw. Try and get as much correct as you can!"""
raw_input(col.format("<purple>Press Anything to Continue</purple>"))

system('clear')
board = reset()
order = []
color = choice(cols.keys())
board = change(color)
order.append(color)

count = 1
while True:
	
	for x, i in enumerate(order):
		board = reset()
		board = change(i)
		print board
		sleep(0.8)
		system('clear')
		sleep(0.05)
	
	print "-" * 30
	print "Input the Order of Colors You Saw"
	print col.format(
		"(<light_green>g</light_green>" + "/<yellow>y</yellow>" 
		+ "/<light_cyan>b</light_cyan>" + "/<light_red>r</light_red>)"
	)
	
	for i in order:
		board = reset()
		answer = raw_input("Color: ")
		if answer == colors[i]:
			token = True
		else:
			token = False
			break
	
	if not token:
		print col.format("\n<red>INCORRECT</red>")
		break
	
	system('clear')
	
	print "*" * 30
	print col.format("Iteration <light_cyan>#%d</light_cyan> Completed" % count)
	raw_input(col.format("<purple>Press Anything to Continue</purple>"))
	
	system('clear')
	
	board = reset()
	color = choice(cols.keys())
	board = change(color)
	order.append(color)
	count += 1