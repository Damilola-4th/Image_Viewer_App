from tkinter import *
from PIL import ImageTk, Image
from collections import deque
root = Tk()

# for titling our GUI applications and iputting a Icon onto the window tab for our GUI App
root.title('Images')
root.iconbitmap('candlestick.ico')



my_img1 =ImageTk.PhotoImage(Image.open('Chistmas_girl.png'))
my_img2 =ImageTk.PhotoImage(Image.open('Lissandra_DHunter.jpg'))
my_img3 =ImageTk.PhotoImage(Image.open('kiyonna.jpg'))
my_img4 =ImageTk.PhotoImage(Image.open('The_butler.jpg'))


#created a list containing all the pictures so i can traverse through it using the forward and buck button i created --> functions like a stack (if back button)| a queue (if forward button)
def input_pics():
    global pictures
    pictures = deque([my_img1, my_img2, my_img3, my_img4])
    global pictures_name
    pictures_name = deque(['Chirstmas girl', 'Lissandra DHunter', 'Kiyonna Slay', 'Mr.Hermedingler'])
input_pics()

#defines a global label to show upon the first pic in our list upon opening up the GUI application
global image_num
image_num = 1
global pic_label
pic_label = Label(root, image=pictures[0])
global name_label
name_label = Label(root, text= pictures_name[0])
pic_number = Label(root, text='image ' + str(image_num) + ' of 4', bd=1, relief=SUNKEN, anchor=E)
#Show on the screen
pic_label.grid(row=0, column=1)
name_label.grid(row=1, column=1)
pic_number.grid(row=3, column=0, columnspan=3, sticky=W+E)

# defined a function to show the next picture if  '>>' is clicked upon and to show the previouse picture if '<<' is clicked upon.
def prevornextpic(button,pic_label, name_label, image_num):
    #clear grid
    pic_label.grid_forget()
    name_label.grid_forget()
    if button == '<<':
        if image_num > 1:
            image_num -= 1
        else:
            image_num = 4
        # define labels
        pic_label = Label(root, image=pictures[-1])
        name_label = Label(root, text=pictures_name[-1])
        #put on the screen
        pic_label.grid(row=0, column=1)
        name_label.grid(row=1, column=1)
        last_pic, last_name = pictures.pop(), pictures_name.pop()
        pictures.insert(0,last_pic), pictures_name.insert(0,last_name)
        Button(root, text='>>', padx=10, pady=10, command=lambda: prevornextpic('>>', pic_label, name_label, image_num)).grid(row=2, column=2)
        Button(root, text='<<', padx=10, pady=10,command=lambda: prevornextpic('<<', pic_label, name_label, image_num)).grid(row=2, column=0)
    if button == '>>':
        if image_num <= len(pictures)-1:
            image_num += 1
        else:
            image_num = 1

        first_pic,first_name = pictures.popleft(), pictures_name.popleft()
        pictures.append(first_pic), pictures_name.append(first_name)

        #define picture and name
        pic_label = Label(root, image=pictures[0])
        name_label = Label(root, text=pictures_name[0])

        #put on the screen
        pic_label.grid(row=0, column=1)
        name_label.grid(row=1, column=1)
        Button(root, text='>>', padx=10, pady=10, command=lambda: prevornextpic('>>', pic_label, name_label, image_num)).grid(row=2, column=2)
        Button(root, text='<<', padx=10, pady=10,command=lambda: prevornextpic('<<', pic_label, name_label, image_num)).grid(row=2, column=0)
    #Label that will show the current pic_number we are on
    pic_number = Label(root, text='image ' + str(image_num) + ' of 4',bd=1, relief=SUNKEN, anchor=E)
    #fit it on the screen
    pic_number.grid(row=3, column=0, columnspan=3, sticky=W+E)




#Created buttons
back_button = Button(root, text='<<', padx= 10, pady= 10, command= lambda: prevornextpic('<<', pic_label, name_label, image_num)).grid(row=2, column=0)
front_button = Button(root, text='>>', padx=10, pady=10, command=lambda: prevornextpic('>>', pic_label, name_label, image_num)).grid(row=2, column=2 )
exit_button = Button(root, text='Exit Program', command=root.quit).grid(row=2, column=1)



root.mainloop()