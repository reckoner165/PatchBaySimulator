__author__ = 'Sumanth Srinivasan'


#CHECKLIST

#1.Get a way to invoke the patch bay after patching has been done, so as to actually get all input stuff to the output.
#2.Error handling
#3.See if it can work with librosa
#4.Look for other audio packages to test it with

class patchbay:

    def __init__(self, ports):

        #Initialize output and input patchpoints. Creates equal number of output and input ports.
        self.output = [patchpoint(False) for i in range(ports)]
        self.input = [patchpoint(True) for i in range(ports)]

        #Initialize to setup mode by default
        self.mode = 'SETUP'
        print('The patch bay has been initialized to', self.mode, 'mode.')

    #Method to set the mode of the patch bay
    def setMode(self,newMode):

        if newMode == 'SETUP':
            self.mode = 'SETUP'
        elif newMode == 'USER':
            self.mode = 'USER'
        else:
            print('Invalid patch bay mode requested. Choose from SETUP and USER')

    #A boolean method to test current mode of the patch bay
    def modeTest(self, currentMode):

        if self.mode == currentMode:
            return True
        else:
            return False

    #Methods available in SETUP mode

    def normal(self,normalType,channel):

        if modeTest('SETUP'):

            if normalType == 'HALF':
                #Write code for half normal connections
                pass
            elif normalType == 'FULL':
                #Write code for full normal connections
                pass
            else:
                print('Invalid normal Type. Choose from HALF and FULL')

        else:
            print('Incorrect mode')

    #Methods availabe in USER mode

    def patch(self,port1,port2):
        pass

    def removePatch(self,port1,port2):
        pass




class patchpoint:

    #Class of patch points. Each patch point corresponds to a single port on the patch bay


    def __init__(self, io):

        #Sets patch flag to false by default, which means nothing has been patched in yet
        self.patchFlag = False

        #Default Label. User can and should change this to read whatever their port stands for later.
        #User must follow naming conventions as there is no external indicator for normalled connections.
        self.label = str(self)

        #Initialize whether given port is input or output

        if io:
            self.inputFlag = True

        else:
            self.inputFlag = True

        self.refreshPatchState()

    def refreshPatchState(self):
        if self.patchFlag:
            pass #Set TRS and normals
        else:
            pass #Set TRS and normals


#DEBUG
a = False

h = patchpoint(a)

print(h.label)




