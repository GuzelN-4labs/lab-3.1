from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Плохая практика: хардкод креденшелов в коде - учетные данные (например, логины, пароли, API-ключи, токены доступа) встраиваются прямо в исходный код
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@mydb/dbname"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()