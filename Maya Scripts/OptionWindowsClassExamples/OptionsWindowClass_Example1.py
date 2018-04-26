import maya.cmds as mc

#implementation of a basic window class 

class OptionsWindow:

    
    def showUI(cls):
        win = cls()
        win.create()
        return win
  
    def __init__(self): #CTOR, with default values for attributes
        self.window = "myWindow"
        self.title = "Options Window"
        self.size = (546, 350)
        self.supportsToolAction = False 
        self.actionName = "Apply and Close"

    def create(self): #create-> creates the window how you want it; customize to how you see fit
        if mc.window(self.window, exists = True):
            mc.deleteUI(self.window, window=True)      
        self.window = mc.window(self.window, title = self.title, widthHeight = self.size, menuBar = True)
        self.mainForm = mc.formLayout(nd=100)
        self.commonMenu()
        self.commonButtons()
        self.optionsBorder = mc.tabLayout(scrollable=True,tabsVisible=False,height=1)
        mc.formLayout(self.mainForm, e = True, attachForm=([self.optionsBorder,"top",0],[self.optionsBorder,"left",2],[self.optionsBorder,"right",2]))
        mc.showWindow()

    def commonMenu(self):
        
        self.editMenu = mc.menu( label = "Edit")
        self.editMenuSave = mc.menuItem( label = "Save Settings")
        self.editMenuReset = mc.menuItem( label = "Reset Settings")
        self.editMenuDiv = mc.menuItem( d = True)
        
        self.helpMenu = mc.menu( label = "Help")
        self.helpMenuItem = mc.menuItem( label = "Help on %s "% self.title, command = self.helpMenuCmd)
        
        self.customMenu = mc.menu( label = "Custom")
        self.customMenuItem = mc.menuItem( label = "create custom object", command = self.createShapeCmd)




#"""
#    following functions are used when the corresponding button is pressed
#
#"""
        
    def helpMenuCmd(self, *args):
        mc.launch(web="http://www.python.org")
        
    def createShapeCmd(self, *args):
        obj = mc.polyHelix(subdivisionsAxis = 2, subdivisionsCoil = 10, width = 3)
        polycount = mc.polyEvaluate(obj[0],face = True)
        print polycount
        for i in range(0, polycount-2,2):
            face = "%s.f[%s]"%(obj[0], i)
            mc.polyExtrudeFacet(face, ltz = 1, ls=[0.1,0.1,0.1])
        

    def editMenuSaveCmd(self,*args):pass
    def editMenuResetCmd(self,*args):pass
    
    def applyBtnCmd(self,*args):pass
    def closeBtnCmd(self,*args):
        mc.deleteUI(self.window,window=True)

    def commonButtons(self):
        self.commonBtnSize=(self.size[0]-18/3,26)
        self.actionBtn=mc.button(label="ActionName",height=self.commonBtnSize[1])    
        self.applyBtn=mc.button(label="Apply",height=self.commonBtnSize[1],command=self.applyBtnCmd)
        self.closeBtn = mc.button(label="Close",height=self.commonBtnSize[1],command=self.closeBtnCmd)
        
        
        mc.formLayout(self.mainForm, e=True, attachForm=([self.actionBtn,"left",5], [self.actionBtn,"bottom",5], 
                                                         [self.applyBtn,"bottom",5],[self.closeBtn,"bottom",5], 
                                                         [self.closeBtn,"right",5]),
                                             attachPosition=([self.actionBtn,"right",1,33], [self.closeBtn,"left",0,67]), 
                                             attachControl=([self.applyBtn,"left",4,self.actionBtn],[self.applyBtn,"right",4,self.closeBtn]), 
                                             attachNone=([self.actionBtn,"top"], [self.applyBtn,"top"], [self.closeBtn,"top"]))
        
                                                        
                                                        
    def displayOptions(self):pass      


       
        
testWindow = OptionsWindow()
testWindow.create()
