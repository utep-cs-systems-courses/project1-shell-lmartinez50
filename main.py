# Copyright (c) 2020 Lorenzo Martinez
#
# This program build a user shell for a Unix operating system
#
# Author Lorenzo Martinez
# Version 1.0
# Creation Date: 09/06/2020
# Due date: 09/09/2020
# Lab 1
# CS 4375 Theory of Operating Systems
# Instructor PhD Eric Freudenthal
# Rev. 1 09/05/2020 Initial approach
# Rev. 2 09/06/2020

import re       # regular expression tools
import sys      # command line arguments
import os       # interacting with the operating system

prompt = os.getenv("PS1")

while True:
    prompt = str(input("?> "))
    shellString = prompt

    if shellString == "exit":
        print("Hasta la vista, baby!")
        sys.exit(1)

