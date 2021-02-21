from tkinter import *
import tkinter as tk
import csv
import os.path
import random

if os.path.isfile('input.csv'):
    print("yes")
    with open('input.csv', 'r') as file:   #code referenced from: https://www.programiz.com/python-programming/csv
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            state = line[0]
            num = int(line[1])
        if state == "Alaska":
            state = "ak"
        if state == "Arizona":
            state = "az"
        if state == "Colorado":
            state = "co"
        if state == "Hawaii":
            state = "hi"
        if state == "Idaho":
            state = "id"
        if state == "Montana":
            state = "mt"
        if state == "Nevada":
            state = "nv"
        if state == "Oregon":
            state = "or"
        if state == "Utah":
            state = "ut"
        if state == "Washington":
            state = "wa"
        if state == "Wyoming":
            state = "wy"
        stateFile = state + '.csv'
        with open(stateFile, 'r') as file:  #code referenced from: https://www.programiz.com/python-programming/csv
            all_data = csv.reader(file)
            next(all_data)
            with open('output.csv', 'w') as output_file:
                writer = csv.writer(output_file)
                writer.writerow(["input_state","input_number_to_generate","output_content_type","output_content_value"])
                data = []
                for line in all_data:
                    data.append(line)
                count = num
                while count >0:
                    x = random.randint(1, 280000)
                    writer.writerow([state, num, "street address", data[x][2] + " " + data[x][3] + data[x][4] + data[x][5] + data[x][6] + data[x][7] + " " + data[x][8]])
                    count -=1

else:

    root = Tk()

    # app title
    myTitle = Label(root, text= "Person Generator")
    myTitle.pack()

    #selecting state to import from
    whichState = Label(root, text= "Which state would you like addresses from?")
    whichState.pack()

    def selectState():
        state = chosen.get()
        stConfirm = Label(root, text="How many addresses from " + state + " would you like?").pack()
        stateFile = state + '.csv'
        with open(stateFile, 'r') as file:
            all_data = csv.reader(file)
            addData = []
            for row in all_data:
                addData.append(row[2]+" "+row[3]+row[4]+row[5]+row[6]+row[7]+" "+row[8])

        numInput = Entry(root, width=5, borderwidth=5)
        numInput.pack()

        # function to run when search button is clicked
        def searchButton():    #code reference from: https://www.youtube.com/watch?v=YXPyB4XeYLA&feature=emb_logo
            genNum = int(numInput.get())
            exportData = []
            count = genNum
            text_widget = tk.Text(root, height=60, width=60) #set up text widget for output on gui ref: https://www.askpython.com/python-modules/tkinter/tkinter-text-widget-tkinter-scrollbar
            scroll_bar = tk.Scrollbar(root) #add scroll bar for text widget
            scroll_bar.pack(side=tk.RIGHT)
            text_widget.pack(side =tk.LEFT)
            while count != 0:
                x = random.randint(1, 280000)
                #toDo1 = Label(root, text=addData[x])
                toDo1 = addData[x]
                exportData.append([state, genNum,"street address", addData[x]])
                #toDo1.pack()
                text_widget.insert(tk.END, toDo1 + "\n") #put generated data into text widget
                count -= 1


            def csvButton():
                with open('output.csv', 'w') as output_file:
                    writer = csv.writer(output_file)
                    writer.writerow(["input_state", "input_number_to_generate", "output_content_type", "output_content_value"])
                    data = []
                    for line in exportData:
                        writer.writerow(line)

            csvButton = Button(root, text="Get CSV file", command=csvButton).pack()
            # creation of search button and packing(putting on the screen) of search button
        searchButton = Button(root, text="Get Data", command=searchButton).pack()



    #select state dropdown box  code reference from: https://www.youtube.com/watch?v=YXPyB4XeYLA&feature=emb_logo
    chosen= StringVar()
    chosen.set("AK")
    dropDown = OptionMenu(root, chosen, "AK","AZ","CA","CO","HI","ID","MT","NV","OR","UT","WA","WY")
    dropDown.pack()
    stateButton = Button(root, text="click to select state", command = selectState).pack()

    root.mainloop()