# import travel.thailand # Module이나 package만 바로 import가능
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()


# from travel.thailand import ThailandPackage # from import 구문에서는 클래스, 함수 import 가능
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# __all__
from travel import * 
# # *을 쓴다는 것은 모든것을 쓰겠다는거
# # 근데 범위를 설정 해 줘야함 
# trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

import inspect
import random
print(inspect.getfile(random)) # random이라는 묘듈이 어디 있는지 파일 정보를 알려줌
print(inspect.getfile(thailand))