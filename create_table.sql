CREATE TABLE IF NOT EXISTS `utwifi` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '自增ID',
  `alt` text NOT NULL COMMENT '地点代码',
  `coords` text NOT NULL COMMENT '坐标',
  `num_connection` int(11) NOT NULL COMMENT '连接数',
  `num_active_access_points` int(11) NOT NULL COMMENT '活跃热点数',
  `num_total_access_points` int(11) NOT NULL COMMENT '总共热点数',
  `num_conn_per_ap` int(11) NOT NULL COMMENT '平均每个热点连接数',
  `name` text NOT NULL COMMENT '地点名',
  `time` datetime NOT NULL COMMENT '时间',

  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;
