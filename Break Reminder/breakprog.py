import time
import webbrowser

totalNo_of_breaks = 3
breakCount = 1

print("The program started at " + time.ctime())
print("After every hour, I will interrupt you to take a break and sooth you with the best of Mozart")
while(breakCount <= totalNo_of_breaks):
    time.sleep(3600)
    url = "https://www.youtube.com/watch?v=Rb0UmrCXxVA"
    webbrowser.open(url)
    print("This is break number: " + str(breakCount) + "and this is the best of Mozart") 
    breakCount = breakCount + 1
