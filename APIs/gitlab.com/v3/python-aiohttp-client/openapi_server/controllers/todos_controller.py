from typing import List, Dict
from aiohttp import web

from openapi_server.models.todo import Todo
from openapi_server import util


async def delete_v3_todos(request: web.Request, ) -> web.Response:
    """Mark all todos as done

    Mark all todos as done


    """
    return web.Response(status=200)


async def delete_v3_todos_id(request: web.Request, id) -> web.Response:
    """Mark a todo as done

    Mark a todo as done

    :param id: The ID of the todo being marked as done
    :type id: int

    """
    return web.Response(status=200)


async def get_v3_todos(request: web.Request, page=None, per_page=None) -> web.Response:
    """Get a todo list

    Get a todo list

    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int

    """
    return web.Response(status=200)
