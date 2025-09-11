# 准备研究下String
print("%05d" % 14);

sec_a = "aaaaaa"; # 6个a
sec_b = "bbb";
sec_c = "ccccccc";
# sec_a'预留显示位'为5, 靠右对齐; sec_b则是6个'字符位', 靠左对齐; sec_c是15个'字符位', 靠右对齐
print("%5s %-6s - %15s" % (sec_a, sec_b, sec_c));
# print(f"{sec_a:>5} {sec_b:<6} - {sec_c:>15}") # 发现有一个'多出来'的a (超'预留显示位'了)

sec_a = "aaaaa";
# print(f"{sec_a:>5} {sec_b:<6} - {sec_c:>15}")
print("%5s %-6s - %15s" % (sec_a, sec_b, sec_c));

sec_a = "aaa";
# print(f"{sec_a:>5} {sec_b:<6} - {sec_c:>15}")
print("%5s %-6s - %15s" % (sec_a, sec_b, sec_c));