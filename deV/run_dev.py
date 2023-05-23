import sys
import subprocess
# print('processing please wait... ... .. . . .. .. ')


# result = subprocess.run(['pip','install','cx_Freeze'], capture_output=True, text=True)
# print(result.stdout)

# print('building exe file please wait... ... .. . . .. .. ')
# result = subprocess.run(['python','E:\\VSC\\Interst\\#ANAI\\T2\\An_Eye\\wd\\deV\\prs\\exe_control.py','build'], capture_output=True, text=True)
# print(result.stdout)

# print("DONE THE PROCESSES.")

# ui=input("press c for cxfrezze version // press pi for pyinstaller version\n")
# if ui=='c':
    # print('processing please wait... ... .. . . .. .. ')
    # result = subprocess.run(['pip','install','cx_Freeze'], capture_output=True, text=True)
    # print(result.stdout)
    # print('building exe file please wait... ... .. . . .. .. ')
    # result = subprocess.run(['python','E:\\VSC\\Interst\\#ANAI\\T2\\An_Eye\\wd\\deV\\prs\\exe_control.py','build'], capture_output=True, text=True)
    # print(result.stdout)
    # print("DONE THE PROCESSES.")
# elif ui=='pi':
#     print('processing please wait... ... .. . . .. .. ')
#     result = subprocess.run(['pip','install','pyinstaller'], capture_output=True, text=True)
#     print(result.stdout)
#     print('building exe file please wait... ... .. . . .. .. ')
#     result = subprocess.run(['pyinstaller','--onefile','an_eye_textwala.py'], capture_output=True, text=True)
#     print(result.stdout)
#     print("DONE THE PROCESSES.")

# print('processing please wait... ... .. . . .. .. ')
# result = subprocess.run(['pip','install','cx_Freeze'], capture_output=True, text=True)
# print(result.stdout)
# print('building exe file please wait... ... .. . . .. .. ')
# result = subprocess.run(['python','E:\\VSC\\Interst\\#ANAI\\T2\\An_Eye\\deV\\prs\\exe_control.py','build'], capture_output=True, text=True)
# print(result.stdout)
# print("DONE THE PROCESSES.")
print('processing please wait... ... .. . . .. .. ')
result = subprocess.run(['pip','install','pyinstaller'], capture_output=True, text=True)
print(result.stdout)
print('building exe file please wait... ... .. . . .. .. ')
# path=subprocess.run(['cd','wd'])
result = subprocess.run(['pyinstaller','--onefile','a.py'], capture_output=True, text=True)
print(result.stdout)
print("DONE THE PROCESSES.")