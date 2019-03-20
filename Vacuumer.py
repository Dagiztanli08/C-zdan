import wmi
import os
from shutil import copyfile,copytree,ignore_patterns
import shutil
import time


class Vacuum(object):
     
    def __init__(self):
        self.c=wmi.WMI()
        self.list=[]
        self.say=0
        self.a=True
        

    def copytree(self,src, dst, symlinks=False, ignore=None):
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, symlinks, ignore)
            else:
                shutil.copy2(s, d)

    def Scan(self):
        for drive in self.c.Win32_LogicalDisk():
            print("...")
        
            if drive.Description=="Çıkarılabilir Disk":
                print("Target as found")
                print (os.path.abspath(drive.VolumeName))
                for exp in os.listdir(str(os.path.abspath(drive.DeviceID))):
                    self.say +=1
                    self.list.append(exp)
                    self.a=False
                    
        

print("---------------------------------------")
print("")
print("This Script've coded by MarineEngineer")
print("")
print("---------------------------------------")
time.sleep(1)
print("Initilazing...")
time.sleep(1)

x=sample.c.Win32_LogicalDisk()

sample=Vacuum()

while sample.a==True:
    sample.Scan()
    if  sample.a==False:
        sample.copytree((x[-1].DeviceID+"\\"),"C:\\Users\\Admin\\Desktop\\1")
        
    else:
        pass














#for drive in sample.c.Win32_LogicalDisk() :
 #   print(os.path.abspath(drive.DeviceID)[:-1])
 #print(x[-1].DeviceID)
