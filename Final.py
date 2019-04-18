import graphics as g
import time
import datetime
import os

class Health_center_Management:

    def __init__(self):
        win=g.GraphWin("HOSPITAL MANAGEMENT SYSTEM",920,600)
        win.setCoords(-20,-20,20,20)
        header=g.Text(g.Point(0,18),"HOSPITAL MANAGEMENT SYSTEM").draw(win)
        header.setSize(30)
        nameBtn=g.Rectangle(g.Point(0,0),g.Point(3,3)).draw(win)
        majorBtn=g.Rectangle(g.Point(0,0),g.Point(3,3)).draw(win)
        yearGroupBtn=g.Rectangle(g.Point(0,0),g.Point(3,3)).draw(win)
        dateBtn=g.Rectangle(g.Point(0,0),g.Point(3,3)).draw(win)
        diseaseBtn=g.Rectangle(g.Point(0,0),g.Point(3,3)).draw(win)
       
        database=open("Health_center_DB",'a+')



    def createBtn():
        pass
         
        
            

    def Add_patient():
        pass

    def Delete_patient():
        pass

    def Search_Pattient():
        pass

    def Update_patient_Info():
        pass


    def delete_item(s):
        pass


     
        






patient=Health_center_Management()
