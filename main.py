cube_list = [x**3 for x in range(100,10000) # 1-е задание
             if x % 3 == 0 and x % 7 == 0
             and str(x)[-1] != '3'
             and str(x)[-1] != '7']
print(cube_list)



