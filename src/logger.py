

import os
import logging
from datetime import datetime

# Specify the absolute path for the logs directory
logs_directory = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")

# Create the logs directory if it does not exist
os.makedirs(logs_directory, exist_ok=True)

# Specify the log file name with the current date and time
log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Specify the absolute path for the log file
log_file_path = os.path.join(logs_directory, log_file)

# Configure logging
logging.basicConfig(
    filename=log_file_path,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
