# 准备研究下String
## 研究string的'运算符'
greet_str = "Ciallo~";
print("greet_str取到最后一位前的字符为:", greet_str[0:-1]); # "~"为最后一位, 取不到
print("greet_str的最后一位为:", greet_str[-1]);
morning_str = "G"+"o"*8+"d morning!"; 
print(morning_str);
print("D" in morning_str, "d" in morning_str); # False,True morning_str中并没有"D", 但是有"d" (区分大小写)

## \ 各种转义字符
print("\n各种转义字符实验:")
muliti_line_str = "第一行,\
第二行,\
    前面带一个缩进的第三行,\
最后都会拼成一行owo"; # 注: 每一'行'字符串前面的'空格'都会被保留
print(muliti_line_str);

print("单引号\'双引号\""); # 特殊符号
print("(\a这一行为'系统响铃'测试)"); # 打印此行时电脑响铃, cmd中运行有效
print("我是大啥\b比\b聪明"); # 注: 此行在Vscode等IDE中运行时可能不会生效, 但cmd是没有问题的, 和运行环境有关(和上面print("\a")一样)
print("你知道嘛\n我换行了owo"); # 换行
print("\000"); # 这一行什么东西都没有

print("Name\tAge\tSex");
print("Tekon\t32\tMale");
print("IceWing\t28\tFemale");
print("Kleery\t9\tFemboy")

print("\nHello~\rCia"); # Cialo~
print("八进制Ascii输出: \102\141\153\141"); # Baka
print("十六进制Ascii输出: \x43\x69\x72\x6e\x6f"); # Cirno

## %模版字符串 (这里只实验常用的%s, %d, %f), 用法和C中的printf基本一致
print("\n以下为'模版字符串'的实验");
print("我是 %s, 今年 %d岁, 身高 %.2f 米" % ("Cirno",9,0.99));
dot_precision = 4; # 定义'小数精度' (动态传入)
print("%.*f" % (dot_precision, 3.141592535)); # 保留四位小数舍入, 3.1416
# %0数字, 申明这里的'几位数', 没数的地方为
print("定义'五位数': %05d" % (8)); # 00008
print("定义'五位数': %05d" % (214)); # 00214

# %数字, '预留显示位', 将字符串自己分成不同的'区', 定义每个'区'的大小, 规整输出
sec_a = "aaaaaa"; # 6个a
sec_b = "bbb";
sec_c = "ccccccc";

# sec_a'预留显示位'为5, 靠右对齐(Python默认); 
# sec_b则是6个'字符位', 靠左对齐(%- 实现'左对齐'); 
# sec_c是15个'字符位', 靠右对齐;
print("%5s %-6s | %15s" % (sec_a, sec_b, sec_c)); # 发现有一个'多出来'的a (超'预留显示位'了)
# print(f"{sec_a:>5} {sec_b:<6} - {sec_c:>15}") # f-string也能做, 一会儿开个f-string工程单独实验

sec_a = "aaaaa"; #a区5个字
print("%5s %-6s | %15s" % (sec_a, sec_b, sec_c));

sec_a = "aaa"; #a区3个字, c区变成'靠左对齐'
print("%5s %-6s | %-15s" % (sec_a, sec_b, sec_c));

print("%+d, %+d" % (18, -9)) # %+ 给数字带上正负符号
print("十进制数字%d对应的十六进制数为%#x" % (102, 102));
"""

print("%5.2f" % 3.1415); 

print(f"{17:#b}");

print("i am sussy baka".title())
"""