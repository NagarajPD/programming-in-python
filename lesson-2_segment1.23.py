deposit=900
loan=400
limit_reached=0
print("your deposits are ",deposit)
print("your loan amt is ",loan)
while(loan<=deposit and limit_reached==0):
    print("enter the additional loan amt")
    x=int(input())
    loan=loan+x
    if(loan<=deposit):
        print("your deposits are ",deposit)
        print("your loan amt is ",loan)
    else:
        loan=loan-x
        print("your loan is disaproved")
        print("your deposits are ",deposit)
        print("your loan amt is ",loan)
        limit_reached=1

