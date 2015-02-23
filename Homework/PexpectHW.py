#! /usr/bin/python

from __future__ import division

import pexpect, glob


#HOMEWORK ONE:

oldprimates = open("primates.nex").read()
corrected = oldprimates

corrected.find("mcmc")
#Out[33]: 11344

corrected.find("mcmcp")
#Out[34]: -1

corrected=oldprimates.replace("mcmc",  "mcmcp")
corrected.find("mcmcp")

#11344
newprimates.write(corrected)

newprimates = open("primates2.nex", "w")

newprimates.write(corrected)
newprimates.close()

child = pexpect.spawn("mb -i primates2.nex")

child.sendline(r"mcmc") 
#Out[42]: 5

child.sendline("no") 
#Out[43]: 3

child.expect("MrBayes >") 
#Out[44]: 0

print child.before

#QUIT 
child.sendline("quit")
#Out[48]: 5



#HOMEWORK PART 2: 

#spawn an interactive mrbayes process
child = pexpect.spawn("mb -i primates2.nex")


#send the command "execute primates2.nex" to mrbayes
child.sendline("execute primates2.nex")
#Out[51]: 22


#send the sumt command to mrbayes
child.sendline("sumt")
#Out[53]: 5


#check to see that the mrbayes command prompt is returned
child.expect("MrBayes >") 
#Out[54]: 0


#print everything before the mrbayes prompt
print child.before


#send the sump command
child.sendline("sump")
#Out[57]: 5


#quit mrbayes
child.sendline("quit")




#LOOPING
import glob
allfiles = glob.glob("*") #returns a list of all files in the current directory
s_usr_bin = glob.glob("/usr/bin/s*") #files that start with is in /usr/bin 
images = glog.glob("*.jpg") # list of image files in current directory

import glob, pexpect

nexus_files =glob.glob("*.nex")
for nex in nexus_files: output = pexpect.run("mb nex")






#PART THREE: WRITE A FUNCTION

#! /usr/bin/python

from __future__ import division

import pexpect, glob



def function(nexus, numgen = 1100):
    kid = pexpect.spawn("mb -i %s" %(nexus))   #kid could be anything/word. Same as child below
    #%s refers to a string- file names apply; %d refers to the digit #
    kid.sendline("set nowarn = yes")
    kid.sendline("mcmcp ngen = %d" %(numgen))
    kid.sendline("mcmc")
    kid.sendline("no")
    kid.sendline("quit")
    
def functionB(nexusb):
    child = pexpect.spawn("mb -i %s" %(nexusb))
    child.sendline("execute %s" %(nexusb))
    child.sendline("sumt")
    child.sendline("sump")
    child.sendline("quit")
    

allfiles =glob.glob('*')
tfiles =glob.glob('*.t')
    
print("there are " + str(len(allfiles)) + "total files in the current directory and " + str(len(tfiles)) + " files that end in '.t'")
#print("there are " + %d + "total files in the current directory and " + %d + " files that end in '.t'")
#followed by %(len(all files), len(tfiles))


function("primates2.nex")
functionB("primates2.nex")

allfiles2 =glob.glob('*')
tfiles2 =glob.glob('*.t')

print("there are " + str(len(allfiles2)) + "total files in the current directory and " + str(len(tfiles2)) + " files that end in '.t'")
print ("these files end in '.t': " + str(tfiles2))




