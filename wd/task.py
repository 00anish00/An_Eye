
# Processing dots *
import process_dots as pd
def dots():
    pd.dots()

# Output audio *
import voiceoutput as vc
def speak(text):
    vc.spk(text)

# text insert taker *
def qery():
    a=str(input("enter.....:"))
    return a

# write and speak at a time
import speakandwrite as sw
def dic(text):
    sw.dictate(text)

# System Commands
import sys

# ---------------modules_imported_and_created---------------------------------------------------------------------------------------
# ------------------------------------task-modules-------------------------------------------------------------

# tk1
import wikipedia
# tk2
import webbrowser




def run():
    
    # qryf = filtered query
    # iv=qery()
    
    speak('Type the message querry or problem to pruh·seed further and press the enter key')
    speak("To Close Type 'exit' and press enter")
    while True:
        
        print("\nType the message querry or problem and press enter to procced further  || To Close Type 'exit' and press enter")
        qry=qery()
        
        if 'wikipedia' in qry  or 'Wikipedia' in qry or 'WIKIPEDIA' in qry :
            # tk1
            qryf=qry
            try:
                results = wikipedia.summary(qryf,sentences=4)
                dic("As per the wikipedia",)
                dots()
                print()      
                # new line
                dic(results)
                print()
            
            except wikipedia.exceptions.WikipediaException as e:
                # print(e)
                dic('Wikipedia can not find it or server connection error ')
                print()
                
                

        if 'youtube' in qry: 
            # tk2 
            if qry=='youtube':
                dic("opening   youtube")
                webbrowser.open(url=f"https://www.youtube.com")
                print()
            else:
                dic("opening   youtube")
                dots()
                qryf=qry.replace('youtube','')
                webbrowser.open(url=f"https://www.youtube.com/results?search_query={qryf}")
                print()
        

        elif 'exit' in qry or 'Exit' in qry or 'EXIT'in qry:
            dic("\nByee")
            dots()
            sys.exit()

        else:
            qryf=qry
            dic("Opening Browser")
            dots()
            webbrowser.open_new(url=f'https://www.google.com/search?q={qryf}')
            print('Sorry for the inconvenience || by-ghatiya developer ')
        
        
        
        # elif '' in qry:
            # tk3

        # elif 'i love u' in query0:
        #     speak("i love you so much aanee ")
        #     print("i love you so much aniii ")
        # elif 'spotify' in query0:
        #     querysf=query0.replace('spotify','')
        #     webbrowser.open(url=f"https://open.spotify.com/search/{querysf}")
        #     #    
        # else :
        #     start() 