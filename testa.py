import time
xs=0
xm=0
k=0
while k!=439:
    xs+=1
    print (xs, "segundos e", xm, "minutos")
    time.sleep(1)
    if xs==59:
        xs=0
        xm+=1
        print (xs, "segundos e", xm, "minutos")
        time.sleep(1)
        
