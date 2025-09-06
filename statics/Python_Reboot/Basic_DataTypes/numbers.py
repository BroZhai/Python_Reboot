a, b, c, d = 4, 6.2, False, 4+3j; # 直接给多个变量'依次赋值'
print(type(a), type(b), type(c), type(d));
# a的类型 <class'int'>, b <class'float>, c <class'bool'>, d <class'complex'>

print(isinstance(a, int)); # 判断 变量a 是否为 int类, 返回True
print(a is b); # 比较 a, b 两者的'对象类型', False

del a; # 删除a变量(引用/赋值) 的数据

print(10 / 4); # 返回 2.5
print(10 // 4); # 返回整数2

# 各种'进制数'的表示
binary_num = 0b1010; #二进制
octopus_num = 0o12; #八进制
hex_num = 0xa; # 十六进制
print(binary_num, octopus_num, hex_num); # 10 10 10
print(7%2)
