from ntpath import join
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np



class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("Algerian",20,"bold"),bg="lightgreen",fg="Blue")
        title_lbl.place(x=0,y=0,width=1366,height=35)
        
        img_top = Image.open(r"C:\Users\Reks\Desktop\myProj\Facial-Recognition-Based-Student-Attendance-System\Images\re2.jpg")
        img_top=img_top.resize((1366, 700),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=1366,height=650)
        
        # Button
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("Algerian",25,"bold"),bg="green",fg="white")
        b1_1.place(x=500,y=450,width=300,height=150)

        
    def train_classifier(self):
        data_dir = (r"C:\Users\Reks\Desktop\myProj\Facial-Recognition-Based-Student-Attendance-System\data")
        path=[os.path.join(data_dir,file) for  file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert('L')  # grAY SCALE image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)


        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed !",parent=self.root)




    
if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()