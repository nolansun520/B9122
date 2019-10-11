#question 1
r = int(input('% of float rate'))
n = int(input('N'))
PV = int(input('PV'))
FV = int(input('FV'))   #input all the values for calculation
a = PV + (FV/(1+r/100)**n)   #sub into emi formula
b = (r/100)*((1+r/100)**n)
c = ((1+r/100)**n)-1
EMI = a*b/c #calculate emi
print ("EMI is", EMI )












