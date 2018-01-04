/*
Navicat MySQL Data Transfer

Source Server         : local
Source Server Version : 50720
Source Host           : 127.0.0.1:3306
Source Database       : ippool

Target Server Type    : MYSQL
Target Server Version : 50720
File Encoding         : 65001

Date: 2018-01-04 15:23:38
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `tblippool`
-- ----------------------------
DROP TABLE IF EXISTS `tblippool`;
CREATE TABLE `tblippool` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `hash` char(32) NOT NULL,
  `ip` varchar(15) NOT NULL DEFAULT '',
  `port` int(10) unsigned zerofill NOT NULL,
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `hash` (`hash`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of tblippool
-- ----------------------------
