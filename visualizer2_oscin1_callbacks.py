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

names = []
values = []

def input(addr, args):
	l = len(args)
	
	if addr not in names:
		names.append(addr)
		values.append([])
	i = names.index(addr)

	if values[i] != args:
		values[i] = args

		#print(address)
		#print(names)
		#print(values)
		print(i)
		control(i)

	return i

def control(i):
	pass

def onReceiveOSC(dat, rowIndex, message, bytes, timeStamp, address, args, peer):	
	input(address, args)
	return
