
import numpy as np
from psychopy import visual, core, event, data, hardware, gui, logging
import copy

winSize = (1536, 864) # Specify Window Size
go = 'run';
class spikeapp():
    
    def __init__(self):
        self.win = visual.Window(size=winSize, monitor='testMonitor',
        units='pix',bitsMode=None, allowGUI=False, winType='pyglet',screen=1, fullscr=True,color=(1,1,1))	
        #Generate the mouse and make it visible
        self.mouse = event.Mouse(visible = True)
        #self.graphList = np.array([[100,100]]*100)
        
        self.prelimListXs = list(range(-1000,800))
        self.spikeListXs = list(range(-1000,800))
        self.prelimListYs = [-500]*100
        self.spikeListYs = [0]*100
        self.spikevector = [0]*1800
        self.finalList = []
        self.spikeline = []
        self.spikeplacementdict = {};
        for i in range(len(self.prelimListXs)):
            for j in range(len(self.prelimListYs)):
                self.finalList.append((self.prelimListXs[i], self.prelimListYs[j]))
                self.spikeline.append((self.spikeListXs[i], self.spikeListYs[j]))
        self.linegraph = visual.shape.ShapeStim(self.win, units='pix', colorSpace='rgb', 
            fillColor=False, lineColor=False, lineWidth=10, vertices=self.finalList, 
            windingRule=None, closeShape=True, size=1, anchor=None, pos = [100,100], ori=0.0, 
            opacity=1.0, contrast=1.0, depth=0, interpolate=True, name=None, autoLog=None, 
            autoDraw=False, color=False, lineRGB=False, fillRGB=False, fillColorSpace=None, lineColorSpace=None)
            
        self.axisLine = copy.copy(self.linegraph)
        self.axisLine.lineColor=False
        self.axisLine.color=False
        self.spikelinegraph = visual.shape.ShapeStim(self.win, units='pix', colorSpace='rgb', 
            fillColor=False, lineColor=False, lineWidth=10, vertices=self.spikeline, 
            windingRule=None, closeShape=True, size=1, anchor=None, pos = [100,100], ori=0.0, 
            opacity=1.0, contrast=1.0, depth=0, interpolate=True, name=None, autoLog=None, 
            autoDraw=False, color=False, lineRGB=False, fillRGB=False, fillColorSpace=None, lineColorSpace=None)
        
        
    def listenKey(self):
        for key in event.getKeys():
            #If the escape key has been pressed, quit the program.
            if key in ['escape']:
                core.quit()
    
    def listenSpikeClick(self):
        buttons = self.mouse.getPressed();
        if buttons[0] == 1:
            [currentX,currentY] = self.mouse.getPos()
            if currentY < -200 and currentY > -600:
                self.spikeplacementdict[currentX] = visual.Line(self.win, start=(currentX,-400), end=(currentX,-200),lineColor="grey")
                core.wait(0.2)
                #self.mouse.clickReset()
        if buttons[2] == 1:
            [currentX,currentY] = self.mouse.getPos()
            
            if currentY < -200 and currentY > -600: 
                deletable_x_range = set(list(range(currentX.astype('int')-10,currentX.astype('int')+10)))
                intersected_spots = deletable_x_range.intersection(set(list(self.spikeplacementdict.keys())))
                if len(list(intersected_spots)) > 0:
                    del self.spikeplacementdict[list(intersected_spots)[0]]
        for spike in list(self.spikeplacementdict.values()):
            spike.draw()
        
        for spike in list(self.spikeplacementdict.values()):
            spike.draw()
    
    def updateSpikeVectors(self):
        self.spikevector = [0]*1800
        spiketimes = list(self.spikeplacementdict.keys())
        for spike in spiketimes:
            self.spikeline = copy.copy(self.axisLine);
            print(self.spikeline.vertices[spike])
            self.spikevector[list(spiketimes)[0]] = 200;
        

        
def main():
    viewGen = spikeapp()
    while True:
        
        viewGen.spikelinegraph.draw()
        viewGen.axisLine.draw()
        viewGen.linegraph.draw()
        viewGen.listenKey()
        viewGen.listenSpikeClick()
        viewGen.win.flip()
        
            
        
main()
