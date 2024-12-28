import os

workers = os.cpu_count() * 2 + 1
bind = "0.0.0.0:18080"
worker_class = "uvicorn.workers.UvicornWorker"
