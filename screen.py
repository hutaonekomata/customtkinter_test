import customtkinter as ct
import pandas as pd

class prodList(ct.CTkScrollableFrame):
    def __init__(self,master,title,values):
        super().__init__(master)
        self.grid_columnconfigure(0,weight=1)
        self.values = master.num
        self.checkboxes = []

        for index,value in enumerate(self.values):
            #checkbox = ct.CTkCheckBox(self,text=value[1])
            checkbox = ct.CTkCheckBox(self,text=value)
            checkbox.grid(row=index,column=0,padx=10,pady=(10,0),sticky="w")
            self.checkboxes.append(checkbox)

    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
            return checked_checkboxes

class lendFrame(ct.CTkFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)
        self.num = "1"
        self.setup_form()

    def segmented_button_callback(self,value):
        print("segmented button clicked",value)

    def lendAction(self,**kwargs):
        # ToplevelWindow
        return

    def setup_form(self):
        values = ["1","2","3","4","5","6","7","8"]
        self.scrollFrame = prodList(self,title="values",values=values)
        self.scrollFrame.pack()

        self.segmented_button = ct.CTkSegmentedButton(self,values=["0.5","1","1.5","3","4","6","8"],command = self.segmented_button_callback)
        self.segmented_button.pack()
        self.segmented_button.set("0.5")

        # authButtonをクリックしたときに現在のsegmentButtonの値を取得する
        self.authButton = ct.CTkButton(self,text="借りる",command=self.lendAction)
        self.authButton.pack()

class MainFrame(ct.CTkTabview):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)

        self.add("lend")
        self.add("return")
        self.add("info")
        self.add("config")

        self.frame1 = lendFrame(master = self.tab("lend"))
        self.frame1.grid(row=0,column=0,padx=20,pady=10)

class App(ct.CTk):
    def __init__(self):
        super().__init__()
        self.geometry="400x220"

        self.setup_form()

    def setup_form(self):
        self.tab_view = MainFrame(master=self)
        self.tab_view.grid(row=0,column=0,padx=20,pady=(20,0))

app = App()
app.mainloop()
