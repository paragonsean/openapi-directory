from typing import List, Dict
from aiohttp import web

from openapi_server.models.lifecycle_many_to_one_request import LifecycleManyToOneRequest
from openapi_server.models.lifecycle_one_to_one_request import LifecycleOneToOneRequest
from openapi_server.models.planning_level_data_dto import PlanningLevelDataDto
from openapi_server import util


async def lifecycle_many_to_one_post(request: web.Request, token=None, body=None) -> web.Response:
    """Map from old product to new product to create artifical history

    Supports the creation of artificial startup history for new products, based on a flexible mapping of old to new. This is an Enterprise feature.

    :param token: User Authentication Token
    :type token: str
    :param body: 
    :type body: dict | bytes

    """
    body = LifecycleManyToOneRequest.from_dict(body)
    return web.Response(status=200)


async def lifecycle_one_to_one_post(request: web.Request, token=None, body=None) -> web.Response:
    """Map from old product to new product to create artifical history

    Supports the creation of artificial startup history for new products, based on a flexible mapping of old to new. This is an Enterprise feature.

    :param token: User Authentication Token
    :type token: str
    :param body: 
    :type body: dict | bytes

    """
    body = LifecycleOneToOneRequest.from_dict(body)
    return web.Response(status=200)
