import math
import matplotlib as plt 
import matplotlib.pyplot as plt

class LPF :
    def __init__(self):
        pass
    def setNoise(self,*noise_data):             ## input dictionary
        self.freq=list(noise_data[0].keys())    ## separate frequencies
        self.amp=list(noise_data[0].values())   ## separarte amplitudes
    def setCutfrequency(self,fc=1):
        self.fc=fc                              ## setting cut off frequency
    def setInputSignal(self,dc=3.3,fi=0,ai=0,sine=True):
        self.dc=dc                              ## dc input voltage
        self.fi=fi                              ## ac frequency
        self.ai=ai                              ## ac amplitude
        self.sine=sine
    def signalSettings(self,max_time=1,sampling_time=0.0001):
        self.max_time=max_time                  ## signal window
        self.sampling_time=sampling_time        ## sampling time
    def noiseConstruct(self):
        self.r=[]                               ## real readings
        self.time=[]                            ## time values for y axis plotting
        self.t=0                                ## start time = 0
        self.sum=0
        while self.t<self.max_time :            ## loop till time reaches max time
            self.time.append(self.t)            ## add time ti time list in order ti plot the signal (y-axis values)
            self.sum=0
            for i in range(0,len(self.freq)):
                self.sum=self.sum+self.amp[i]*math.sin(self.freq[i]*2*3.1415*self.t) 
                                                ## adding the noise frequencies
            self.sum = self.sum+self.ai*math.sin(self.fi*2*3.1415*self.t)+self.dc
                                                ## adding main signal
            self.r.append(self.sum) 
            self.t=self.t+self.sampling_time    ## increment sampling time
    def startLPF (self):
        self.signalSettings()
        self.noiseConstruct()
        self.x=[self.r[0]]                      ## values read by ADC for example >> fill first location by first reading
        self.y=[self.r[0]]                      ## real output values >> first output value is first read value
        self.a=(2*3.1415*self.sampling_time*self.fc)/(2*3.1415*self.sampling_time*self.fc+1)
                                                ## a=2*pi*sampling_time*fcut/(2*pi*sampling_time*fcut+1)
        self.t=0                                ## sampling time
        self.z=1                                ## counter
        
        while self.t <self.max_time-self.sampling_time :
            self.x.append(self.r[self.z])                                 ## add new reading to x
            self.y.append(self.a*self.x[self.z]+(1-self.a)*self.y[self.z-1])   ## Yi=aXi=(1-a)*Yi-1 ## calculating the output
            self.t=self.t+self.sampling_time                         ## sampling time
            self.z=self.z+1                                                    ## increment counter
        plt.plot(self.time, self.r)
        plt.plot(self.time, self.y , color='r')
        plt.show()
        

 
 

 


 

     
