from typing import List, Dict
from aiohttp import web

from openapi_server.models.count import Count
from openapi_server.models.field_item_describe import FieldItemDescribe
from openapi_server.models.field_item_entity import FieldItemEntity
from openapi_server.models.field_item_entity_relation import FieldItemEntityRelation
from openapi_server import util


async def create_field_item_entity(request: web.Request, x_api2_crm_user_key, x_api2_crm_application_key, field_id, body, x_api2_crm_describe_lifetime=None) -> web.Response:
    """POST for fieldItem

    Add field item into the system

    :param x_api2_crm_user_key: User Key
    :type x_api2_crm_user_key: str
    :param x_api2_crm_application_key: Application Key
    :type x_api2_crm_application_key: str
    :param field_id: Field Identifier
    :type field_id: str
    :param body: Add field item into the system
    :type body: dict | bytes
    :param x_api2_crm_describe_lifetime: Describe lifetime
    :type x_api2_crm_describe_lifetime: str

    """
    body = FieldItemEntity.from_dict(body)
    return web.Response(status=200)


async def delete_field_item_entity(request: web.Request, x_api2_crm_user_key, x_api2_crm_application_key, field_id, field_item_id) -> web.Response:
    """DELETE for fieldItem

    Delete field item information

    :param x_api2_crm_user_key: User Key
    :type x_api2_crm_user_key: str
    :param x_api2_crm_application_key: Application Key
    :type x_api2_crm_application_key: str
    :param field_id: Field Identifier
    :type field_id: str
    :param field_item_id: Field Item Identifier
    :type field_item_id: str

    """
    return web.Response(status=200)


async def get_field_item_collection(request: web.Request, x_api2_crm_user_key, x_api2_crm_application_key, field_id, x_api2_crm_describe_lifetime=None, page_size=None, page=None, fields=None) -> web.Response:
    """GET for fieldItem

    Returns all fields from the system items

    :param x_api2_crm_user_key: User Key
    :type x_api2_crm_user_key: str
    :param x_api2_crm_application_key: Application Key
    :type x_api2_crm_application_key: str
    :param field_id: Field Identifier
    :type field_id: str
    :param x_api2_crm_describe_lifetime: Describe lifetime
    :type x_api2_crm_describe_lifetime: str
    :param page_size: Amount of results (default: 25)
    :type page_size: int
    :param page: Page to show (default: 1)
    :type page: int
    :param fields: Comma-separated list of fields to include in the response
    :type fields: str

    """
    return web.Response(status=200)


async def get_field_item_count_collection(request: web.Request, x_api2_crm_user_key, x_api2_crm_application_key, field_id) -> web.Response:
    """COUNT for fieldItem

    Count all field items from the system

    :param x_api2_crm_user_key: User Key
    :type x_api2_crm_user_key: str
    :param x_api2_crm_application_key: Application Key
    :type x_api2_crm_application_key: str
    :param field_id: Field Identifier
    :type field_id: str

    """
    return web.Response(status=200)


async def get_field_item_describe(request: web.Request, x_api2_crm_user_key, x_api2_crm_application_key, field_id, x_api2_crm_describe_lifetime=None) -> web.Response:
    """DESCRIBE for fieldItem

    Returns describe for field items

    :param x_api2_crm_user_key: User Key
    :type x_api2_crm_user_key: str
    :param x_api2_crm_application_key: Application Key
    :type x_api2_crm_application_key: str
    :param field_id: Field Identifier
    :type field_id: str
    :param x_api2_crm_describe_lifetime: Describe lifetime
    :type x_api2_crm_describe_lifetime: str

    """
    return web.Response(status=200)


async def get_field_item_entity(request: web.Request, x_api2_crm_user_key, x_api2_crm_application_key, field_id, field_item_id, x_api2_crm_describe_lifetime=None, fields=None) -> web.Response:
    """GET for fieldItem

    Return field item information

    :param x_api2_crm_user_key: User Key
    :type x_api2_crm_user_key: str
    :param x_api2_crm_application_key: Application Key
    :type x_api2_crm_application_key: str
    :param field_id: Field Identifier
    :type field_id: str
    :param field_item_id: Field Item Identifier
    :type field_item_id: str
    :param x_api2_crm_describe_lifetime: Describe lifetime
    :type x_api2_crm_describe_lifetime: str
    :param fields: Comma-separated list of fields to include in the response
    :type fields: str

    """
    return web.Response(status=200)


async def update_field_item_entity(request: web.Request, x_api2_crm_user_key, x_api2_crm_application_key, field_id, field_item_id, body, x_api2_crm_describe_lifetime=None) -> web.Response:
    """PUT for fieldItem

    Update field item information

    :param x_api2_crm_user_key: User Key
    :type x_api2_crm_user_key: str
    :param x_api2_crm_application_key: Application Key
    :type x_api2_crm_application_key: str
    :param field_id: Field Identifier
    :type field_id: str
    :param field_item_id: Field Item Identifier
    :type field_item_id: str
    :param body: Update field item information
    :type body: dict | bytes
    :param x_api2_crm_describe_lifetime: Describe lifetime
    :type x_api2_crm_describe_lifetime: str

    """
    body = FieldItemEntity.from_dict(body)
    return web.Response(status=200)
