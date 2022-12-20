async def get_employees_structure(pool):
    query = """select 
                    e.id,
                    e.last_name || ' ' || e.first_name || ' ' || e.middle_name as full_name,
                    p.name as position_name,
                    er.monthly_rate,
                    e.manager_id
                from employees e
                left join employee_positions ep on e.id = ep.employee_id
                left join positions p on p.id = ep.position_id
                left join employee_rates er on e.id = er.employee_id"""
    async with pool.acquire() as connection:
        return await connection.fetch(query)


async def get_all_employees(pool):
    query = """select 
                 id,
                 last_name || ' ' || first_name || ' ' || middle_name as full_name
               from employees"""
    async with pool.acquire() as connection:
        return await connection.fetch(query)


async def create_employee(first_name, last_name, middle_name, manager_id, connection):
    query = """insert into employees (first_name, last_name, middle_name, manager_id)
                values
                ($1, $2, $3, $4)
                returning id"""
    return await connection.fetchval(query, first_name, last_name, middle_name, manager_id)


async def assign_position(employee_id, position_id, connection):
    query = """insert into employee_positions (employee_id, position_id) 
                values 
                ($1, $2)"""
    await connection.execute(query, employee_id, position_id)


async def set_rate(employee_id, monthly_rate, connection):
    query = """insert into employee_rates (employee_id, monthly_rate) 
                values 
                ($1, $2)"""
    await connection.execute(query, employee_id, monthly_rate)


def build_employees_tree(employees):
    structure = {}
    root_ids = set()
    for employee in employees:
        structure[employee["id"]] = {**employee, "subordinates": {}}
        if not employee["manager_id"]:
            root_ids.add(employee["id"])

    for employee_id, employee in structure.items():
        if employee["manager_id"]:
            manager = structure[employee["manager_id"]]
            manager["subordinates"][employee["id"]] = employee

    return {employee_id: employee for employee_id, employee in structure.items() if employee_id in root_ids}
