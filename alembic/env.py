import sys
import os
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool, create_engine
from alembic import context
from dotenv import load_dotenv

# 🧭 Додаємо шлях до кореня проєкту (на 1 рівень вгору)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 🛠 Завантажуємо змінні середовища з .env файлу
load_dotenv()

# 📦 Імпортуємо Base з db.models
from db.models import Base

# 🔧 Alembic конфіг
config = context.config

# 📋 Налаштування логування
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# 📚 Вказуємо метадані моделей для Alembic
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = os.getenv("DATABASE_URL")  # Використовуємо DATABASE_URL з .env
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    url = os.getenv("DATABASE_URL")  # Використовуємо DATABASE_URL з .env
    connectable = create_engine(url, poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
