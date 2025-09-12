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


"""
print("%05d" % 14);

sec_a = "aaaaaa"; # 6个a
sec_b = "bbb";
sec_c = "ccccccc";

# sec_a'预留显示位'为5, 靠右对齐; 
# sec_b则是6个'字符位', 靠左对齐; 
# sec_c是15个'字符位', 靠右对齐;
print("%5s %-6s - %15s" % (sec_a, sec_b, sec_c));
# print(f"{sec_a:>5} {sec_b:<6} - {sec_c:>15}") # 发现有一个'多出来'的a (超'预留显示位'了)

sec_a = "aaaaa";
# print(f"{sec_a:>5} {sec_b:<6} - {sec_c:>15}")
print("%5s %-6s - %15s" % (sec_a, sec_b, sec_c));

sec_a = "aaa";
# print(f"{sec_a:>5} {sec_b:<6} - {sec_c:>15}")
print("%5s %-6s - %15s" % (sec_a, sec_b, sec_c));

print("%5.2f" % 3.1415); 

print(f"{17:#b}");

print("i am sussy baka".title())
"""