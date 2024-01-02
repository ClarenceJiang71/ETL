"""
Define the order model
"""
import json
import sys
sys.path.append('/Users/clarencestudy/Desktop/Tech/ETL/ETL')
from util import time_util, str_util
import config.project_config as config 

class OrderModel:
    def __init__(self, data) -> None:
        data = json.loads(data)

        self.discount_rate = data['discountRate']  # 折扣率
        self.store_shop_no = data['storeShopNo']  # 店铺店号（无用列）
        self.day_order_seq = data['dayOrderSeq']  # 本单为当日第几单
        self.store_district = data['storeDistrict']  # 店铺所在行政区
        self.is_signed = data['isSigned']  # 是否签约店铺（签约第三方支付体系）
        self.store_province = data['storeProvince']  # 店铺所在省份
        self.origin = data['origin']  # 原始信息（无用）
        self.store_gps_longitude = data['storeGPSLongitude']  # 店铺GPS经度
        self.discount = data['discount']  # 折扣金额
        self.store_id = data['storeID']  # 店铺ID
        self.product_count = data['productCount']  # 本单售卖商品数量
        self.operator_name = data['operatorName']  # 操作员姓名
        self.operator = data['operator']  # 操作员ID
        self.store_status = data['storeStatus']  # 店铺状态
        self.store_own_user_tel = data['storeOwnUserTel']  # 店铺店主电话
        self.pay_total = data['payedTotal']  # 支付总金额
        self.pay_type = data['payType']  # 支付类型
        self.discount_type = data['discountType']  # 折扣类型
        self.store_name = data['storeName']  # 店铺名称
        self.store_own_user_name = data['storeOwnUserName']  # 店铺店主名称
        self.date_ts = data['dateTS']  # 订单时间
        self.small_change = data['smallChange']  # 找零金额
        self.store_gps_name = data['storeGPSName']  # 店铺GPS名称
        self.erase = data['erase']  # 是否抹零
        self.store_gps_address = data['storeGPSAddress']  # 店铺GPS地址
        self.order_id = data['orderID']  # 订单ID
        self.money_before_whole_discount = data['moneyBeforeWholeDiscount']  # 折扣前金额
        self.store_category = data['storeCategory']  # 店铺类别
        self.receivable = data['receivable']  # 应收金额
        self.face_id = data['faceID']  # 面部识别ID
        self.store_own_user_id = data['storeOwnUserId']  # 店铺店主ID
        self.payment_channel = data['paymentChannel']  # 付款通道
        self.payment_scenarios = data['paymentScenarios']  # 付款情况（无用）
        self.store_address = data['storeAddress']  # 店铺地址
        self.total_no_discount = data['totalNoDiscount']  # 整体价格（无折扣）
        self.payed_total = data['payedTotal']  # 已付款金额
        self.store_gps_latitude = data['storeGPSLatitude']  # 店铺GPS纬度
        self.store_create_date_ts = data['storeCreateDateTS']  # 店铺创建时间
        self.store_city = data['storeCity']  # 店铺所在城市
        self.member_id = data['memberID']  # 会员ID

    def to_csv(self, sep = ','):
        self.check_and_transform_area()
        csv_line = f"{self.order_id}{sep}" \
               f"{self.store_id}{sep}" \
               f"{self.store_name}{sep}" \
               f"{self.store_status}{sep}" \
               f"{self.store_own_user_id}{sep}" \
               f"{self.store_own_user_name}{sep}" \
               f"{self.store_own_user_tel}{sep}" \
               f"{self.store_category}{sep}" \
               f"{self.store_address}{sep}" \
               f"{self.store_shop_no}{sep}" \
               f"{self.store_province}{sep}" \
               f"{self.store_city}{sep}" \
               f"{self.store_district}{sep}" \
               f"{self.store_gps_name}{sep}" \
               f"{self.store_gps_address}{sep}" \
               f"{self.store_gps_longitude}{sep}" \
               f"{self.store_gps_latitude}{sep}" \
               f"{self.is_signed}{sep}" \
               f"{self.operator}{sep}" \
               f"{self.operator_name}{sep}" \
               f"{self.face_id}{sep}" \
               f"{self.member_id}{sep}" \
               f"{time_util.ts13_to_date_string(self.store_create_date_ts)}{sep}" \
               f"{self.origin}{sep}" \
               f"{self.day_order_seq}{sep}" \
               f"{self.discount_rate}{sep}" \
               f"{self.discount_type}{sep}" \
               f"{self.discount}{sep}" \
               f"{self.money_before_whole_discount}{sep}" \
               f"{self.receivable}{sep}" \
               f"{self.erase}{sep}" \
               f"{self.small_change}{sep}" \
               f"{self.total_no_discount}{sep}" \
               f"{self.pay_total}{sep}" \
               f"{self.pay_type}{sep}" \
               f"{self.payment_channel}{sep}" \
               f"{self.payment_scenarios}{sep}" \
               f"{self.product_count}{sep}" \
               f"{time_util.ts13_to_date_string(self.date_ts)}"
        return csv_line
    

    def check_and_transform_area(self):
        if str_util.check_null(self.store_province):
            self.store_province = "unknown province"
        if str_util.check_null(self.store_city):
            self.store_city = "unknown city"
        if str_util.check_null(self.store_district):
            self.store_district = "unknown district"

    def generate_insert_sql(self):
        ''' 生成插入订单表的SQL语句 '''
        return f"insert ignore into {config.target_orders_table_name}(order_id,store_id,store_name,store_status,store_own_user_id,store_own_user_name,store_own_user_tel,store_category,store_address,store_shop_no,store_province,store_city,store_district,store_gps_name,store_gps_address,store_gps_longitude,store_gps_latitude,is_signed,operator,operator_name,face_id,member_id,store_create_date_ts,origin,day_order_seq,discount_rate,discount_type,discount,money_before_whole_discount,receivable,erase,small_change,total_no_discount,pay_total,pay_type,payment_channel,payment_scenarios,product_count,date_ts) values (" \
               f"'{self.order_id}'," \
               f"{self.store_id}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.store_name)}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.store_status)}," \
               f"{self.store_own_user_id}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.store_own_user_name)}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.store_own_user_tel)}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.store_category)}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.store_address)}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.store_shop_no)}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.store_province)}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.store_city)}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.store_district)}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.store_gps_name)}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.store_gps_address)}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.store_gps_longitude)}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.store_gps_latitude)}," \
               f"{self.is_signed}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.operator)},"\
               f"{str_util.check_str_null_and_transform_to_sql_null(self.operator_name)}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.face_id)}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.member_id)}," \
               f"'{time_util.ts13_to_date_string(self.store_create_date_ts)}'," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.origin)}," \
               f"{self.day_order_seq}," \
               f"{self.discount_rate}," \
               f"{self.discount_type}," \
               f"{self.discount}," \
               f"{self.money_before_whole_discount}," \
               f"{self.receivable}," \
               f"{self.erase}," \
               f"{self.small_change}," \
               f"{self.total_no_discount}," \
               f"{self.payed_total}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.pay_type)}," \
               f"{self.payment_channel}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.payment_scenarios)}," \
               f"{self.product_count}," \
               f"'{time_util.ts13_to_date_string(self.date_ts)}'" \
               f");"
    
