import aiohttp_jinja2
import jinja2
from aiohttp import web
from aiohttp.web_app import Application

from employee_app.config import config
from employee_app.database import setup_database
from employee_app.routes.employees import EmployeesTreeHandler, create_employee_handler


def init_jinja2(app: web.Application) -> None:
    aiohttp_jinja2.setup(
        app, loader=jinja2.FileSystemLoader(str(config.project_dir / config.templates_dir))
    )
    app['static_root_url'] = f"/{config.static_dir}"


def setup_routes(app):
    app.router.add_static('/static/', path=config.project_dir / 'static', name='static')
    app.router.add_get('/employees_tree', EmployeesTreeHandler, name="employees_tree")
    app.router.add_get('/create_employee', create_employee_handler, name="create_employee")
    app.router.add_post('/create_employee', create_employee_handler, name="create_employee")


def create_app() -> Application:
    app = Application()
    setup_routes(app)
    init_jinja2(app)
    setup_database(app)
    return app


app = create_app()


if __name__ == '__main__':
    web.run_app(app, host=config.app_host, port=config.app_port)
