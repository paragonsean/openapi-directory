from typing import List, Dict
from aiohttp import web

from openapi_server.models.request_entity import RequestEntity
from openapi_server.models.request_entity_relation import RequestEntityRelation
from openapi_server import util


async def create_request_entity(request: web.Request, x_api2_crm_user_key, x_api2_crm_application_key, body) -> web.Response:
    """POST for request

    Execute request into the system

    :param x_api2_crm_user_key: User Key
    :type x_api2_crm_user_key: str
    :param x_api2_crm_application_key: Application Key
    :type x_api2_crm_application_key: str
    :param body: Execute request into the system
    :type body: dict | bytes

    """
    body = RequestEntity.from_dict(body)
    return web.Response(status=200)
