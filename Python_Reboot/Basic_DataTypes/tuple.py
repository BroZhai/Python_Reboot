# 研究一下'元组' (即是'不可修改'的'列表')

## 创建一个元组
tekon_tuple = ("tekon",27,True,["IceWing", "CyanCandy"]); # 直接用()声明, 不同元素用','隔开; 元组中的数据类型'能混着存'

## 访问元组 (即支持下标 + 运算访问, 又支持'解构赋值'访问, 和ES6一样)
# 使用下标 + 运算 访问
extracted_name = tekon_tuple[0];
extracted_name_and_age = tekon_tuple[0:2]; # 取值范围[0,2), 返回一个'子元组'
print(f"下标0取得的值为: {extracted_name}, 类型为{type(extracted_name)}"); # tekon, <class 'str'>
print(f"下标0取到2前面的值为: {extracted_name_and_age}, 类型为{type(extracted_name_and_age)}"); # ("tekon", 27), <class 'tuple'>, 返回的是一个'子元组'

# 使用'解构赋值'
name, age, isMale, friend_list = tekon_tuple;
print(f"使用'结构赋值'取得的信息:\n \
    姓名: {name}\n \
    年龄: {age}\n \
    是B♂y吗: {isMale}\n \
    朋友列表: {friend_list}");

## 合并元组 (直接用+运算即可)
num_tuple = (1,2);
letter_tuple = ('a','b');
mix_tuple = num_tuple + letter_tuple;
print(f"混合的mix_tuple为:{mix_tuple}");

## 元组的一些内置方法
print(f"mix_tuple的长度为{len(mix_tuple)}"); # 4
print(f"其中最大的元素为{max(mix_tuple)}, 最小的元素为{min(tuple)}"); # 2, 1
