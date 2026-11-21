import json
from  datetime import datetime
import math
from pathlib import Path

BASE_DIR=Path(__file__).resolve().parent
FILE_PATH=BASE_DIR/"expenses.json"

#1.save expenses into json file
def save_expense(expense):
    with open(FILE_PATH,"w") as file:
        json.dump(expense,file,indent=4)


#2.load expenses from json
def load_expense():    
    try:
        with open(FILE_PATH,"r") as file:
            expense=json.load(file)
            if not isinstance(expense,list):
                print("Error :Expense data must be a list.")
                return None
            
            for item in expense:
                if not isinstance(item,dict):
                    print("Error: Invalid expense record.")
                    return None
                
                if not all(key in item for key in ("Amount","Category","Description","Date")):
                    print("Error :An expense record is missing required info")
                    return None
                
                
                if isinstance(item["Amount"],bool) or not isinstance(item["Amount"],(int,float)):
                    print("Error:Amount must be a valid number.")
                    return None
                
                if item["Amount"]<=0 or not math.isfinite(item["Amount"]):
                    print("Error: Amount must be a positive,finite number.")
                    return None

                if not isinstance(item["Category"],str) or not isinstance(item["Description"],str):
                    print("Error:Category and Description must be strings.")
                    return None
                
                if not item["Category"].strip() or not item["Description"].strip():
                    print("Error:Category and Description cannot be empty.")
                    return None
                
                if not isinstance(item["Date"],str):
                    print("Error: Date must be a string.")
                    return None
                
                try:
                    datetime.strptime(item["Date"],"%Y-%m-%d")
                except ValueError:
                    print("Error: Invalid date format. Use YYYY-MM-DD. ")
                    return None
                
                    
            return expense


        
    except FileNotFoundError:
        return []
    
    except json.JSONDecodeError:
        print("Error : Expenses file contains invalid JSON data.")
        return None




#3.Add expense
def add_expense(expense):
        while True:            
            try:            
                amount=float(input("Amount:"))
                
            except ValueError:
                print("Please enter a valid number")
                continue
            if amount<=0 or not math.isfinite(amount):
                print("Amount must be positive and finite.")
                continue
            break


        while True:
                category=input('Category:').strip().strip("\"'").strip()
                if not category:
                    print("Category cannot be empty.")
                    continue
                break
        for item in expense:
            if item['Category'].casefold()==category.casefold():
                existing_category=item['Category']
                break
        if existing_category:
            print(f"An existing category {existing_category} was found.")
            choice=input("Do you want to use this category? (y/n): ").strip().lower()
            if choice=="y":
                category=existing_category

                
        while True:
            description=input('Description:').strip().strip("\"'").strip()
            if not description:
                print("Description cannot be empty")
                continue
            break

        while True:
            date=input('Date(YYYY-MM-DD)[Press enter button for today]:').strip()
            if not date:
                date=datetime.today().strftime("%Y-%m-%d")
                break
            try:
                datetime.strptime(date,"%Y-%m-%d")
                break
            except ValueError:
                print("Invalid date! Please use YYYY-MM-DD.")

        expense1={
        'Amount':amount,
        'Category':category,
        'Description':description,
        'Date':date
         }
        expense.append(expense1)
        print("Expense added successfully!")

        
#4.view
def view_expense(expense):
          if not expense:
              print("No expense available.")
              return
          for index,item in enumerate(expense,start=1):
               print(f"\nExpense {index}")
               print(f"Amount:₹{item['Amount']}")
               print(f"Category:{item['Category']}")
               print(f"Description:{item['Description']}")
               print(f"Date:{item['Date']}")


