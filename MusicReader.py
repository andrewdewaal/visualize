import sys
import os

def getFileContents(filename):
    file = open(filename, 'r')
    content = file.read()
    file.close()
    return content

def writeFileContents(filename, fileContents):
    file = open(filename, 'w')
    file.write(fileContents)
    file.close()
    return os.path.getsize(filename)

sourceFilename = sys.argv[1]
targetFilename = sys.argv[2]
print ("reading from " + sourceFilename)

content = getFileContents(sourceFilename)
print("found content with length " + str(len(content)))

print("writing to " + targetFilename)

desinationBytesLength = writeFileContents(targetFilename, content)

print("target file " + targetFilename + " is now " + str(desinationBytesLength) + " bytes")
