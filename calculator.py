
import math
from datetime import datetime
from history import History

class Calculator:
    def __init__(self):
        self.history = History()
        self.memory = 0.0
        self.count = 0

    def log(self, text):
        self.history.add(text)
        self.count += 1

    def run(self):
        while True:
            print("\n===== ADVANCED SCIENTIFIC CALCULATOR =====")
            print("1.Add 2.Subtract 3.Multiply 4.Divide")
            print("5.Power 6.Sqrt 7.Sin 8.Cos")
            print("9.Tan 10.Log10 11.Factorial")
            print("12.Memory Recall 13.Show History 0.Exit")
            ch = input("Choice: ")

            try:
                if ch == "0":
                    print(f"Operations this session: {self.count}")
                    break
                elif ch in ("1","2","3","4","5"):
                    a=float(input("First: "))
                    b=float(input("Second: "))
                    if ch=="1": r=a+b; op="+"
                    elif ch=="2": r=a-b; op="-"
                    elif ch=="3": r=a*b; op="*"
                    elif ch=="4":
                        if b==0:
                            print("Division by zero!")
                            continue
                        r=a/b; op="/"
                    else:
                        r=a**b; op="^"
                    print("Result:",r)
                    self.memory=r
                    self.log(f"{datetime.now()} : {a} {op} {b} = {r}")
                elif ch=="6":
                    x=float(input("Number: "))
                    if x<0:
                        print("Cannot sqrt negative.")
                        continue
                    r=math.sqrt(x)
                    print(r)
                    self.memory=r
                    self.log(f"sqrt({x})={r}")
                elif ch=="7":
                    x=float(input("Angle: "))
                    r=math.sin(math.radians(x))
                    print(r)
                    self.memory=r
                    self.log(f"sin({x})={r}")
                elif ch=="8":
                    x=float(input("Angle: "))
                    r=math.cos(math.radians(x))
                    print(r)
                    self.memory=r
                    self.log(f"cos({x})={r}")
                elif ch=="9":
                    x=float(input("Angle: "))
                    r=math.tan(math.radians(x))
                    print(r)
                    self.memory=r
                    self.log(f"tan({x})={r}")
                elif ch=="10":
                    x=float(input("Positive number: "))
                    if x<=0:
                        print("Must be positive.")
                        continue
                    r=math.log10(x)
                    print(r)
                    self.memory=r
                    self.log(f"log10({x})={r}")
                elif ch=="11":
                    x=int(input("Integer: "))
                    if x<0:
                        print("Must be non-negative.")
                        continue
                    r=math.factorial(x)
                    print(r)
                    self.memory=r
                    self.log(f"{x}!={r}")
                elif ch=="12":
                    print("Memory =", self.memory)
                elif ch=="13":
                    self.history.show()
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Invalid numeric input.")
