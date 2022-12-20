async def get_positions(pool):
    query = "select * from positions"
    async with pool.acquire() as connection:
        return await connection.fetch(query)
