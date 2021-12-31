# import theater_module
# theater_module.price(3) # 3명이서 영화보러 갔을때 가격
# theater_module.price_morning(4) # 4명이서 조조영화보러 갔을때 가격
# theater_module.price_soldier(5) # 군인 5명이 영화보러 갔을때 가격

# import theater_module as mv # 별명을 통해 줄여서 사용가능
# mv.price(3)
# mv.price_morning
# mv.price_soldier

# from theater_module import * # theater_module 없이 바로 함수 끌어와 사용 가능
# price(3)
# price_morning(3)
# price_morning(3)

# from theater_module import price, price_morning # 명시적으로 특정 함수만 가져올 수 있음
# price(5)
# price_morning(6)

from theater_module import price_soldier as price
price(4)
# price_solider만 가져다 쓰니까 이거를 price로 줄여서 사용하겠다