from django.shortcuts import render,redirect
from django.conf import settings
from upld.models import Content,UserInfo,Purpose

import pyrebase

from datetime import datetime

# Example list of participants



config = {
    "apiKey": "AIzaSyDQKQeK-8Z7EKAW2Cecb5JCIz9REecQwkU",
    "authDomain": "hisabkitab-ef4ac.firebaseapp.com",
    "projectId": "hisabkitab-ef4ac",
    "storageBucket": "hisabkitab-ef4ac.appspot.com",
    "messagingSenderId": "440470464914",
    "appId": "1:440470464914:web:150db7d031c226a2c9394b",
    "measurementId": "G-C07RT1H0ES",
    "databaseURL": "https://hisabkitab-ef4ac-default-rtdb.firebaseio.com",
  }


firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database= firebase.database()
member_name = database.child('Groups').child('Delhi').child('members').child('Aaryan').child('name').get().val()
members = database.child('Groups').child('Delhi').child('members').get().val()


# Create your views here.
def home(request):
    if request.method == 'GET':
        message = request.GET.get("message")
        print(message)

        if message is not None:
            # Create a new Content object only if there's a valid message
            Content.objects.create(content=message)

            # Redirect to the same view to avoid form resubmission
            return redirect('home')  # Update 'home' to the actual URL name of your view

    # If it's not a POST request or an invalid form submission, render the initial form
    ct = Content.objects.all().order_by('-id')
    
    return render(request, 'index.html', {'ct': ct})
def group(request):
    # Assuming 'Delhi' is the group name, adjust accordingly
    group_name = 'Delhi'

    transactions = database.child('Groups').child(group_name).child('transactions').get().val()

    transaction_list = []
    if transactions:
        for key, transaction_data in transactions.items():
            title = transaction_data.get('title')
            paidBy = transaction_data.get('paidBy')
            amount = transaction_data.get('amount')
            SplitBtw = transaction_data.get('SplitBtw')

            transaction_list.append({
                'title': title,
                'paidBy': paidBy,
                'amount': amount,
                'SplitBtw': SplitBtw,
            })
           
    transaction_list.reverse()
    purposes = Purpose.objects.all()

    
    return render(request, 'group.html', {'purposes': purposes, 'transactions': transaction_list})
def expenses(request):
    if request.method=='POST':
        title=request.POST.get("title")
        paidBy=request.POST.get("paidBy")
        amount=request.POST.get("amount")
        SplitBtw=request.POST.get("SplitBtw")
        group_name = 'Delhi'
        SplitBtwList = SplitBtw.split(',')
      
        
        new_transaction_key = {
            "title": title,
            "paidBy": paidBy,
            "amount": amount,
            "SplitBtw": SplitBtw,
        }
        split_option='1'
        print("*************************************")
        idList=[]
        participants_list = []
        for person in SplitBtwList:
            id = database.child('Groups').child('Delhi').child('members').child(person).child('id').get().val()
            mobile_number = database.child('Groups').child('Delhi').child('members').child(person).child('phone').get().val()
            upi_id = database.child('Groups').child('Delhi').child('members').child(person).child('upi').get().val()
            participants_list.append(
                {'id': id, 'name': person, 'mobile_number': mobile_number, 'upi_id': upi_id},
            )
            idList.append(id)
        database.child('Groups').child('Delhi').child('transactions').push(new_transaction_key)
        print(participants_list)
       
        paid_by_id = database.child('Groups').child('Delhi').child('members').child(paidBy).child('id').get().val()
        print(paid_by_id)
        purpose= title
        print(title)
        people_involved_ids = idList
        print(people_involved_ids)
        split_option='1'
        print(amount)
        amount = int(amount)
        net_amounts = {participant['id']: 0 for participant in participants_list}
        payments = []


        if split_option == '1':
            # Split equally
            print("hi")
            num_people_involved = len(people_involved_ids)
            print(amount)
            print(num_people_involved)
            split_amount = int(amount) / int(num_people_involved)
            print(split_amount)
            net_amounts[paid_by_id] -= amount
            print(net_amounts[paid_by_id])
            
            for person_id in people_involved_ids:
                net_amounts[person_id] += split_amount
                
                payments.append({
                    'from': paid_by_id,
                    'to': person_id,
                    'amount': split_amount
                })

        elif split_option == '2':
            # Split unequally
            amounts_split = input("Enter the amounts to be split for each person (comma-separated): ").split(',')
            amounts_split = [float(amount) for amount in amounts_split]
            if sum(amounts_split) != amount:
                print("Error: Sum of amounts provided should match the total amount.")
                return None

            net_amounts[paid_by_id] -= amount

            for i, person_id in enumerate(people_involved_ids):
                net_amounts[person_id] += amounts_split[i]
                payments.append({
                    'from': paid_by_id,
                    'to': person_id,
                    'amount': amounts_split[i]
                })
        

        else:
            print("Invalid choice for split option.")
            return None

        print(payments)
        
        
        for payment in payments:
            paymentFrom = paidBy
            
            for participant in participants_list:
              if participant['id'] == payment['to']:
                  paymentTo = participant['name']
            print(paymentTo,paymentFrom)
            if paymentTo == paymentFrom:
                pass
            else:
                negativePaymentAmount = int(payment['amount'])*(-1)
                paymentToCurrent = database.child('Groups').child('Delhi').child('members').child(paymentFrom).child('balances').child(paymentTo).get().val()
                paymentToNew = paymentToCurrent + payment['amount']
                paymentFromCurrent = database.child('Groups').child('Delhi').child('members').child(paymentTo).child('balances').child(paymentFrom).get().val()
                paymentFromNew = paymentFromCurrent + negativePaymentAmount
                database.child('Groups').child('Delhi').child('members').child(paymentFrom).child('balances').update({paymentTo: paymentToNew})
                database.child('Groups').child('Delhi').child('members').child(paymentTo).child('balances').update({paymentFrom: paymentFromNew})
                
              
            
                
    
        print("**************")
      

        return redirect('group')
    return render(request,'expenses.html')

def groups(request):
    return render(request,'groups.html')

def friends(request):
    aaryanIrfan = database.child('Groups').child('Delhi').child('members').child('Aaryan').child('balances').child('Irfan').get().val()
    aaryanBhavya = database.child('Groups').child('Delhi').child('members').child('Aaryan').child('balances').child('Bhavya').get().val()
    aaryanVaibhav = database.child('Groups').child('Delhi').child('members').child('Aaryan').child('balances').child('Vaibhav').get().val()
    print(aaryanIrfan)
    total_balance = aaryanIrfan+aaryanVaibhav+aaryanBhavya
    balance_list = {"aaryanBhavya":aaryanBhavya,"aaryanIrfan":aaryanIrfan,"aaryanVaibhav":aaryanVaibhav,"total_balance":total_balance}
    return render(request,'friends.html',{'balances': balance_list})
