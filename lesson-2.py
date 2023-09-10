bill_amt=input("eneter the amt")
bill_amt=int(bill_amt)
if bill_amt>100 and bill_amt<=200:
    print("10%")
elif bill_amt>200 and bill_amt<=500:
    print("20%")
elif bill_amt>500:
    print("30%")
else:
    print("no disc")