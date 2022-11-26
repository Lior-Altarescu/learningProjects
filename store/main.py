from logging.config import dictConfig
from app.log_config import log_config
from app.routes.apiv1 import app
import uvicorn


if __name__ == "__main__":
    dictConfig(log_config)
    uvicorn.run(app, host="0.0.0.0", port=8000)

