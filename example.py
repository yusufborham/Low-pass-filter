from LPF import LPF
noise={2000:0.1,1400:0.2,1000:0.05}   ## set noises (frequency:amplitude) ## 2000 hz: 0.1 amplitude ,etc 
l1=LPF()                              ## create object      
l1.setNoise(noise)                    ## set noise 
l1.setCutfrequency(100)               ## set cut off frequency for the signal by default 1
l1.setInputSignal(2.5,50,2.5)         ## set your main input frequency ## (dc input for dc offsets,sine wave frequency ,sine wave amplitude) ## dc by default 3.3 others are 0
l1.signalSettings(0.1,0.0001)         ## max time scale and sampling time
l1.startLPF()
