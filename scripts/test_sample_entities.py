import json
import logging
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, func
from iotfunctions import bif
from iotfunctions.metadata import EntityType
from iotfunctions.db import Database
from iotfunctions import entity
from iotfunctions.enginelog import EngineLogging

EngineLogging.configure_console_logging(logging.DEBUG)

# replace with a credentials dictionary or provide a credentials file
with open('credentials_as_dev.json', encoding='utf-8') as F:
    credentials = json.loads(F.read())
db = Database(credentials = credentials)
db_schema = None #  set if you are not using the default

e1 = entity.Robot(name='test_robot',
                            db=db,
                            drop_existing=True,
                            generate_days=5)
e1.register(raise_error=False)
df = db.read_table(table_name='test_robot',
                   schema=db_schema)
print(df.head())

e1.exec_local_pipeline()
