import sys
import subprocess
print('processing please wait... ... .. . . .. .. ')


result = subprocess.run(['pip','install','cx_Freeze'], capture_output=True, text=True)
print(result.stdout)

print('building exe file please wait... ... .. . . .. .. ')
result = subprocess.run(['python','E:\\VSC\\Interst\\#ANAI\\T2\\An_Eye\\wd\\deV\\prs\\exe_control.py','build'], capture_output=True, text=True)
print(result.stdout)

print("DONE THE PROCESSES.")