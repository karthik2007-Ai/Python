
nums=[1,2,3,4,56,6,7,8,9,9,99,88,76,54,34,67,32,12,90]
name=["Karthik","Musk","metla","udbhav","sai","karthik"]
z=list(zip(nums,name))
print(z)

nums.append(2)
print(nums)

nums.extend([2,4,5,6])
print(nums)

nums.extend(name)
print(nums)

nums.pop()
print(nums)

nums.pop(1)
print(nums)

nums.remove(1)
print(nums)

nums.reverse()
print(nums)

nums=[1,2,3,4]
nums.sort()
print(nums)

nums.sort(reverse = True)
print(nums)

name=["karthik","metla","udbhav","sai","karthik"]
name.sort()
print(name)

name.sort(reverse = True)
print(name)

name.sort(key = str.lower)
print(name)

nums.index(1)
print(nums)

name.insert(2,"saran")
print(name)

z=name.copy()
print(z)