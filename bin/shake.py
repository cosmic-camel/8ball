#!/usr/bin/env python
#shake.py

import sys
import os
import random
text_responses_file = open(os.path.dirname(__file__) + "/../data/shake_responses.txt", 'r')
text_responses_tuple = tuple(text_responses_file)

response = text_responses_tuple[random.randint(0,len(text_responses_tuple)-1)]

print(response)
sys.exit(5)
