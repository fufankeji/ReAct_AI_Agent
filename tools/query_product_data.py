# -*- coding: utf-8 -*-

import sqlite3

def query_by_product_name(product_name):
    # 连接 SQLite 数据库
    conn = sqlite3.connect('SportsEquipment.db')
    cursor = conn.cursor()

    # 使用SQL查询按名称查找产品。'%'符号允许部分匹配。
    cursor.execute("SELECT * FROM products WHERE product_name LIKE ?", ('%' + product_name + '%',))

    # 获取所有查询到的数据
    rows = cursor.fetchall()

    # 关闭连接
    conn.close()

    return rows

def create_and_populate_database():
    # 连接到本地数据库文件
    conn = sqlite3.connect('SportsEquipment.db')  # 指定文件名来保存数据库
    cursor = conn.cursor()

    # 检查是否存在名为 'products' 的表，如果不存在则创建
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='products';")
    if cursor.fetchone() is None:
        # 创建表
        cursor.execute('''
        CREATE TABLE products (
            product_id TEXT,
            product_name TEXT,
            description TEXT,
            specifications TEXT,
            usage TEXT,
            brand TEXT,
            price REAL,
            stock_quantity INTEGER
        )
        ''')
        # 数据列表，用于插入表中
        products = [
            (
            '001', '足球', '高品质职业比赛用球，符合国际标准', '圆形，直径22 cm', '职业比赛、学校体育课', '耐克', 120, 50),
            ('002', '羽毛球拍', '轻量级，适合初中级选手，提供优秀的击球感受', '碳纤维材质，重量85 g', '业余比赛、家庭娱乐',
             '尤尼克斯', 300, 30),
            ('003', '篮球', '室内外可用，耐磨耐用，适合各种天气条件', '皮质，标准7号球', '学校、社区运动场', '斯伯丁', 200,
             40),
            ('004', '跑步鞋', '适合长距离跑步，舒适透气，提供良好的足弓支撑', '多种尺码，透气网布', '长跑、日常训练',
             '阿迪达斯', 500, 20),
            ('005', '瑜伽垫', '防滑材料，厚度适中，易于携带和清洗', '长180cm，宽60cm，厚5mm', '瑜伽、普拉提', '曼达卡', 150,
             25),
            ('006', '速干运动衫', '吸汗快干，适合各种户外运动，持久舒适', 'S/M/L/XL，多色可选', '运动、徒步、旅游', '诺斯脸',
             180, 60),
            ('007', '电子计步器', '精确计步，带心率监测功能，蓝牙连接手机应用', '可充电，续航7天', '日常健康管理、运动',
             'Fitbit', 250, 15),
            ('008', '乒乓球拍套装', '包括两只拍子和三个球，适合家庭娱乐和业余训练', '标准尺寸，拍面防滑处理', '家庭、社区',
             '双鱼', 160, 35),
            ('009', '健身手套', '抗滑耐磨，保护手部，适合各种健身活动', '多种尺码，通风设计', '健身房、户外运动',
             'Under Armour', 120, 50),
            ('010', '膝盖护具', '减少运动伤害，提供良好的支撑和保护，适合篮球和足球运动', '弹性织物，可调节紧度',
             '篮球、足球及其他运动', '麦克戴维', 220, 40)
        ]

        # 插入数据到表中
        cursor.executemany('''
        INSERT INTO products (product_id, product_name, description, specifications, usage, brand, price, stock_quantity)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', products)

        # 提交更改以确保数据被保存在文件中
        conn.commit()

    # 检索并打印所有记录以验证插入
    cursor.execute('SELECT * FROM products')
    all_rows = cursor.fetchall()

    conn.close()  # 关闭连接以释放资源

    return all_rows


if __name__ == '__main__':
    # # 创建模拟的商品后台数据库信息
    create_and_populate_database()