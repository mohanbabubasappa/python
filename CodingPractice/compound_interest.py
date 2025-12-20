p=float(input("principal:"))
r=float(input("rate of interest:"))
t=float(input("time:"))

amount=p*pow((1+r/100),t)
print(amount)
ci=amount-p
print(ci)