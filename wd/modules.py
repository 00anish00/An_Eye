import subprocess

# def install_module(module_name):

#     """ 
#     Installs a module
#     module_name (str): The name of the module to install.

#     """
#     try:
#         subprocess.check_call(["pip","install",module_name])
#         print(f" Module {module_name} has been successfully installed ")
#     except subprocess.CalledProcessError as error:
#         print(f'Try again to run the program please.(module name ={module_name})')
    


import subprocess
def install_module(module_name):

    result = subprocess.run(['pip','install',module_name], capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)
    print(result.returncode)
    print(result.check_returncode())

import subprocess
def uninstall_module(module_name):
    print("y/n")
    result = subprocess.run(['pip','uninstall',module_name], capture_output=True, text=True)
    print(result.stdout)
    print("PROCESSESS DONE")

def module_installer_an_eye():
    install_module('pyttsx3')
    install_module('speechrecognition')
    install_module('numpy')
    install_module('matplotlib')

while True:
    print("Module will install press y/Y (type 'exit()' to quit):")
    mdn=input()
    if mdn == "exit()" or mdn=='exit' or mdn=='quit':
        break
    if mdn=='y' or mdn=='Y':
        module_installer_an_eye()
        print('Process done....')
        break
