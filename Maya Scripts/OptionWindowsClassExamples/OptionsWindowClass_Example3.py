"""
 OptionsWindow is a class definition of the basic window class.
 The class is adding a set of controls to create a template
 that resembles Maya's built-in tool option windows.

"""
import maya.cmds as mc

class OptionsWindow(object):
    """Base Window Class"""
    #@classmethod
    def showUI(cls):
        win = cls()
        win.create()
        return win
    def __init__(self):
        self.window = "optionsWindow"
        self.title = "OptionsWindow"
        self.size = (546,350)
        

        
    def create(self):
        if mc.window(self.window,exists=True): 
            mc.deleteUI(self.window,window=True)

        self.window = mc.window(self.window, title=self.title,widthHeight=self.size,menuBar=True)
        self.mainForm = mc.formLayout(nd=100)
        self.commandMenu()
        self.commonButtons()
        self.optionsBorder = mc.tabLayout(scrollable=True,tabsVisible=False,height=1)
       
        mc.formLayout(self.mainForm,e=True,
                      attachForm=(
                                  [self.optionsBorder,"top",0],
                                  [self.optionsBorder,"left",2],
                                  [self.optionsBorder,"right",2]),
                      attachControl=([self.optionsBorder,"bottom",5,self.applyBtn]))
                      
        self.optionsForm=mc.formLayout(nd=100)
        #mc.tabLayout(self.optionsBorder,edit=True,tabLabel=(self.optionsForm,"Test"))    
        self.displayOptions()
        mc.showWindow()
       
    def commandMenu(self):
        self.editMenu = mc.menu(label="Edit")
        self.editMenuSave = mc.menuItem(label="Save Settings",command=self.editMenuSaveCmd)
        self.editMenuReset = mc.menuItem(label="Reset Settings",command=self.editMenuResetCmd)
        self.helpMenu = mc.menu(label="Help")
        self.helpMenuItem = mc.menuItem(label="Help on %s"%(self.title),command=self.helpMenuCmd)
    def helpMenuCmd(self,*args):
        mc.launch(web="http://maya-python.com")
    def editMenuSaveCmd(self,*args):pass
    def editMenuResetCmd(self,*args):pass
    
    def actionCmd(self,*args):
        print "ACTION"
    def applyBtnCmd(self,*args):
        print "APPLY"
    def closeBtnCmd(self,*args):
        mc.deleteUI(self.window,window=True)

   

    def commonButtons(self):
        self.commonBtnSize=(self.size[0]-18/3,26)
        self.acctionBtn=mc.button(label="Action",height=self.commonBtnSize[1], command = self.actionCmd)    
        self.applyBtn=mc.button(label="Apply",height=self.commonBtnSize[1],command=self.applyBtnCmd)
        self.closeBtn = mc.button(label="Close",height=self.commonBtnSize[1],command=self.closeBtnCmd)
        
        
        mc.formLayout(self.mainForm, e=True, attachForm=([self.acctionBtn,"left",5],
                                                         [self.acctionBtn,"bottom",5],
                                                         [self.applyBtn,"bottom",5],
                                                         [self.closeBtn,"bottom",5],
                                                         [self.closeBtn,"right",5]),
                                             attachPosition=([self.acctionBtn,"right",1,33],
                                                             [self.closeBtn,"left",0,67]),
                                             attachControl=([self.applyBtn,"left",4,self.acctionBtn],
                                                            [self.applyBtn,"right",4,self.closeBtn]),
                                             attachNone=([self.acctionBtn,"top"],
                                                         [self.applyBtn,"top"],
                                                         [self.closeBtn,"top"]))
    def displayOptions(self):pass


class MyOptionsWindow(OptionsWindow):
    """Custom Window Class, subclass
    of the OptionWindow base class """
                
    def displayOptions(self):
        """ displayOptions() All custom UI controlls should be added to this method
        These controlls will be childred of the formLayout whose name is self.optionsForm  
        """
        self.floatInput = mc.floatFieldGrp(numberOfFields = 1, label = "Sphere Radius", value1 = 1.0, cc = self.updateFloat)
        
    def updateFloat(self,*args):
        size = mc.floatFieldGrp(self.floatInput, query = True, value1 = True)
        return size    
        
    def actionCmd(self,*args):
        self.radius = mc.floatFieldGrp(self.floatInput, query = True, value1 = True)
        mc.polySphere(r=self.radius)

 
win = MyOptionsWindow()
win.create()