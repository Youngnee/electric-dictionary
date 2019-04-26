/*
name: create db
用来建立数据库表结构的语法文件
没有实质性的意义,不用深究用法
*/

-- 创建库
CREATE database elec_dic DEFAULT charset=utf8;

-- 创建用户信息表格
CREATE TABLE user_info(
id INT PRIMARY KEY auto_increment,
name VARCHAR(32) NOT NULL,
passwd VARCHAR(16) DEFAULT "000000"
)DEFAULT charset=utf8;

-- 创建历史记录表格
CREATE TABLE hist(
id INT PRIMARY KEY auto_increment,
name VARCHAR(32) NOT NULL ,
word VARCHAR(32) NOT NULL ,
time VARCHAR(64)
)DEFAULT charset=utf8;

-- 创建单词表
CREATE TABLE words(
id INT PRIMARY KEY auto_increment,
word VARCHAR(32),
mean text,
index(word)
)DEFAULT charset=utf8;



