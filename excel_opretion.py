import win32com.client as win32
import os
from selenium import webdriver
import time
from Recognizer_Speech import *

def OpenExcel():
    x1App = win32.Dispatch('Excel.Application')
    x1App.Visible = True
    x1App = win32.Dispatch('Excel.Application')
    x1App.Visible = True
    wb =x1App.Workbooks.Add()

    run = True
    while run:
            speak("what can i do for you?")
            voice = recognizer_speech()
            print(voice)
            
            # if "save file" in voice:
            #       wb.SaveAs(os.path.join(os.getcwd(),'text.xlsx'))
            
            if "close window":
                  run= False
                  wb.close()
    

# OpenExcel()

            # if "write data" in voice:
            #       ws_sheet1 = wb.WorkSheets('Sheet1')
            #       time.sleep(3)
            #       speak("which column")
            #       col = recognizer_speech()
            #       print(col)
            #       speak("which row")
            #       time.sleep(2)
            #       row = recognizer_speech()
            #       print(row)
            #       time.sleep(2)
            #       speak("tell me data")
            #       data = recognizer_speech()
            #       print(data)
            #       ws_sheet1.Cells(row,col).value = data
                  


        



# x1App = win32.Dispatch('Excel.Application')
# x1App.Visible = True

# wb =x1App.Workbooks.Add()
# wb.name
# print(wb.name)
# # save the excel file

# # wb.SaveAs(os.path.join(os.getcwd(),'text.xlsx'))
# ws_sheet1 = wb.WorkSheets('Sheet1')
# print(ws_sheet1.name)
# # ws_sheet1.Cells(1,'A').value = 'Cell A1'
# # ws_sheet1.Cells(1,'B').value = 'Cell B1'
# # ws_sheet1.Cells(2,'A').value = 'Cell A2'

# # wb.close()