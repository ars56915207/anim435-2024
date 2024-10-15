import argparse
import maya.standalone
maya.standalone.initialize()
import maya.cmds as cmds
import math
import os

parser = argparse.ArgumentParser()
parser.add_argument('-R', '--Rings', default=5, help="Define the number of rings, the number of rows is twice the amount inputted for rings.")
parser.add_argument('-n', '--name', default="sphereRings", help="Define scene name, default name is sphereRings. File extension should NOT be included")
args = parser.parse_args()

print("Creating Spheres...")

def createSpheres(numRings):
  '''
    Creates spheres in rings that increase in size.
      
    numRings is the number of rings
    
    returns nothing
  '''
  numRings = int(numRings)
# number of rings
  for i in range(0,numRings):
      radius = i*10
      # spheres per row
      for j in range(0,numRings*2):
          angle = (2*math.pi*j)/(numRings*2)
          x = radius * math.cos(angle)
          z = radius * math.sin(angle)
          sphere = cmds.polySphere(r=1+i)
          cmds.move(x,1,z)
          
# deletes spheres created on top of each other     
  for i in range(0,(numRings*2)-1):
      if i == 0:
          cmds.select('pSphere1')
      cmds.select('pSphere' + str(i+1), add=True)
  cmds.delete()
  
# puts spheres into a group
  print("Grouping Spheres...")
  cmds.select(all=True)
  cmds.group(n='spheres')

# main code

createSpheres(args.Rings)

# gets current directory and filepath
dirname= os.path.dirname(__file__)
filename = args.name
filepath = os.path.join(dirname, filename + ".mb")

# checks if file already exists in current directory
# creates new file name if it file already exists
iterations = 0
while os.path.exists(filepath):
    iterations += 1
    newname = filename + str(iterations) + ".mb"
    filepath = os.path.join(dirname, newname)

# saves scene
print("Saving Scene...")
cmds.file(rename=filepath)
cmds.file(save=True)
print("Saved Scene:", filepath)