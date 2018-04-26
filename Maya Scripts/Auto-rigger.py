import maya.cmds as cmd
import OptionsWindowBaseClass

#Maya Toolbar Implementation
def Final_AutoRigger() :
    thing = RiggingWindow()
    thing.create()
    

#this is useful later (Defines our control colors)
def yellowcon(s):
	cmd.setAttr(s+'overrideEnabled',1)
	cmd.setAttr(s+'.overrideColor',17)
def bluecon(s):
	cmd.setAttr(s+'.overrideEnabled',1)
	cmd.setAttr(s+'.overrideColor',6)
def redcon(s):
	cmd.setAttr(s+'.overrideEnabled',1)
	cmd.setAttr(s+'.overrideColor',13)
	
	#function used to assign positions to a joint or control
def assignPos(joint, x, y, z) :
	cmd.setAttr(joint+'.tx', x)
	cmd.setAttr(joint+'.ty', y)
	cmd.setAttr(joint+'.tz', z)
	
	
	
#Function to create the joints and controls
def createJointWithControl(joint, parent, control_grp, parent_control, x, y, z) : 
	
	#Create joint
	rht1 = cmd.joint(n= joint + '_JNT')
	
	#translate the joint to the proper position
	assignPos(rht1, x, y, z)
	
	#create control and set control group position
	rht1c = cmd.circle(n= joint + '_CNTRL')
	rht1cg = cmd.group(n= joint + '_Cntrl_GRP')
	
	assignPos(rht1cg, x, y, z)
	
	#parent constrain the joint and control joint
	cmd.parentConstraint(rht1c, rht1, mo=True, n= joint + '_Constraint')
	
	bluecon(rht1c[0])
	cmd.select(d=True)
	#parent this joint
	cmd.parent( joint + '_JNT', parent + '_JNT') #currently this isn't giving the behavior we want. ASK ALEX ON MONDAY
	cmd.select(d=True)

	# Parent the control group to the previous control group in the heirarchy
	cmd.parent( control_grp + '_Cntrl_GRP', parent_control + '_Cntrl_GRP')
	cmd.select(d=True)
	    
	

#class to handle the attributes of a given joint
class JointData :
#Every joint has its name, its parent, its group, its group's parent, and its location in x, y, z
	def __init__(self, joint, parent, control_grp, parent_control, x, y, z) :
		self.joint = joint
		self.parent = parent
		self.control_grp = control_grp
		self.parent_control = parent_control
		self.x = x
		self.y = y
		self.z = z
		
	
