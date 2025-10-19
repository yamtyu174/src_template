import sys
sys.dont_write_bytecode = True

from settings import get_settings
from logger import setup_logger

settings = get_settings(into_env=True)
logger = setup_logger()
