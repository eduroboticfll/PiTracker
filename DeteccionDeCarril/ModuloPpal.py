import WebcamModule
from ModuloCarril import getLaneCurve

def main():
    
    img = WebcamModule.getImg()
    curveVal= getLaneCurve(img,1)
    
    sen = 1.3
    maxVal= 0.3
    if curveVal>maxVal:curveVal = maxVAl
    if curveVal<-maxVal:curveVal = -maxVAl
    print(curveVal)
    if curveVal>0:
        sen =1.7
        if curveVal<0.05: curveVal=0
    else:
        if curveVal>-0.08: curveVal=0
        
        
if __name__=='__main__':
    while True:
        main()
    
