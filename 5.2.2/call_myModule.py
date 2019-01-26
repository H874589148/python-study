import myModule

print("count =",myModule.func())
myModule.count = 10
print("count =",myModule.count)
import myModule
print("count =",myModule.func())