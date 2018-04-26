"""
 OptionsWindow is a class definition of the basic window class.
 The class is adding a set of controls to create a template
 that resembles Maya's built-in tool option windows.

"""
import maya.cmds as cmd
import random

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
        self.actionName = "Apply and Close"
        self.applyName = "Apply"
        

        
    def create(self):
        if cmd.window(self.window,exists=True): 
            cmd.deleteUI(self.window,window=True)

        self.window = cmd.window(self.window, title=self.title,widthHeight=self.size,menuBar=True)
        self.mainForm = cmd.formLayout(nd=100)
        self.commandMenu()
        self.commonButtons()
        self.optionsBorder = cmd.tabLayout(scrollable=True,height=1,tabsVisible = False)
        cmd.formLayout(self.mainForm,e=True,
                      attachForm=(
                                  [self.optionsBorder,"top",0],
                                  [self.optionsBorder,"left",2],
                                  [self.optionsBorder,"right",2]),
                      attachControl=([self.optionsBorder,"bottom",5,self.applyBtn]))
                      
        self.optionsForm=cmd.formLayout(nd=100)
        #cmd.tabLayout(self.optionsBorder,edit=True,tabLabel=(self.optionsForm,"Test"))    
        self.displayOptions()
        cmd.showWindow()
       
    def commandMenu(self):
        self.editMenu = cmd.menu(label="Edit")
        self.editMenuSave = cmd.menuItem(label="Save Settings",command=self.editMenuSaveCmd)
        self.editMenuReset = cmd.menuItem(label="Reset Settings",command=self.editMenuResetCmd)
        self.helpMenu = cmd.menu(label="Help")
        self.helpMenuItem = cmd.menuItem(label="Help on %s"%(self.title),command=self.helpMenuCmd)
    def helpMenuCmd(self,*args):
        cmd.launch(web="http://maya-python.com")
    def editMenuSaveCmd(self,*args):pass
    def editMenuResetCmd(self,*args):pass
    
    def actionCmd(self,*args):
        print "ACTION"
    def applyBtnCmd(self,*args):
        print "APPLY"
    def closeBtnCmd(self,*args):
        cmd.deleteUI(self.window,window=True)

   

    def commonButtons(self):
        self.commonBtnSize=(self.size[0]-18/3,26)
        self.acctionBtn=cmd.button(label=self.actionName,height=self.commonBtnSize[1], command = self.actionCmd)    
        self.applyBtn=cmd.button(label=self.applyName,height=self.commonBtnSize[1],command=self.applyBtnCmd)
        self.closeBtn = cmd.button(label="Close",height=self.commonBtnSize[1],command=self.closeBtnCmd)
        
        
        cmd.formLayout(self.mainForm, e=True, attachForm=([self.acctionBtn,"left",5],
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