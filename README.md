BlockX is a block language that is still in development,
it was inpired by Scratch.
This program is made in Python.

VERSION = 0.2.2
You can see this constant in main.py

In editor.py there are the blocks that are on the program,
the blocks are:
* print()
* wait()

How the blocks are is writed in the list BLOCKS

BLOCKS:

{
  "type": ..., #The name of the block ("string")
  
  "entry": ..., #If it has an entry (boolean)
  
  "numeric": ..., #It is no necesary if entry = False but if not, it describes if the entry admits just numbers or any character (boolean)
  
  "color": ... #The color of the block (color name)
}

What does the block does is in the function Play()

The module bloques.py creates the blocks according to what there is in editor.py,
this module also contains the save system.

