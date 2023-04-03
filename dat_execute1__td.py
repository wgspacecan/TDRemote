# 
# RGB Visuals
# 
# 

def onStart():
	return

def onCreate():
	return

def onExit():
	return

def onFrameStart(frame):
	return

def onFrameEnd(frame):
	op('filter1').par.reset = False 	# fade visual
	op('load_switch').par.index = 0 	# close load
	op('loadOSC_switch').par.index = 0	# close OSC load
	op('load_radio').par.index = 0 		# do not load radio
	op('refresh_switch').par.index = 0

def onPlayStateChange(state):
	return

def onDeviceChange():
	return

def onProjectPreSave():
	return

def onProjectPostSave():
	return




# me - this DAT
# frame - the current frame
# state - True if the timeline is paused