__author__ = 'Sumanth Srinivasan'


#CHECKLIST

#1.Get a way to invoke the patch bay after patching has been done, so as to actually get all signals across the patchbay into applications using it.
#2.Error handling
#3.See if it can work with librosa
#4.Look for other audio packages to test it with
#5.Get the TRS and normal connections figured out
#6.Get the half and full normal done

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
                self.input[channel].normal = self.output[channel].portSignal2
            elif normalType == 'FULL':
                #Write code for full normal connections (AKA Single normalling)
                self.input[channel].normal = self.output[channel].normal
            else:
                print('Invalid normal Type. Choose from HALF and FULL')

        else:
            print('Incorrect mode')

    #Methods availabe in USER mode

    #Method to patch two ports on the patch bay
    def setPatch(self,outputPort,inputPort):

        #Check if patch bay is in USER mode
        if self.modeTest('USER'):
            if ~self.output[outputPort].patchFlag:
                if ~self.input[inputPort].patchFlag:
                    self.input[inputPort].portSignal = self.output[outputPort].portSignal

                    #Set patch flags
                    self.input[inputPort].patchFlag = True
                    self.output[outputPort].patchFlag = True

                    #Refresh both patch states so the reflect the connections
                    self.input[inputPort].refreshPatchState()
                    self.output[outputPort].refreshPatchState()
                    #TO-DO: Add a patched-label that gives info on where the given port is patched to/from
                else:
                    print('Input port is already patched to something else.')
            else:
                print('Output port is already patched to something else')
        else:
            print('Incorrect mode')


    #Method to remove a patch between two ports
    def removePatch(self,outputPort,inputPort):

        #Check if patch bay is in USER mode
        if self.modeTest('USER'):
            if self.output[outputPort].patchFlag:
                if self.input[inputPort].patchFlag:
                    #Reset patch flags
                    self.input[inputPort].patchFlag = False
                    self.output[outputPort].patchFlag = False

                    #Refresh both patch states so the reflect the connections
                    self.input[inputPort].refreshPatchState()
                    self.output[outputPort].refreshPatchState()
                    #TO-DO: Reset patched label to 'Nothing' or whatever.
                else:
                    print('Input port is patched to nothing.')
            else:
                print('Output port is patched to nothing')
        else:
            print('Incorrect mode')




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
            self.inputFlag = False

        self.refreshPatchState()

    #Refresh patch state in the event of patching or un patching of ports so that the normals will engage accordingly.
    def refreshPatchState(self):
        if self.inputFlag: #If input port
            if self.patchFlag:
                self.portSignal = self.portSignal
            else:
                self.portSignal = self.normal

        else: #If output port
            if self.patchFlag:
                self.normal = 0
            else:
                self.normal = self.portSignal
            self.portSignal2 = self.portSignal #Make a copy for half normal


#DEBUG
a = False

h = patchpoint(a)

print(h.label)




