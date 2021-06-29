def get_weapon(w_name):
    w = "%s을(를) 획득했습니다" % w_name
    return w

print(get_weapon("도끼"))
print(get_weapon("지팡이"))
print(get_weapon("단검"))