class OrderDetailModel(object):
    def __init__(self, data):
        data = json.loads(data)
        # more like the primary key that serves as a foreign key too 
        # connect with the order model 
        self.order_id = data['orderID']  
        self.products_detail = []

        # iterate each product and instantiate product object and store it in the list 
        for single_product in data['product'] :
            product = SingleProductSoldModel(self.order_id, single_product)
            self.products_detail.append(product)

    def to_csv(self):
        res = ""
        for product in self.products_detail:
            res += product.to_csv()
            res += '\n'
        return res 
    
    def generate_insert_sql(self):
        sql = f"insert ignore into {config.target_orders_detail_table_name}(order_id, barcode, name, count, price_per, retail_price, trade_price, category_id, unit_id) values "

        for single_product in self.products_detail:
            sql += f"(" \
               f"'{single_product.order_id}'," \
               f"{str_util.check_str_null_and_transform_to_sql_null(single_product.barcode)}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(single_product.name)}," \
               f"{single_product.count}," \
               f"{single_product.price_per}," \
               f"{single_product.retail_price}," \
               f"{single_product.trade_price}," \
               f"{single_product.category_id}," \
               f"{single_product.unit_id}" \
               f"), "
        # SQL中语句中最后一个圆括号，多了一个逗号+空格 => insert into T values (), (), (),  => 最后一个空格是-1，最后一个逗号是-2
        sql = sql[:-2]
        return sql

