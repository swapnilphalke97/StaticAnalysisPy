# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import tkinter
import ast
import inspect
from bubblesort import xyz
# importing tkinter and tkinter.ttk
# and all their functions and classes
# importing tkinter and tkinter.ttk
# and all their functions and classes
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
# importing askopenfile function
# from class filedialog
from tkinter.filedialog import askopenfile

root = tk.Tk()
root.geometry('200x100')

def don(filename):
    tree = ast.parse(filename)
    # for node in ast.walk(tree):
    #         print(node.__class__.__name__)
    tbl=[]
    data = filename.replace('\n', '')
    # Vulture  tool
    #bandit  
    tbl.append( ( 'Number of occurrence of def:', data.count('def') ))
    tbl.append(('Number of occurrence of class:',data.count('class')))
    tbl.append(('Number of occurrence of break:',data.count('break')))
    tbl.append(('Number of occurrence of continue:',data.count('continue')))
    tbl.append(('Number of occurrence of pass:',data.count('pass')))
    tempList=tbl
    import tkinter as tk
    from tkinter import ttk

    def show():

       
       
        

        for i, (start,end) in enumerate(tempList, start=1):
            listBox.insert("", "end", values=(i, start,end))

    sc = tk.Tk() 
    label = tk.Label(sc, text="def/class/breakpoint info", font=("Arial",50)).grid(row=0, columnspan=4)
# create Treeview with 3 columns
    cols = ('Index', 'Start Line','End Line')
    listBox = ttk.Treeview(sc, columns=cols, show='headings')
# set column headings
    for col in cols:
        listBox.heading(col, text=col)    
        listBox.grid(row=1, column=0, columnspan=2)

    showScores = tk.Button(sc, text="Show Data", width=50, command=show).grid(row=4, column=0)
    closeButton = tk.Button(sc, text="Close", width=50).grid(row=4, column=1)

    sc.mainloop()


def giveme(filename):
    
    tree = ast.parse(filename)
    table=[]
    i=0
    is_print = False
    for node in ast.walk(tree):
        try:
            is_print = (node.id == 'def')
        except AttributeError:  # only expect id to exist for Name objs
            pass
        if is_print:
            
            print("hgdjavljaj")
            break
        
        if isinstance(node, (ast.For)):
            table.append(('For Loop',node.lineno,node.end_lineno))
            i=i+1
        
        if isinstance(node, (ast.For)):
            table.append(('For Loop',node.lineno,node.end_lineno))
            i=i+1
        if isinstance(node, (ast.While)):
            table.append(('While Loop',node.lineno,node.end_lineno))
            i=i+1
        if isinstance(node, (ast.If)):
            table.append(('If',node.lineno,node.end_lineno))
            i=i+1
        if isinstance(node, (ast.Dict)):
            table.append(('Dict',node.lineno,node.end_lineno))
            i=i+1
        if isinstance(node, (ast.Set)):
            table.append(('Set',node.lineno,node.end_lineno))
            i=i+1
        if isinstance(node, (ast.BoolOp)):
            table.append(('BoolOp',node.lineno,node.end_lineno))
            i=i+1
        if isinstance(node, (ast.BinOp)):
            table.append(('BinOp',node.lineno,node.end_lineno))
            i=i+1
        if isinstance(node, (ast.Tuple)):
            table.append(('Tuple',node.lineno,node.end_lineno))
            i=i+1
        if isinstance(node, (ast.List)):
            table.append(('List',node.lineno,node.end_lineno))
            i=i+1
        if isinstance(node, (ast.Dict)):
            table.append(('Dict',node.lineno,node.end_lineno))
            i=i+1
        if isinstance(node, (ast.Import)):
            table.append(('Import',node.lineno,node.end_lineno))
            i=i+1
           
        if isinstance(node, (ast.Import)):
            table.append(('Import',node.lineno,node.end_lineno))
            i=i+1
    print(table)
    tempList=table
    import tkinter as tk
    from tkinter import ttk

    def show():

       
       
        

        for i, (name, start,end) in enumerate(tempList, start=1):
            listBox.insert("", "end", values=(i, name, start,end))

    scores = tk.Tk() 
    label = tk.Label(scores, text="Static Analysis", font=("Arial",50)).grid(row=0, columnspan=4)
# create Treeview with 3 columns
    cols = ('Index', 'Name', 'Start Line','End Line')
    listBox = ttk.Treeview(scores, columns=cols, show='headings',height=30)
# set column headings
    for col in cols:
        listBox.heading(col, text=col)    
        listBox.grid(row=1, column=0, columnspan=2)

    showScores = tk.Button(scores, text="Show Data", width=50, command=show).grid(row=4, column=0)
    closeButton = tk.Button(scores, text="Close", width=50).grid(row=4, column=1)

    scores.mainloop()
    
    
   #  class Table:
        
         
   #      def __init__(self,root):
             
   #         # code for creating table
   #          for i in range(total_rows):
   #              for j in range(total_columns):
                     
   #                  self.e = Entry(root, width=20, fg='blue',
   #                                font=('Arial',16,'bold'))
                     
   #                  self.e.grid(row=i, column=j)
   #                  self.e.insert(END, lst[i][j])

      
   # # find total number of rows and
   # # columns in list
   #  total_rows = len(table)
   #  total_columns = len(table[0])
      
   # # create root window
   #  root = Tk()
   #  t = Table(root)
   #  root.mainloop()

 
   
    



  
  





    
# This function will be used to open
# file in read mode and only Python files
# will be opened
def open_file():
	file = askopenfile(mode ='r', filetypes =[('Python Files', '*.py')])
	if file is not None:
		content = file.read()
		giveme(content)
        
        
