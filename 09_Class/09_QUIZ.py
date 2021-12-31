class House:
    #매물 초기화
    def __init__(self,location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
    #매물 정보 표시
    def show_detail(self):
        print( self.location, self.house_type, self.deal_type ,self.price, self.completion_year)   
        pass
    
House1 = House('강남','아파트','매매','10억','2010년')
House2 = House('마포','오피스텔','전세','5억','2007년')
House3 = House('송파','빌라','월세','500/50','2000년')

House_list = []
House_list.append(House1)
House_list.append(House2)
House_list.append(House3)

print('매물은 총 {0} 개 입니다.'.format(len(House_list)))
for house in House_list:
    house.show_detail() # house번째 요소의 클래스 내부의 show_detail을 가져옴
    