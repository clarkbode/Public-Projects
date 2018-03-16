#Midterm/Final: Auto-Rigging
#Step 1 (midterm assignment): Rig a hand
import maya.cmds as cmd

#this is useful later
def yellowcon(s):
	cmd.setAttr(s+'overrideEnabled',1)
	cmd.setAttr(s+'.overrideColor',17)
def bluecon(s):
	cmd.setAttr(s+'.overrideEnabled',1)
	cmd.setAttr(s+'.overrideColor',6)
def redcon(s):
	cmd.setAttr(s+'.overrideEnabled',1)
	cmd.setAttr(s+'.overrideColor',13)
	
#Create the rig
#Variables named by abbreviation. Rhw = Right Hand Wrist, Rht = right hand thumb, etc

#Create Wrist joint
Rhw = cmd.joint(n='r_wrist_JNT')
#rht = cmd.joint(n='r_thumb1_JNT')
#cmd.setAttr(rht+'.ty',.5) #set attributes of rht, 'ty' is 'translate y', .5 is the amount translated.
#cmd.setAttr(rht+'.visibility', 0)
#Create Wrist Control
Rhwc = cmd.circle(n='r_wrist_CNTRL')
Rhwcg = cmd.group(n='r_wristCntrl_GRP')
cmd.parentConstraint(Rhwc, Rhw, mo=True, n='myConstraint') #make sure this constrains the correct object
#cmd.setAttr(Rhwcg+'.tx',5) #translate control group 5 along the X-axis (this also moves the joint) (This is commented out for the wrist, because I want to START at 0,0. This will be different in the final full-rig version.)
bluecon(Rhwc[0]) #color the controller using the definitions set above
cmd.select(d=True) #Deselect the current joint so that we can make the next joint independantly (might not need this for hand rig)


#This rig doesnt use a palm joint
#Create thumb base joint
rht1 = cmd.joint(n='r_thumb1_JNT')
#translate the joint to the proper position (translation values subject to change
cmd.setAttr(rht1+'.tx', -5) #translate X
cmd.setAttr(rht1+'.ty', -5) #translate Y
cmd.setAttr(rht1+'.tz', 5) #translate Z
#create control and set control group position
rht1c = cmd.circle(n='r_thumb1_CNTRL')
rht1cg = cmd.group(n='r_thumb1Cntrl_GRP')
cmd.setAttr(rht1cg+'.tx', -5) #translate X
cmd.setAttr(rht1cg+'.ty', -5) #translate Y
cmd.setAttr(rht1cg+'.tz', 5) #translate Z
cmd.parentConstraint(rht1c, rht1, mo=True, n='thumb1Constraint')

bluecon(rht1c[0])
cmd.select(d=True)
#parent this joint to the previous joint
cmd.parent( 'r_thumb1_JNT', 'r_wrist_JNT') #currently this isn't giving the behavior we want. ASK ALEX ON MONDAY
cmd.select(d=True)

#thumb knuckle 1
rht2 = cmd.joint(n='r_thumb2_JNT')
#translate the joint to the proper position (translation values subject to change
cmd.setAttr(rht2+'.tx', -8) #translate X
cmd.setAttr(rht2+'.ty', -7) #translate Y
cmd.setAttr(rht2+'.tz', 8) #translate Z
#create control and set control group position
rht2c = cmd.circle(n='r_thumb2_CNTRL')
rht2cg = cmd.group(n='r_thumb2Cntrl_GRP')
cmd.setAttr(rht2cg+'.tx', -8) #translate X
cmd.setAttr(rht2cg+'.ty', -7) #translate Y
cmd.setAttr(rht2cg+'.tz', 8) #translate Z
cmd.parentConstraint(rht2c, rht2, mo=True, n='thumb2Constraint')

bluecon(rht2c[0])
#parent this joint to the previous joint
cmd.parent( 'r_thumb2_JNT', 'r_thumb1_JNT') #currently this isn't giving the behavior we want. ASK ALEX ON MONDAY
cmd.select(d=True)

#thumb knuckle 2
rht3 = cmd.joint(n='r_thumb3_JNT')
#translate the joint to the proper position (translation values subject to change
cmd.setAttr(rht3+'.tx', -9) #translate X
cmd.setAttr(rht3+'.ty', -8) #translate Y
cmd.setAttr(rht3+'.tz', 9) #translate Z
#create control and set control group position
rht3c = cmd.circle(n='r_thumb3_CNTRL')
rht3cg = cmd.group(n='r_thumb31Cntrl_GRP')
cmd.setAttr(rht3cg+'.tx', -9) #translate X
cmd.setAttr(rht3cg+'.ty', -8) #translate Y
cmd.setAttr(rht3cg+'.tz', 9) #translate Z
cmd.parentConstraint(rht3c, rht3, mo=True, n='thumb3Constraint')

