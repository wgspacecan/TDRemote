##
## RGB Visuals
## TouchOSC Controller
## 
## 03/31/2023
##

max_scene = 5
powerSettings = [3, 6, 12, 24, 48]

resolutions = {'4K':[3840, 2160], '2K':[2560, 1440], 'QD':[2048, 1080], 'HD':[1920, 1080],
	       '2S':[1440, 1440], 'HS':[1080, 1080]}

logoPositions = {'4K':[-1610, -920], '2K':[-1080, -600], 'QD':[-830, -430], 'HD':[-770, -440],
			'2S':[-530, -610], 'HS':[-390, -460]}

eq_reset_data = 'eq_grid_reset_data/out_eq_grid'
sceneBase = '../scenes'

data = op('data')
constant = op('constant1')
visual_filter = op('filter1')		# scene fade
eqDevice = op('../audioband')
audioDevice = op('../audiodevout')
oscData = op('osc_data')
logo = op('../logo')
logoText = op('../logo/text')
movie = op('../movie_select')
movieFX = op('../movie_fx')

outRadio = op('out_radio')
outGain = op('out_gain')
outClip = op('out_clip')
outProfile = op('out_profile')
outM1 = op('out_mode1')
outM2 = op('out_mode2')
outM3 = op('out_mode3')
outM4 = op('out_mode4')

loadSwitch = op('load_switch') 		# upload state
loadOSCSwitch = op('loadOSC_switch')
radioSwitch = op('load_radio')		# upload profile
baseSwitch = op('load_base')		# upload base
danceSwitch = op('dance_switch') 	# enable dancing

refreshSwitch = op('refresh_switch')
refreshEqStates = op('eq_states')
refreshOscStates = op('controller_refresh/osc_states')
refreshOscInfo = op('controller_refresh/osc_info')

# outputs for state
outS = [op('out_fader1'), op('out_fader2'), op('out_fader3'), op('out_fader4'),
       op('out_x'), op('out_y'), op('out_mode1'),
	   op('out_mode2'), op('out_mode3'), op('out_mode4')]

outSosc = [op('out_max1'), op('out_max2'), op('out_max3'), op('out_max4'), op('out_max5'), 
           op('out_min1'), op('out_min2'), op('out_min3'), op('out_min4'), op('out_min5'), 
           op('out_rate1'), op('out_rate2'), op('out_rate3'), op('out_rate4'), op('out_rate5')]

outSosc2 = op('out_osc_state')

outSosc3 = [op('out_mapA_1'), op('out_mapA_2'), op('out_mapA_3'), op('out_mapA_4'), op('out_mapA_5'), 
	    op('out_mapB_1'), op('out_mapB_2'), op('out_mapB_3'), op('out_mapB_4'), op('out_mapB_5')]

def resetOSCData():
	# max
	oscData.par.value0 = 1
	oscData.par.value1 = 1
	oscData.par.value2 = 1
	oscData.par.value3 = 1
	oscData.par.value4 = 1
	# min
	oscData.par.value5 = 0
	oscData.par.value6 = 0
	oscData.par.value7 = 0
	oscData.par.value8 = 0
	oscData.par.value9 = 0
	# rate
	oscData.par.value10 = 0.5
	oscData.par.value11 = 0.5
	oscData.par.value12 = 0.5
	oscData.par.value13 = 0.5
	oscData.par.value14 = 0.5
	# state
	oscData.par.value15 = 0
	oscData.par.value16 = 0
	oscData.par.value17 = 0
	oscData.par.value18 = 0
	oscData.par.value19 = 0
	# enable
	oscData.par.value20 = 1

def setResolution(r):
	if r in resolutions:
		constant.par.value3 = resolutions[r][0]
		constant.par.value4 = resolutions[r][1]
	if r in logoPositions:
		logoText.par.positionx = logoPositions[r][0]
		logoText.par.positiony = logoPositions[r][1]