# Window class taken from in-class work
class RiggingWindow(OptionsWindowBaseClass.OptionsWindow) :
    
    def __init__(self) :
        OptionsWindowBaseClass.OptionsWindow.__init__(self)
        self.title = "Rigging Tool"
        
    def actionCmd (self, *args) :
        
        self.applyBtnCmd()
        cmd.deleteUI( self.window, window=True )
    
	#when button is pushed:
    def applyBtnCmd (self, *args) :
        

		#List of joints
		# jointList is only going to have HALF of the skeleton (plus central joints like the spine)
		jointList = []
		
		#spine, does not include root but is parented to it
		jointList.append(JointData('spine', 'root', 'spine', 'root', 0, 3, -2))
		jointList.append(JointData('chest', 'spine','chest', 'spine', 0, 7, 1))
		jointList.append(JointData('neck_base', 'chest','neck_base', 'chest', 0, 16, -3))
		jointList.append(JointData('skull_base', 'neck_base','skull_base', 'neck_base', 0, 22, -2))
		jointList.append(JointData('skull_top', 'skull_base','skull_top', 'skull_base', 0, 28, -3))
		
		
		#Arm and shoulder, starting from neck_base
		jointList.append(JointData('r_shoulder', 'neck_base','r_shoulder', 'neck_base', -5, 18, -1))
		jointList.append(JointData('r_elbow', 'r_shoulder','r_elbow', 'r_shoulder', -12, 16, -2))
		jointList.append(JointData('r_wrist', 'r_elbow','r_wrist', 'r_elbow', -18, 16, 0))
		
		
		#Hand
		jointList.append(JointData('r_thumb1', 'r_wrist','r_thumb1', 'r_wrist', -18.5, 15.2, 1))
		jointList.append(JointData('r_thumb2', 'r_thumb1','r_thumb2', 'r_thumb1', -19.4, 14.65, 1.68))
		jointList.append(JointData('r_thumb3', 'r_thumb2','r_thumb3', 'r_thumb2', -20.2, 14, 2.9))
		
		jointList.append(JointData('r_index1', 'r_wrist','r_index1', 'r_wrist', -19.8, 15.9, 0.9))
		jointList.append(JointData('r_index2', 'r_index1','r_index2', 'r_index1', -21.4, 15.9, 1))
		jointList.append(JointData('r_index3', 'r_index2','r_index3', 'r_index2', -22.8, 15.9, 1.1))
		jointList.append(JointData('r_index_tip', 'r_index3','r_index_tip', 'r_index3', -24.2, 15.9, 1.1))
		
		jointList.append(JointData('r_middle1', 'r_wrist','r_middle1', 'r_wrist', -20.5, 16, -0.1))
		jointList.append(JointData('r_middle2', 'r_middle1','r_middle2', 'r_middle1', -21.8, 16, -0.1))
		jointList.append(JointData('r_middle3', 'r_middle2','r_middle3', 'r_middle2', -23.6, 16, -0.1))
		jointList.append(JointData('r_middle_tip', 'r_middle3','r_middle_tip', 'r_middle3', -24.4, 16, -0.1))
		
		jointList.append(JointData('r_ring1', 'r_wrist','r_ring1', 'r_wrist', -19.875, 16, -1.2))
		jointList.append(JointData('r_ring2', 'r_ring1','r_ring2', 'r_ring1', -21.15, 16, -1.2))
		jointList.append(JointData('r_ring3', 'r_ring2','r_ring3', 'r_ring2', -22.4, 16, -1.2))
		jointList.append(JointData('r_ring_tip', 'r_ring3','r_ring_tip', 'r_ring3', -23.55, 16, -1.2))
		
		
		#Leg, foot, and Hip
		jointList.append(JointData('r_hip', 'spine','r_hip', 'spine', -4, 2.5, -2))
		jointList.append(JointData('r_knee', 'r_hip','r_knee', 'r_hip', -4, -10, 0.5))
		jointList.append(JointData('r_ankle', 'r_knee','r_ankle', 'r_knee', -4, -20, -1))
		jointList.append(JointData('r_toe', 'r_ankle','r_toe', 'r_ankle', -4, -20.0, 1))
		
		
		# ACTUALLY BUILD THE SKELETON
		
		
		#Create the rig
		#THE ROOT NODE ****MUST**** BE WRITTEN OUTSIDE OF THE LOOP VVVVVVV
		#The root joint has to be created first, and needs to be done outside the function because it has no parent.
		
		# change size of the joints so that they're more useable with smaller bones like the hands
		cmd.jointDisplayScale( 0.5 )
		
		#Create Root joint
		r = cmd.joint(n='root_JNT')
		
		#Create Root Control
		rControl = cmd.circle(n='root_CNTRL')
		rControlGroup = cmd.group(n='root_Cntrl_GRP')
		cmd.parentConstraint(rControl, r, mo=True, n='myConstraint')
	
		bluecon(rControl[0]) #color the controller using the functions set above
		cmd.select(d=True)
		
		
		
		#Create and place the joints and mirror
		for jData in jointList :
			#build the right side
			createJointWithControl(jData.joint, jData.parent, jData.control_grp, jData.parent_control, jData.x, jData.y, jData.z)
			
			#mirror
			#This works for mirroring. I *COULD* use maya.cmds(mirror) but where's the fun in that?
			
			#check whether a joint or control begins with 'r_', meaning it is a right-side joint
			#if yes, copy the joint, rename the beginning to 'l_'
			if jData.joint[0] == 'r' and jData.joint[1] == '_' :
				lJointStr = jData.joint
				lJointStr = 'l' + lJointStr[1:]
				lParentStr = jData.parent
				lControlGRP = jData.control_grp
				lControlGRP = 'l' + lControlGRP[1:]
				lControlParent = jData.parent_control
				
				#Do the same with the parents
				if lParentStr[0] == 'r' and lParentStr[1] == '_':
					lParentStr = 'l' + lParentStr[1:]
					lControlParent = 'l' + lControlParent[1:]
				#build the left side	
				createJointWithControl(lJointStr, lParentStr, lControlGRP, lControlParent, -jData.x, jData.y, jData.z)