bluecon(rht3c[0])
#parent this joint to the previous joint
cmd.parent( 'r_thumb3_JNT', 'r_thumb2_JNT') #currently this isn't giving the behavior we want. ASK ALEX ON MONDAY
cmd.select(d=True)

#thumb tip (might actually not be necessary


#index 1
rhi1 = cmd.joint(n='r_index1_JNT')
#translate the joint to the proper position (translation values subject to change
cmd.setAttr(rhi1+'.tx', -13) #translate X
cmd.setAttr(rhi1+'.ty', 0) #translate Y
cmd.setAttr(rhi1+'.tz', 3) #translate Z
#create control and set control group position
rhi1c = cmd.circle(n='r_index1_CNTRL')
rhi1cg = cmd.group(n='r_index11Cntrl_GRP')
cmd.setAttr(rhi1cg+'.tx', -13) #translate X
cmd.setAttr(rhi1cg+'.ty', 0) #translate Y
cmd.setAttr(rhi1cg+'.tz', 3) #translate Z
cmd.parentConstraint(rhi1c, rhi1, mo=True, n='index1Constraint')

bluecon(rhi1c[0])
#parent this joint to the previous joint
cmd.parent( 'r_index1_JNT', 'r_wrist_JNT') #currently this isn't giving the behavior we want. ASK ALEX ON MONDAY
cmd.select(d=True)

#index 2
rhi2 = cmd.joint(n='r_index2_JNT')
#translate the joint to the proper position (translation values subject to change
cmd.setAttr(rhi2+'.tx', -19) #translate X
cmd.setAttr(rhi2+'.ty', 0) #translate Y
cmd.setAttr(rhi2+'.tz', 3) #translate Z
#create control and set control group position
rhi2c = cmd.circle(n='r_index2_CNTRL')
rhi2cg = cmd.group(n='r_index21Cntrl_GRP')
cmd.setAttr(rhi2cg+'.tx', -19) #translate X
cmd.setAttr(rhi2cg+'.ty', 0) #translate Y
cmd.setAttr(rhi2cg+'.tz', 3) #translate Z
cmd.parentConstraint(rhi2c, rhi2, mo=True, n='index2Constraint')

bluecon(rhi2c[0])
#parent this joint to the previous joint
cmd.parent( 'r_index2_JNT', 'r_index1_JNT') #currently this isn't giving the behavior we want. ASK ALEX ON MONDAY
cmd.select(d=True)

#index 3
rhi3 = cmd.joint(n='r_index3_JNT')
#translate the joint to the proper position (translation values subject to change
cmd.setAttr(rhi3+'.tx', -24) #translate X
cmd.setAttr(rhi3+'.ty', 0) #translate Y
cmd.setAttr(rhi3+'.tz', 3) #translate Z
#create control and set control group position
rhi3c = cmd.circle(n='r_index3_CNTRL')
rhi3cg = cmd.group(n='r_index31Cntrl_GRP')
cmd.setAttr(rhi3cg+'.tx', -24) #translate X
cmd.setAttr(rhi3cg+'.ty', 0) #translate Y
cmd.setAttr(rhi3cg+'.tz', 3) #translate Z
cmd.parentConstraint(rhi3c, rhi3, mo=True, n='index3Constraint')

bluecon(rhi3c[0])
#parent this joint to the previous joint
cmd.parent( 'r_index3_JNT', 'r_index2_JNT') #currently this isn't giving the behavior we want. ASK ALEX ON MONDAY
cmd.select(d=True)

#index tip
rhit = cmd.joint(n='r_indexTip_JNT')
#translate the joint to the proper position (translation values subject to change
cmd.setAttr(rhit+'.tx', -26) #translate X
cmd.setAttr(rhit+'.ty', 0) #translate Y
cmd.setAttr(rhit+'.tz', 3) #translate Z
#create control and set control group position
rhitc = cmd.circle(n='r_indexTip_CNTRL')
rhitcg = cmd.group(n='r_indexTip1Cntrl_GRP')
cmd.setAttr(rhitcg+'.tx', -26) #translate X
cmd.setAttr(rhitcg+'.ty', 0) #translate Y
cmd.setAttr(rhitcg+'.tz', 3) #translate Z
cmd.parentConstraint(rhitc, rhit, mo=True, n='indexTipConstraint')

