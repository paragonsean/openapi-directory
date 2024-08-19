from typing import List, Dict
from aiohttp import web

from openapi_server.models.aggregate import Aggregate
from openapi_server.models.bulk_entity import BulkEntity
from openapi_server.models.bulk_entity_relation import BulkEntityRelation
from openapi_server.models.count import Count
from openapi_server.models.email_describe import EmailDescribe
from openapi_server.models.email_entity import EmailEntity
from openapi_server.models.email_entity_relation import EmailEntityRelation
from openapi_server import util


async def create_email_entity(request: web.Request, x_api2_crm_user_key, x_api2_crm_application_key, body, x_api2_crm_native_enable=None, x_api2_crm_describe_lifetime=None) -> web.Response:
    """POST for email

    Add email into the system

    :param x_api2_crm_user_key: User Key
    :type x_api2_crm_user_key: str
    :param x_api2_crm_application_key: Application Key
    :type x_api2_crm_application_key: str
    :param body: Add email into the system
    :type body: dict | bytes
    :param x_api2_crm_native_enable: Return native response
    :type x_api2_crm_native_enable: str
    :param x_api2_crm_describe_lifetime: Describe lifetime
    :type x_api2_crm_describe_lifetime: str

    """
    body = EmailEntity.from_dict(body)
    return web.Response(status=200)


async def create_email_entity_bulk(request: web.Request, x_api2_crm_user_key, x_api2_crm_application_key, body, x_api2_crm_native_enable=None, x_api2_crm_describe_lifetime=None) -> web.Response:
    """POST bulk  for email

    Add email into the system

    :param x_api2_crm_user_key: User Key
    :type x_api2_crm_user_key: str
    :param x_api2_crm_application_key: Application Key
    :type x_api2_crm_application_key: str
    :param body: Add email into the system
    :type body: dict | bytes
    :param x_api2_crm_native_enable: Return native response
    :type x_api2_crm_native_enable: str
    :param x_api2_crm_describe_lifetime: Describe lifetime
    :type x_api2_crm_describe_lifetime: str

    """
    body = BulkEntity.from_dict(body)
    return web.Response(status=200)


