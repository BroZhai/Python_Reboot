# 在Python中, 字典就是用来存'键值对'的, 每一对'键值对映射'在Python中叫一个'项'

## 创建 & 访问字典
my_dictionary = {"name":"Tekon", "age": 29, "isMale": True, "friends":["IceWings","VVokos","Cirno"]}; # Tips:'键名'需要是一个'不可变的对象', 如各种'字面量'(字符串, 数值等)
my_name = my_dictionary["name"];
my_friends = my_dictionary["friends"];
print(f"你好, 我是{my_name}, 我的朋友有: {my_friends}");
my_dictionary["age"] = 39; # 修改字典中的'项'
print(f"目前{my_dictionary['age']}");

## 清除'项' / 删除字典
del my_dictionary["friends"];
# print(f"我的朋友现在有: {my_dictionary['friends']}"); # 抛出KeyError异常, 因为 "friends"键已经被删掉了(不存在)
# # Tips： 双引号中不能还有其他的"双引号", 建议使用'单引号'
my_dictionary.clear(); # 清空所有的'项'
print(f"使用.clear()方法清空了my_dictionary中的所有项: {my_dictionary}, 但是'该对象'仍然存在");
# del my_dictionary; # 直接删除'my_dictionary'对象 (变量不再可用)

## 字典的'内置方法' (其实也是全Python万用的 XD)
print("\n以下为字典'内置方法'的实验区");
my_dictionary = {"name":"Tekon", "age": 29, "isMale": True, "friends":["IceWings","VVokos","Cirno"]};
print(f"重新赋值后的my_dictionary中共有{len(my_dictionary)}个'项'(键值对)"); # len(对象), 查看对象的'长度'
print(f"以字符串的形式进行输出: {str(my_dictionary)}"); # str(对象), 相当于Java 所有Object的toString()
print(f"my_dictionary的类型为: {type(my_dictionary)}"); # type(对象), 相当于Java 反射中的 object的.getClass()

## 字典的'实例方法' (这个就是'字典对象'才能用的了)
print("\n以下为字典的'实例方法'实验区");
# 浅拷贝 .copy()
copied_dic = my_dictionary.copy(); # 创建一个'浅拷贝'字典 (这里的'浅拷贝'逻辑 和 list是一样的, 或者说, 所有Python的'浅拷贝'都是 "顶层独立, 嵌套共享" 这一套逻辑)
copied_dic['name'] = "YellowCake"; 
copied_dic['friends'][0] = "RedCake";
print(f"通过.copy()创建了一个浅拷贝'copied_dic', 并对其中的'name' 和 'friends'进行了修改");
print(f"copied_dictionary当前的内容: {copied_dic}");
print(f"此时my_dictionary中的内容: {my_dictionary}"); # 只有 copied_dic的'name'发生了变动, 但是这两个字典的'friend'列表(嵌套元素)都变了

# 取值 .get('键名', 默认返回值) /设值 .setDefault('键名', 默认返回值) /设置'默认值' / 移除值 .pop('键名', 默认返回值)
print(my_dictionary.get("isSingle", "isSingle键不存在!"));
my_dictionary.setdefault("isSingle", "Default_Single Value"); # 注: setdefault()在'键存在'时返回'已有的键值', 不存在时则返回'默认的设置的值'(Default_Single Value)
print(my_dictionary.get("isSingle", "isSingle键不存在!"));
print(my_dictionary);
my_dictionary.pop("isSingle");
print(f".pop()移除了'isSingle'键: {my_dictionary}");
print(f"'isSingle'项现在还在my_dictionary中吗? {'isSingle' in my_dictionary}"); # False

# 将字典返回成一个'视图'views .items(), 之后进一步了解'视图'是个什么东西, 这里先直接将其转成list即可
returned_view = my_dictionary.items();
converted_list = list(returned_view);
print(f"\n用.item()取得'视图'后手动转成的list为: {converted_list}"); 
# .keys() 和 .values() 分别返回 '纯键名' 和 '纯键值'的'视图'
keynames_view = my_dictionary.keys();
values_view = my_dictionary.values();
print(f"纯键名视图: {keynames_view}, 纯键值视图: {values_view}");

# '合并'字典 .update(字典对象)
dic_a = {"name":"IceWing", "Band": "Ave_Mujica"};
dic_b = {"Band": "CRY_SHIC", "Position": "主唱这招太狠了"};
print(f"\n\
dic_a: {dic_a} \n\
dic_b: {dic_b}");
dic_a.update(dic_b);
print(f"dic_a.update(dic_b)的结果为: {dic_a}"); # 若存在同样的键, 新的键值将会覆盖原来的(Band), 若不存在, 直接追加 (Position)