bluecon(rhitc[0])
#parent this joint to the previous joint
cmd.parent( 'r_indexTip_JNT', 'r_index3_JNT') #currently this isn't giving the behavior we want. ASK ALEX ON MONDAY
cmd.select(d=True)


#middle 1
rhm1 = cmd.joint(n='r_middle1_JNT')
#translate the joint to the proper position (translation values subject to change
cmd.setAttr(rhm1+'.tx', -13) #translate X
cmd.setAttr(rhm1+'.ty', 0) #translate Y
cmd.setAttr(rhm1+'.tz', 0) #translate Z
#create control and set control group position
rhm1c = cmd.circle(n='r_middle1_CNTRL')
rhm1cg = cmd.group(n='r_middle11Cntrl_GRP')
cmd.setAttr(rhm1cg+'.tx', -13) #translate X
cmd.setAttr(rhm1cg+'.ty', 0) #translate Y
cmd.setAttr(rhm1cg+'.tz', 0) #translate Z
cmd.parentConstraint(rhm1c, rhm1, mo=True, n='middle1Constraint')

bluecon(rhm1c[0])
#parent this joint to the previous joint
cmd.parent( 'r_middle1_JNT', 'r_wrist_JNT') #currently this isn't giving the behavior we want. ASK ALEX ON MONDAY
cmd.select(d=True)

#middle 2
rhm2 = cmd.joint(n='r_middle2_JNT')
#translate the joint to the proper position (translation values subject to change
cmd.setAttr(rhm2+'.tx', -20) #translate X
cmd.setAttr(rhm2+'.ty', 0) #translate Y
cmd.setAttr(rhm2+'.tz', 0) #translate Z
#create control and set control group position
rhm2c = cmd.circle(n='r_middle2_CNTRL')
rhm2cg = cmd.group(n='r_middle21Cntrl_GRP')
cmd.setAttr(rhm2cg+'.tx', -20) #translate X
cmd.setAttr(rhm2cg+'.ty', 0) #translate Y
cmd.setAttr(rhm2cg+'.tz', 0) #translate Z
cmd.parentConstraint(rhm2c, rhm2, mo=True, n='middle2Constraint')

bluecon(rhm2c[0])
#parent this joint to the previous joint
cmd.parent( 'r_middle2_JNT', 'r_middle1_JNT') #currently this isn't giving the behavior we want. ASK ALEX ON MONDAY
cmd.select(d=True)

#middle 3
rhm3 = cmd.joint(n='r_middle3_JNT')
#translate the joint to the proper position (translation values subject to change
cmd.setAttr(rhm3+'.tx', -26) #translate X
cmd.setAttr(rhm3+'.ty', 0) #translate Y
cmd.setAttr(rhm3+'.tz', 0) #translate Z
#create control and set control group position
rhm3c = cmd.circle(n='r_middle3_CNTRL')
rhm3cg = cmd.group(n='r_middle31Cntrl_GRP')
cmd.setAttr(rhm3cg+'.tx', -26) #translate X
cmd.setAttr(rhm3cg+'.ty', 0) #translate Y
cmd.setAttr(rhm3cg+'.tz', 0) #translate Z
cmd.parentConstraint(rhm3c, rhm3, mo=True, n='middle3Constraint')

bluecon(rhm3c[0])
#parent this joint to the previous joint
cmd.parent( 'r_middle3_JNT', 'r_middle2_JNT') #currently this isn't giving the behavior we want. ASK ALEX ON MONDAY
cmd.select(d=True)

#middle tip
rhmt = cmd.joint(n='r_middleTip_JNT')
#translate the joint to the proper position (translation values subject to change
cmd.setAttr(rhmt+'.tx', -29) #translate X
cmd.setAttr(rhmt+'.ty', 0) #translate Y
cmd.setAttr(rhmt+'.tz', 0) #translate Z
#create control and set control group position
rhmtc = cmd.circle(n='r_middleTip_CNTRL')
rhmtcg = cmd.group(n='r_middleTip1Cntrl_GRP')
cmd.setAttr(rhmtcg+'.tx', -29) #translate X
cmd.setAttr(rhmtcg+'.ty', 0) #translate Y
cmd.setAttr(rhmtcg+'.tz', 0) #translate Z
cmd.parentConstraint(rhmtc, rhmt, mo=True, n='middleTipConstraint')

bluecon(rhmtc[0])
#parent this joint to the previous joint
cmd.parent( 'r_middleTip_JNT', 'r_middle3_JNT') #currently this isn't giving the behavior we want. ASK ALEX ON MONDAY
cmd.select(d=True)


