import maya.cmds as cmd
import OptionsWindowBaseClass

#this is useful later (Defines our control colors
def yellowcon(s):
	cmd.setAttr(s+'overrideEnabled',1)
	cmd.setAttr(s+'.overrideColor',17)
def bluecon(s):
	cmd.setAttr(s+'.overrideEnabled',1)
	cmd.setAttr(s+'.overrideColor',6)
def redcon(s):
	cmd.setAttr(s+'.overrideEnabled',1)
	cmd.setAttr(s+'.overrideColor',13)
	
	
def assignPos(joint, x, y, z) :
	cmd.setAttr(joint+'.tx', x)
	cmd.setAttr(joint+'.ty', y)
	cmd.setAttr(joint+'.tz', z)
	
	
	
#Function to create the joints and controls
def createJointWithControl(joint, parent, x, y, z) :
    #NOTES FOR THIS FUNCTION: WHEN PLACING THE JOINT, TRANSLATE THE CONTROL GROUP, *NOT* THE JOINT OR CONTROL
	
	#Create thumb base joint
	rht1 = cmd.joint(n= joint + '_JNT')
	#translate the joint to the proper position (translation values subject to change
	assignPos(rht1, x, y, z)
	
	#create control and set control group position
	rht1c = cmd.circle(n= joint + '_CNTRL')
	rht1cg = cmd.group(n= joint + 'Cntrl_GRP')
	
	assignPos(rht1cg, x, y, z)
	
	cmd.parentConstraint(rht1c, rht1, mo=True, n= joint + '_Constraint')
	
	bluecon(rht1c[0])
	cmd.select(d=True)
	#parent this joint
	cmd.parent( joint + '_JNT', parent + '_JNT') #currently this isn't giving the behavior we want. ASK ALEX ON MONDAY
	cmd.select(d=True)
	

#class to handle the attributes of a given joint
class JointData :
    
	def __init__(self, joint, parent, x, y, z) :
		self.joint = joint
		self.parent = parent
		self.x = x
		self.y = y
		self.z = z
		
	

class RiggingWindow(OptionsWindowBaseClass.OptionsWindow) :
    
    def __init__(self) :
        OptionsWindowBaseClass.OptionsWindow.__init__(self)
        self.title = "Rigging Tool"
        
    def actionCmd (self, *args) :
        
        self.applyBtnCmd()
        cmd.deleteUI( self.window, window=True )
        
    def applyBtnCmd (self, *args) :
        
        # jointList is only going to have HALF of the skeleton (plus central joints like the spine)
		# Later we will copy one side, mirror it, and rename it
		
		#List of joints (currently all these number values are invalid. I'm working on fixing these.)
		jointList = []
		
		#spine, starting at the root
		jointList.append(JointData('spine', 'root', 0, 3, -2))
		jointList.append(JointData('chest', 'spine', 0, 7, 1))
		jointList.append(JointData('neck_base', 'chest', 0, 16, -3))
		jointList.append(JointData('skull_base', 'neck_base', 0, 22, -2))
		jointList.append(JointData('skull_top', 'skull_base', 0, 28, -3))
		
		
		#Arm and shoulder, starting from neck_base
		jointList.append(JointData('r_shoulder', 'neck_base', -5, 18, -1))
		jointList.append(JointData('r_elbow', 'r_shoulder', -12, 16, -2))
		jointList.append(JointData('r_wrist', 'r_elbow', -18, 16, 0))
		
		#note: I *could* just create the hand with the same values from the midterm, 
		# then translate the wrist a set amount to make room for the arm and torso before mirroring...
		#Hand NEED ALEX'S HELP WITH THIS
		jointList.append(JointData('r_thumb1', 'r_wrist', -5, -5, 5))
		jointList.append(JointData('r_thumb2', 'r_thumb1', -8, -7, 8))
		jointList.append(JointData('r_thumb3', 'r_thumb2', -9, -8, 9))
		
		jointList.append(JointData('r_index1', 'r_wrist', -13, 0, 3))
		jointList.append(JointData('r_index2', 'r_index1', -5, -5, 5))
		jointList.append(JointData('r_index3', 'r_index2', -5, -5, 5))
		jointList.append(JointData('r_index_tip', 'r_index3', -5, -5, 5))
		
		jointList.append(JointData('r_middle1', 'r_wrist', -5, -5, 5))
		jointList.append(JointData('r_middle2', 'r_middle1', -5, -5, 5))
		jointList.append(JointData('r_middle3', 'r_middle2', -5, -5, 5))
		jointList.append(JointData('r_middle_tip', 'r_middle3', -5, -5, 5))
		
		jointList.append(JointData('r_ring1', 'r_wrist', -5, -5, 5))
		jointList.append(JointData('r_ring2', 'r_ring1', -5, -5, 5))
		jointList.append(JointData('r_ring3', 'r_ring2', -5, -5, 5))
		jointList.append(JointData('r_ring_tip', 'r_ring3', -5, -5, 5))
		
		#pinkie did not exist in the midterm, but could be added
		#jointList.append(JointData('r_pinkie1', 'r_wrist', -5, -5, 5))
		#jointList.append(JointData('r_pinkie2', 'r_pinkie1', -5, -5, 5))
		#jointList.append(JointData('r_pinkie3', 'r_pinkie2', -5, -5, 5))
		#jointList.append(JointData('r_pinkie_tip', 'r_pinkie3', -5, -5, 5))
		
		
		#Leg and Hip
		jointList.append(JointData('r_hip', 'spine', -4, 2.5, -2))
		jointList.append(JointData('r_knee', 'r_hip', -4, -10, 0.5))
		jointList.append(JointData('r_ankle', 'r_knee', -4, -20, -1))
		jointList.append(JointData('r_toe', 'r_ankle', -4, -20.0, 1))
		
		
		# ACTUALLY BUILD THE SKELETON
		
		
			#Create the rig
			#THE ROOT NODE ****MUST**** BE WRITTEN OUTSIDE OF THE LOOP VVVVVVV
			
		#Variables named by abbreviation. Rhw = Right Hand Wrist, Rht = right hand thumb, etc
		
		#The root joint has to be created first, and needs to be done outside the function because it has no parent.
		#Create Root joint
		r = cmd.joint(n='root_JNT')
		#Create Root Control
		rControl = cmd.circle(n='root_CNTRL')
		rControlGroup = cmd.group(n='root_GRP')
		cmd.parentConstraint(rControl, r, mo=True, n='myConstraint') #make sure this constrains the correct object
		#cmd.setAttr(Rhwcg+'.tx',5) #translate control group 5 along the X-axis (this also moves the joint) (This is commented out for the wrist, because I want to START at 0,0. This will be different in the final full-rig version.)
		bluecon(rControl[0]) #color the controller using the definitions set above
		cmd.select(d=True)
		
		
		#Create everything else and mirror
		for jData in jointList :
			createJointWithControl(jData.joint, jData.parent, jData.x, jData.y, jData.z)
			
			#mirror
			#This works for mirroring. I *COULD* use maya.cmds(mirror) but where's the fun in that?
			if jData.joint[0] == 'r' and jData.joint[1] == '_' :
				lJointStr = jData.joint
				lJointStr = 'l' + lJointStr[1:]
				lParentStr = jData.parent
				
				if lParentStr[0] == 'r' and lParentStr[1] == '_':
					lParentStr = 'l' + lParentStr[1:]
					
				createJointWithControl(lJointStr, lParentStr, -jData.x, jData.y, jData.z)


thing = RiggingWindow()
thing.create()