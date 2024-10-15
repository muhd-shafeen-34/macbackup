def common(lis,dis):
    for i in lis:
        for j in dis:
            if i == j:
                return True
                break
lis = [10,20,30,40]
dis = [60,70,80,10]
l = common(lis,dis)
print(l)

