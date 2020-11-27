

config = configparser.ConfigParser()
config.read('/home/user/TestingTool_GUI/data/config.ini')
secs = config.sections()
print (secs) #['section1', 'section2']
#section_a_Value = config.get('items','times')#GET "Value_ABC"
#section_b_Value = config.get('items','lan') #Get "Some thing here"
#print("section_a_Value = ", section_a_Value) 
#print("section_b_Value = ", section_b_Value )
