from typing import List, Dict
from aiohttp import web

from openapi_server.models.aggregate import Aggregate
from openapi_server.models.bulk_entity import BulkEntity
from openapi_server.models.bulk_entity_relation import BulkEntityRelation
from openapi_server.models.count import Count
from openapi_server.models.event_describe import EventDescribe
from openapi_server.models.event_entity import EventEntity
from openapi_server.models.event_entity_relation import EventEntityRelation
from openapi_server import util


async def create_event_entity(request: web.Request, x_api2_crm_user_key, x_api2_crm_application_key, body, x_api2_crm_native_enable=None, x_api2_crm_describe_lifetime=None) -> web.Response:
    """POST for event

    Add event into the system

    :param x_api2_crm_user_key: User Key
    :type x_api2_crm_user_key: str
    :param x_api2_crm_application_key: Application Key
    :type x_api2_crm_application_key: str
    :param body: Add event into the system
    :type body: dict | bytes
    :param x_api2_crm_native_enable: Return native response
    :type x_api2_crm_native_enable: str
    :param x_api2_crm_describe_lifetime: Describe lifetime
    :type x_api2_crm_describe_lifetime: str

    """
    body = EventEntity.from_dict(body)
    return web.Response(status=200)


async def create_event_entity_bulk(request: web.Request, x_api2_crm_user_key, x_api2_crm_application_key, body, x_api2_crm_native_enable=None, x_api2_crm_describe_lifetime=None) -> web.Response:
    """POST bulk  for event

    Add event into the system

    :param x_api2_crm_user_key: User Key
    :type x_api2_crm_user_key: str
    :param x_api2_crm_application_key: Application Key
    :type x_api2_crm_application_key: str
    :param body: Add event into the system
    :type body: dict | bytes
    :param x_api2_crm_native_enable: Return native response
    :type x_api2_crm_native_enable: str
    :param x_api2_crm_describe_lifetime: Describe lifetime
    :type x_api2_crm_describe_lifetime: str

    """
    body = BulkEntity.from_dict(body)
    return web.Response(status=200)


async def delete_event_collection_bulk(request: web.Request, x_api2_crm_user_key, x_api2_crm_application_key, body) -> web.Response:
    """DELETE bulk  for event

    

    :param x_api2_crm_user_key: User Key
    :type x_api2_crm_user_key: str
    :param x_api2_crm_application_key: Application Key
    :type x_api2_crm_application_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = BulkEntity.from_dict(body)
    return web.Response(status=200)


async def delete_event_entity(request: web.Request, x_api2_crm_user_key, x_api2_crm_application_key, event_id) -> web.Response:
    """DELETE for event

    Delete event information

    :param x_api2_crm_user_key: User Key
    :type x_api2_crm_user_key: str
    :param x_api2_crm_application_key: Application Key
    :type x_api2_crm_application_key: str
    :param event_id: Event Identifier
    :type event_id: str

    """
    return web.Response(status=200)


async def get_event_aggregate(request: web.Request, x_api2_crm_user_key, x_api2_crm_application_key, x_api2_crm_native_enable=None, x_api2_crm_data_enable=None, x_api2_crm_data_build=None, x_api2_crm_data_is_final=None, x_api2_crm_data_strategy=None, x_api2_crm_data_coherent_entities=None, x_api2_crm_data_always_actual=None, x_api2_crm_data_actual_at=None, x_api2_crm_describe_lifetime=None, filter=None, pipeline=None) -> web.Response:
    """AGGREGATE for event

    Returns aggregate for events

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


async def get_event_collection(request: web.Request, x_api2_crm_user_key, x_api2_crm_application_key, x_api2_crm_native_enable=None, x_api2_crm_data_enable=None, x_api2_crm_data_build=None, x_api2_crm_data_is_final=None, x_api2_crm_data_strategy=None, x_api2_crm_data_coherent_entities=None, x_api2_crm_data_always_actual=None, x_api2_crm_data_actual_at=None, x_api2_crm_describe_lifetime=None, page_size=None, page=None, filter=None, expand=None, fields=None, sort=None, unique=None) -> web.Response:
    """GET for event

    Returns all events from the system

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


async def get_event_count_collection(request: web.Request, x_api2_crm_user_key, x_api2_crm_application_key, x_api2_crm_data_enable=None, x_api2_crm_data_build=None, x_api2_crm_data_is_final=None, x_api2_crm_data_strategy=None, x_api2_crm_data_coherent_entities=None, x_api2_crm_data_always_actual=None, x_api2_crm_data_actual_at=None, filter=None) -> web.Response:
    """COUNT for event

    Count all events from the system

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


async def get_event_describe(request: web.Request, x_api2_crm_user_key, x_api2_crm_application_key, x_api2_crm_data_enable=None, x_api2_crm_data_build=None, x_api2_crm_data_is_final=None, x_api2_crm_data_strategy=None, x_api2_crm_data_coherent_entities=None, x_api2_crm_data_always_actual=None, x_api2_crm_data_actual_at=None, x_api2_crm_describe_lifetime=None) -> web.Response:
    """DESCRIBE for event

    Returns describe for events

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


async def get_event_entity(request: web.Request, x_api2_crm_user_key, x_api2_crm_application_key, event_id, x_api2_crm_native_enable=None, x_api2_crm_data_enable=None, x_api2_crm_data_build=None, x_api2_crm_data_is_final=None, x_api2_crm_data_strategy=None, x_api2_crm_data_coherent_entities=None, x_api2_crm_data_always_actual=None, x_api2_crm_data_actual_at=None, x_api2_crm_describe_lifetime=None, expand=None, fields=None) -> web.Response:
    """GET for event

    Return event information

    :param x_api2_crm_user_key: User Key
    :type x_api2_crm_user_key: str
    :param x_api2_crm_application_key: Application Key
    :type x_api2_crm_application_key: str
    :param event_id: Event Identifier
    :type event_id: str
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


async def update_event_entity(request: web.Request, x_api2_crm_user_key, x_api2_crm_application_key, event_id, body, x_api2_crm_native_enable=None, x_api2_crm_describe_lifetime=None) -> web.Response:
    """PUT for event

    Update event information

    :param x_api2_crm_user_key: User Key
    :type x_api2_crm_user_key: str
    :param x_api2_crm_application_key: Application Key
    :type x_api2_crm_application_key: str
    :param event_id: Event Identifier
    :type event_id: str
    :param body: Update event information
    :type body: dict | bytes
    :param x_api2_crm_native_enable: Return native response
    :type x_api2_crm_native_enable: str
    :param x_api2_crm_describe_lifetime: Describe lifetime
    :type x_api2_crm_describe_lifetime: str

    """
    body = EventEntity.from_dict(body)
    return web.Response(status=200)


async def update_event_entity_bulk(request: web.Request, x_api2_crm_user_key, x_api2_crm_application_key, body, x_api2_crm_native_enable=None, x_api2_crm_describe_lifetime=None) -> web.Response:
    """PUT bulk  for event

    

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
