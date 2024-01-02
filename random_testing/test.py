# Make the output into console 
# """
# Just use logger to trigger the 5 types of information, not direclty use logging. 

# logging模块: 主要是为了记录程序运行期间产生的日志信息

# 日志器对象的创建和配置
# 1. 日志器对象的创建
# 2. 日志处理器的创建
# 3. 将日志处理器绑定到日志器对象上

# 日志的输出
# 1. 设置日志输出级别
# 2. 输出不同级别的日志信息
# """
# # 0.导入模块
# import logging

# ####################### 日志器对象的创建和配置  #####################
# # 1. 日志器对象的创建
# logger = logging.getLogger()
# # 2. 日志处理器的创建
# stream_handler = logging.StreamHandler()

# # TODO: 4. 创建一个格式对象
# fmt = logging.Formatter('%(asctime)s - [%(levelname)s] - %(filename)s[%(lineno)d]：%(message)s')

# # TODO: 5. 将日志格式对象绑定到日志处理器上
# stream_handler.setFormatter(fmt)

# # 3. 将日志处理器绑定到日志器对象上
# logger.addHandler(stream_handler)




# ############################ 日志的输出  #######################
# # 1. 设置日志输出级别 (默认warning及warning级别以上的日志信息会被输出)
# # 忘记日志自己别的数据值,因为如果使用10 20 30 就会做不到见名知意,降低代码的可读性
# logger.setLevel(logging.INFO)

# # 2. 输出不同级别的日志信息
# """
# 日志级别 5个:
# debug: 代码调试时输出的日志信息
# info: 代码正常运行过程中输出的日志信息
# warning: 代码的运行结果可能和预期结果发生偏差时输出的日志信息
# error: 代码出现异常时输出的日志信息
# critical: 一般我们遇不到,遇到了解决不了的问题 例如: 磁盘或者内存空间已满等.
# """
# logger.debug('这是一个debug级别的日志信息')
# logger.info('这是一个info级别的日志信息')
# logger.warning('这是一个warning级别的日志信息')
# logger.error('这是一个error级别的日志信息')
# logger.critical('这是一个critical级别的日志信息')



# -----------------------------
# Make the output as a file 

# # 导入logging模块
# import logging

# #################### 日志器对象的创建和配置 ####################
# # 1. 日志器对象的创建
# logger = logging.getLogger()

# # TODO: 2. 创建换一个文件类型的日志处理器
# # 注意: filename要传入一个log文件的路径,可以使用绝对路径也可以使用相对路径,但是文件目录一定要存在,文件可以不存在
# # 举例: ../logs/test.log 路径中 logs目录必须存在, test.log可以不存在
# file_handler = logging.FileHandler(
#     filename='logs/test.log',
#     mode='a',
#     encoding='utf8'
# )
# # 3. 将日志处理器绑定到日志器对象上
# logger.addHandler(file_handler)
# # 4. 创建一个格式对象
# fmt = logging.Formatter('%(asctime)s - [%(levelname)s] - %(filename)s[%(lineno)d]：%(message)s')
# # 5. 将日志格式对象绑定到日志处理器上
# file_handler.setFormatter(fmt)


# ######################### 日志的输出 #######################
# # 1. 设置日志输出级别
# logger.setLevel(logging.INFO)
# # 2. 输出不同级别的日志信息
# logger.debug('这是一个debug级别的日志信息')
# logger.info('这是一个info级别的日志信息')
# logger.warning('这是一个warning级别的日志信息')
# logger.error('这是一个error级别的日志信息')
# logger.critical('这是一个critical级别的日志信息')

# -----------------
# Trigger from util 

import sys
sys.path.append('/Users/clarencestudy/Desktop/Tech/ETL/ETL')
from util.logging_util import init_logger

# logger = init_logger()
# logger.info("测试 info")
from util.mysql_util import MySQLUtil
db_util = MySQLUtil(database="test")
target_orders_detail_table_create_cols = \
    f"order_id varchar(255), " \
    f"barcode varchar(255), " \
    f"name varchar(255), " \
    f"count int comment 'how many products in this order', "\
    f"price_per decimal(10,5), " \
    f"retail_price decimal(10,5), " \
    f"trade_price decimal(10,5), " \
    f"category_id int, " \
    f"unit_id int, " \
    f"primary key (order_id, barcode)"
    
db_util.create_table('test', 'test_order_details', target_orders_detail_table_create_cols)