class SingleProductSoldModel(object):
    def __init__(self, order_id, product_detail):
        self.order_id = order_id
        self.barcode = product_detail['barcode']
        self.name = product_detail['name']
        self.count = product_detail['count']
        self.price_per = product_detail['pricePer']
        self.retail_price = product_detail['retailPrice']
        self.trade_price = product_detail['tradePrice']
        self.category_id = product_detail['categoryID']
        self.unit_id = product_detail['unitID']

    def to_csv(self, sep = ','):
        return f"{self.order_id}{sep}" \
            f"{self.barcode}{sep}" \
            f"{self.name}{sep}" \
            f"{self.count}{sep}" \
            f"{self.price_per}{sep}" \
            f"{self.retail_price}{sep}" \
            f"{self.trade_price}{sep}" \
            f"{self.category_id}{sep}" \
            f"{self.unit_id}\n"

if __name__ == '__main__':
    json_str = '{"discountRate": 1, "storeShopNo": "277551753310004", "dayOrderSeq": 26, "storeDistrict": "开福区", "isSigned": 1, "storeProvince": "湖南省", "origin": 0, "storeGPSLongitude": "112.99564674496649", "discount": 0, "storeID": 622, "productCount": 3, "operatorName": "OperatorName", "operator": "NameStr", "storeStatus": "open", "storeOwnUserTel": 12345678910, "payType": "cash", "discountType": 2, "storeName": "刘伟明便利店", "storeOwnUserName": "OwnUserNameStr", "dateTS": 1542436507000, "smallChange": 0, "storeGPSName": "None", "erase": 0, "product": [{"count": 1, "name": "健达缤纷乐T40g", "unitID": 3, "barcode": "80177609", "pricePer": 8, "retailPrice": 8, "tradePrice": 6, "categoryID": 1}, {"count": 1, "name": "娃哈哈氧道饮用水 550ml", "unitID": 2, "barcode": "6902083901233", "pricePer": 2, "retailPrice": 2, "tradePrice": 0, "categoryID": 1}, {"count": 1, "name": "红牛维生素功能饮料250ml", "unitID": 4, "barcode": "6920202888883", "pricePer": 6, "retailPrice": 6, "tradePrice": 0, "categoryID": 1}], "storeGPSAddress": "None", "orderID": "15424365069006223306", "moneyBeforeWholeDiscount": 16, "storeCategory": "normal", "receivable": 16, "faceID": "", "storeOwnUserId": 463, "paymentChannel": 0, "paymentScenarios": "OTHER", "storeAddress": "StoreAddress", "totalNoDiscount": 16, "payedTotal": 16, "storeGPSLatitude": "28.249745727366196", "storeCreateDateTS": 1531790437000, "storeCity": "长沙市", "memberID": "0"}'
    # model = OrderModel(json_str)
    # print(model.to_csv())
    # print(model.generate_insert_sql())
    order_detail_model = OrderDetailModel(json_str)
    print(order_detail_model.to_csv())
    print(order_detail_model.generate_insert_sql())
