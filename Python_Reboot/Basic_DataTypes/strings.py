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
# %0数字, 申明这里的'几位数', 没数的地方被'0'填充
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

## String的内置常用方法
print("\n以下为String中的'内置方法'实验: ")
print("sec_a当前的长度为:", len(sec_a)); # 3
print("sec_a.upper()大写:", sec_a.upper()); # AAA
print("sec_a.capitalize()首字母大写:", sec_a.capitalize()); # Aaa
sec_a = "   aaa "
print("修改后的sec_a为%s, .strip()后的结果为%s" % (sec_a, sec_a.strip())); # '   aaa ', 'aaa'
split_symbol = "||";
complex_string = "bibi||lailai||chaochaobei";
print(complex_string.split(sep=split_symbol, maxsplit=-1)); # "有分隔符"字符串 -> 列表

str_list = complex_string.split(sep=split_symbol, maxsplit=-1)
join_result = split_symbol.join(str_list);
print("使用'||'作为主体split(str_list列表)的结果为:",join_result); # 列表 -> 带'分隔符'的字符串

print(complex_string.find("lai")); # 6, 找到了'lai', 首字母l的起始下标为6
print(complex_string.find("le")); # 找不到'le', 返回 -1
# print(complex_string.index("lai")); # 使用和 find()一样, 但是找不到时会抛出ValueError异常
print("complex_string中, 'i'一共出现了%d次" % complex_string.count("i"));
print("complex_string.replace()的结果为:",complex_string.replace("bei","bing"), ""); # 替换并返回"新字符串", 不会对'原字符串'修改操作
print("complex_string仍以bei结尾吗?", complex_string.endswith("bei")); # True
print("complex_string中是字母 或 数字的组合吗",complex_string.isalnum()); # False, 因为包含了特殊符号 '|'