import math

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

# 不同Number类之间的转换
float_value = 11.4;
int_value = int(float_value);
print("int_value取得的值为:", int_value);

# Number内置函数
# abs()取绝对值, 返回的数据类型 与 输入的一致
neg_value = -5.5;
print("abs取到的值为: ", abs(neg_value));

# round() 四舍五入
round_value = 4.5;
print("4.5的round四舍五入的值为: ", round(round_value));

# max() / min() 取最大/最小值, 输入可以使一个 序列, 列表, 字典等...
num_list = [4,5,1,3,8,0,7]; # max 8 , min 0
print("num_list中最小的值为", min(num_list), ",最大的值为", max(num_list));

# pow() 算指定次幂
print(pow(2, 4)); # 16