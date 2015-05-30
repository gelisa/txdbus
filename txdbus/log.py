"""
Logging facility for txdbus.

@author: Pontus Karlsson
"""
import logging


logger = logging.getLogger( __package__ )


def useTwistedPythonLog():
    """
    Adds a L{logging.StreamHandler} to our logger instance that will
    pipe all logging output back to twisteds configured log system.
    """
    from twisted.python.log import logfile

    logger.addHandler(
        logging.StreamHandler( stream=logfile )
    )
