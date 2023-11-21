#!/usr/bin/env python3
import ipdb

from classes.many_to_many import NationalPark
from classes.many_to_many import Visitor
from classes.many_to_many import Trip

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")
    p_1 = NationalPark("Yosemite")
    vis_1 = Visitor("Tom")
    vis_2 = Visitor("Mark")
    Trip(vis_1, p_1, "May 5th", "May 9th")
    Trip(vis_1, p_1, "January 5th", "January 20th")
    Trip(vis_2, p_1, "January 5th", "January 20th")
    ipdb.set_trace()
