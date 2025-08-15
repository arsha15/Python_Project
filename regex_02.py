import re

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"

match = re.search(r'\[(\d+)\]', log) # what is this regex doing here

print(match)

if match:
   process_id = match.group(1)
   print("The extracted process id is", process_id)