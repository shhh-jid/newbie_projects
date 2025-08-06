def Calculator(x, o , y):
    if o == "+": return x+y
    if o == "-": return x-y
    if o == "x": return x*y
    if o == "/": return x/y
    if o == "//": return x//y #floor op
    if o == "%": return x%y #mod op

x = int(input("Enter first number: "))
o = input("Enter operation: +  -  x  /  //  % : ")
y = int(input("Enter second number: "))

print(f" ___ Answer: {Calculator(x,o,y)} ___")