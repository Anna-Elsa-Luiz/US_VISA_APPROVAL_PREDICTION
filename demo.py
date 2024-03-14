

from us_visa_approval.logger import logging
from us_visa_approval.exception import USvisaException
import sys 


logging.info("welcome to the custom log")

try: 
  a= 1/"10"

except Exception as e:
  logging.info(e)
  raise USvisaException(e , sys) from  e 
   