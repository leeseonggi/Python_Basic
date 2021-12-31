class ThailandPackage:
    def detail(self):
        print('[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원')
        
if __name__ =='__main__': # name이 메인이면 thailand Module 안에서 직접 실행 될떄
    print('Thailand 모듈을 직접 실행')
    print('이 문장은 모듈을 직접 실행 할 때에만 실행됨')
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print('Thailand 외부에서 모듈 호출')