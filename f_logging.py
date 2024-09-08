import logging,datetime,sys

def f_initLog():
    logging.basicConfig(filename="f_log.log",
                    filemode='a',
                    format='%(asctime)s:%(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)       
    logger = logging.getLogger('f_logging')
    logger.debug('--------------------------------------------')
    logger.debug('---------------NEW---LOG-------------------')
    logger.debug('--------------------------------------------')
    logger.debug('f_logger.initLog() called')
    logger.debug('---')



def f_log(in_log):
    whocalled=str(sys._getframe().f_back.f_code.co_name)
    out_log=whocalled+":"+str(in_log)
    logging.debug(out_log)