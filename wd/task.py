
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

# ---------------modules_imported_and_created---------------------------------------------------------------------------------------
# ------------------------------------task-modules-------------------------------------------------------------

# tk1
import wikipedia
# tk2
import webbrowser




def run():
    
    # qryf = filtered query
    # iv=qery()
    
    speak('Type the message querry or problem to pruh·seed further')
    
    while True:
        
        print("Type the message querry or problem to procced further  || To Close Press 'ESC' key")
        qry=qery()
        
        if 'wikipedia' in qry:
            # tk1
            qryf=qry
            try:
                results = wikipedia.summary(qryf,sentences=4)
                dic("As per the wikipedia",)
                dic(results)
            
            except wikipedia.exceptions.WikipediaException as e:
                print(e)
                dic('Wikipedia can not find it or server connection error ')
                break
                


        elif 'youtube'or'Youtube'or'YOUTUBE'  in qry: 
            # tk2   
            dic("opening   youtube")
            qryf=qry.replace('youtube','')
            webbrowser.open(url=f"https://www.youtube.com/results?search_query={qryf}")

        
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
        else:
            try:
                qryf=qry
                webbrowser.open_new(url=f'https://www.google.com/search?q={qryf}')
            except:
                print('Sorry for the inconvenience || by-ghatiya developer ')
