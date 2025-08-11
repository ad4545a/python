latter='''Dear <|NAME|>,
Your are selected!

Date: <|DATE|>'''
a=input("enter your name:- ")
b=input("enetr the date:- ")
latter=latter.replace("<|NAME|>",a)
latter=latter.replace("<|DATE|>",b)
print(latter)