def op():
	file = askopenfile(mode ='r', filetypes =[('Python Files', '*.py')])
	if file is not None:
		content = file.read()
		don(content)       
        
        

                

btn1 = tk.Button(root, text ='Click here- Open file to Get Loop Info', command = lambda:open_file()).grid(row=4, column=0)
btn2 = tk.Button(root, text ='Click here- Open file to Get def/class/breakpoint info', command = lambda:op()).grid(row=5, column=0)
# btn.pack(side = TOP, pady = 10)

mainloop()


    

# with filename as f:
#       tree = ast.parse(f.read())
# for node in ast.walk(tree):
#         print(node.__class__.__name__)
# with open('x1.py', 'r') as file:
#     data = file.read().replace('\n', '')
# # Vulture  tool
# #bandit  
# print("start") 

# print("End") 
# print('Number of occurrence of def:', data.count('def'))
# print('Number of occurrence of Class:', data.count('class'))
# print('Number of occurrence of def:', data.count('break'))
# print('Number of occurrence of Class:', data.count('continue'))
# print('Number of occurrence of def:', data.count('pass'))


# class CallCollector(ast.NodeVisitor):
#     def __init__(self):
#         self.calls = []
#         self.current = None

#     def visit_Call(self, node):
#         # new call, trace the function expression
#         self.current = ''
#         self.visit(node.func)
#         self.calls.append(self.current)
#         self.current = None

#     def generic_visit(self, node):
#         if self.current is not None:
#             print ( "warning: {} node in function expression not supported".format(
#                 node.__class__.__name__))
#         super(CallCollector, self).generic_visit(node)

#     # record the func expression 
#     def visit_Name(self, node):
#         if self.current is None:
#             return
#         self.current += node.id

#     def visit_Attribute(self, node):
#         if self.current is None:
#             self.generic_visit(node)
#         self.visit(node.value)  
#         self.current += '.' + node.attr

# # def prints_something(func):
# #     is_print = False
# #     for node in ast.walk(ast.parse(inspect.getsource(func))):
#         # try:
#         #     is_print = (node.id == 'arr')
#         # except AttributeError:  # only expect id to exist for Name objs
#         #     pass
#         # if is_print:
#         #     print("hgdjavljaj")
#         #     break
# #     return is_print
# # prints_something(xyz)

# cc = CallCollector()
# cc.visit(tree)
# print (cc.calls)



# table =[]
# i=0
# is_print = False
# for node in ast.walk(tree):
   
#     # try:
#     #     print(node)
       
        
#     # except AttributeError:  # only expect id to exist for Name objs
#     #     pass
#     # if is_print:
        
#     #     print("hgdjavljaj")
#     #     break
   
#     try:
#         is_print = (node.id == 'def')
#     except AttributeError:  # only expect id to exist for Name objs
#         pass
#     if is_print:
        
#         print("hgdjavljaj")
#         break
    
#     if isinstance(node, (ast.For)):
#         table[i]=['For Loop',node.lineno,node.end_lineno]
#         i=i+1
    
#     if isinstance(node, (ast.For)):
#         table[i]=['For Loop',node.lineno,node.end_lineno]
#         i=i+1
#     if isinstance(node, (ast.While)):
#         table[i]=['While Loop',node.lineno,node.end_lineno]
#         i=i+1
#     if isinstance(node, (ast.If)):
#         table[i]=['If',node.lineno,node.end_lineno]
#         i=i+1
#     if isinstance(node, (ast.Dict)):
#         table[i]=['Dict',node.lineno,node.end_lineno]
#         i=i+1
#     if isinstance(node, (ast.Set)):
#         table[i]=['Set',node.lineno,node.end_lineno]
#         i=i+1
#     if isinstance(node, (ast.BoolOp)):
#         table[i]=['BoolOp',node.lineno,node.end_lineno]
#         i=i+1
#     if isinstance(node, (ast.BinOp)):
#         table[i]=['BinOp',node.lineno,node.end_lineno]
#         i=i+1
#     if isinstance(node, (ast.Tuple)):
#         table[i]=['Tuple',node.lineno,node.end_lineno]
#         i=i+1
#     if isinstance(node, (ast.List)):
#         table[i]=['List',node.lineno,node.end_lineno]
#         i=i+1
#     if isinstance(node, (ast.Dict)):
#         table[i]=['Dict',node.lineno,node.end_lineno]
#         i=i+1
#     if isinstance(node, (ast.Import)):
#         table[i]=['Import ',node.lineno,node.end_lineno]
#         i=i+1
       
#     if isinstance(node, (ast.Import)):
#         table[i]=['Import',node.lineno,node.end_lineno]
#         i=i+1



# from tkinter import *
  
  
# class Table:
      
#     def __init__(self,root):
          
#         # code for creating table
#         for i in range(total_rows):
#             for j in range(total_columns):
                  
#                 self.e = Entry(root, width=20, fg='blue',
#                                font=('Arial',16,'bold'))
                  
#                 self.e.grid(row=i, column=j)
#                 self.e.insert(END, lst[i][j])

   
# # find total number of rows and
# # columns in list
# total_rows = len(table)
# total_columns = len(table[0])
   
# # create root window
# root = Tk()
# t = Table(root)
# root.mainloop()








# # Print the names of the columns.
# print ("{:<10} {:<10} {:<10}".format('Keyword', 'StartAt', 'EndAt'))
 
# # print each data item.
# for key, value in table.items():
#     Keyword, StartAt, EndAt = value
#     print ("{:<10} {:<10} {:<10}".format(Keyword, StartAt, EndAt))

    

