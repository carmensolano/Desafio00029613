from tkinter import *
from PIL import ImageTk, Image

root= Tk()
root.title("MEF 3D")
root.geometry("965x600")
root.config(bg="white")

mainFrame= Frame()
mainFrame.pack(fill="both", expand="True")
mainFrame.config(bg="white")

img1= ImageTk.PhotoImage(Image.open("C:\\Users\\ADMIN\\Desktop\\Simu2020\\DesafioDP00029613\\StartPage.png"))
img2= ImageTk.PhotoImage(Image.open("C:\\Users\\ADMIN\\Desktop\\Simu2020\\DesafioDP00029613\\modelo.png"))
img3= ImageTk.PhotoImage(Image.open("C:\\Users\\ADMIN\\Desktop\\Simu2020\\DesafioDP00029613\\dominio.png"))
img4= ImageTk.PhotoImage(Image.open("C:\\Users\\ADMIN\\Desktop\\Simu2020\\DesafioDP00029613\\concontorno.png"))
img5= ImageTk.PhotoImage(Image.open("C:\\Users\\ADMIN\\Desktop\\Simu2020\\DesafioDP00029613\\mallaytabla.png"))
img6= ImageTk.PhotoImage(Image.open("C:\\Users\\ADMIN\\Desktop\\Simu2020\\DesafioDP00029613\\paso1y2.png"))
img7= ImageTk.PhotoImage(Image.open("C:\\Users\\ADMIN\\Desktop\\Simu2020\\DesafioDP00029613\\paso3y4.png"))
img8= ImageTk.PhotoImage(Image.open("C:\\Users\\ADMIN\\Desktop\\Simu2020\\DesafioDP00029613\\paso5.png"))
img9= ImageTk.PhotoImage(Image.open("C:\\Users\\ADMIN\\Desktop\\Simu2020\\DesafioDP00029613\\paso52.png"))
img10= ImageTk.PhotoImage(Image.open("C:\\Users\\ADMIN\\Desktop\\Simu2020\\DesafioDP00029613\\paso6.png"))
img11= ImageTk.PhotoImage(Image.open("C:\\Users\\ADMIN\\Desktop\\Simu2020\\DesafioDP00029613\\paso62.png"))
img12= ImageTk.PhotoImage(Image.open("C:\\Users\\ADMIN\\Desktop\\Simu2020\\DesafioDP00029613\\def1.png"))
img13= ImageTk.PhotoImage(Image.open("C:\\Users\\ADMIN\\Desktop\\Simu2020\\DesafioDP00029613\\def2.png"))
img14= ImageTk.PhotoImage(Image.open("C:\\Users\\ADMIN\\Desktop\\Simu2020\\DesafioDP00029613\\k.png"))
img15= ImageTk.PhotoImage(Image.open("C:\\Users\\ADMIN\\Desktop\\Simu2020\\DesafioDP00029613\\l.png"))
img16= ImageTk.PhotoImage(Image.open("C:\\Users\\ADMIN\\Desktop\\Simu2020\\DesafioDP00029613\\g.png"))
img17= ImageTk.PhotoImage(Image.open("C:\\Users\\ADMIN\\Desktop\\Simu2020\\DesafioDP00029613\\g2.png"))
img18= ImageTk.PhotoImage(Image.open("C:\\Users\\ADMIN\\Desktop\\Simu2020\\DesafioDP00029613\\f.png"))
img19= ImageTk.PhotoImage(Image.open("C:\\Users\\ADMIN\\Desktop\\Simu2020\\DesafioDP00029613\\f2.png"))
img20= ImageTk.PhotoImage(Image.open("C:\\Users\\ADMIN\\Desktop\\Simu2020\\DesafioDP00029613\\galerkinmodif.png"))
img21= ImageTk.PhotoImage(Image.open("C:\\Users\\ADMIN\\Desktop\\Simu2020\\DesafioDP00029613\\r.png"))
img22= ImageTk.PhotoImage(Image.open("C:\\Users\\ADMIN\\Desktop\\Simu2020\\DesafioDP00029613\\r2.png"))
img23= ImageTk.PhotoImage(Image.open("C:\\Users\\ADMIN\\Desktop\\Simu2020\\DesafioDP00029613\\r3.png"))
img24= ImageTk.PhotoImage(Image.open("C:\\Users\\ADMIN\\Desktop\\Simu2020\\DesafioDP00029613\\q.png"))
img25= ImageTk.PhotoImage(Image.open("C:\\Users\\ADMIN\\Desktop\\Simu2020\\DesafioDP00029613\\q2.png"))
img26= ImageTk.PhotoImage(Image.open("C:\\Users\\ADMIN\\Desktop\\Simu2020\\DesafioDP00029613\\q3.png"))
img27= ImageTk.PhotoImage(Image.open("C:\\Users\\ADMIN\\Desktop\\Simu2020\\DesafioDP00029613\\emsam.png"))




image_list= [img1, img2, img3,img4, img5, img6, img7, img8, img9, img10, img11, img12, img13,img14, img15,img16,img17,img18,img19,img20,img21,img22, img23,img24, img25, img26, img27]

my_label = Label(mainFrame, image= img1)
my_label.grid(row=0, column= 0, columnspan= 3)




def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(mainFrame, image= image_list[image_number - 1])
    button_forward= Button(mainFrame, text=">>", command=lambda: forward(image_number+1))
    button_back= Button(mainFrame, text="<<", command=lambda:back(image_number - 1))
    
    if image_number == 27:
        button_forward= Button(mainFrame, text= ">>", state= DISABLED)
    
    my_label.grid(row=0, column= 0, columnspan= 3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)



def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(mainFrame, image= image_list[image_number - 1])
    button_forward= Button(mainFrame, text=">>", command=lambda: forward(image_number+1))
    button_back= Button(mainFrame, text="<<", command=lambda:back(image_number - 1))
    
    if image_number == 1:
        button_back= Button(mainFrame, text= "<<", state= DISABLED)
    
    my_label.grid(row=0, column= 0, columnspan= 3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)



button_back= Button(mainFrame, text="<<", command= back, state= DISABLED)
#button_exit= Button(mainFrame, text="Exit")
button_forward= Button(mainFrame, text=">>", command= lambda:forward(2))

button_back.grid(row=1, column=0)
#button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)






root.mainloop()