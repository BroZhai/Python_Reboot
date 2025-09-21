# 看看List 列表
## 创建 & 访问列表
my_list = [1,"a", True, (22,33)]; # 啥元素类型都可以往里面塞
boolean_value = my_list[-2]; # '倒数'第二个元素
first_two_as_subset = my_list[0:2]; # 切片(子list), 取值范围 [0,2)
print(f"my_list倒数第二个元素为{boolean_value}, [0:3]切片的元素为{first_two_as_subset}");

## 列表的'内置方法' (全Python数据类型通用!)
print(f"my_list的长度为:{len(my_list)}");
# print(f"其中的最大值为:{max(my_list)}"); # 使用前提: 数组中的所有元素都是'可比较的值' (如整数)
my_tup = (1,2,3);
tup_to_list = list(my_tup); # 通过list()方法'强转'其他数据(序列)类型 为 List
tup_to_list[0] = 5;
print(f"修改后的tup_to_list中有: {tup_to_list}");

## 列表的'实例方法'
tup_to_list.append(9); # .append()追加元素到列表尾部
print(f"追加了一个新元素至tup_to_list尾部: {tup_to_list}");
another_list = [6,4,5];

tup_to_list.extend(another_list); #.extend()追加'其他序列'到列表尾部
print(f".extend()拼接后的tup_to_list中有: {tup_to_list}") # 5,2,3,9,6,4,5

print(f"其中元素'5'一种出现了{tup_to_list.count(5)}次"); # 2次

tup_to_list.insert(2,1); # .insert(下标, 元素) 在指定下标'前'追加元素, 在 2 3 元素间插个 1
print(f"在'元素3'前插入了元素: {tup_to_list}");

tup_to_list.pop(); # 移去最后一个元素
print(f"pop默认移除了最后一个元素: {tup_to_list}"); # 5 被移除了
tup_to_list.pop(-3); # 移去'倒数第三个'元素
print(f"又移除了倒数第三个元素: {tup_to_list}") # 9 被移除了

tup_to_list.remove(1); # .remove()移除'首个出现'的对应元素
print(f"移除了首次出现的'元素1': {tup_to_list}");

tup_to_list.sort(); # .sort()排序, 默认升序, 使用reverse=True降序
print(f"sort()后的升序tup_to_list: {tup_to_list}");
tup_to_list.sort(reverse=True);
print(f"reverse=True降序: {tup_to_list}")

tup_to_list.clear();
print(f"使用.clear()对tup_to_list的所有内容进行了清空: {tup_to_list}")

origin_list = [1,2,[3,4]];
copied_list = origin_list.copy(); # 创建一个元素的'浅拷贝'
# Python中的'浅拷贝'逻辑: 顶层(第一层数据)独立, 嵌套(第二层+数据)共享
print(f"现有origin_list:{origin_list}, 复制的copied_list:{copied_list}");
copied_list[0] = 5; # 只会修改copied_list中的值 (顶层元素)
copied_list[2][1] = 9; # copied_list 和 origin_list 都会被修改, 因为该元素是一个'嵌套元素'(共享)
print(f"修改copied_list中的第一个元素: {copied_list}, origin_list的内容: {origin_list}");
