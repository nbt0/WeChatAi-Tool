# -*- coding: utf-8 -*-
from typing import Any, Dict, List, Optional, Tuple, Union
import pymysql
from pymysql.cursors import DictCursor
from config.settings import MYSQL_CONFIG

class Database:
    """数据库操作封装类"""
    
    def __init__(self):
        """初始化数据库连接"""
        self.conn = None
        self.cursor = None
        
    def connect(self) -> None:
        """创建数据库连接"""
        try:
            self.conn = pymysql.connect(
                host=MYSQL_CONFIG['host'],
                port=MYSQL_CONFIG['port'],
                user=MYSQL_CONFIG['user'],
                password=MYSQL_CONFIG['password'],
                database=MYSQL_CONFIG['database'],
                charset=MYSQL_CONFIG['charset'],
                cursorclass=DictCursor
            )
            self.cursor = self.conn.cursor()
        except Exception as e:
            raise Exception(f"数据库连接失败: {str(e)}")
    
    def close(self) -> None:
        """关闭数据库连接"""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
    
    def execute(self, sql: str, params: Optional[Union[Tuple, Dict]] = None) -> int:
        """执行SQL语句
        
        Args:
            sql: SQL语句
            params: SQL参数
            
        Returns:
            影响的行数
        """
        try:
            if not self.conn or self.conn.open is False:
                self.connect()
            affected_rows = self.cursor.execute(sql, params)
            self.conn.commit()
            return affected_rows
        except Exception as e:
            self.conn.rollback()
            raise Exception(f"SQL执行失败: {str(e)}")
    
    def fetch_one(self, sql: str, params: Optional[Union[Tuple, Dict]] = None) -> Optional[Dict]:
        """查询单条记录
        
        Args:
            sql: SQL语句
            params: SQL参数
            
        Returns:
            查询结果字典
        """
        self.execute(sql, params)
        return self.cursor.fetchone()
    
    def fetch_all(self, sql: str, params: Optional[Union[Tuple, Dict]] = None) -> List[Dict]:
        """查询多条记录
        
        Args:
            sql: SQL语句
            params: SQL参数
            
        Returns:
            查询结果列表
        """
        self.execute(sql, params)
        return self.cursor.fetchall()
    
    def insert(self, table: str, data: Dict[str, Any]) -> int:
        """插入数据
        
        Args:
            table: 表名
            data: 插入的数据字典
            
        Returns:
            插入记录的ID
        """
        fields = ','.join(data.keys())
        values = ','.join(['%s'] * len(data))
        sql = f"INSERT INTO {table} ({fields}) VALUES ({values})"
        self.execute(sql, tuple(data.values()))
        return self.cursor.lastrowid
    
    def update(self, table: str, data: Dict[str, Any], where: str, params: Optional[Union[Tuple, Dict]] = None) -> int:
        """更新数据
        
        Args:
            table: 表名
            data: 更新的数据字典
            where: WHERE条件
            params: WHERE条件参数
            
        Returns:
            影响的行数
        """
        set_fields = ','.join([f"{k}=%s" for k in data.keys()])
        sql = f"UPDATE {table} SET {set_fields} WHERE {where}"
        params = tuple(data.values()) + (params if isinstance(params, tuple) else tuple())
        return self.execute(sql, params)
    
    def delete(self, table: str, where: str, params: Optional[Union[Tuple, Dict]] = None) -> int:
        """删除数据
        
        Args:
            table: 表名
            where: WHERE条件
            params: WHERE条件参数
            
        Returns:
            影响的行数
        """
        sql = f"DELETE FROM {table} WHERE {where}"
        return self.execute(sql, params)

# 创建全局数据库实例
db = Database()