def setRefreshDataEQ():
	v = powerSettings[int(constant.par.value5)]
	a = constant.par.value6
	refreshEqStates.par.value0 = eqDevice.par.band1/v + a
	refreshEqStates.par.value1 = eqDevice.par.band2/v + a
	refreshEqStates.par.value2 = eqDevice.par.band3/v + a
	refreshEqStates.par.value3 = eqDevice.par.band4/v + a
	refreshEqStates.par.value4 = eqDevice.par.band5/v + a
	refreshEqStates.par.value5 = eqDevice.par.band6/v + a
	refreshEqStates.par.value6 = eqDevice.par.band7/v + a
	refreshEqStates.par.value7 = eqDevice.par.band8/v + a
	refreshEqStates.par.value8 = eqDevice.par.band9/v + a
	refreshEqStates.par.value9 = eqDevice.par.band10/v + a
	refreshEqStates.par.value10 = eqDevice.par.band11/v + a
	refreshEqStates.par.value11 = eqDevice.par.band12/v + a
	refreshEqStates.par.value12 = eqDevice.par.band13/v + a
	refreshEqStates.par.value13 = eqDevice.par.band14/v + a
	refreshEqStates.par.value14 = eqDevice.par.band15/v + a
	refreshEqStates.par.value15 = eqDevice.par.band16/v + a

def setRefreshData():
	i1 = int(refreshOscInfo[0])
	i2 = int(refreshOscInfo[1])
	i3 = int(refreshOscInfo[2])
	i4 = int(refreshOscInfo[3])
	i5 = int(refreshOscInfo[4])

	refreshOscStates.par.value0 = 0
	refreshOscStates.par.value1 = 0
	refreshOscStates.par.value2 = 0
	refreshOscStates.par.value3 = 0
	refreshOscStates.par.value4 = 0
	refreshOscStates.par.value5 = 0
	refreshOscStates.par.value6 = 0
	refreshOscStates.par.value7 = 0
	refreshOscStates.par.value8 = 0
	refreshOscStates.par.value9 = 0
	refreshOscStates.par.value10 = 0
	refreshOscStates.par.value11 = 0
	refreshOscStates.par.value12 = 0
	refreshOscStates.par.value13 = 0
	refreshOscStates.par.value14 = 0
	refreshOscStates.par.value15 = 0
	refreshOscStates.par.value16 = 0
	refreshOscStates.par.value17 = 0
	refreshOscStates.par.value18 = 0
	refreshOscStates.par.value19 = 0
	refreshOscStates.par.value20 = 0
	refreshOscStates.par.value21 = 0
	refreshOscStates.par.value22 = 0
	refreshOscStates.par.value23 = 0
	refreshOscStates.par.value24 = 0

	if i1 == 1: refreshOscStates.par.value0 = 1
	if i1 == 2: refreshOscStates.par.value1 = 1
	if i1 == 3: refreshOscStates.par.value2 = 1
	if i1 == 4: refreshOscStates.par.value3 = 1
	if i1 == 5: refreshOscStates.par.value4 = 1
	if i2 == 1: refreshOscStates.par.value5 = 1
	if i2 == 2: refreshOscStates.par.value6 = 1
	if i2 == 3: refreshOscStates.par.value7 = 1
	if i2 == 4: refreshOscStates.par.value8 = 1
	if i2 == 5: refreshOscStates.par.value9 = 1
	if i3 == 1: refreshOscStates.par.value10 = 1
	if i3 == 2: refreshOscStates.par.value11 = 1
	if i3 == 3: refreshOscStates.par.value12 = 1
	if i3 == 4: refreshOscStates.par.value13 = 1
	if i3 == 5: refreshOscStates.par.value14 = 1
	if i4 == 1: refreshOscStates.par.value15 = 1
	if i4 == 2: refreshOscStates.par.value16 = 1
	if i4 == 3: refreshOscStates.par.value17 = 1
	if i4 == 4: refreshOscStates.par.value18 = 1
	if i4 == 5: refreshOscStates.par.value19 = 1
	if i5 == 1: refreshOscStates.par.value20 = 1
	if i5 == 2: refreshOscStates.par.value21 = 1
	if i5 == 3: refreshOscStates.par.value22 = 1
	if i5 == 4: refreshOscStates.par.value23 = 1
	if i5 == 5: refreshOscStates.par.value24 = 1

# determine and return save block operator
# 	current visual					int
# 	profile							int
def getSaveBlockID(vis, pro):
	if pro == -2:
		s = 'saves/' + 'osc_data' + str(vis)
	elif pro == -1:
		s = 'saves/' + str(vis) + 'state'
	elif pro == 0:
		s = 'saves/' + str(vis) + 'default_save'
	else:
		s = 'saves/' + str(vis) + 'save' + str(pro)
	return op(s)

