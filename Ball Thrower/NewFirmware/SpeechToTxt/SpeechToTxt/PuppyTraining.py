#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.parameters import Color, Port
from pybricks.ev3devices import (Motor, TouchSensor,
          ColorSensor, UltrasonicSensor, GyroSensor)
from pybricks.tools import wait, StopWatch
import random
import ujson, urequests
ev3 = EV3Brick()
# Initialize the EV3
# Initialize the EV3
class PuppyTraining:
    """ PuppyTraining is an AI module and class for an EV3 running micropython.
    We use a 1-dimenional, 2-cluster K-Means Clustering algorithm
    for training a robot to detect two gyroscope states corresponding to 
    "command A" and "command B" for a puppy learning a trick.
    To add a third cluster, for an additional command look for the extension comments, indicated with "+++"
    """

    def __init__(self,port):
        """initializes the PuppyTraining class
        port argument determines which port number is used 
        for the training Gyroscope"""
        self.ev3 = EV3Brick()
        self.ev3.speaker.beep()
        self.gyro = GyroSensor(port)
        self.gyro.reset_angle(0)
        self.boundary = None #Initial Decision boundary
        self.ATraining =  [] #Initial A examples
        self.BTraining = [] #Initial B examples
        self.averageA = None # Initial average for the A training
        self.averageB = None #Initial average for the B training
        # +++ If you want to add more commands, initialize a Training array and average for the new command here.

    def observation(self):
        """Adds one training observation to the training data"""
        
        print('Press up or down button to tell the puppy which command you are demonstrating.\
         Press the center to stop training')
        self.ev3.screen.print("Press up or down button to give example. Center to exit")        
        while True:  # Waits for the next button press to record the observation       
            if Button.UP in brick.buttons():
                #Record an A command observation
                Angle = self.gyro.angle()
                DogCommand = 'A'
                print('Puppy learns that this means command A')
                brick.sound.beep()
                #Adds the observation to the recorded data
                self.ATraining.append(Angle)
                wait(100)
                return Angle, DogCommand

            elif Button.DOWN in brick.buttons():
                #Record a B command observation
                Angle = self.gyro.angle()
                DogCommand = 'B'
                print('Puppy learns that this means command B')
                brick.sound.beep()
                #Adds the observation to the recorded data
                self.BTraining.append(Angle)
                wait(100)
                return Angle, DogCommand

            elif Button.LEFT in brick.buttons():
                # +++ Record examples for additional commands here
                pass

            elif Button.CENTER in brick.buttons():
                #Stop training
                Angle = 0
                DogCommand = 'Exit'
                brick.sound.beep()
                print('Puppy is done training for now.')
                return Angle,DogCommand

    def watch(self):
        """Adds multiple training observations to the training data"""
        """Puppy watches for example commands until the center button is pressed"""
        self.gyro.reset_angle(0) #Resets the gyro angle 
        command = ""
        print('Puppy is ready to start learning!')
        while Button.CENTER not in brick.buttons() and command != "Exit":
            #Repeat observations until the center button is pressed
            angle, command = self.observation()
        print('Training Over.')


    def train(self):
        """Calculate where the decision boundary for 1 Dimension 2-Mean Clustering is located"""
        sumA = 0
        sumB = 0 
        #Calculate totals   
        for observation in self.ATraining:
            sumA += observation #Totals all A Training examples
        for observation in self.BTraining:
            sumB += observation #Totals all B Training examples
        #Calculate averages
        self.averageA = sumA/len(self.ATraining) #Finds mean value of all A commands
        self.averageB = sumB/len(self.BTraining) #Finds mean value of all B commands
        # +++ If you are adding additional commands, be sure to calculate the new totals and averages too!
        self.boundary = (self.averageA + self.averageB)/2 #The decision boundary is halfway between the A and B means.
        return self.boundary

    def distance(self, angle, command):
        #"""Calculates the one dimensional distance between the current angle and given command average"""
        if command =='A':
            return abs(angle - self.averageA)
        elif command =='B':
            return abs(angle - self.averageB)
        else:
            # +++ You can add distance calculations for more commands here.   
            return 1000


    def prediction(self):
        #"""Calculate the current prediction of the current Gyro angle based on the training"""
        angle = self.gyro.angle()
        if self.distance(angle, 'B') >= self.distance(angle, 'A'):
            #If the current angle is closer to the A average, predict it is an A.
            prediction = 'A'
        elif self.distance(angle, 'B') < self.distance(angle, 'A'):
             #If the current angle is closer to the B average, predict it is an B.
            prediction = 'B'
        else:
            pass # +++ You can add additional commands here.    
        print('The puppy thinks that is a ' + prediction + ' command!')
        return prediction

    def report(self):
        """Prints out the current state of the model"""
        tablewidth = 20 #Adjust this constant to change table width
        print("The Puppy Training Report")
        print("*"*tablewidth)
        print("These are the examples of command A that puppy has seen: \n", self.ATraining)
        print("The average is %.2f" % self.averageA)
        print("*"*tablewidth)
        print("These are the examples of command B that puppy has seen: \n", self.BTraining)
        print("The average is %.2f" % self.averageB)
        print("*"*tablewidth)
        print('The puppy has learned that the decision boundary is: ', self.boundary)
        print("*"*tablewidth)
    
    def forget(self):
        """Reset the training data and the model"""
        self.boundary = None #Reset Decision boundary
        self.angledata = [] #Reset observation measurements
        self.commanddata = [] #Reset observation labels
        self.averageA = None # Reset average for the A training
        self.averageB = None #Reset average for the B training
        # +++ If you added an extra command, be sure to reset it here too!
        print('The puppy has forgotten the training!')