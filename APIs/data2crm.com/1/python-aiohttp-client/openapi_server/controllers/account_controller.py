from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_describe import AccountDescribe
from openapi_server.models.account_entity import AccountEntity
from openapi_server.models.account_entity_relation import AccountEntityRelation
from openapi_server.models.aggregate import Aggregate
from openapi_server.models.bulk_entity import BulkEntity
from openapi_server.models.bulk_entity_relation import BulkEntityRelation
from openapi_server.models.count import Count
from openapi_server import util


async def create_account_entity(request: web.Request, x_api2_crm_user_key, x_api2_crm_application_key, body, x_api2_crm_native_enable=None, x_api2_crm_describe_lifetime=None) -> web.Response:
    """POST for account

    Add account into the system

    :param x_api2_crm_user_key: User Key
    :type x_api2_crm_user_key: str
    :param x_api2_crm_application_key: Application Key
    :type x_api2_crm_application_key: str
    :param body: Add account into the system
    :type body: dict | bytes
    :param x_api2_crm_native_enable: Return native response
    :type x_api2_crm_native_enable: str
    :param x_api2_crm_describe_lifetime: Describe lifetime
    :type x_api2_crm_describe_lifetime: str

    """
    body = AccountEntity.from_dict(body)
    return web.Response(status=200)


async def create_account_entity_bulk(request: web.Request, x_api2_crm_user_key, x_api2_crm_application_key, body, x_api2_crm_native_enable=None, x_api2_crm_describe_lifetime=None) -> web.Response:
    """POST bulk  for account

    Add account into the system

    :param x_api2_crm_user_key: User Key
    :type x_api2_crm_user_key: str
    :param x_api2_crm_application_key: Application Key
    :type x_api2_crm_application_key: str
    :param body: Add account into the system
    :type body: dict | bytes
    :param x_api2_crm_native_enable: Return native response
    :type x_api2_crm_native_enable: str
    :param x_api2_crm_describe_lifetime: Describe lifetime
    :type x_api2_crm_describe_lifetime: str

    """
    body = BulkEntity.from_dict(body)
    return web.Response(status=200)


async def delete_account_collection_bulk(request: web.Request, x_api2_crm_user_key, x_api2_crm_application_key, body) -> web.Response:
    """DELETE bulk  for account

    

    :param x_api2_crm_user_key: User Key
    :type x_api2_crm_user_key: str
    :param x_api2_crm_application_key: Application Key
    :type x_api2_crm_application_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = BulkEntity.from_dict(body)
    return web.Response(status=200)


async def delete_account_entity(request: web.Request, x_api2_crm_user_key, x_api2_crm_application_key, account_id) -> web.Response:
    """DELETE for account

    Delete account information

    :param x_api2_crm_user_key: User Key
    :type x_api2_crm_user_key: str
    :param x_api2_crm_application_key: Application Key
    :type x_api2_crm_application_key: str
    :param account_id: Account Identifier
    :type account_id: str

    """
    return web.Response(status=200)


async def get_account_aggregate(request: web.Request, x_api2_crm_user_key, x_api2_crm_application_key, x_api2_crm_native_enable=None, x_api2_crm_data_enable=None, x_api2_crm_data_build=None, x_api2_crm_data_is_final=None, x_api2_crm_data_strategy=None, x_api2_crm_data_coherent_entities=None, x_api2_crm_data_always_actual=None, x_api2_crm_data_actual_at=None, x_api2_crm_describe_lifetime=None, filter=None, pipeline=None) -> web.Response:
    """AGGREGATE for account

    Returns aggregate for accounts

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


async def get_account_collection(request: web.Request, x_api2_crm_user_key, x_api2_crm_application_key, x_api2_crm_native_enable=None, x_api2_crm_data_enable=None, x_api2_crm_data_build=None, x_api2_crm_data_is_final=None, x_api2_crm_data_strategy=None, x_api2_crm_data_coherent_entities=None, x_api2_crm_data_always_actual=None, x_api2_crm_data_actual_at=None, x_api2_crm_describe_lifetime=None, page_size=None, page=None, filter=None, expand=None, fields=None, sort=None, unique=None) -> web.Response:
    """GET for account

    Returns all accounts from the system

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


async def get_account_count_collection(request: web.Request, x_api2_crm_user_key, x_api2_crm_application_key, x_api2_crm_data_enable=None, x_api2_crm_data_build=None, x_api2_crm_data_is_final=None, x_api2_crm_data_strategy=None, x_api2_crm_data_coherent_entities=None, x_api2_crm_data_always_actual=None, x_api2_crm_data_actual_at=None, filter=None) -> web.Response:
    """COUNT for account

    Count all accounts from the system

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


async def get_account_describe(request: web.Request, x_api2_crm_user_key, x_api2_crm_application_key, x_api2_crm_data_enable=None, x_api2_crm_data_build=None, x_api2_crm_data_is_final=None, x_api2_crm_data_strategy=None, x_api2_crm_data_coherent_entities=None, x_api2_crm_data_always_actual=None, x_api2_crm_data_actual_at=None, x_api2_crm_describe_lifetime=None) -> web.Response:
    """DESCRIBE for account

    Returns describe for accounts

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


async def get_account_entity(request: web.Request, x_api2_crm_user_key, x_api2_crm_application_key, account_id, x_api2_crm_native_enable=None, x_api2_crm_data_enable=None, x_api2_crm_data_build=None, x_api2_crm_data_is_final=None, x_api2_crm_data_strategy=None, x_api2_crm_data_coherent_entities=None, x_api2_crm_data_always_actual=None, x_api2_crm_data_actual_at=None, x_api2_crm_describe_lifetime=None, expand=None, fields=None) -> web.Response:
    """GET for account

    Return account information

    :param x_api2_crm_user_key: User Key
    :type x_api2_crm_user_key: str
    :param x_api2_crm_application_key: Application Key
    :type x_api2_crm_application_key: str
    :param account_id: Account Identifier
    :type account_id: str
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


async def update_account_entity(request: web.Request, x_api2_crm_user_key, x_api2_crm_application_key, account_id, body, x_api2_crm_native_enable=None, x_api2_crm_describe_lifetime=None) -> web.Response:
    """PUT for account

    Update account information

    :param x_api2_crm_user_key: User Key
    :type x_api2_crm_user_key: str
    :param x_api2_crm_application_key: Application Key
    :type x_api2_crm_application_key: str
    :param account_id: Account Identifier
    :type account_id: str
    :param body: Update account information
    :type body: dict | bytes
    :param x_api2_crm_native_enable: Return native response
    :type x_api2_crm_native_enable: str
    :param x_api2_crm_describe_lifetime: Describe lifetime
    :type x_api2_crm_describe_lifetime: str

    """
    body = AccountEntity.from_dict(body)
    return web.Response(status=200)


async def update_account_entity_bulk(request: web.Request, x_api2_crm_user_key, x_api2_crm_application_key, body, x_api2_crm_native_enable=None, x_api2_crm_describe_lifetime=None) -> web.Response:
    """PUT bulk  for account

    

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
