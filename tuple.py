things='pen','kolom','kata','bed','boi','bow'
print(things)
print(things[2])
print(things[3:6])


if 'pen' in things:
    print('yes')
for item in things:
    print(item)
print(len(things))
#tuple ke dairwk change kora jai nah kinto
mega=([2,3,4],[6,7,8,9])
mega[0][1]=232
print(mega)