# get and return state from data block
def getState():
	dataFader1 = data.par.value6
	dataFader2 = data.par.value7
	dataFader3 = data.par.value8
	dataFader4 = data.par.value9
	dataInX = data.par.value10
	dataInY = data.par.value11
	dataMode1 = data.par.value2
	dataMode2 = data.par.value3
	dataMode3 = data.par.value4
	dataMode4 = data.par.value5

	vals = []
	vals.append(dataFader1)
	vals.append(dataFader2)
	vals.append(dataFader3)
	vals.append(dataFader4)
	vals.append(dataInX)
	vals.append(dataInY)
	vals.append(dataMode1)
	vals.append(dataMode2)
	vals.append(dataMode3)
	vals.append(dataMode4)
	return vals

# save current state to a block
# input:
# 	current visual					int
# 	profile							int
def saveState(vis, pro):
	state = getState()
	block = getSaveBlockID(vis, pro)
	block.par.value0 = state[0] # dataFader1
	block.par.value1 = state[1] # dataFader2
	block.par.value2 = state[2] # dataFader3
	block.par.value3 = state[3] # dataFader4
	block.par.value4 = state[4] # dataInX
	block.par.value5 = state[5] # dataInY
	block.par.value6 = state[6] # dataMode1
	block.par.value7 = state[7] # dataMode2
	block.par.value8 = state[8] # dataMode3
	block.par.value9 = state[9] # dataMode4

# load state from a save block
# input: save block operator		operator
def loadBlock(block):
	d = []
	d.append(block.par.value0)
	d.append(block.par.value1)
	d.append(block.par.value2)
	d.append(block.par.value3)
	d.append(block.par.value4)
	d.append(block.par.value5)
	d.append(block.par.value6)
	d.append(block.par.value7)
	d.append(block.par.value8)
	d.append(block.par.value9)
	return d

# manage setting controller state
# input: state to upload 			[]
def updateControllerState(d):
	for i in range(len(outS)):
		outS[i].par.value0 = d[i]
	loadSwitch.par.index = 1 # load to controller

def updateControllerStateOSC(d):
	for i in range(len(outSosc)):
		outSosc[i].par.value0 = d[i]
	
	for i in range(len(outSosc3)):
		outSosc3[i].par.value0 = d[i+len(outSosc)+6]
	
	i1 = int(d[15])
	i2 = int(d[16])
	i3 = int(d[17])
	i4 = int(d[18])
	i5 = int(d[19])
	
	outSosc2.par.value0 = 0
	outSosc2.par.value1 = 0
	outSosc2.par.value2 = 0
	outSosc2.par.value3 = 0
	outSosc2.par.value4 = 0
	outSosc2.par.value5 = 0
	outSosc2.par.value6 = 0
	outSosc2.par.value7 = 0
	outSosc2.par.value8 = 0
	outSosc2.par.value9 = 0
	outSosc2.par.value10 = 0
	outSosc2.par.value11 = 0
	outSosc2.par.value12 = 0
	outSosc2.par.value13 = 0
	outSosc2.par.value14 = 0
	outSosc2.par.value15 = 0
	outSosc2.par.value16 = 0
	outSosc2.par.value17 = 0
	outSosc2.par.value18 = 0
	outSosc2.par.value19 = 0
	outSosc2.par.value20 = 0
	outSosc2.par.value21 = 0
	outSosc2.par.value22 = 0
	outSosc2.par.value23 = 0
	outSosc2.par.value24 = 0

	if i1 == 1: outSosc2.par.value0 = 1
	if i1 == 2: outSosc2.par.value1 = 1
	if i1 == 3: outSosc2.par.value2 = 1
	if i1 == 4: outSosc2.par.value3 = 1
	if i1 == 5: outSosc2.par.value4 = 1
	if i2 == 1: outSosc2.par.value5 = 1
	if i2 == 2: outSosc2.par.value6 = 1
	if i2 == 3: outSosc2.par.value7 = 1
	if i2 == 4: outSosc2.par.value8 = 1
	if i2 == 5: outSosc2.par.value9 = 1
	if i3 == 1: outSosc2.par.value10 = 1
	if i3 == 2: outSosc2.par.value11 = 1
	if i3 == 3: outSosc2.par.value12 = 1
	if i3 == 4: outSosc2.par.value13 = 1
	if i3 == 5: outSosc2.par.value14 = 1
	if i4 == 1: outSosc2.par.value15 = 1
	if i4 == 2: outSosc2.par.value16 = 1
	if i4 == 3: outSosc2.par.value17 = 1
	if i4 == 4: outSosc2.par.value18 = 1
	if i4 == 5: outSosc2.par.value19 = 1
	if i5 == 1: outSosc2.par.value20 = 1
	if i5 == 2: outSosc2.par.value21 = 1
	if i5 == 3: outSosc2.par.value22 = 1
	if i5 == 4: outSosc2.par.value23 = 1
	if i5 == 5: outSosc2.par.value24 = 1

	loadOSCSwitch.par.index = 1 # load to controller

