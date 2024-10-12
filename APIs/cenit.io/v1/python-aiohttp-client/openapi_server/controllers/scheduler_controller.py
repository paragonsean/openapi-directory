from typing import List, Dict
from aiohttp import web

from openapi_server.models.scheduler import Scheduler
from openapi_server import util


async def setup_scheduler_get(request: web.Request, ) -> web.Response:
    """Returns a list of schedulers

    Returns a list of schedulers you&#39;ve previously created. The schedulers are returned in sorted order, with the most recent scheduler appearing first.


    """
    return web.Response(status=200)


async def setup_scheduler_id_delete(request: web.Request, id) -> web.Response:
    """Delete an schedule

    Deletes the specified scheduler.

    :param id: Scheduler ID
    :type id: str

    """
    return web.Response(status=200)


async def setup_scheduler_id_get(request: web.Request, id) -> web.Response:
    """Retrieve an existing schedule

    Retrieves the details of an existing scheduler. You need only supply the unique scheduler identifier that was returned upon scheduler creation.

    :param id: Scheduler ID
    :type id: str

    """
    return web.Response(status=200)


async def setup_scheduler_post(request: web.Request, ) -> web.Response:
    """Create or update an scheduler

    Creates or updates the specified scheduler. Any parameters not provided will be left unchanged.


    """
    return web.Response(status=200)
