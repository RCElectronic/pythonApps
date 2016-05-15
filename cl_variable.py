#! python3
# get the variables after the script command
import sys
if len(sys.argv) > 1:
    variable = ' '.join(sys.argv[1:])
print(variable)
