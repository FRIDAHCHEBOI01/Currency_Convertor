# Convert ksh to ghc and vice versa
# Convert ksh to dollars and vice verse
# Convert ghc to dollars

def ghana_to_dollar(x):
    return x/14.99
def dollar_to_ghana(x):
    return x*14.99
def ksh_to_dollar(x):
    return x/122.10
def dollar_to_ksh(x):
    return x*122.10
def ghana_to_ksh(x):
    return x*8.72
def ksh_to_ghana(x):
    return x/8.72

currency1 = input("Please enter currency to be convert(usd, ghc, ksh)")
currency2 = input("Please enter the currency you want results for:) (usd,ghc, ksh)")

if currency1 in ['usd','ksh','ghc']:
    amount = int(input("Please enter amount to be converted"))
    if currency1 == "ghc" and currency2 == "usd":
        print("Dollar equivalent for your money is {}".format(ghana_to_dollar(amount)))
    if currency1 == "ghc" and currency2 == "ksh":
        print("KSH equivalent for your money is {}".format(ghana_to_ksh(amount)))
    if currency1 == "usd" and currency2 == "ksh":
        print("KSH equivalent for your money is {}".format(dollar_to_ksh(amount)))
    if currency1 == "ksh" and currency2 == "ghc":
        print("Cedis equivalent for your money is {}".format(ksh_to_ghana(amount)))
    if currency1 == "usd" and currency2 == "ghc":
        print("Cedis equivalent for your money is {}".format(dollar_to_ghana(amount)))
    if currency1 == "ksh" and currency2 == "usd":
        print("Dollar equivalent for your money is {}".format(ksh_to_dollar(amount)))
else:
    print('''
    Invalid entry babe : )
    Let's try that again!
    Yeeeh !)
          ''')
    
    
    
    
