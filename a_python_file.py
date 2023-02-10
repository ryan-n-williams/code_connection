import maya.cmds as cmds



"""This is a python file for use in Maya
"""

selection = cmds.ls(sl=True)

if len(selection) > 0:
    print()
    for i in selection:
        print(i)
else:
    print("\nNo objects selected")


if "Yeah":
    print("\nTrue")
else:
    print("\nFalse")


