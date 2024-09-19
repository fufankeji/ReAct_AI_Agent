def read_store_promotions(product_name):
    # 指定优惠政策文档的文件路径
    file_path = 'store_promotions.txt'

    try:
        # 打开文件并按行读取内容
        with open(file_path, 'r', encoding='utf-8') as file:
            promotions_content = file.readlines()

        # 搜索包含产品名称的行
        filtered_content = [line for line in promotions_content if product_name in line]

        # 返回匹配的行，如果没有找到，返回一个默认消息
        if filtered_content:
            return ''.join(filtered_content)
        else:
            return "没有找到关于该产品的优惠政策。"
    except FileNotFoundError:
        # 文件不存在的错误处理
        return "优惠政策文档未找到，请检查文件路径是否正确。"
    except Exception as e:
        # 其他潜在错误的处理
        return f"读取优惠政策文档时发生错误: {str(e)}"


if __name__ == '__main__':

    # 重新创建一个包含店铺优惠政策的文本文档
    promotions_content = """
    店铺优惠政策：
    1. 足球 - 购买足球即可享受9折优惠。
    2. 羽毛球拍 - 任意购买羽毛球拍两支以上，享8折优惠。
    3. 篮球 - 单笔订单满300元，篮球半价。
    4. 跑步鞋 - 第一次购买跑步鞋的顾客可享受满500元减100元优惠。
    5. 瑜伽垫 - 每购买一张瑜伽垫，赠送价值50元的瑜伽教程视频一套。
    6. 速干运动衫 - 买三送一，赠送的为最低价商品。
    7. 电子计步器 - 购买任意电子计步器，赠送配套手机APP永久会员资格。
    8. 乒乓球拍套装 - 乒乓球拍套装每套95折。
    9. 健身手套 - 满200元包邮。
    10. 膝盖护具 - 每件商品配赠运动护膝一个。
    
    注意：
    - 所有优惠活动不可与其他优惠同享。
    - 优惠详情以实际到店或下单时为准。
    """

    # 将优惠政策写入文件
    file_path = './store_promotions.txt'
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(promotions_content)

    print(file_path)