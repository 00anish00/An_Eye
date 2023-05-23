
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
# tk ig
# tk fb
# tk tt
# tk li
# tk id
# tk wh
# tk sc
# tk spt
# tk flp
# tk mt
# tk bk
# tk amz
# tk nfx
# tk htr
# tk jc
# tk vt


# tk win 11 
# tk ms 
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
        elif 'youtube' in qry or 'yt'in qry: 
            # tk yt
            if 'yt' in qry:
                qry=qry.replace('yt','youtube')
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
        # -----------------------------------
        # ---------------------social-media------------------------
        elif 'instagram' in qry:
            # tk ig
            if qry=='instagram':
                dic("opening   instagram ")
                dots()
                webbrowser.open(url=f"https://www.instagram.com/")
                print()
            else:
                dic("opening   instagram")
                dots()
                qryf=qry.replace('instagram','')
                webbrowser.open(url=f"https://www.instagram.com/{qryf}")
                print()
        elif 'facebook' in qry:
            # tk fb
            if qry=='facebook':
                dic("opening   facebook ")
                dots()
                webbrowser.open(url=f"https://www.facebook.com/")
                print()
            else:
                dic("opening   facebook")
                dots()
                qryf=qry.replace('facebook','')
                webbrowser.open(url=f"https://www.facebook.com/{qryf}")
                print()
        elif 'twitter' in qry:
            # tk tt
            if qry=='twitter':
                dic("opening   twitter ")
                dots()
                webbrowser.open(url=f"https://www.twitter.com/")
                print()
            else:
                dic("opening   twitter")
                dots()
                qryf=qry.replace('twitter','')
                webbrowser.open(url=f"https://www.twitter.com/{qryf}")
                print()
        elif 'linked in' in qry:
            # tk li
            if qry=='linked in':
                dic("opening   linked in ")
                dots()
                webbrowser.open(url=f"https://www.linkedin.com")
                print()
            else:
                dic("opening   linked in")
                dots()
                qryf=qry.replace('linked in','')
                webbrowser.open(url=f"https://www.linkedin.com/search/results/all/?keywords={qryf}")
                print()
        elif 'indeed' in qry:
            # tk id
            if qry=='indeed':
                dic("opening   indeed ")
                dots()
                webbrowser.open(url=f"https://in.indeed.com/")
                print()
            else:
                dic("opening   indeed")
                dots()
                qryf=qry.replace('indeed','')
                webbrowser.open(url=f"https://in.indeed.com/jobs?q={qryf}")
                print()
        elif 'whatsapp' in qry:
            # tk wh
            if qry=='whatsapp web':
                dic("opening   whatsapp web ")
                dots()
                webbrowser.open(url="https://web.whatsapp.com/")
                print()
            else:
                dic("opening   whatsapp  ")
                dots()
                webbrowser.open(url="https://www.whatsapp.com/")
                print()

        elif 'snapchat' in qry:
            # tk sc
                dic("opening   snapchat ")
                dots()
                webbrowser.open(url=f"https://www.snapchat.com/")
                print()
            
        # -----------------------------------------------------------------
        # ------------songs------------
        elif 'spotify' in qry: 
            # tk spt
            # try:
            #     os._path.dirname('"C:\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Spotify.lnk"')
            if qry=='spotify':
                dic("opening   spotify ")
                dots()
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
                dic('opening   hotstar')
                dots()
                webbrowser.open(url=f"https://www.hotstar.com/in/explore?is_paywall_onboarding=true&search_query={qryf}")
                print()
        # prime already given
        
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
        elif 'windows 11' in qry:
            # tk w11
            dic("opening   windows 11")
            dots()
            webbrowser.open(url="https://www.microsoft.com/software-download/windows11")

        elif 'microsoft store' in qry:
            # tk ms
            if qry=='microsoft store':
                dic("opening   microsoft store")
                dots()
                webbrowser.open(url="https://apps.microsoft.com/store/")
            else:
                qryf=qry.replace('microsoft store','')
                dic("opening   microsoft store")
                dots()
                webbrowser.open(url=f"https://apps.microsoft.com/store/search/{qryf}")
            


                
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
