#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 19:38:30 2019

@author: alshammery
Homework Assignment #2: Functions

Song Characteristics Program
"""

# ---------------------------------------------------------------------
# Song Function
# ---------------------------------------------------------------------

# Define Artist Function
def Artist():
    ArtistName="Dave Brubeck"
    return ArtistName 
# Call the Artist Function    
print ("Artist Name:      ", Artist())


# Define Genre Function
def Genre():
    GenreType="Jazz"
    return GenreType 
 
# Call the Genre Function    
print ("Song Genre Type:  ", Genre())


# Define Year Function
def Year():
    SongYear=1990
    return SongYear
 
# Call the Year Function    
print ("Song Year:        ", Year())


# Define booleans Function
def SongAvailable(SongName):
    if SongName == "Take Five":
        result = True
    else:
        result = False

    return result

# Call the booleans Function    
print ("Is Song Available:", SongAvailable("Take Five"))

