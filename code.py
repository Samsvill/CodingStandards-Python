class Myclass:
    def __init__(self):
        self.my_fav = {'Paris': 500, 'NYC': 600}
    
    def get_extra_cost(self, dest):
        return self.my_fav.get(dest, 0)
    
    def valid_this(self, dest):
        return isinstance(dest, str)

class Passenger:
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
        self.myclass = Myclass()
        self.passenger = Passenger(num)
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

class TotalTime:
    def __init__(self, dur):
        self.dur = dur

    def is_valid_total_time(self):
        return isinstance(self.dur, int) and self.dur > 0

    def get_fee(self):
        return 200 if self.dur < 7 else 0

    def get_the_best_promo_ever(self):
        return 200 if self.dur > 30 else 0
    
    def get_weekend(self):
        return 100 if self.dur > 7 else 0
    

class Vacation:
    cost_base = 1000

    def __init__(self, dest, num, dur):
        self.myclass = Myclass()
        self.passenger = Passenger(num)
        self.total_time = TotalTime(dur)
        self.dest = dest

    def sum(self):
        
        if not self.myclass.valid_this(self.dest) or not self.passenger.validnumber() or not self.total_time.is_valid_total_time():
            return -1
        
        number_total = self.cost_base
        number_total += self.myclass.get_extra_cost(self.dest)
        number_total += self.total_time.get_fee()
        number_total -= self.total_time.get_the_best_promo_ever() | self.passenger.promotion_policy_passenger()

        discount = self.passenger.for_here_discount()
        number_total = number_total - (number_total * discount)
        
        return max(int(number_total), 0)


def main():
   
    dest = "Paris"
    num = 2
    dur = 31

    calculator = Vacation(dest, num, dur)
    cost = calculator.sum()

    if cost == -1:
        print("Invalid input.")
    else:
        print(f"The total cost of the vacation package is: ${cost}")

#main event function
if __name__ == "__main__":
    main()
