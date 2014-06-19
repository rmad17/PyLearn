import re
"""
char_left:char_right
check for ":"--> char_left=character before ":" excluding '""'
if "{" after ":" then char_left= char_left0.charleft1
else char_right=character after ":"  excluding '""'
goto 3
"""

objstr='{"a":"b","c":{"d":"e","f":{"g":"h","i":"j"}}}'
finalstr=''

"""def getChar(i):
	char=objstr[i-2:i-1]
	print i 
	return char
"""
def left(i):
	 return objstr[i-2:i-1]

def right(i):
	return objstr[i+2:i+3]		
for i in range(len(objstr)):
	#print i
	#match=re.search(r'"[a-z]"+:',i)
	if objstr[i:i+1] is ":":#i is ':':
		finalstr+='"'+left(i)+'"'
		if objstr[i+2:i+3] is not "{":
			finalstr+=":"+objstr[i+2:i+3]+","
		if objstr[i+2:i+3] is "{":
			finalstr=finalstr[0:len(finalstr)-1]
			finalstr+="."

#finalstr=finalstr+'"'
		
print finalstr
