import datetime
import logging
import os
import sys


class Log(object):
    def __init__(self):
        pass

    def _create_log(self, log_file_name):
        log = logging.getLogger(__name__)
        log.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler(log_file_name, mode="w+")
        file_handler.setLevel(logging.INFO)
        log.addHandler(file_handler)
        log.info("Execution Time : " + str(datetime.datetime.now()))
        log.info("Command line: python " + " ".join(sys.argv) + "\n")
        return log

    def _log_args(self, log, arg_list):
        log.info("List of Parameters:")
        for k in arg_list:
            log.info(k + " : " + str(arg_list[k]))
        log.info("\n")
