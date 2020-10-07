counts = dict()
names = ['csew', 'cwen', 'csew', 'zqian','cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name]+=1
print(counts)
