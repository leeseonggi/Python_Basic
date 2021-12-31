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
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year) # self. 변수들은 self.으로 클래스 내에서 받아감
    
    
houses = []
house1 = House('강남','아파트','매매','10억','2010년')
house2 = House('마포','오피스텔','전세','5억','2007년')
house3 = House('송파','빌라','월세','500/50','2000년')
houses.append(house1)
houses.append(house2)
houses.append(house3)

print('총 {0}매의 매물이 있습니다.'.format(len(houses)))
for house in houses:
    house.show_detail() 
    # 출력할때 House 클래스에 show_detail을 불러옴
    # i를 i말고 house로 보기 쉽게 해서
    # 배열 첫번째부터 하나하나 반복문 들어가고
    # House클래스 형태로 하나하나 저장되었있다 - 내부 __init__함수 부분과  show_detail함수 부분
    # 따라서 show_detail부분만 반복문으로 하나하나 찍으면은
    # show_detail 내부의 print함수에 따라 저장된 매물 정보다 출력됨