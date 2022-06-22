/*
Navicat MySQL Data Transfer

Source Server         : piao
Source Server Version : 80003
Source Host           : localhost:3306
Source Database       : library

Target Server Type    : MYSQL
Target Server Version : 80003
File Encoding         : 65001

Date: 2022-06-13 10:33:56
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `book`
-- ----------------------------
DROP TABLE IF EXISTS `book`;
CREATE TABLE `book` (
  `id` bigint(4) DEFAULT NULL,
  `name` varchar(20) NOT NULL,
  `number` varchar(8) DEFAULT NULL,
  `author` varchar(20) DEFAULT NULL,
  `publicationdate` date DEFAULT NULL,
  `isborrow` int(4) DEFAULT NULL,
  `remark` varchar(50) DEFAULT NULL,
  `location` varchar(20) DEFAULT NULL,
  `borrowname` varchar(20) DEFAULT NULL,
  `borrowtime` date DEFAULT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='press 出版社';

-- ----------------------------
-- Records of book
-- ----------------------------
INSERT INTO `book` VALUES (null, 'Android基础', 'b019', '未知', '2019-02-05', '1', '暂无描述', '图书馆', '张三', '2022-06-06');
INSERT INTO `book` VALUES (null, 'c++基础', 'b020', '未知', '2015-02-01', '0', '暂无描述', '图书馆', null, null);
INSERT INTO `book` VALUES (null, 'javaweb', 'b018', '未知', '2017-01-04', '0', '暂无描述', '图书馆', null, null);
INSERT INTO `book` VALUES (null, 'java基础入门', 'b016', '未知', '2017-01-01', '0', '该书讲述', '图书馆', null, null);
INSERT INTO `book` VALUES (null, 'php基础', 'b021', '未知', '2010-02-01', '0', '暂无描述', '图书馆', null, null);
INSERT INTO `book` VALUES (null, 'python基础入门', 'b017', '未知', '2019-06-01', '1', '暂无描述', '图书馆', '李四', '2022-06-08');
INSERT INTO `book` VALUES (null, '人类简史', 'b005', '尤瓦尔·赫拉利 ', '2014-11-01', '0', '暂无描述', '图书馆', null, null);
INSERT INTO `book` VALUES ('23', '控方证人', 'b011', '阿加莎·克里斯蒂 ', '2017-05-01', '0', null, '图书馆', null, null);
INSERT INTO `book` VALUES (null, '操作系统', 'b001', '未知', '2022-01-09', '1', '暂无描述', '图书馆', '张三', '2022-05-18');
INSERT INTO `book` VALUES (null, '数据库系统概述', 'b009', '王珊', '2016-01-01', '0', '暂无描述', '图书馆', null, null);
INSERT INTO `book` VALUES (null, '数据结构', 'b002', '未知', '2007-04-03', '0', '暂无描述', '图书馆', null, null);
INSERT INTO `book` VALUES (null, '明朝那些事儿', 'b006', '未知', '2009-04-06', '1', '暂无描述', '图书馆', '王五', '2022-06-01');
INSERT INTO `book` VALUES (null, '机器学习实战', 'b004', '张三', '2019-06-30', '0', '暂无描述', '图书馆', null, null);
INSERT INTO `book` VALUES (null, '离散数学', 'b013', '未知', '2003-01-01', '0', '暂无描述', '图书馆', null, null);
INSERT INTO `book` VALUES (null, '第一行代码', 'b008', '郭霖', '2017-04-01', '0', '暂无描述', '图书馆', null, null);
INSERT INTO `book` VALUES (null, '解忧杂货店', 'b015', '东野圭吾', '2012-03-01', '1', '该书讲述', '图书馆', '赵六', '2022-06-02');
INSERT INTO `book` VALUES (null, '计算机组成原理', 'b007', '唐朔飞', '2003-08-05', '0', '暂无描述', '图书馆', null, null);
INSERT INTO `book` VALUES ('22', '造彩虹的人', 'b010', '东野圭吾 ', '2017-06-01', '0', null, '图书馆', null, null);
INSERT INTO `book` VALUES (null, '高等数学(上)', 'b012', '未知', '2007-01-01', '1', '暂无描述', '图书馆', '小明', '2022-06-04');
INSERT INTO `book` VALUES (null, '高等数学(下)', 'b014', '未知', '2015-06-01', '1', '暂无描述', '图书馆', '小红', '2022-06-10');

-- ----------------------------
-- Table structure for `record`
-- ----------------------------
DROP TABLE IF EXISTS `record`;
CREATE TABLE `record` (
  `id` bigint(4) NOT NULL AUTO_INCREMENT,
  `readernumber` varchar(8) DEFAULT NULL,
  `booknumber` varchar(8) DEFAULT NULL,
  `borrowdate` date DEFAULT NULL,
  `returndate` date DEFAULT NULL,
  `remark` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `reader` (`readernumber`),
  KEY `book` (`booknumber`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of record
-- ----------------------------
INSERT INTO `record` VALUES ('2', 'dasdsad', 'b014', '2022-06-25', '2022-06-25', null);
INSERT INTO `record` VALUES ('4', 'adasd', 'b006', '2022-06-26', '2022-06-26', null);
INSERT INTO `record` VALUES ('5', 'dasdd', 'b001', '2022-06-27', '2022-06-27', null);
INSERT INTO `record` VALUES ('6', 'sadas', null, '2022-06-27', null, null);
INSERT INTO `record` VALUES ('7', 'dasd', null, '2022-06-27', null, null);
INSERT INTO `record` VALUES ('8', 'r002', 'b001', '2022-06-27', '2022-06-27', null);
INSERT INTO `record` VALUES ('9', 'r001', 'b001', '2022-06-27', '2022-06-27', null);
INSERT INTO `record` VALUES ('10', 'r001', 'b001', '2022-06-27', '2022-06-27', null);

-- ----------------------------
-- Table structure for `student`
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `id` bigint(4) DEFAULT NULL,
  `name` varchar(10) NOT NULL,
  `psw` varchar(10) NOT NULL,
  `class` varchar(10) DEFAULT NULL,
  `learnnumber` varchar(20) DEFAULT NULL,
  `phonenumber` varchar(20) DEFAULT NULL,
  `borrownumber` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`name`,`psw`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student` VALUES ('5', '刘一', '000', '计科三班', '1705928765', '12789543342', '2');
INSERT INTO `student` VALUES ('1', '张三', '000', '计科一班', '1706128701', '17899098765', '3');
INSERT INTO `student` VALUES ('2', '李四', '000', '计科二班', '1703454237', '18900753346', '6');
INSERT INTO `student` VALUES ('3', '王五', '000', '计科一班', '1705945346', '18865432865', '1');
INSERT INTO `student` VALUES ('4', '赵六', '000', '计科三班', '1705928067', '13288764432', '1');

-- ----------------------------
-- Table structure for `user`
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` bigint(4) DEFAULT NULL,
  `username` varchar(20) NOT NULL,
  `psw` varchar(20) NOT NULL,
  PRIMARY KEY (`username`,`psw`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1', '1111', '1111');
INSERT INTO `user` VALUES (null, '123', '123');
INSERT INTO `user` VALUES ('2', 'lipiao', '123');
