#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A single if statement."""

MYINPUT = raw_input('Tell me a story! ')
MAX_LENGTH = 80
LONGSTR = 'short'

# Your code goes here
LONGSTR = 'long' if len(MYINPUT) > MAX_LENGTH else 'short'

OUTPUT = 'That certainly was a {} story!'.format(LONGSTR)
print OUTPUT
