def test_fn(param1):
    print("I like ",param1)

test_fn("c ++")
test_fn("pyrhon")
test_fn("sql")


def calc_disc(bill_amt):
    if bill_amt<=5000:
        print("10 % discount")
    else:
        print("15 % discount")

calc_disc(9000)
calc_disc(10000)
calc_disc(5000)


def cust_record(cname, cphone,billamt):
    print("mr.{} your phone number is {} and your bill amt is {}".format(cname,cphone,billamt))

cust_record("nagaraj","7259946596","100000000000")
cust_record("lekhana","8317360297","2134567889900")