# load Radio value to controller
# input: state to upload 			int
def updateControllerRadio(val):
	outRadio.par.value0 = val # prepare load
	radioSwitch.par.index = 1 # prepare load map
	loadSwitch.par.index = 2 # load to controller

# load base to cleanup after dance mode
def updateControllerBase():
	g = data.par.value0
	c = data.par.value1
	s = data.par.value12
	p = data.par.value14
	m1 = data.par.value2
	m2 = data.par.value3
	m3 = data.par.value4
	m4 = data.par.value5
	outGain.par.value0 = g
	outClip.par.value0 = c
	outRadio.par.value0 = s
	outProfile.par.value0 = p
	outM1.par.value0 = m1
	outM2.par.value0 = m2
	outM3.par.value0 = m3
	outM4.par.value0 = m4
	loadSwitch.par.index = 3 # load to controller

# push state to data block
# 	current visual					int
# 	profile							int
def loadState(vis, pro):
	block = getSaveBlockID(vis, pro)
	d = loadBlock(block)
	data.par.value6 = d[0] # dataFader1
	data.par.value7 = d[1] # dataFader2
	data.par.value8 = d[2] # dataFader3
	data.par.value9 = d[3] # dataFader4
	data.par.value10 = d[4] # dataInX
	data.par.value11 = d[5] # dataInY
	data.par.value2 = d[6] # dataMode1
	data.par.value3 = d[7] # dataMode2
	data.par.value4 = d[8] # dataMode3
	data.par.value5 = d[9] # dataMode4
	updateControllerState(d)

def setEQ(pos, input):
	power = powerSettings[int(constant.par.value5)]
	eq_shift = constant.par.value6
	val = (input - eq_shift) * power
	if pos == 1: eqDevice.par.band1 = val
	elif pos == 2: eqDevice.par.band2 = val
	elif pos == 3: eqDevice.par.band3 = val
	elif pos == 4: eqDevice.par.band4 = val
	elif pos == 5: eqDevice.par.band5 = val
	elif pos == 6: eqDevice.par.band6 = val
	elif pos == 7: eqDevice.par.band7 = val
	elif pos == 8: eqDevice.par.band8 = val
	elif pos == 9: eqDevice.par.band9 = val
	elif pos == 10: eqDevice.par.band10 = val
	elif pos == 11: eqDevice.par.band11 = val
	elif pos == 12: eqDevice.par.band12 = val
	elif pos == 13: eqDevice.par.band13 = val
	elif pos == 14: eqDevice.par.band14 = val
	elif pos == 15: eqDevice.par.band15 = val
	elif pos == 16: eqDevice.par.band16 = val

