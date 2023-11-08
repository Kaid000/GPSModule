#function to convert raw Latitude and Longitude
#to actual Latitude and Longitude
def convertToDegree(RawDegrees):

    RawAsFloat = float(RawDegrees)
    firstdigits = int(RawAsFloat/100) #degrees
    nexttwodigits = RawAsFloat - float(firstdigits*100) #minutes
    
    Converted = float(firstdigits + nexttwodigits/60.0)
    Converted = '{0:.6f}'.format(Converted) # to 6 decimal places
    return str(Converted)
    
while True:
    
    getPos(gps_module)

    #if gps data is found then print it on console
    if(FIX_STATUS == True):
        print("fix......")
      
        print(latitude)
        print(longitude)
        print(satellites)
        print(gpsTime)
        
        FIX_STATUS = False
        
    if(TIMEOUT == True):
        print("Request Timeout: No GPS data is found.")
        TIMEOUT = False