class myclass:
    def __init__(self):
        self.my_fav = {'Paris': 500, 'NYC': 600}
    
    def get_extra_cost(self, dest):
        return self.my_fav.get(dest, 0)
    
    def valid_this(self, dest):
        return isinstance(dest, str)

class passenger:
    def __init__(self, num):
        self.num = num
    
    def validnumber(self):
        print("this working here")
        return isinstance(self.num, int) and self.num > 0 and self.num <= 80

    def for_here_discount(self):
        if 4 < self.num < 10:
            return 0.1
        elif self.num >= 10:
            return 0.2
        elif self.num >= 20:
            return 0.25
        elif self.num >= 30:
            return 0.3
        else:
            return 0.0
    def promotion_policy_passenger (self):
        return 200 if self.num == 2 else 0.0

class Plane:
    def __init__(self, dest, num, dur):
        self.myclass = myclass()
        self.passenger = passenger(num)
        self.total_time = TotalTime(dur)
        self.dest = dest
        self.seats = 200

    def sum(self):
        if not self.myclass.validThis(self.dest) or not self.passenger.validnumber() or not self.total_time.is_valid_total_time():
            return -1

        number_total = self.cost_base
        number_total += self.myclass.get_extra_cost(self.dest)
        number_total += self.total_time.get_fee()
        number_total -= self.total_time.get_the_best_promo_ever()

        discount = self.passenger.for_here_discount()
        number_total = number_total - (number_total * discount)
        
        return max(int(number_total), 0)