def shiftEQ(pos, input):
	power = powerSettings[int(constant.par.value5)]
	eq_shift = constant.par.value6
	val = (input)
	for i in pos:
		if i == 1: eqDevice.par.band1 = eqDevice.par.band1 + val
		elif i == 2: eqDevice.par.band2 = eqDevice.par.band2 + val
		elif i == 3: eqDevice.par.band3 = eqDevice.par.band3 + val
		elif i == 4: eqDevice.par.band4 = eqDevice.par.band4 + val
		elif i == 5: eqDevice.par.band5 = eqDevice.par.band5 + val
		elif i == 6: eqDevice.par.band6 = eqDevice.par.band6 + val
		elif i == 7: eqDevice.par.band7 = eqDevice.par.band7 + val
		elif i == 8: eqDevice.par.band8 = eqDevice.par.band8 + val
		elif i == 9: eqDevice.par.band9 = eqDevice.par.band9 + val
		elif i == 10: eqDevice.par.band10 = eqDevice.par.band10 + val
		elif i == 11: eqDevice.par.band11 = eqDevice.par.band11 + val
		elif i == 12: eqDevice.par.band12 = eqDevice.par.band12 + val
		elif i == 13: eqDevice.par.band13 = eqDevice.par.band13 + val
		elif i == 14: eqDevice.par.band14 = eqDevice.par.band14 + val
		elif i == 15: eqDevice.par.band15 = eqDevice.par.band15 + val
		elif i == 16: eqDevice.par.band16 = eqDevice.par.band16 + val

def centerEQBlock():
	eqDevice.par.band1 = 0
	eqDevice.par.band2 = 0
	eqDevice.par.band3 = 0
	eqDevice.par.band4 = 0
	eqDevice.par.band5 = 0
	eqDevice.par.band6 = 0
	eqDevice.par.band7 = 0
	eqDevice.par.band8 = 0
	eqDevice.par.band9 = 0
	eqDevice.par.band10 = 0
	eqDevice.par.band11 = 0
	eqDevice.par.band12 = 0
	eqDevice.par.band13 = 0
	eqDevice.par.band14 = 0
	eqDevice.par.band15 = 0
	eqDevice.par.band16 = 0

def setControllerEQValue():
	eqShifted = int(constant.par.value6)
	if eqShifted == 1: val = 1
	else: val = 0.5
	for i in range(16):
		c = eq_reset_data + str(i+1)
		op(c).par.value0 = val

def saveOSCState(vis):
	vals = []
	vals.append(oscData.par.value0)
	vals.append(oscData.par.value1)
	vals.append(oscData.par.value2)
	vals.append(oscData.par.value3)
	vals.append(oscData.par.value4)
	vals.append(oscData.par.value5)
	vals.append(oscData.par.value6)
	vals.append(oscData.par.value7)
	vals.append(oscData.par.value8)
	vals.append(oscData.par.value9)
	vals.append(oscData.par.value10)
	vals.append(oscData.par.value11)
	vals.append(oscData.par.value12)
	vals.append(oscData.par.value13)
	vals.append(oscData.par.value14)
	vals.append(oscData.par.value15)
	vals.append(oscData.par.value16)
	vals.append(oscData.par.value17)
	vals.append(oscData.par.value18)
	vals.append(oscData.par.value19)
	vals.append(oscData.par.value20)
	vals.append(oscData.par.value21)
	vals.append(oscData.par.value22)
	vals.append(oscData.par.value23)
	vals.append(oscData.par.value24)
	vals.append(oscData.par.value25)
	vals.append(oscData.par.value26)
	vals.append(oscData.par.value27)
	vals.append(oscData.par.value28)
	vals.append(oscData.par.value29)
	vals.append(oscData.par.value30)

	block = getSaveBlockID(vis, -2)
	block.par.value0 = vals[0]
	block.par.value1 = vals[1]
	block.par.value2 = vals[2]
	block.par.value3 = vals[3]
	block.par.value4 = vals[4]
	block.par.value5 = vals[5]
	block.par.value6 = vals[6]
	block.par.value7 = vals[7]
	block.par.value8 = vals[8]
	block.par.value9 = vals[9]
	block.par.value10 = vals[10]
	block.par.value11 = vals[11]
	block.par.value12 = vals[12]
	block.par.value13 = vals[13]
	block.par.value14 = vals[14]
	block.par.value15 = vals[15]
	block.par.value16 = vals[16]
	block.par.value17 = vals[17]
	block.par.value18 = vals[18]
	block.par.value19 = vals[19]
	block.par.value20 = vals[20]
	block.par.value21 = vals[21]
	block.par.value22 = vals[22]
	block.par.value23 = vals[23]
	block.par.value24 = vals[24]
	block.par.value25 = vals[25]
	block.par.value26 = vals[26]
	block.par.value27 = vals[27]
	block.par.value28 = vals[28]
	block.par.value29 = vals[29]
	block.par.value30 = vals[30]

