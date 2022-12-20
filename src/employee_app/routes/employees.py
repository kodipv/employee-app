import aiohttp_jinja2
from aiohttp import web

from employee_app.services.employees import get_employees_structure, build_employees_tree, get_all_employees
from employee_app.services.positions import get_positions
from employee_app.use_cases.employees import create_employee_use_case


class EmployeesTreeHandler(web.View):

    @aiohttp_jinja2.template("employees_tree.html")
    async def get(self):
        employees = await get_employees_structure(self.request.app['pool'])
        tree = build_employees_tree(employees)
        return {"employees_tree": tree}


@aiohttp_jinja2.template('create_employee.html')
async def create_employee_handler(request):
    if request.method == 'POST':
        form = await request.post()
        first_name = form['first_name']
        last_name = form['last_name']
        middle_name = form['middle_name']
        manager_id = form.get('manager', None)
        if manager_id:
            manager_id = int(manager_id)
        position_id = int(form['position'])
        monthly_rate = int(form['monthly_rate'])
        await create_employee_use_case(
            first_name, last_name, middle_name, manager_id, position_id, monthly_rate, request.app['pool']
        )
        raise web.HTTPFound(location=request.app.router['employees_tree'].url_for())

    positions = await get_positions(request.app['pool'])
    employees = await get_all_employees(request.app['pool'])
    return {"positions": positions, "employees": employees}
