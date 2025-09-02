import subprocess
subprocess.run(["cal"])

result_01 = subprocess.run(["cal"], capture_output=True)        
print(result_01.returncode)
print(result_01.stdout)
print(result_01.stdout.decode())