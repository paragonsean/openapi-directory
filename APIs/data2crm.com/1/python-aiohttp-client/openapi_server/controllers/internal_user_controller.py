from typing import List, Dict
from aiohttp import web

from openapi_server.models.count import Count
from openapi_server.models.internal_user_entity import InternalUserEntity
from openapi_server.models.internal_user_entity_relation import InternalUserEntityRelation
from openapi_server import util


async def create_internal_user_entity(request: web.Request, x_api2_crm_user_key, body) -> web.Response:
    """POST for internalUser

    

    :param x_api2_crm_user_key: User Key
    :type x_api2_crm_user_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = InternalUserEntity.from_dict(body)
    return web.Response(status=200)


async def delete_internal_user_entity(request: web.Request, x_api2_crm_user_key, internal_user_id) -> web.Response:
    """DELETE for internalUser

    

    :param x_api2_crm_user_key: User Key
    :type x_api2_crm_user_key: str
    :param internal_user_id: Internal User Key
    :type internal_user_id: str

    """
    return web.Response(status=200)


async def get_internal_user_collection(request: web.Request, x_api2_crm_user_key, page_size=None, page=None, filter=None, fields=None, sort=None, application_request_start=None, application_request_end=None) -> web.Response:
    """GET for internalUser

    Returns all internal users from the system

    :param x_api2_crm_user_key: User Key
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
    :param application_request_start: All Application Requests from this date
    :type application_request_start: str
    :param application_request_end: All Application Requests until this date
    :type application_request_end: str

    """
    application_request_start = util.deserialize_date(application_request_start)
    application_request_end = util.deserialize_date(application_request_end)
    return web.Response(status=200)


async def get_internal_user_count_collection(request: web.Request, x_api2_crm_user_key, filter=None) -> web.Response:
    """COUNT for internalUser

    Count all internal users from the system

    :param x_api2_crm_user_key: User Key
    :type x_api2_crm_user_key: str
    :param filter: Filter
    :type filter: str

    """
    return web.Response(status=200)


async def get_internal_user_entity(request: web.Request, x_api2_crm_user_key, internal_user_id, fields=None, application_request_start=None, application_request_end=None) -> web.Response:
    """GET for internalUser

    Return internal user information

    :param x_api2_crm_user_key: User Key
    :type x_api2_crm_user_key: str
    :param internal_user_id: Internal User Key
    :type internal_user_id: str
    :param fields: Comma-separated list of fields to include in the response
    :type fields: str
    :param application_request_start: All Application Requests from this date
    :type application_request_start: str
    :param application_request_end: All Application Requests until this date
    :type application_request_end: str

    """
    application_request_start = util.deserialize_date(application_request_start)
    application_request_end = util.deserialize_date(application_request_end)
    return web.Response(status=200)


async def update_internal_user_entity(request: web.Request, x_api2_crm_user_key, internal_user_id, body) -> web.Response:
    """PUT for internalUser

    

    :param x_api2_crm_user_key: User Key
    :type x_api2_crm_user_key: str
    :param internal_user_id: Internal User Key
    :type internal_user_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = InternalUserEntity.from_dict(body)
    return web.Response(status=200)