async def delete_email_collection_bulk(request: web.Request, x_api2_crm_user_key, x_api2_crm_application_key, body) -> web.Response:
    """DELETE bulk  for email

    

    :param x_api2_crm_user_key: User Key
    :type x_api2_crm_user_key: str
    :param x_api2_crm_application_key: Application Key
    :type x_api2_crm_application_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = BulkEntity.from_dict(body)
    return web.Response(status=200)


async def delete_email_entity(request: web.Request, x_api2_crm_user_key, x_api2_crm_application_key, email_id) -> web.Response:
    """DELETE for email

    Delete email information

    :param x_api2_crm_user_key: User Key
    :type x_api2_crm_user_key: str
    :param x_api2_crm_application_key: Application Key
    :type x_api2_crm_application_key: str
    :param email_id: Email Identifier
    :type email_id: str

    """
    return web.Response(status=200)


async def get_email_aggregate(request: web.Request, x_api2_crm_user_key, x_api2_crm_application_key, x_api2_crm_native_enable=None, x_api2_crm_data_enable=None, x_api2_crm_data_build=None, x_api2_crm_data_is_final=None, x_api2_crm_data_strategy=None, x_api2_crm_data_coherent_entities=None, x_api2_crm_data_always_actual=None, x_api2_crm_data_actual_at=None, x_api2_crm_describe_lifetime=None, filter=None, pipeline=None) -> web.Response:
    """AGGREGATE for email

    Returns aggregate for emails

    :param x_api2_crm_user_key: User Key
    :type x_api2_crm_user_key: str
    :param x_api2_crm_application_key: Application Key
    :type x_api2_crm_application_key: str
    :param x_api2_crm_native_enable: Return native response
    :type x_api2_crm_native_enable: str
    :param x_api2_crm_data_enable: Data Enable
    :type x_api2_crm_data_enable: str
    :param x_api2_crm_data_build: Data Build
    :type x_api2_crm_data_build: str
    :param x_api2_crm_data_is_final: Data Is Final
    :type x_api2_crm_data_is_final: str
    :param x_api2_crm_data_strategy: Data Strategy
    :type x_api2_crm_data_strategy: str
    :param x_api2_crm_data_coherent_entities: Coherent Entities
    :type x_api2_crm_data_coherent_entities: str
    :param x_api2_crm_data_always_actual: Data Is Actual
    :type x_api2_crm_data_always_actual: str
    :param x_api2_crm_data_actual_at: Data Actual At
    :type x_api2_crm_data_actual_at: str
    :param x_api2_crm_describe_lifetime: Describe lifetime
    :type x_api2_crm_describe_lifetime: str
    :param filter: Filter
    :type filter: str
    :param pipeline: Pipeline
    :type pipeline: str

    """
    x_api2_crm_data_actual_at = util.deserialize_datetime(x_api2_crm_data_actual_at)
    return web.Response(status=200)


async def get_email_collection(request: web.Request, x_api2_crm_user_key, x_api2_crm_application_key, x_api2_crm_native_enable=None, x_api2_crm_data_enable=None, x_api2_crm_data_build=None, x_api2_crm_data_is_final=None, x_api2_crm_data_strategy=None, x_api2_crm_data_coherent_entities=None, x_api2_crm_data_always_actual=None, x_api2_crm_data_actual_at=None, x_api2_crm_describe_lifetime=None, page_size=None, page=None, filter=None, expand=None, fields=None, sort=None, unique=None) -> web.Response:
    """GET for email

    Returns all emails from the system

    :param x_api2_crm_user_key: User Key
    :type x_api2_crm_user_key: str
    :param x_api2_crm_application_key: Application Key
    :type x_api2_crm_application_key: str
    :param x_api2_crm_native_enable: Return native response
    :type x_api2_crm_native_enable: str
    :param x_api2_crm_data_enable: Data Enable
    :type x_api2_crm_data_enable: str
    :param x_api2_crm_data_build: Data Build
    :type x_api2_crm_data_build: str
    :param x_api2_crm_data_is_final: Data Is Final
    :type x_api2_crm_data_is_final: str
    :param x_api2_crm_data_strategy: Data Strategy
    :type x_api2_crm_data_strategy: str
    :param x_api2_crm_data_coherent_entities: Coherent Entities
    :type x_api2_crm_data_coherent_entities: str
    :param x_api2_crm_data_always_actual: Data Is Actual
    :type x_api2_crm_data_always_actual: str
    :param x_api2_crm_data_actual_at: Data Actual At
    :type x_api2_crm_data_actual_at: str
    :param x_api2_crm_describe_lifetime: Describe lifetime
    :type x_api2_crm_describe_lifetime: str
    :param page_size: Amount of results (default: 25)
    :type page_size: int
    :param page: Page to show (default: 1)
    :type page: int
    :param filter: Filter
    :type filter: str
    :param expand: Expand relations
    :type expand: str
    :param fields: Comma-separated list of fields to include in the response
    :type fields: str
    :param sort: Specifies ascending or descending sort on existing fields
    :type sort: str
    :param unique: Find all unique values for selected field
    :type unique: str

    """
    x_api2_crm_data_actual_at = util.deserialize_datetime(x_api2_crm_data_actual_at)
    return web.Response(status=200)


async def get_email_count_collection(request: web.Request, x_api2_crm_user_key, x_api2_crm_application_key, x_api2_crm_data_enable=None, x_api2_crm_data_build=None, x_api2_crm_data_is_final=None, x_api2_crm_data_strategy=None, x_api2_crm_data_coherent_entities=None, x_api2_crm_data_always_actual=None, x_api2_crm_data_actual_at=None, filter=None) -> web.Response:
    """COUNT for email

    Count all emails from the system

    :param x_api2_crm_user_key: User Key
    :type x_api2_crm_user_key: str
    :param x_api2_crm_application_key: Application Key
    :type x_api2_crm_application_key: str
    :param x_api2_crm_data_enable: Data Enable
    :type x_api2_crm_data_enable: str
    :param x_api2_crm_data_build: Data Build
    :type x_api2_crm_data_build: str
    :param x_api2_crm_data_is_final: Data Is Final
    :type x_api2_crm_data_is_final: str
    :param x_api2_crm_data_strategy: Data Strategy
    :type x_api2_crm_data_strategy: str
    :param x_api2_crm_data_coherent_entities: Coherent Entities
    :type x_api2_crm_data_coherent_entities: str
    :param x_api2_crm_data_always_actual: Data Is Actual
    :type x_api2_crm_data_always_actual: str
    :param x_api2_crm_data_actual_at: Data Actual At
    :type x_api2_crm_data_actual_at: str
    :param filter: Filter
    :type filter: str

    """
    x_api2_crm_data_actual_at = util.deserialize_datetime(x_api2_crm_data_actual_at)
    return web.Response(status=200)


async def get_email_describe(request: web.Request, x_api2_crm_user_key, x_api2_crm_application_key, x_api2_crm_data_enable=None, x_api2_crm_data_build=None, x_api2_crm_data_is_final=None, x_api2_crm_data_strategy=None, x_api2_crm_data_coherent_entities=None, x_api2_crm_data_always_actual=None, x_api2_crm_data_actual_at=None, x_api2_crm_describe_lifetime=None) -> web.Response:
    """DESCRIBE for email

    Returns describe for emails

    :param x_api2_crm_user_key: User Key
    :type x_api2_crm_user_key: str
    :param x_api2_crm_application_key: Application Key
    :type x_api2_crm_application_key: str
    :param x_api2_crm_data_enable: Data Enable
    :type x_api2_crm_data_enable: str
    :param x_api2_crm_data_build: Data Build
    :type x_api2_crm_data_build: str
    :param x_api2_crm_data_is_final: Data Is Final
    :type x_api2_crm_data_is_final: str
    :param x_api2_crm_data_strategy: Data Strategy
    :type x_api2_crm_data_strategy: str
    :param x_api2_crm_data_coherent_entities: Coherent Entities
    :type x_api2_crm_data_coherent_entities: str
    :param x_api2_crm_data_always_actual: Data Is Actual
    :type x_api2_crm_data_always_actual: str
    :param x_api2_crm_data_actual_at: Data Actual At
    :type x_api2_crm_data_actual_at: str
    :param x_api2_crm_describe_lifetime: Describe lifetime
    :type x_api2_crm_describe_lifetime: str

    """
    x_api2_crm_data_actual_at = util.deserialize_datetime(x_api2_crm_data_actual_at)
    return web.Response(status=200)


async def get_email_entity(request: web.Request, x_api2_crm_user_key, x_api2_crm_application_key, email_id, x_api2_crm_native_enable=None, x_api2_crm_data_enable=None, x_api2_crm_data_build=None, x_api2_crm_data_is_final=None, x_api2_crm_data_strategy=None, x_api2_crm_data_coherent_entities=None, x_api2_crm_data_always_actual=None, x_api2_crm_data_actual_at=None, x_api2_crm_describe_lifetime=None, expand=None, fields=None) -> web.Response:
    """GET for email

    Return email information

    :param x_api2_crm_user_key: User Key
    :type x_api2_crm_user_key: str
    :param x_api2_crm_application_key: Application Key
    :type x_api2_crm_application_key: str
    :param email_id: Email Identifier
    :type email_id: str
    :param x_api2_crm_native_enable: Return native response
    :type x_api2_crm_native_enable: str
    :param x_api2_crm_data_enable: Data Enable
    :type x_api2_crm_data_enable: str
    :param x_api2_crm_data_build: Data Build
    :type x_api2_crm_data_build: str
    :param x_api2_crm_data_is_final: Data Is Final
    :type x_api2_crm_data_is_final: str
    :param x_api2_crm_data_strategy: Data Strategy
    :type x_api2_crm_data_strategy: str
    :param x_api2_crm_data_coherent_entities: Coherent Entities
    :type x_api2_crm_data_coherent_entities: str
    :param x_api2_crm_data_always_actual: Data Is Actual
    :type x_api2_crm_data_always_actual: str
    :param x_api2_crm_data_actual_at: Data Actual At
    :type x_api2_crm_data_actual_at: str
    :param x_api2_crm_describe_lifetime: Describe lifetime
    :type x_api2_crm_describe_lifetime: str
    :param expand: Expand relations
    :type expand: str
    :param fields: Comma-separated list of fields to include in the response
    :type fields: str

    """
    x_api2_crm_data_actual_at = util.deserialize_datetime(x_api2_crm_data_actual_at)
    return web.Response(status=200)


async def update_email_entity(request: web.Request, x_api2_crm_user_key, x_api2_crm_application_key, email_id, body, x_api2_crm_native_enable=None, x_api2_crm_describe_lifetime=None) -> web.Response:
    """PUT for email

    Update email information

    :param x_api2_crm_user_key: User Key
    :type x_api2_crm_user_key: str
    :param x_api2_crm_application_key: Application Key
    :type x_api2_crm_application_key: str
    :param email_id: Email Identifier
    :type email_id: str
    :param body: Update email information
    :type body: dict | bytes
    :param x_api2_crm_native_enable: Return native response
    :type x_api2_crm_native_enable: str
    :param x_api2_crm_describe_lifetime: Describe lifetime
    :type x_api2_crm_describe_lifetime: str

    """
    body = EmailEntity.from_dict(body)
    return web.Response(status=200)


async def update_email_entity_bulk(request: web.Request, x_api2_crm_user_key, x_api2_crm_application_key, body, x_api2_crm_native_enable=None, x_api2_crm_describe_lifetime=None) -> web.Response:
    """PUT bulk  for email

    

    :param x_api2_crm_user_key: User Key
    :type x_api2_crm_user_key: str
    :param x_api2_crm_application_key: Application Key
    :type x_api2_crm_application_key: str
    :param body: 
    :type body: dict | bytes
    :param x_api2_crm_native_enable: Return native response
    :type x_api2_crm_native_enable: str
    :param x_api2_crm_describe_lifetime: Describe lifetime
    :type x_api2_crm_describe_lifetime: str

    """
    body = BulkEntity.from_dict(body)
    return web.Response(status=200)
