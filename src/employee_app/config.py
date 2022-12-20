from dataclasses import dataclass
from pathlib import Path

import yaml

BASE_DIR = Path(__file__).parent.parent


@dataclass
class DatabaseConfig:
    host: str
    port: int
    username: str
    password: str
    db_name: str

    @property
    def dsn(self):
        return f"postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.db_name}"


@dataclass
class Config:
    database: DatabaseConfig
    project_dir: str = Path(__file__).parent
    templates_dir: str = "templates"
    static_dir: str = "static"
    app_host: str = "0.0.0.0"
    app_port: int = 3000


def _load_config():
    config_path = BASE_DIR / 'config.yaml'
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)


def init_config(raw_config: dict):
    return Config(database=DatabaseConfig(**raw_config["database"]))


_config = _load_config()
config = init_config(_config)
