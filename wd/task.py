
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
import os

# ---------------modules_imported_and_created---------------------------------------------------------------------------------------
# ------------------------------------task-modules----------------------------------------------------------------------------------

# tk wiki
import wikipedia
# tk gpt
# tk yt
import webbrowser
# tk spt
# tk flp
# tk mt
# tk bk
# tk amz
# tk htr



# tk E
import sys
# tk EL
import webbrowser


# ...................................................................................................................................

def run():
    
    # qryf = filtered query
    
    
    speak('Type the message querry or problem to pruh·seed further and press the enter key')
    speak("To Close Type 'exit' and press enter")
    while True:
        
        print("\nType the message querry or problem and press enter to procced further  || To Close Type 'exit' and press enter")
        qry=qery()
        

        # TASKS--------------
        # BROWSING TASK----
        if 'wikipedia' in qry  or 'Wikipedia' in qry or 'WIKIPEDIA' in qry :
            # tk wiki
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

        if 'chat gpt' in qry or'chatgpt'in qry:
            # tk gpt
            dic("opening Chat GPT")
            dots()
            webbrowser.open(url=f"https://chat.openai.com")
            print()
                
        # -------------------------------
        # -------------related to google------------
        elif 'youtube' in qry: 
            # tk yt
            if qry=='youtube':
                dic("opening   youtube")
                dots()
                webbrowser.open(url=f"https://www.youtube.com")
                print()
            
            elif qry=='youtube music':
                dic("opening   youtube")
                dots()
                webbrowser.open(url=f"https://music.youtube.com/")
                print()
            
            elif qry=='youtube studio':
                dic("opening   youtube")
                dots()
                webbrowser.open(url="https://studio.youtube.com/")
                print()
            else:
                if 'music' in qry:
                    dic("opening   youtube")
                    qryf=qry.replace('youtube'and'music',''and'')
                    dots()
                    webbrowser.open(url=f"https://music.youtube.com/search?q={qryf}")
                    print()
                else:
                    dic("opening   youtube")
                    dots()
                    qryf=qry.replace('youtube','')
                    webbrowser.open(url=f"https://www.youtube.com/results?search_query={qryf}")
                    print()
        
        # ------------
        elif 'spotify' in qry: 
            # tk spt
            # try:
            #     os._path.dirname('"C:\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Spotify.lnk"')
            if qry=='spotify':
                dic("opening   spotify ")
                webbrowser.open(url=f"https://open.spotify.com/")
                print()
            else:
                dic("opening   spotify")
                dots()
                qryf=qry.replace('spotify','')
                webbrowser.open(url=f"https://open.spotify.com/search/{qryf}")
                print()
        
        # -----------------------------
        # ------------shopping------------
        elif 'flipkart' in qry: 
            # tk flp
            if qry=='flipkart':
                dic("opening   flipkart ")
                dots()
                webbrowser.open(url=f"https://www.flipkart.com/")
                print()
            else:
                dic("opening   flipkart shoppings")
                dots()
                qryf=qry.replace('flipkart','')
                webbrowser.open(url=f"https://www.flipkart.com/search?q={qryf}")
                print()


        elif 'myntra' in qry: 
            # tk mt
            if qry=='myntra':
                dic("opening   myntra shoppings ")
                dots()
                webbrowser.open(url=f"https://www.myntra.com/")
                print()
            else:
                dic("opening   myntra shoppings")
                dots()
                qryf=qry.replace('myntra','')
                webbrowser.open(url=f"https://www.myntra.com/{qryf}")
                print()
        
        
        elif 'bewakoof' in qry: 
            # tk bk
            if qry=='bewakoof':
                dic("opening   bewakoof shoppings ")
                dots()
                webbrowser.open(url=f"https://www.bewakoof.com/")
                print()
            else:
                dic("opening   bewakoof shoppings")
                dots()
                qryf=qry.replace('bewakoof','')
                webbrowser.open(url=f"https://www.bewakoof.com/search/dvvd?ga_q={qryf}")
                print()

        # -----------------------------------------------------------------
        
        # ---------------------------------amazon-----------------------------------------
        elif 'amazon' in qry or ('prime'and 'music')in qry  or ('prime'and 'video') in qry: 
            # tk amz
            if qry=='amazon':
                dic("opening   amazon shoppings")
                webbrowser.open(url=f"https://www.amazon.in/")
                print()
            
            elif qry=='amazon prime':
                dic("opening   amazon prime ")
                webbrowser.open(url=f"https://www.primevideo.com/")
                print()
            
            elif qry=='prime video':
                dic("opening   amazon prime video")
                webbrowser.open(url=f"https://www.primevideo.com/")
                print()
            
            elif qry=='prime music':
                dic("opening   amazon prime music")
                webbrowser.open(url=f"https://music.amazon.in/")
                print()
            else:
                if 'music' in qry:
                    dic("opening prime music")
                    dots()
                    qryf=qry.replace("prime" and "music","" and "" )
                    webbrowser.open(url=f"https://music.amazon.in/search/{qryf}")
                    
                elif 'video' in qry:
                    dic("opening  prime video")
                    dots()
                    qryf=qry.replace('amazon'and'prime',''and'')
                    webbrowser.open(url=f"https://www.primevideo.com/region/eu/search/ref=atv_nb_sug?ie=UTF8&phrase={qryf}")
                    print()
                else:
                    dic("opening   amazon shoppings")
                    dots()
                    qryf=qry.replace('amazon','')
                    webbrowser.open(url=f"https://www.amazon.in/s?k={qryf}")
                    print()
        # ---------streaming----ott----------
        elif 'netflix' in qry: 
        # tk nfx
            dic("opening   Netflix ")
            dots()
            webbrowser.open(url="https://www.netflix.com/in/")
            print()


        elif 'hotstar' in qry:
        # tk htr
            if qry=='hotstar':
                dic("opening   hotstar ")
                dots()
                webbrowser.open(url="https://www.hotstar.com/in/")
                print()
            else :
                qryf=qry.replace('hotstar','')
                dic()
                dots()
                webbrowser.open(url=f"https://www.hotstar.com/in/explore?search_query={qryf}")
                print()
        # prime already given
        # jio cinema
        
        elif 'jio cinema' in qry:
        # tk jc
            dic("opening   jio cinema ")
            dots()
            webbrowser.open(url="https://www.jiocinema.com/")
            print()

        
        elif 'voot' in qry:
        # tk vt
            dic("opening   voot ")
            dots()
            webbrowser.open(url="https://www.voot.com/")
            print()


# --------------SYSYTEM AND EXCEPTION-----------
        elif 'exit' in qry or 'Exit' in qry or 'EXIT'in qry:
            # tk E
            dic("\nByee")
            print("_A___R__")
            dots()
            sys.exit()
        
        # elif 'date' in qry or 'time ' in qry:
        #     if qry=='date' or 'time':
        #         wishme()

        else:
            # tk EL
            qryf=qry
            dic("Opening Browser")
            dots()
            webbrowser.open_new(url=f'https://www.google.com/search?q={qryf}')
            # print('Sorry for the inconvenience || by-ghatiya developer ')
        
        
        # time and date 




        # elif 'i love u' in query0:
        #     speak("i love you so much aanee ")
        #     print("i love you so much aniii ")
  
        # else :
