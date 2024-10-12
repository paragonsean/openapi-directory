from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def query(request: web.Request, sql, shape) -> web.Response:
    """Execute a SQLite SQL query against the content database

    Accepts SQLite SQL query, returns JSON. Does not allow PRAGMA statements.

    :param sql: The SQL query to be executed
    :type sql: str
    :param shape: The shape of the response data. Must be \&quot;array\&quot;
    :type shape: str

    """
    return web.Response(status=200)
