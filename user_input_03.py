import os
import sys
print("Home variable is", os.environ.get("HOME","Not found"))
print("SHELL: " + os.environ.get("SHELL", ""))
print("FRUIT: " + os.environ.get("FRUIT", "Not available"))
print(sys.argv)