count=0
for numbers in range(2000,3200):
    if numbers % 7 ==0 and numbers % 5!= 0:
        print(str(numbers)+',')
        count=count+1
print(count)

