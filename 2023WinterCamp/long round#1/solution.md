# A
给定一组数，求有多少个子段异或和等于给定数

# B

##题意：
提供两种操作：
- 删除字符串尾部一个字符
- 增加字符串尾部一个字符

定义d(A,B)表示通过两种操作，将字符串A变成字符串B的操作次数

给定字符串S，求其中两子串，使得d(子串1,子串2)最大

## 题解：

令字符串A为字符串S

找到第一个首字母与S不同的S的后缀，作为B

如果没有，那就n-1即可

## 证明：

记stri表示第i个字符开头的S后缀

若存在一组解stri,strj，那么其首字母必然不同（否则肯定可以更优），那么为什么不选择其中之一与str1作为一组解呢
