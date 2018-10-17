class ParkingSpace():   #停车位
    ps_sum_total = 0    #停车位总个数
    def __init__(self,ps_number,ps_price):
        self.ps_number = ps_number
        self.ps_price = ps_price
        ParkingSpace.ps_sum_total += 1

ps001 = ParkingSpace('001',5)
ps002 = ParkingSpace('002',5)
ps003 = ParkingSpace('003',5)
psvip004 = ParkingSpace('004',10)
psvip005 = ParkingSpace('005',10)
