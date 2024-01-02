import logging
# 10 20 30 40 50  set level triggers >= threshold 
logging.getLogger().setLevel(30)
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.fatal( "fatal")


