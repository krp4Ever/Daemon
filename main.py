#!/usr/bin/python
from logger.Logger import Logger
def main():
    Logger.initlogger("conf/logconf.ini")
    Logger.debug("logger init complete")
    Logger.error("this is a error log")
    Logger.warning("this is a warning log")

if __name__ == "__main__":
	main()