#5.update
def update_expense(expense):
     view_expense(expense)
     while True:
         try:         
             edit_number=int(input("Which expense do you want to edit?"))
             
         except ValueError:
             print("Please enter valid expense number")
             continue

         if 1<=edit_number<=len(expense):
          break
         print("Please enter a valid expense number.")
     selected_expense=expense[edit_number-1]
     new_amount=input(f"New amount (Press Enter to keep {selected_expense['Amount']}):").strip()

     if not new_amount:
         pass
     else:
         while True:
             try:
                 amount=float(new_amount)
             except ValueError:
                 print("Please enter a valid number.")
                 new_amount=input("Enter new amount: ")
                 continue
             if amount<=0 or not math.isfinite(amount):
                 print("Amount must be positive and finite")
                 new_amount=input("Enter new amount: ")
                 continue
             selected_expense['Amount']=amount
             break
         
     new_category=input(f"New category (Press enter to keep {selected_expense['Category']}): ").strip().strip("\"'").strip()
     if not new_category:
         pass
     else:
         selected_expense['Category']=new_category
     new_description=input(f"New description (Press enter to keep {selected_expense['Description']}): ").strip().strip("\"'").strip()


     if not new_description:
         pass
     else:
         selected_expense['Description']=new_description


     current_date=selected_expense['Date']
     new_date=input(f"New date (YYYY-MM-DD, Press Enter to keep {current_date}): ").strip()     

     if not new_date:
         pass
     else:
         while True:
             try:
                 datetime.strptime(new_date,"%Y-%m-%d")
                 selected_expense['Date']=new_date
                 break
             except ValueError:
                 print("Invalid date!! Please use YYYY-MM-DD. ")
                 new_date=input("Enter date again: ").strip()

     print("Expense updated successfully!.")



#6.delete 
def delete_expense(expense):   
     view_expense(expense) 
     while True:
         try:            
              delete_number=int(input("Which expense do you want to delete?: "))
              
         except ValueError:
             print("Please enter valid expense number.")
             continue
         if 1<=delete_number<=len(expense):
             break
          
         else:
          print("Please enter valid number.")
     expense.pop(delete_number-1)
     print("Expense deleted successfully!")


  
#7.calculate total 
def calculate_total(expense):             
    total=0
    for item in expense:
        total+=item['Amount']
    return total


    
#8.calculate total category wiseee
def category_summary(expense):             
    summary={}
    for item in expense:
        category=item['Category']
        if category not in summary:
            summary[category]={
                'Count':0,
                'Total':0
            }
        summary[category]['Count']+=1
        summary[category]['Total']+=item['Amount']
    for category,details in summary.items():
        print(f"{category}:Count={details['Count']},Total=₹{details['Total']:.2f}")


#9.main program 
if __name__=="__main__":
    
    print("EXPENSE TRACKER")
    print("Welcome ! Track your expenses.....")

    expense=load_expense()

    if expense is None:
     print("Cannot start Expense Tracker because the saved data is corrupted.")
     exit()


    if __name__=="__main__":    
     while True:
      print("...what would you like to do >>>")
      print("\n1.Add Expense" \
"\n2.View All Expense" \
"\n3.Calculate Total Expense" \
"\n4.Calculate Category-wise Expense" \
"\n5.Edit Expense" \
"\n6.Delete Expense" \
"\n7.Exit")
    
      choice=input("enter ur choice(1-7):")
      if choice=="1":
        add_expense(expense)
        save_expense(expense)

      elif choice=="2":
        if not expense:
            print("No expense available to view")
        else:
            view_expense(expense)

      elif choice=="3":
        if not expense:
            print("No expense available")
        else:
            total=calculate_total(expense)
            print(f"Total Spending : ₹{total:.2f}")

      elif choice=="4":
           if not expense:
               print("No expense available")
           else:
               print("Here is your category wise summary: ")
               category_summary(expense)

      elif choice=="5":
        if not expense:
            print("No expense available to edit")
        else:
            update_expense(expense)
            save_expense(expense)

      elif choice=="6":
        if not expense:
            print("No expense data to delete")
        else:
            delete_expense(expense)
            save_expense(expense)

      elif choice=="7":
        print("\n we are exiting expense tracker....")
        print("Thank you ! Please come again")
        break
    else:
        print("Invalid Choice! Please enter a valid choice from 1 to 7.")
    



