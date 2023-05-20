import sys
import cx_Freeze 

from cx_Freeze import setup, Executable
# setup(name = fn,
# 	version = vrs ,
# 	description = des ,
# 	executables = [Executable(fp)])

setup(name = 'An_Eye',
	version = '0.2.5' ,
	description = 'des' ,
	executables = [Executable('E:\\VSC\\Interst\\#ANAI\\T2\\An_Eye\\wd\\modules.py')])
