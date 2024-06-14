from tkinter import*
from PIL import Image,ImageTk       #pip install pillow
import w
import requests
class MyWeather:
    def __init__(self,root):
        self.root=root
        self.root.title("My Weather App")
        self.root.geometry("360x410+460+110") 
        self.root.config(bg="white")
        #==icon====
        self.search_icon=Image.open("icons/search.png")
        self.search_icon=self.search_icon.resize((15,15))
        self.search_icon=ImageTk.PhotoImage(self.search_icon)
        
        #===Vraiable====
        self.var_search=StringVar()
        
        title=Label(self.root,text="Weather App",font=("goudy old style",30,"bold"),bg="#140301",fg="white").place(x=0,y=0,relwidth=1,height=60)
        lbl_city=Label(self.root,text="City Name",font=("goudy old style",15),bg="#57068a",fg="white",anchor="w",padx=5).place(x=0,y=60,relwidth=1,height=40)
        txt_city=Entry(self.root,textvariable=self.var_search,font=("goudy old style",15),bg="lightYellow",fg="#262626").place(x=100,y=68,width=200,height=25)
        btn_search=Button(self.root,cursor="hand2",image=self.search_icon,activebackground="#033958",bd=0,command=self.get_weather).place(x=310,y=68,width=25,height=25)



        #=============Results====
        self.lbl_city=Label(self.root,text="City Name",font=("goudy old style",15),bg="white",fg="green").place(x=0,y=110,relwidth=1,height=20)
        self.lbl_city.place(x=0,y=110,relwidth=1,height=20)

        self.lbl_icon=Label(self.root,text="Icons",font=("goudy old style",15),bg="white").place(x=0,y=135,relwidth=1,height=100)
        self.lbl_temp=Label(self.root,text="temp",font=("goudy old style",15),bg="white",fg="orange").place(x=0,y=240,relwidth=1,height=20)
        lbl_wind=Label(self.root,text="wind",font=("goudy old style",15),bg="white",fg="#262626").place(x=0,y=265,relwidth=1,height=20)

        lbl_error=Label(self.root,text="Error",font=("goudy old style",15),bg="white",fg="red").place(x=0,y=285,relwidth=1,height=20)



        #=========footer=======
        lbl_footer=Label(self.root,text="Venator-R",font=("goudy old style",15),bg="#57068a",fg="white",pady=5).pack(side=BOTTOM,fill=X)
        

     def get_weather(self):
         api_key=w.api_key
         complete_url=f"https://api.openweathermap.org/data/2.5/weather?lat={self.var_search.get()}&lon={lon}&appid={api_key}
         #cityname,countryname,icons,temo_c,temp_f,wind
         results=requests.get(complete_url)
         if result:
             json=result.json()
             city_name=json["name"}
             country=json["sys"]["country"]
             icons=json["weather"][0]["icon"]
             temp_c=json["main"]["temp"]-273.15
             temp_f=(json["main"]["temp"]-273.15)*9/5+32
             wind=json["weather"]["main"]

            #print(city_name,country,icons,temp_c,temp_f,wind)


         
root=Tk()
obj=MyWeather(root)
root.mainloop()
