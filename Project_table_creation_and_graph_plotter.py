# Take user input of weather its a csv file of excel file then we will extract data and ask the user to enter the column to be ploted and what type of graph

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#file taking input from the user
def file():
    f_type=input("Which type of file you want to take input (csv/excel): ")
    f_name=input("Enter the file name:")
    t=0
    if(f_type=="csv"):
        f_name=f_name+".csv"
        t=pd.read_csv(f_name, encoding="latin1")
        # print(t)
    elif(f_type=="excel"):
        f_name=f_name+".xlsx"
        t=pd.read_excel(f_name)
        # print(t)
    else:
        print("You have entered a wrong type of file!!!")
        file()
    print(t)
    return t

def col_select(t):
    print(t.columns)
    inp=input("Enter the column name:")
    var=t.get(inp)
    var.dropna()
    check(var)
    if(check(var)==True):
        return var
    else:
        print("Please enter a numerical containing column!!!")
        col_select(t)
        
def check(var):
    try:
        for i in var:
            float(i)
            return True
    except(ValueError):
        return False
    
def plot_scatter(v1,v2):
    plt.scatter(v1,v2)
    plt.show()
def plot_line(v1,v2):
    plt.plot(v1,v2)
    plt.show()
def add_col(t):
    inp=input("Enter the new column name:")
    values=[]
    for i in range(0,len(t)):
        val=input("Enter the Values:")
        values.append(val)
    t[inp]=values
    name=input("Enter new file name: ")
    t.to_excel(name,index=False)
    print("New file has been created!!!")
def remove_col(t):
    print(t.columns)
    inp=str(input("Enter the removing column name:"))
    t= t.drop(columns=[inp])
    return t
def file_create():
    table=pd.DataFrame()
    row=int(input("Enter the Number of Rows:"))
    col=int(input("Enter the Number of columns:"))
    for i in range(0,col):
        col_name=input("You are creating a new column name please: ")
        values=[]
        d_type=input("What type of data you want to enter (str/int): ")
        if(d_type.lower()=="int"):
            for i in range(0,row):
                value=int(input("Enter the integer value:"))
                values.append(value)
            table[col_name]=values
            values.clear()
        elif(d_type.lower()=="str"):
            for i in range(0,row):
                value=input("Enter the string value:")
                values.append(value)
            table[col_name]=values
            values.clear()
    print(table)
    inp=input("Want to export this table (Yes/No):")
    if(inp.lower()=="yes"):
        f_type=input("Enter which file wants to to exported (csv/excel):")
        f_name=input("Enter file name with extension:")
        f_name.strip()
        if(f_type.lower()=="csv"):
            table.to_csv(f_name,index=False)
        elif(f_type.lower()=="excel"):
            table.to_excel(f_name,index=False)
    elif(inp.lower()=="no"):
        print("this file was not exported!!!")
        
            

def main():
    e=input("Create a new file or existing file?? ")
    if(e.lower()=="new"):
        table=print(file_create())
        inp=input("Want to run again (Yes/No):")
        if(inp.lower()=="yes"):
            main()
        elif(inp.lower()=="no"):
            print("New file was successfully created.")
    elif(e.lower()=="exist"):
        inp=input("Want to start the program (Yes/No): ")
        if(inp.lower()=="yes"):
            r=file()
            dic={"Add_col":1,"Remove_col":2,"Plot_scatter":3,"Plot_line":4}
            print(dic)
            inp=int(input("Enter your value: "))
            if(inp==1):
                print(add_col(r))
                main()
            elif(inp==2):
                print(remove_col(r))
                main()
            elif(inp==3):
                plot_scatter(col_select(r),col_select(r))
                main()
            elif(inp==4):
                plot_line(col_select(r),col_select(r))
                main()
        elif(inp.lower()=="no"):
            print("Arre Bsdk")  
main()
    
        