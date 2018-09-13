
from random import randint
from decimal import *

""" Settings """
Bankroll     = "0.00033300$"
Starting_Bet = "0.00000002$"

Bets = "5184000"
Win_Chance = "49.5%"

Multiply_On_Lose = 2
Multiply_On_Win = 1




# Chance of winning calculation
Errors = []


def RaiseErrors():
    index = 0
    for item in Errors:
        index += 1


class Simulator:
    def __init__(self):
        self.FWinChance = float(Win_Chance.replace("%", ""))

    def Win_Chance(self):

        if self.FWinChance > 100:
            Errors.append("Error: Win chance cannot exeed 100%")
            return

        else:

            PWinChance = self.FWinChance * 10
            DWinChance = 1000 - PWinChance
            Data = [PWinChance, DWinChance]
            return (Data)

    def Roll(self):
        Numbers = 1000
        Current_Bet = 0

        Profit = 0
        Loss_Streak_total = 0
        Loss_Streak = 0
        Win_Streak = 0

        Starting_Bet_Amount = float(Starting_Bet.replace("$", ""))
        Bankroll_Amount = float(Bankroll.replace("$", ""))
        while Current_Bet < int(Bets):

            Result = randint(1, Numbers)
            if Result > Simulator.Win_Chance()[0]:
                # Loss
                Bankroll_Amount -= Starting_Bet_Amount
                Win_Streak = 0
                Loss_Streak += 1
                if Loss_Streak > Loss_Streak_total:
                    Loss_Streak_total = Loss_Streak


                if Bankroll_Amount - float(Bankroll.replace("$", "")) > 0:
                    Profit = "+%s" % format(Bankroll_Amount - float(Bankroll.replace("$", "")), '.8f')

                else:
                    Profit = "%s" % format(Bankroll_Amount - float(Bankroll.replace("$", "")), '.8f')

                print(
                    "Bankroll: %s    |     L/W: %s    |     Current Bet: %s$    |     Next Bet: %s$    |     Profit: %s    |     WS: %s    |     LS: %s" % (
                        str(Decimal(Bankroll_Amount))[:10], "Loss",
                        "%s" % format(Starting_Bet_Amount, ".8f"),
                        format(Starting_Bet_Amount * float(Multiply_On_Lose), ".8f"), Profit, Win_Streak,
                        Loss_Streak))

                Starting_Bet_Amount *= float(Multiply_On_Lose)

                if Bankroll_Amount <= 0:
                    print("Simulator stopped: You have no money")
                    return


            else:
                # Win
                Bankroll_Amount += Starting_Bet_Amount * float(99.0 / Simulator.FWinChance)
                Win_Streak += 1
                Loss_Streak = 0

                if Bankroll_Amount - float(Bankroll.replace("$", "")) > 0:
                    Profit = "+%s" % format(Bankroll_Amount - float(Bankroll.replace("$", "")), '.8f')

                else:
                    Profit = "%s" % format(Bankroll_Amount - float(Bankroll.replace("$", "")), '.8f')

                print(
                    "Bankroll: %s    |     L/W: %s    |     Current Bet: %s$    |     Next Bet: %s$    |     Profit: %s    |     WS: %s    |     LS: %s" % (
                        str(Decimal(Bankroll_Amount))[:10], "Win ","%s" % format(Starting_Bet_Amount, ".8f"),
                        format((float(Starting_Bet.replace("$", ""))), '.8f'), Profit, Win_Streak, Loss_Streak))

                Starting_Bet_Amount = float(Starting_Bet.replace("$", ""))

            Current_Bet += 1
        else:
            print("Highest lose streak: %i" % (Loss_Streak_total))


Simulator = Simulator()
""" Simulation """

Simulator.Roll()