def loadOSCState(vis):
	d = [] # load
	block = getSaveBlockID(vis, -2)
	d.append(block.par.value0)
	d.append(block.par.value1)
	d.append(block.par.value2)
	d.append(block.par.value3)
	d.append(block.par.value4)
	d.append(block.par.value5)
	d.append(block.par.value6)
	d.append(block.par.value7)
	d.append(block.par.value8)
	d.append(block.par.value9)
	d.append(block.par.value10)
	d.append(block.par.value11)
	d.append(block.par.value12)
	d.append(block.par.value13)
	d.append(block.par.value14)
	d.append(block.par.value15)
	d.append(block.par.value16)
	d.append(block.par.value17)
	d.append(block.par.value18)
	d.append(block.par.value19)
	d.append(block.par.value20)
	d.append(block.par.value21)
	d.append(block.par.value22)
	d.append(block.par.value23)
	d.append(block.par.value24)
	d.append(block.par.value25)
	d.append(block.par.value26)
	d.append(block.par.value27)
	d.append(block.par.value28)
	d.append(block.par.value29)
	d.append(block.par.value30)

	oscData.par.value0 = d[0]
	oscData.par.value1 = d[1]
	oscData.par.value2 = d[2]
	oscData.par.value3 = d[3]
	oscData.par.value4 = d[4]
	oscData.par.value5 = d[5]
	oscData.par.value6 = d[6]
	oscData.par.value7 = d[7]
	oscData.par.value8 = d[8]
	oscData.par.value9 = d[9]
	oscData.par.value10 = d[10]
	oscData.par.value11 = d[11]
	oscData.par.value12 = d[12]
	oscData.par.value13 = d[13]
	oscData.par.value14 = d[14]
	oscData.par.value15 = d[15]
	oscData.par.value16 = d[16]
	oscData.par.value17 = d[17]
	oscData.par.value18 = d[18]
	oscData.par.value19 = d[19]
	oscData.par.value20 = d[20]
	oscData.par.value21 = d[21]
	oscData.par.value22 = d[22]
	oscData.par.value23 = d[23]
	oscData.par.value24 = d[24]
	oscData.par.value25 = d[25]
	oscData.par.value26 = d[26]
	oscData.par.value27 = d[27]
	oscData.par.value28 = d[28]
	oscData.par.value29 = d[29]
	oscData.par.value30 = d[30]

	updateControllerStateOSC(d)

def refreshEQAdjust():
	setRefreshDataEQ()
	refreshSwitch.par.index = 2

# manage autoloading
# input: old state to save and new state to load
def autoload(old, new):
	disableAutoload = constant.par.value1
	autoloadFlag = constant.par.value2
	if disableAutoload == 0: # autoload
		# do not save when autoload was enabled
		if autoloadFlag == 0: saveState(old, -1)
		loadState(new, -1)
	constant.par.value2 = disableAutoload # set autoload flag
	enableOSCSaveLoad = constant.par.value10
	if enableOSCSaveLoad == 1: # OSC
		if autoloadFlag == 0: saveOSCState(old)
		loadOSCState(new)

