def ride_bus(bus, user):
    # 버스가 만석인지 확인합니다.
    # 버스가 만석이라면 함수를 종료하고, 그렇지 않다면 유저가 해당 버스에 탑승합니다.
    if bus.is_gull():
        return
    user.get_on(bus)

    ADULT_AGE = 19
    CHILD_FEE = 800
    ADULT_FEE = 1300
    THE_ELDELY_AGE = 65
    # 탑승해서 나의 나이에 맞게 사용요금을 냅니다.
    if user.age < ADULT_AGE:
        user.pay(CHILD_FEE)
    elif user.age > THE_ELDELY_AGE:
        pass
    else:
        user.pay(ADULT_FEE)

    # 만약 버스의 현재 위치가 내가 내리고 싶은 종착지라면 하차합니다.
    if bus.location == user.dstination:
        user.get_off(bus)
