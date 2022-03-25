from black import out


nums = [1,2,3,4,1,1,1,1,1,1,1,1]
# Expected output: [1,3,6,10]

output =[]
for i in range(0,len(nums)):
    if i == 0:
        output.append(nums[i])
    else: 
        output.append(output[i-1] + nums[i])

print(output)
