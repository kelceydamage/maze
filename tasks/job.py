
import pygame
import sys
import os
from pygame.locals import *
import pprint

class Job(object):
    """ Job class, generic class for a job """
    def __init__(self, name, move, dest):
        self.name = name
        self.move = move
        self.dest = dest
    def __repr__(self):
        return self.name


class Tasks:

    def mining(self):
        selected = self.renderer.map.get_selected(2)
        print("Selected: ", selected)
        for coord in selected: # change this at some point
            # checking if the neighboring tiles are accessible from 1 tile away in every direction
            # would have to make this more intelligent in the future, but it works for now.
            job = self.find_mining_job(coord)
            inqueue = False
            if job: #check if the dorfs already have that job
                for m in self.mobs:
                    if m.job != None:
                        if m.job.name == job.name and m.job.move == job.move and m.job.dest == job.dest:
                            inqueue = True
                        continue
                
            if inqueue == False and job:
                self.renderer.map.writeEMapQueue(job.dest[0], job.dest[1], job.dest[2], True)
                self.queued_jobs.append(job)

    def t(self):
        pass


    def channel(self):
        selected = self.renderer.map.get_selected(3)
        for coord in selected: # change this at some point
            # checking if the neighboring tiles are accessible from 1 tile away in every direction
            # would have to make this more intelligent in the future, but it works for now.
            adjacent_open_tiles = self.renderer.map.successors(coord)
            queue = []
            if adjacent_open_tiles != []:
                queue.append(coord)
            if len(queue):
                dest = queue.pop(0)
                #if self.renderer.map.checkEMapQueue(dest[0], dest[1], dest[2]) == True:
                #   continue
                list = self.renderer.map.successors(dest)
                for move in list:
                    if len(self.renderer.map.successors(move)):
                        #dest[2] = dest[2] -1 #channel digs a zlevel below but creates a ramp
                        self.renderer.map.writeEMapQueue(dest[0], dest[1], dest[2], True)
                        self.queued_jobs.append(Job('Channeling', move, dest))
                        continue

    def moveitem(self):
        selected = self.renderer.map.get_selected_items()
        dropoff = self.renderer.map.get_selected(4)
        if dropoff == []:
            return
        else:
            for coord in selected: # change this at some point
                adjacent_open_tiles = self.renderer.map.successors(coord)
                queue = []
                if adjacent_open_tiles != []:
                    queue.append(coord)
                if len(queue):
                    for move in queue:
                        if len(self.renderer.map.successors(move)):
                            content = self.renderer.map.get_items(move[0], move[1], move[2])
                            if content != None:
                                for item in content:
                                    if item.selected == True and item.inqueue == False:
                                        item.inqueue = True
                                        self.queued_jobs.append(Job('MoveItem', move, dropoff))
                                        continue