class SavingAccount():...

class CheckingAccount():...

class BankAccount(SavingAccount,CheckingAccount):...
class Stock():...
class Bond():...
class Security(Bond,Stock):...
class InterestBearingitem(BankAccount,Security):...
class RealEstate():...
class Asset(BankAccount,RealEstate):...

class Insurableltem(BankAccount,RealEstate):...





