import asyncpg

from employee_app.config import config


def setup_database(app):
    app.on_startup.append(_on_connect)
    app.on_cleanup.append(_on_shutdown)


async def _on_connect(app):
    app["pool"] = await asyncpg.create_pool(dsn=config.database.dsn)


async def _on_shutdown(app):
    await app["pool"].close()
