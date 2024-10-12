from typing import List, Dict
from aiohttp import web

from openapi_server.models.application_entity import ApplicationEntity
from openapi_server.models.application_entity_list import ApplicationEntityList
from openapi_server.models.application_entity_relation import ApplicationEntityRelation
from openapi_server.models.application_entity_write import ApplicationEntityWrite
from openapi_server.models.count import Count
from openapi_server import util


async def create_application_entity(request: web.Request, x_api2_crm_user_key, body) -> web.Response:
    """POST for application

    Add application into the system

    :param x_api2_crm_user_key: API2CRM user key
    :type x_api2_crm_user_key: str
    :param body: Add application into the system
    :type body: dict | bytes

    """
    body = ApplicationEntityWrite.from_dict(body)
    return web.Response(status=200)


async def delete_application_entity(request: web.Request, x_api2_crm_user_key, key) -> web.Response:
    """DELETE for application

    Delete application information

    :param x_api2_crm_user_key: API2CRM user key
    :type x_api2_crm_user_key: str
    :param key: Application key
    :type key: str

    """
    return web.Response(status=200)


async def get_application_collection(request: web.Request, x_api2_crm_user_key, page_size=None, page=None, filter=None, fields=None, sort=None) -> web.Response:
    """GET for application

    Returns all applications from the system

    :param x_api2_crm_user_key: API2CRM user key
    :type x_api2_crm_user_key: str
    :param page_size: Amount of results (default: 25)
    :type page_size: int
    :param page: Page to show (default: 1)
    :type page: int
    :param filter: Filter
    :type filter: str
    :param fields: Comma-separated list of fields to include in the response
    :type fields: str
    :param sort: Specifies ascending or descending sort on existing fields
    :type sort: str

    """
    return web.Response(status=200)


async def get_application_count_collection(request: web.Request, x_api2_crm_user_key, filter=None) -> web.Response:
    """COUNT for application

    Count all applications from the system

    :param x_api2_crm_user_key: API2CRM user key
    :type x_api2_crm_user_key: str
    :param filter: Filter
    :type filter: str

    """
    return web.Response(status=200)


async def get_application_entity(request: web.Request, x_api2_crm_user_key, key, fields=None) -> web.Response:
    """GET for application

    Return application information

    :param x_api2_crm_user_key: API2CRM user key
    :type x_api2_crm_user_key: str
    :param key: Application key
    :type key: str
    :param fields: Comma-separated list of fields to include in the response
    :type fields: str

    """
    return web.Response(status=200)


async def update_application_entity(request: web.Request, x_api2_crm_user_key, key, body) -> web.Response:
    """PUT for application

    Update application information

    :param x_api2_crm_user_key: API2CRM user key
    :type x_api2_crm_user_key: str
    :param key: Application key
    :type key: str
    :param body: Update application information
    :type body: dict | bytes

    """
    body = ApplicationEntityWrite.from_dict(body)
    return web.Response(status=200)
