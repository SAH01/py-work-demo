import logging

# Create a logger
logger = logging.getLogger("variable_logger")
# 设置 logger 的级别
logger.setLevel(logging.DEBUG)

# 配置日志记录
logging.basicConfig(level=logging.DEBUG)

# Example usage:
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical(f"This is a critical message")
