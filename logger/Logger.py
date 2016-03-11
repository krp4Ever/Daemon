import logging
import logging.config

class Logger:
    fileLogger = None
    consoleLogger = None

    @staticmethod
    def initlogger(confFile):
	    logging.config.fileConfig(confFile)
	    Logger.fileLogger = logging.getLogger("daemon")
	    Logger.consoleLogger = logging.getLogger("console")

    @staticmethod
    def debug(msg):
		Logger.consoleLogger.info(msg)

    @staticmethod
    def warning(msg):
        Logger.consoleLogger.warning(msg)
        Logger.fileLogger.warning(msg)

    @staticmethod
    def error(msg):
        Logger.consoleLogger.error(msg)
        Logger.fileLogger.error(msg)
