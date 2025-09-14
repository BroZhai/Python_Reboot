# f-string: 即为Python中一种更高级的'模版字符串', 高级在不用'%'了, 用{xxx}直接显示变量 XD (更常用, 和ES6的${}类似)
## 基本使用 f"字符串{xxx变量}..." ==> 字符串 变量"值"(自动转字符串)
name = "baka";
print(f"Hello, my name is {name}"); # Hello, my name is baka
my_friend = {"name":"CyanCandy", "age":26};
print(f"And this is my friend {my_friend['name']}, he is {my_friend['age']}");

## f-string中的'辅助操作符'
#所用的'辅助操作'都是在 {str} 括号内'中'的str后面跟着修饰

# 设置 对齐 & '最小展示位' :对齐符号 数字
sec_a = "a"*5;
sec_b = "b"*4;
sec_c = "c"*8;
print(f"{sec_a:<7}|{sec_b:>6}|{sec_c:>12}"); # a区展示位7, 左对齐; b区展示位6, 右对齐; c区展示位12, 右对齐
print(f"{sec_a:>7}|{sec_b:<6}|{sec_c:<12}"); # 展示位和上面一样, 但是对齐全部都反过来

# 保留小数位 :.数字f
dot_precision = 3; # 保留3位小数
dot_value = 3.1415926;
print(f"{dot_value}手动保留两位小数的结果为: {dot_value:.2f}");
print(f"通过动态传参保留3位的结果为: {dot_value:.{dot_precision}f}"); # 这里{dot_precision} 替换掉了上面的'2'

# 千位分隔符 :,
stink_value = 1145141919810;
print(f"{stink_value:,}")

# 小数转百分比 :%, 用'.数字' 保留指定小数位
progress = 0.7523;
print(f"{progress:%}"); # 75.230000% (有一堆0)
print(f"{progress:.2%}"); # 75.23% (指定保留2位小数)

# 自动显示数字的'正负符号' :+ (:-只会显示负号)
pos_value = 51;
neg_value = -91;
print(f"正数: {pos_value:+}, 负数: {neg_value:+}"); # +51, -91

# 切换数字的'进制表示' :#b binary, :#o octopus, :#x hex
decimal_value = 11;
print(f"整数{decimal_value}对应的十六进制表示形式为: {decimal_value:#x}"); # 0xb