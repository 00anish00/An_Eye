import voiceoutput as vc
def speak(aud):
    vc.spk(aud)
import speakandwrite as sw
def dic(text):
    sw.dictate(text)
import subprocess
def cal():
    subprocess.Popen('calc.exe')

def start_calc(eqn):
    # eqn = input("Type algebraic Equation: (USE: + - * / [{(0-9)}])\nType Here:")
    result = eval(eqn)
    dic(f'result is  {result}')
    return result


