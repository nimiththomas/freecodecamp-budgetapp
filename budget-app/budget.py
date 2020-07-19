class Category:


    def __init__(self,name):
        self.name=name
        self.ledger=list()
    def check_funds(self,amount):
        fund=0
        n=len(self.ledger)
        for i in range(n):
            fund=fund+self.ledger[i]["amount"]
        if fund<amount:
            return False
        else:
            return True
    def deposit(self,amount,description=""):
        #initialising a dictionary
        self.dep=dict()
        #adding the amount and description to dictionary
        self.dep["amount"]=amount
        self.dep["description"]=description
        #adding the deposit to ledger list
        self.ledger.append(self.dep)

    def withdraw(self,amount,description=""):
        #checking if total amount less than or greaten than amount to be withdrawn
        l=self.check_funds(amount)

        if(l==True):
            self.withd=dict()
            self.withd["amount"]=-(amount)
            self.withd["description"]=description
            self.ledger.append(self.withd)
            return True
        else:
            return False
    def get_balance(self):
        fund=0
        n=len(item.ledger)
        #retrieving the total fund in ledger
        for i in range(n):
            fund=fund+item.ledger[i]["amount"]
        return fund
    def transfer(self,amount,obname):
        objectname=obname.name
        a=self.withdraw(amount,f"Transfer to {objectname}")
        b=obname.deposit(amount,f"Transfer from {self.name}")
        if(a==True):
            return True
        else:
            return False
    def check_funds(self,amount):
        fund=0
        n=len(self.ledger)
        for i in range(n):
            fund=fund+self.ledger[i]["amount"]
        if fund<amount:
            return False
        else:
            return True
    def __str__(self):
         output = self.name.center(30, "*") + "\n"
         for item in self.ledger:
             output += f"{item['description'][:23].ljust(23)}{format(item['amount'], '.2f').rjust(7)}\n"
         output += f"Total: {format(self.get_balance(), '.2f')}"
         return output

def create_spend_chart(categories):
  category_names = []
  spent = []
  spent_percentages = []

  for category in categories:
    total = 0
    for item in category.ledger:
      if item['amount'] < 0:
        total -= item['amount']
    spent.append(round(total, 2))
    category_names.append(category.name)

  for amount in spent:
    spent_percentages.append(round(amount / sum(spent), 2)*100)

  graph = "Percentage spent by category\n"

  values = range(100, -10, -10)

  for value in values:
    graph += str(value).rjust(3) + "| "
    for percent in spent_percentages:
      if percent >= value:
        graph += "o  "
      else:
        graph += "   "
    graph += "\n"

  graph += "    ----" + ("---" * (len(category_names) - 1))
  graph += "\n     "

  longest_name_length = 0

  for name in category_names:
    if longest_name_length < len(name):
      longest_name_length = len(name)

  for i in range(longest_name_length):
    for name in category_names:
      if len(name) > i:
        graph += name[i] + "  "
      else:
        graph += "   "
    if i < longest_name_length-1:
      graph += "\n     "



  return(graph)
