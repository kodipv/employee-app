from employee_app.services.employees import create_employee, assign_position, set_rate


async def create_employee_use_case(
    first_name, last_name, middle_name, manager_id, position_id, monthly_rate, pool
):
    async with pool.acquire() as connection:
        async with connection.transaction():
            employee_id = await create_employee(first_name, last_name, middle_name, manager_id, connection)
            await assign_position(employee_id, position_id, connection)
            await set_rate(employee_id, monthly_rate, connection)
