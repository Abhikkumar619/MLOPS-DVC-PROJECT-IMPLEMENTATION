import logging
import os

log_dir="logs"
os.makedirs(log_dir, exist_ok=True)


log=logging.getLogger('data_ingestion')
log.setLevel('DEBUG')

# Logging configuration
console_handler=logging.StreamHandler()
console_handler.setLevel('DEBUG')

log_file_path=os.path.join(log_dir, 'data_ingestion.log')
file_handler=logging.FileHandler(log_file_path)
file_handler.setLevel('DEBUG')



formetter=logging.Formatter("[%(asctime)s : %(levelname)s : %(module)s : %(message)s]")
console_handler.setFormatter(formetter)
console_handler.setFormatter(formetter)

log.addHandler(console_handler)
log.addHandler(file_handler)