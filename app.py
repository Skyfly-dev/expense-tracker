import streamlit as st
from expense_tracker import load_expense,save_expense
from datetime import date

st.set_page_config(
    page_title="Expense Tracker",
    page_icon="💰",
    layout="centered"
)
st.title("💰Expense Tracker")
st.write("Welcome to your personal Expense Tracker")


 #Add expense

st.header("Add New Expense")
with st.form("add_expense_form"):
    amount =st.number_input("Amount (₹)",min_value=0.01)
    category=st.text_input("Category")
    description=st.text_input("Description")
    expense_date=st.date_input("Date",value=date.today())
    submitted=st.form_submit_button("Add Expense")

if submitted:
    if category.strip() and description.strip() and amount>0:
        new_expense={
            "Amount":float(amount),
            "Category":category.strip(),
            "Description":description.strip(),
            "Date":str(expense_date)
        }
        expense=load_expense()
        expense.append(new_expense)
        save_expense(expense)

        st.success("Expense added successfully!")
        st.rerun()

    else:
        st.error("Please fill all fields correctly.")



#view expense

st.header("All Expenses")
expense=load_expense()
if expense:
    st.dataframe(expense,use_container_width=True)
    total=sum(item['Amount'] for item in expense)
    st.metric("Total Spending ",f"₹{total:.2f}")

else:
    st.info("No expenses added yet.")



#category wise summary

st.subheader("Category-wise Summary")
if expense:
    summary={}
    for item in expense:
        cat=item['Category']
        if cat not in summary:
            summary[cat]={"Count":0,"Total":0}

        summary[cat]['Count']+=1
        summary[cat]['Total']+=item['Amount']

    for cat,details in summary.items():
        st.write(
            f"**{cat}** -> Count:{details['Count']}, "
            f"Total:₹{details['Total']:.2f}"
        )
else:
        st.info("No expenses available for summary. ")




#edit expense

st.header("Edit expense")
expense=load_expense()
if expense:
    selected_index=st.selectbox(
        "Select an expense to edit",range(len(expense)),format_func=lambda i:(f"{expense[i]['Category']}-" f"{expense[i]['Amount']:.2f}-"
                                                                              f"{expense[i]['Description']}")
    )
    selected_expense=expense[selected_index]

    with st.form("edit_form"):
        amount=st.number_input(
            "Amount (₹)",min_value=0.01,
            value=float(selected_expense['Amount'])
        )
        category=st.text_input(
            "Category",value=selected_expense['Category']
        )

        description=st.text_input('Description',value=selected_expense['Description'])

        expense_date=st.date_input("Date",value=date(*map(int,selected_expense['Date'].split("-"))))


        updated=st.form_submit_button("Update Expense")


        if updated:
            if category.strip() and description.strip() and amount>0:
                expense[selected_index]={
                    'Amount':float(amount),
                    'Category':category.strip(),
                    'Description':description.strip(),
                    'Date':str(expense_date)
                }
                save_expense(expense)
                st.success("Expense updated successfully! ")
                st.rerun()
            else:
                st.error("Please fill all fields correctly.")

else:
    st.info("No expenses available to edit.")





#delete expense
st.header("Delete Expense")
expense=load_expense()
if expense:
    selected_index=st.selectbox(
        "Select an expense to delete",range(len(expense)),format_func=lambda i:(
            f"{expense[i]['Category']}-"
            f"₹{expense[i]['Amount']:.2f}-"
            f"{expense[i]['Description']}"
        ),
        key="delete_select"
    )
    if st.button("Delete expense"):
        expense.pop(selected_index)
        save_expense(expense)

        st.success("Expense deleted successfully!")
        st.rerun()


else:
    st.info("No expenses available to delete.")