#ring 1
rhr1 = cmd.joint(n='r_ring1_JNT')
#translate the joint to the proper position (translation values subject to change
cmd.setAttr(rhr1+'.tx', -13) #translate X
cmd.setAttr(rhr1+'.ty', 0) #translate Y
cmd.setAttr(rhr1+'.tz', -3) #translate Z
#create control and set control group position
rhr1c = cmd.circle(n='r_ring1_CNTRL')
rhr1cg = cmd.group(n='r_ring11Cntrl_GRP')
cmd.setAttr(rhr1cg+'.tx', -13) #translate X
cmd.setAttr(rhr1cg+'.ty', 0) #translate Y
cmd.setAttr(rhr1cg+'.tz', -3) #translate Z
cmd.parentConstraint(rhr1c, rhr1, mo=True, n='ring1Constraint')

bluecon(rhr1c[0])
#parent this joint to the previous joint
cmd.parent( 'r_ring1_JNT', 'r_wrist_JNT') #currently this isn't giving the behavior we want. ASK ALEX ON MONDAY
cmd.select(d=True)

#ring 2
rhr2 = cmd.joint(n='r_ring2_JNT')
#translate the joint to the proper position (translation values subject to change
cmd.setAttr(rhr2+'.tx', -18) #translate X
cmd.setAttr(rhr2+'.ty', 0) #translate Y
cmd.setAttr(rhr2+'.tz', -3) #translate Z
#create control and set control group position
rhr2c = cmd.circle(n='r_ring2_CNTRL')
rhr2cg = cmd.group(n='r_ring21Cntrl_GRP')
cmd.setAttr(rhr2cg+'.tx', -18) #translate X
cmd.setAttr(rhr2cg+'.ty', 0) #translate Y
cmd.setAttr(rhr2cg+'.tz', -3) #translate Z
cmd.parentConstraint(rhr2c, rhr2, mo=True, n='ring2Constraint')

bluecon(rhr2c[0])
#parent this joint to the previous joint
cmd.parent( 'r_ring2_JNT', 'r_ring1_JNT') #currently this isn't giving the behavior we want. ASK ALEX ON MONDAY
cmd.select(d=True)

#ring 3
rhr3 = cmd.joint(n='r_ring3_JNT')
#translate the joint to the proper position (translation values subject to change
cmd.setAttr(rhr3+'.tx', -23) #translate X
cmd.setAttr(rhr3+'.ty', 0) #translate Y
cmd.setAttr(rhr3+'.tz', -3) #translate Z
#create control and set control group position
rhr3c = cmd.circle(n='r_ring3_CNTRL')
rhr3cg = cmd.group(n='r_ring31Cntrl_GRP')
cmd.setAttr(rhr3cg+'.tx', -23) #translate X
cmd.setAttr(rhr3cg+'.ty', 0) #translate Y
cmd.setAttr(rhr3cg+'.tz', -3) #translate Z
cmd.parentConstraint(rhr3c, rhr3, mo=True, n='ring3Constraint')

bluecon(rhr3c[0])
#parent this joint to the previous joint
cmd.parent( 'r_ring3_JNT', 'r_ring2_JNT') #currently this isn't giving the behavior we want. ASK ALEX ON MONDAY
cmd.select(d=True)

#ring tip
rhrt = cmd.joint(n='r_ringTip_JNT')
#translate the joint to the proper position (translation values subject to change
cmd.setAttr(rhrt+'.tx', -25) #translate X
cmd.setAttr(rhrt+'.ty', 0) #translate Y
cmd.setAttr(rhrt+'.tz', -3) #translate Z
#create control and set control group position
rhrtc = cmd.circle(n='r_ringTip_CNTRL')
rhrtcg = cmd.group(n='r_ringTip1Cntrl_GRP')
cmd.setAttr(rhrtcg+'.tx', -25) #translate X
cmd.setAttr(rhrtcg+'.ty', 0) #translate Y
cmd.setAttr(rhrtcg+'.tz', -3) #translate Z
cmd.parentConstraint(rhrtc, rhrt, mo=True, n='ringTipConstraint')

bluecon(rhrtc[0])
#parent this joint to the previous joint
cmd.parent( 'r_ringTip_JNT', 'r_ring3_JNT') #currently this isn't giving the behavior we want. ASK ALEX ON MONDAY
cmd.select(d=True)



#pinky 1

#pinky 2

#pinky 3

#pinky tip