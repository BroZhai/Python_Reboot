import math, random;

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
print("\n以下开始为Number内置函数的实验")
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

# range(起始值, 终止值(不包含), 取值跨度) 直接生成'数字序列'的range对象, 需要手动进一步转成list或其他序列
print(list(range(2,12,3))); # [2,5,8,11]


# math库的各种方法
print("\n以下开始为math库的实验");

# fabs() 也是取绝对值, 但总是返回小数
print("整数-5从fabs()返回的结果为: ", math.fabs(-5)); # -5.0

# ceil() / floor() 往大/小的"整数"取
print("4.5的ceil为", math.ceil(round_value), ", floor为", math.floor(round_value)); # 5 4

# exp(x) 计算指数e的x次幂, 得出的结果为float
print("指数e的0次幂为", math.exp(0)); # 1.0

# log(x, y) 计算'对数', logyX (结果为float), log10(X)则直接以10为底数, 不指定底数时 默认为'e'
print("log以2为底数, 8的对数为",math.log(8,2)); # 3.0

# modf(), 将输入的Number拆成 小数+整数, 返回一个元组, 
print("2.334用modf()拆出来的元组为",math.modf(2.334)); # (0.334000...01, 2.0);

# sqrt(), 计算平方根
print("⑨的平方根为",math.sqrt(9)); # 3


# random随机库实验
print("\以下开始为random库的实验");
print("本次用random()生成的1-10的随机值为:", random.random()*9+1) # random()默认取值范围是[0,1), 和 random.uniform(1,10)类似, 但是uniform()的[左右两边]都可以被取
# num_list = [4,5,1,3,8,0,7];
print("num_list当前的内容:",num_list)
print("从中随机抽出来的值为:", random.choice(num_list));
random.shuffle(num_list);
print("随机打乱后的num_list为",num_list);


