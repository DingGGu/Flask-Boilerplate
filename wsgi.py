from config.production import Production
from server.ggu.app import create_app

application = create_app(Production)
