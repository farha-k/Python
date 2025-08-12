# -*- coding: utf-8 -*-
"""
Created on Thu Jul 31 12:58:04 2025

@author: saofl
"""

class Demo:
    pass

a=Demo()
type(a)
dir(a)
class Demo1:
    def display(self):
        return "hai"
b=Demo1()
dir(b)
b.display()
class Demo2:
    def display(self,name):
        return "hai "+name
    
c=Demo2()
c.display("pradeep")

class Summ:
    def sum_of_list(self,list_name):
        total=0
        for i in list_name:
            total+=i
        return total 
    def pattern(self,value,row):
        for i in range(0,row):
            print(value*i)
list1=[10,20,30,40,50]   
d=Summ()    
d.sum_of_list(list1)
d.pattern("*",6)
dir(d)

class Calculator:
    def summation(self,a,b):
        return a+b
    def subtraction(self,a,b):
        return a-b
    def multiplication(self,a,b):
        return a*b
    def division(self,a,b):
        return a/b
f=Calculator()    
f.summation(2,3)
f.subtraction(3,1)
f.multiplication(2,3)
f.division(15,3)


class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
                 
    def summation(self):
        return self.a+self.b
    def subtraction(self):
        return self.a-self.b
    def multiplication(self):
        return self.a*self.b
    def division(self):
        return self.a/self.b
    def change(self,c,d):
        self.a=c
        self.b=d
g=Calculator(2,4)
g.summation()
g.subtraction()
g.multiplication()
g.division()
g.a
g.b
g.a=3
g.b=5
g.a
g.summation()
g.change(4,6)
g.summation()

class BankAccount:
    def __init__(self,account_number,balance,date_of_opening,customer_name):
        self.account_number=account_number
        self.balance=balance
        self.date_of_opening=date_of_opening
        self.customer_name=customer_name
    def deposite(self,amount):
        if amount>0:
            self.balance=self.balance+amount
        else:
            print("amount must be positive")
    def withdraw(self,amount):
        if amount>0 and amount<self.balance:
            self.balance=self.balance-amount
        else:
            print("amount must be positive or your withdrawing amount greater than balance")
    def check_balance(self):
        return self.balance        
    
h=BankAccount(123456,10000,'10/02/2023','fathima farha k')    
h.deposite(1000)
h.withdraw(500)
h.check_balance()

class Inventory:
    def __init__(self):
        self.item_id=0
        self.item_name=""
        self.stock_count=0
        self.price=0
        self.item_details={}
    def add_item(self,item_id,item_name,stock_count,price):
        self.item_details[item_id]=[item_name,stock_count,price]
    def update_item(self,item_id,stock_count,price):
        self.item_details[item_id][1]=stock_count
        self.item_details[item_id][2]=price
    def check_item_details(self,item_id):
        print(self.item_details[item_id])
i=Inventory()        
i.add_item(1234,"fruits", 10,150)    
i.item_details    
i.update_item(1234, "fruits",20, 100)       
i.item_details
i.update_item(1234,25,110)
i.item_details
i.check_item_details(1234)


class Employee:
    def __init__(self,emp_id,emp_name,emp_salary,emp_department):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.emp_salary=emp_salary
        self.emp_department=emp_department
    def calculate_emp_salary(self,emp_salary,hours_worked):
       self.overtime=hours_worked-50
       if hours_worked>50:
           self.overtime_amount=(self.overtime*(self.emp_salary/50))
           self.emp_salary+=self.overtime_amount
           return self.emp_salary
    def emp_assign_department(self,emp_department):
        self.emp_department=emp_department
    def print_employee_details(self,emp_id):
        self.employee_details={self.emp_id:(self.emp_name,self.emp_salary,self.emp_department)}
        return self.employee_details
j=Employee(1212,"farha",50000,"accounting")           
j.calculate_emp_salary(50000,180)
j.emp_assign_department("Analyst")
j.emp_department
j.print_employee_details(1212)

class Restaurant:
    def __init__(self):
        self.menu_items={}
        self.book_table=[]
        self.customer_orders=[] 
    def add_item_to_menu(self,items,price):
        self.menu_items[items]=price
    def book_tables(self,table_number):
        if table_number in self.book_table:
            print("the table is already booked")
        else:
            self.book_table.append(table_number)
    def customer_order(self,**order_item):
        self.customer_orders.append(order_item)
    def bill(self):
        result=0
        for k,v in self.customer_orders[0].items():
            result=result+v*(self.menu_items.get(k))
        print("total=",result)
            
        
    
                
            
        
h=Restaurant()        
h.add_item_to_menu("Apple_Juice",70) 
h.add_item_to_menu("Biriyani",100)       
h.add_item_to_menu('Lime',15)
h.add_item_to_menu('Avocado_Juice',80)
h.add_item_to_menu('Mandhi_Rice',400)
h.book_tables(1)
h.customer_order(Apple_Juice=1,Mandhi_Rice=1)
h.menu_items
h.book_table
h.customer_orders
h.bill()
h.menu_items.get('Apple Juice')
