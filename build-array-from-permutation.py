nums = [0,2,1,5,3,4]
# Expected output [0,1,2,4,5,3]

res = []
for i in range(0, len(nums)):
    res.append(nums[nums[i]])
print(res)

