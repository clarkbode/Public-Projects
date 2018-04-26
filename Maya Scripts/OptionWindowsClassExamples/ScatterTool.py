import maya.cmds as mc
import random
import OptionsWindowBaseClass

class ScatterBouncyObjects(OptionsWindowBaseClass.OptionsWindow):
    """Custom Window Class, subclass of the OptionWindow base class """
   
        
    def __init__(self):
        OptionsWindowBaseClass.OptionsWindow.__init__(self)
        self.title = "ScatterBouncyObjects"
        self.actionName = "Scatter Objects"
        self.applyName = "Add Dynamics"
    
    def displayOptions(self):
        
        self.objType = mc.radioButtonGrp(label = "Object Type:", labelArray4 = ["Cube","Cone","Cylinder","Sphere"], numberOfRadioButtons = 4, select=1)
        self.xformGrp = mc.frameLayout(label = "Mesh Object Generator", collapsable = True)
        mc.formLayout(self.optionsForm, e = True, attachControl=([self.xformGrp, "top",2,self.objType]), attachForm = ([self.xformGrp, "left",0],[self.xformGrp,"right",0]))
        
        self.xformCol = mc.columnLayout()
        self.position = mc.floatFieldGrp(label = "Range of Translation:",numberOfFields=3, value = [10.0,10.0,10.0,10.0])
        self.rotation = mc.floatFieldGrp(label = "Range of Rotations:",numberOfFields=3, value = [180.0,180.0,180.0,180.0])
        self.scale = mc.floatFieldGrp(label =  "Range of Scale:",numberOfFields=3,value = [3.0,3.0,3.0,3.0])
        self.num = mc.intFieldGrp( label = "Number of Objects", numberOfFields = 1, value1 = 5)
        mc.setParent(self.optionsForm)
        
        
           
    def actionCmd(self,*args):
        """ actionCmd() will be called when the user presses Scatter Objects button 
        This function will read values set by the user and create and possition
        polygonal objects"""
   
        self.objIndAsCmd= { 1 : mc.polyCube, 2 : mc.polyCone, 3 : mc.polyCylinder, 4 : mc.polySphere}
        objIndex = mc.radioButtonGrp(self.objType, q=True, select = True)
        newObject = self.objIndAsCmd[objIndex]()
        
        self.rangeX = mc.floatFieldGrp(self.position, query = True, value1 = True)
        self.rangeY = mc.floatFieldGrp(self.position, query = True, value2 = True)
        self.rangeZ = mc.floatFieldGrp(self.position, query = True, value3 = True)
        
        self.rotX = mc.floatFieldGrp(self.rotation, query = True, value1 = True)
        self.rotY = mc.floatFieldGrp(self.rotation, query = True, value2 = True)
        self.rotZ = mc.floatFieldGrp(self.rotation, query = True, value3 = True)
        
        self.scaleX = mc.floatFieldGrp(self.scale, query = True, value1 = True)
        self.scaleY = mc.floatFieldGrp(self.scale, query = True, value2 = True)
        self.scaleZ = mc.floatFieldGrp(self.scale, query = True, value3 = True)
        
        numberOfObjects = mc.intFieldGrp(self.num, q = True, value1 = True)
        #numberOfObjects = 5
        
        for i in range(numberOfObjects-1):           
            obj = self.objIndAsCmd[objIndex]()
            
            randomX = random.randint(-self.rangeX, self.rangeX)
            randomY = random.randint(-self.rangeY, self.rangeY)
            randomZ = random.randint(-self.rangeZ, self.rangeZ)
                       
            mc.setAttr(obj[0] + ".translateX", randomX)
            mc.setAttr(obj[0] + ".translateY", randomY)
            mc.setAttr(obj[0] + ".translateZ", randomZ)
            
            randRotX = random.randint(-self.rotX, self.rotX)
            randRotY = random.randint(-self.rotY, self.rotY)
            randRotZ = random.randint(-self.rotZ, self.rotZ)
            
            mc.setAttr(obj[0] + ".rotateX", randRotX)
            mc.setAttr(obj[0] + ".rotateY", randRotY)
            mc.setAttr(obj[0] + ".rotateZ", randRotZ)
            
            self.sX = random.randint(1, self.scaleX)
            self.sY = random.randint(1, self.scaleY)
            self.xZ = random.randint(1, self.scaleZ)
            
            mc.setAttr(obj[0] + ".scaleX", self.sX)
            mc.setAttr(obj[0] + ".scaleY", self.sX)
            mc.setAttr(obj[0] + ".scaleZ", self.sX)
            
     
    def applyBtnCmd(self,*args):
        """"applyBtnCmd() function will be called when user presses 
        AddDynamics button. It will create a ground object, turn it into
        passive rigid object in Maya, and loop over all other polygonal objects
        and turn them into active rigid objects. It will connect all active RB to
        gravity.
        """
        
        shapeList = mc.ls(type = "mesh")
        ground = mc.polyCube()
        #move the ground plane under the lowest possible object
        mc.setAttr(ground[0] + ".translateY", -(self.rangeY+4*(self.sX)))
        mc.setAttr(ground[0] + ".scaleX", 5*self.rangeX)
        mc.setAttr(ground[0] + ".scaleY", 1)
        mc.setAttr(ground[0] + ".scaleZ", 5*self.rangeZ)
        
        groundRB = mc.rigidBody( passive = True, bounciness = 0.01, damping = 0.8, staticFriction = 1.0)
        mc.select(clear = True)
        G = mc.gravity(directionX = 0.0, directionY = -1.0, directionZ = 0.0, magnitude = 100)
        listOfObjects = []
        
        for i in shapeList:
            obj = mc.listRelatives(i, p = True)
            mc.select(obj)
            #mc.rigidBody( active = True, mass = 10, initialVelocity = (random.randint(-1,1),random.randint(-1,1),random.randint(-1,1)), bounciness = 0.5)
            mc.rigidBody( active = True, mass = 10, initialVelocity = (0.0,0.0,0.0), bounciness = 0.01, dynamicFriction = 0.8, damping = 0.2)
            mc.connectDynamic(*obj, f = G)

        
        
        


win = ScatterBouncyObjects()
win.create()