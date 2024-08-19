from typing import List, Dict
from aiohttp import web

from openapi_server.models.count import Count
from openapi_server.models.entity_entity import EntityEntity
from openapi_server import util


async def get_entity_collection(request: web.Request, x_api2_crm_user_key, x_api2_crm_application_key, x_api2_crm_native_enable=None, x_api2_crm_describe_lifetime=None, page_size=None, page=None, filter=None, fields=None) -> web.Response:
    """GET for entity

    Returns all entities from the system

    :param x_api2_crm_user_key: User Key
    :type x_api2_crm_user_key: str
    :param x_api2_crm_application_key: Application Key
    :type x_api2_crm_application_key: str
    :param x_api2_crm_native_enable: Return native response
    :type x_api2_crm_native_enable: str
    :param x_api2_crm_describe_lifetime: Describe lifetime
    :type x_api2_crm_describe_lifetime: str
    :param page_size: Amount of results (default: 25)
    :type page_size: int
    :param page: Page to show (default: 1)
    :type page: int
    :param filter: Filter
    :type filter: str
    :param fields: Comma-separated list of fields to include in the response
    :type fields: str

    """
    return web.Response(status=200)


async def get_entity_count_collection(request: web.Request, x_api2_crm_user_key, x_api2_crm_application_key) -> web.Response:
    """COUNT for entity

    Count all entities from the system

    :param x_api2_crm_user_key: User Key
    :type x_api2_crm_user_key: str
    :param x_api2_crm_application_key: Application Key
    :type x_api2_crm_application_key: str

    """
    return web.Response(status=200)


async def get_entity_entity(request: web.Request, x_api2_crm_user_key, x_api2_crm_application_key, entity_id, x_api2_crm_native_enable=None, x_api2_crm_describe_lifetime=None, fields=None) -> web.Response:
    """GET for entity

    Return entity information

    :param x_api2_crm_user_key: User Key
    :type x_api2_crm_user_key: str
    :param x_api2_crm_application_key: Application Key
    :type x_api2_crm_application_key: str
    :param entity_id: Entity Identifier
    :type entity_id: str
    :param x_api2_crm_native_enable: Return native response
    :type x_api2_crm_native_enable: str
    :param x_api2_crm_describe_lifetime: Describe lifetime
    :type x_api2_crm_describe_lifetime: str
    :param fields: Comma-separated list of fields to include in the response
    :type fields: str

    """
    return web.Response(status=200)