# manage OSC input messages
def control(addr, args):
	debug = constant.par.value11
	if debug: print("address: " + addr)

	dancing = danceSwitch.par.index
	if addr[:-1] == "/mode":
		if int(addr[-1:]) == 6: # mode6
			val = int(args[0])
			danceSwitch.par.index = val # dance
			if val == 0: updateControllerBase()
	if not dancing:
		if addr == "/gain":
			# input
			data.par.value0 = args[0]

		elif addr == "/up":
			if data.par.value12 < max_scene and int(args[0]) == 1:
				old = int(data.par.value12) # last scene
				data.par.value12 = old+1 	# set scene
				new = int(data.par.value12) # new scene
				updateControllerRadio(new)
				autoload(old, new)

		elif addr == "/down":
			if data.par.value12 > 0 and int(args[0]) == 1:
				old = int(data.par.value12) # last scene
				data.par.value12 = old-1 	# set scene
				new = int(data.par.value12) # new scene
				updateControllerRadio(new)
				autoload(old, new)

		elif addr == "/radio":
			visual_filter.par.reset = True 	# disable scene fade
			old = int(data.par.value12) 	# last scene
			data.par.value12 = int(args[0]) # set scene
			new = int(data.par.value12) 	# new scene
			autoload(old, new)

		elif addr == "/xy":
			data.par.value10 = args[0]
			data.par.value11 = args[1]

		elif addr == "/showlogo":
			constant.par.value12 = args[0]
			logo.allowCooking = constant.par.value12

		elif addr == "/showclip":
			data.par.value13 = args[0]

		elif addr == "/save":
			if int(args[0]) == 1:
				pro = int(data.par.value14) # profile
				vis = int(data.par.value12) # current visual
				if pro in [1,2,3,4]: saveState(vis, pro)
				elif pro == 0 and constant.par.value0 == 1: saveState(vis, pro)
				else: print("cannot save to profile " + str(pro))

		elif addr == "/load":
			if int(args[0]) == 1:
				pro = int(data.par.value14) # profile
				vis = int(data.par.value12) # current visual
				loadState(vis, pro)

		elif addr == "/profile":
			data.par.value14 = args[0]

		elif addr == "/clip":
			data.par.value1 = args[0]
			
		elif addr == "/overwrite_defaults":
			constant.par.value0 = args[0]
		
		elif addr == "/disable_autoload":
			constant.par.value1 = args[0]
		
		elif addr == "/enable_oscillator":
			oscData.par.value20 = args[0]
		
		elif addr == "/saveload_oscillator":
			constant.par.value10 = args[0]
		
		elif addr == "/reset_oscillator":
			if int(args[0]) == 1:
				loadSwitch.par.index = 5
				resetOSCData()

		elif addr == "/monitor":
			constant.par.value8 = int(args[0])
		
		elif addr == "/perform":
			constant.par.value9 = int(args[0])
		
		elif addr == "/debug":
			constant.par.value11 = int(args[0])

		elif addr == "/refresh_controller":
			setRefreshDataEQ()
			setRefreshData()
			refreshSwitch.par.index = 1

		# fader
		elif addr[:-1] == "/fader":
			x = int(addr[-1:])
			if x == 1:
				data.par.value6 = args[0] 	# fader1
			elif x == 2:
				data.par.value7 = args[0] 	# fader2
			elif x == 3:
				data.par.value8 = args[0] 	# fader3
			elif x == 4:
				data.par.value9 = args[0] 	# fader4

		# mode
		elif addr[:-1] == "/mode":
			x = int(addr[-1:])
			if x == 1:
				data.par.value2 = args[0] 	# mode1
			elif x == 2:
				data.par.value3 = args[0] 	# mode2
			elif x == 3:
				data.par.value4 = args[0] 	# mode3
			elif x == 4:
				data.par.value5 = args[0] 	# mode4
			elif x == 5:
				pass
		
		# resolution
		elif addr[:5] == "/res_":
			if int(args[0]) == 1:
				setResolution(addr[-2:])
		
		# eq 
		elif addr[:3] == "/eq":
			name = addr[3:]
			b = name.split('/')[0][1:]
			if b == 'grid':
				n = int(name.split('/')[1])
				setEQ(n, args[0])
			elif b == 'power':
				constant.par.value5 = int(args[0])
			elif b == 'mute':
				if args[0] == 1.0: audioDevice.par.volume = 0
				else:
					currVolume = constant.par.value7
					audioDevice.par.volume = currVolume
			elif b == 'drywet':
				eqDevice.par.drywet = args[0]
			elif b == 'volume':
				audioDevice.par.volume = args[0]
				constant.par.value7 = args[0]
			elif b == 'shiftdown':
				if int(args[0]) == 1:
					constant.par.value6 = 1
				else: constant.par.value6 = 0.5
			elif b == 'center':
				setControllerEQValue()
				loadSwitch.par.index = 4
				centerEQBlock()
			elif b == 'treble-':
				if int(args[0]) == 1:
					shiftEQ([12,13,14,15,16], -2)
					refreshEQAdjust()
			elif b == 'treble+':
				if int(args[0]) == 1:
					shiftEQ([12,13,14,15,16], 2)
					refreshEQAdjust()
			elif b == 'mids+':
				if int(args[0]) == 1:
					shiftEQ([6,7,8,9,10,11], 2)
					refreshEQAdjust()
			elif b == 'mids-':
				if int(args[0]) == 1:
					shiftEQ([6,7,8,9,10,11], -2)
					refreshEQAdjust()
			elif b == 'bass+':
				if int(args[0]) == 1:
					shiftEQ([1,2,3,4,5], 2)
					refreshEQAdjust()
			elif b == 'bass-':
				if int(args[0]) == 1:
					shiftEQ([1,2,3,4,5], -2)
					refreshEQAdjust()
			else: print(b)
		
		# osc
		elif addr[:4] == "/osc":
			name = addr[4:]
			b = name.split('/')[0][1:]
			if b[:-1] == "param":
				s = int(b[-1:])
				n = int(name.split('/')[1])
				if n == 1 and s == 3: oscData.par.value0 = args[0]
				elif n == 2 and s == 3: oscData.par.value1 = args[0]
				elif n == 3 and s == 3: oscData.par.value2 = args[0]
				elif n == 4 and s == 3: oscData.par.value3 = args[0]
				elif n == 5 and s == 3: oscData.par.value4 = args[0]
				elif n == 1 and s == 2: oscData.par.value5 = args[0]
				elif n == 2 and s == 2: oscData.par.value6 = args[0]
				elif n == 3 and s == 2: oscData.par.value7 = args[0]
				elif n == 4 and s == 2: oscData.par.value8 = args[0]
				elif n == 5 and s == 2: oscData.par.value9 = args[0]
				elif n == 1 and s == 1: oscData.par.value10 = args[0]
				elif n == 2 and s == 1: oscData.par.value11 = args[0]
				elif n == 3 and s == 1: oscData.par.value12 = args[0]
				elif n == 4 and s == 1: oscData.par.value13 = args[0]
				elif n == 5 and s == 1: oscData.par.value14 = args[0]
			elif b[:-1] == "state":
				s = int(b[-1:])
				n = int(name.split('/')[1])
				if args[0] == 1: val = n
				else: val = 0
				if s == 1: oscData.par.value15 = val
				elif s == 2: oscData.par.value16 = val
				elif s == 3: oscData.par.value17 = val
				elif s == 4: oscData.par.value18 = val
				elif s == 5: oscData.par.value19 = val
			elif b[:3] == "map":
				s = b[3:4]
				a = int(b[-1:])
				t = int(args[0])
				if s == "A" and a == 1: oscData.par.value21 = t
				elif s == "A" and a == 2: oscData.par.value22 = t
				elif s == "A" and a == 3: oscData.par.value23 = t
				elif s == "A" and a == 4: oscData.par.value24 = t
				elif s == "A" and a == 5: oscData.par.value25 = t
				elif s == "B" and a == 1: oscData.par.value26 = t
				elif s == "B" and a == 2: oscData.par.value27 = t
				elif s == "B" and a == 3: oscData.par.value28 = t
				elif s == "B" and a == 4: oscData.par.value29 = t
				elif s == "B" and a == 5: oscData.par.value30 = t

		else:
			print('unknown input: ' + addr)

## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
def onReceiveOSC(dat, rowIndex, message, bytes, timeStamp, address, args, peer):
	control(address, args)
	return



# me - this DAT
# 
# dat - the DAT that received a message
# rowIndex - the row number the message was placed into
# message - an ascii representation of the data
#           Unprintable characters and unicode characters will
#           not be preserved. Use the 'bytes' parameter to get
#           the raw bytes that were sent.
# bytes - a byte array of the message.
# timeStamp - the arrival time component the OSC message
# address - the address component of the OSC message
# args - a list of values contained within the OSC message
# peer - a Peer object describing the originating message
#   peer.close()    #close the connection
#   peer.owner  #the operator to whom the peer belongs
#   peer.address    #network address associated with the peer
#   peer.port       #network port associated with the peer
#



#
#
# clip  	movie clip selection				 	int
# radio		visual selection						int
# xy		graph input								x,y float
# mode1		mode selection			(named 1 to 4)	int
# fader1	modifiers				(named 1 to 4)	float
# gain		gain selection							float
# up/down	visual selection		(up, down)		int
#
#