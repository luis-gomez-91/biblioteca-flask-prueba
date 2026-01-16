class Config:
    SECRET_KEY = "NsEEwoWmyQVLgmDmgGqRpgyQNXFmZtMO"
    # Se agrega "+psycopg" para indicar que use la versión 3 instalada
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg://postgres:NsEEwoWmyQVLgmDmgGqRpgyQNXFmZtMO@turntable.proxy.rlwy.net:10658/railway"
    SQLALCHEMY_TRACK_MODIFICATIONS = False