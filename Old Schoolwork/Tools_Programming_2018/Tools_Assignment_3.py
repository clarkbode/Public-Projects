import maya.cmds as cmds

#part 1
cmds.polyCube( sx=10, sy=15, sz=5, h=20 )
cmds.polySphere( sx=10, sy=16, az=5, h=20 )

#part 2
thing = cmds.polySphere()#create mode
print thing
cmds.polySphere(thing[1], edit=True, radius=10) #edit mode
cmds.polySphere(thing[1], q=True, radius = 5) #query mode