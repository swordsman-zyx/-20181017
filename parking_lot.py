from parking_record import pr1
from parking_space import *
class ParkingLot():
    def __init__(self,pl_carport_num,pl_address,
                pl_name,pl_free_carport,pl_record_class):
        self.pl_carport_num = pl_carport_num
        self.pl_address = pl_address
        self.pl_name = pl_name
        self.pl_free_carport = pl_free_carport
        self.pl_record_class = pl_record_class
    def countFreeCarportleave(self):
        pl_carrefour.pl_free_carport +=1
    def countFreeCarportenter(self):
        pl_carrefour.pl_free_carport -=1

pl_carrefour = ParkingLot(ParkingSpace.ps_sum_total,
                '家乐福地下停车场','家乐福停车场',5,pr1)
pl_tesco = ParkingLot(ParkingSpace.ps_sum_total,
                '乐购地下停车场','乐购停车场',5,pr1)
