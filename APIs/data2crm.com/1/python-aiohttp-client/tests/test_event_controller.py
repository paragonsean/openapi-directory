# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.aggregate import Aggregate
from openapi_server.models.bulk_entity import BulkEntity
from openapi_server.models.bulk_entity_relation import BulkEntityRelation
from openapi_server.models.count import Count
from openapi_server.models.event_describe import EventDescribe
from openapi_server.models.event_entity import EventEntity
from openapi_server.models.event_entity_relation import EventEntityRelation


pytestmark = pytest.mark.asyncio

async def test_create_event_entity(client):
    """Test case for create_event_entity

    POST for event
    """
    body = {"updated_at":"2000-01-23T04:56:07.000+00:00","subject":"Subject of the event","created_at":"2000-01-23T04:56:07.000+00:00","description":"Description of the event","started_at":"2000-01-23T04:56:07.000+00:00","is_all_day":True,"location":"London","id":"21312411","ended_at":"2000-01-23T04:56:07.000+00:00","relation":{"note":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"project":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"priceBook":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"quote":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"attachment":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"post":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"contact":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"tag":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"event":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"meeting":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"case":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"email":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"product":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"ticket":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"opportunityProduct":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"opportunity":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"lead":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"call":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"priceBookItem":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"task":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"campaign":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"invoiceItem":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"quoteItem":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"comment":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"invoice":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"user":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"account":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}]},"status":"Held"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_api2_crm_user_key': 'e2a6379ab878ae7e58119d4ec842bf9c',
        'x_api2_crm_application_key': '7ae5b17008fb414d84981191cf3b66a476ef8bef',
        'x_api2_crm_native_enable': 'x_api2_crm_native_enable_example',
        'x_api2_crm_describe_lifetime': 'x_api2_crm_describe_lifetime_example',
    }
    response = await client.request(
        method='POST',
        path='/v1/application/entity/event',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_event_entity_bulk(client):
    """Test case for create_event_entity_bulk

    POST bulk  for event
    """
    body = {"item":[null,null]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_api2_crm_user_key': 'e2a6379ab878ae7e58119d4ec842bf9c',
        'x_api2_crm_application_key': '7ae5b17008fb414d84981191cf3b66a476ef8bef',
        'x_api2_crm_native_enable': 'x_api2_crm_native_enable_example',
        'x_api2_crm_describe_lifetime': 'x_api2_crm_describe_lifetime_example',
    }
    response = await client.request(
        method='POST',
        path='/v1/application/entity/event/bulk',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_event_collection_bulk(client):
    """Test case for delete_event_collection_bulk

    DELETE bulk  for event
    """
    body = {"item":[null,null]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_api2_crm_user_key': 'e2a6379ab878ae7e58119d4ec842bf9c',
        'x_api2_crm_application_key': '7ae5b17008fb414d84981191cf3b66a476ef8bef',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/application/entity/event/bulk',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_event_entity(client):
    """Test case for delete_event_entity

    DELETE for event
    """
    headers = { 
        'x_api2_crm_user_key': 'e2a6379ab878ae7e58119d4ec842bf9c',
        'x_api2_crm_application_key': '7ae5b17008fb414d84981191cf3b66a476ef8bef',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/application/entity/event/{event_id}'.format(event_id='event_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_event_aggregate(client):
    """Test case for get_event_aggregate

    AGGREGATE for event
    """
    params = [('filter', 'filter_example'),
                    ('pipeline', 'pipeline_example')]
    headers = { 
        'Accept': 'application/json',
        'x_api2_crm_user_key': 'e2a6379ab878ae7e58119d4ec842bf9c',
        'x_api2_crm_application_key': '7ae5b17008fb414d84981191cf3b66a476ef8bef',
        'x_api2_crm_native_enable': 'x_api2_crm_native_enable_example',
        'x_api2_crm_data_enable': 'x_api2_crm_data_enable_example',
        'x_api2_crm_data_build': 'x_api2_crm_data_build_example',
        'x_api2_crm_data_is_final': 'x_api2_crm_data_is_final_example',
        'x_api2_crm_data_strategy': 'x_api2_crm_data_strategy_example',
        'x_api2_crm_data_coherent_entities': 'x_api2_crm_data_coherent_entities_example',
        'x_api2_crm_data_always_actual': 'x_api2_crm_data_always_actual_example',
        'x_api2_crm_data_actual_at': '2013-10-20T19:20:30+01:00',
        'x_api2_crm_describe_lifetime': 'x_api2_crm_describe_lifetime_example',
    }
    response = await client.request(
        method='GET',
        path='/v1/application/entity/event/aggregate',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_event_collection(client):
    """Test case for get_event_collection

    GET for event
    """
    params = [('page_size', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('expand', 'expand_example'),
                    ('fields', 'fields_example'),
                    ('sort', 'sort_example'),
                    ('unique', 'unique_example')]
    headers = { 
        'Accept': 'application/json',
        'x_api2_crm_user_key': 'e2a6379ab878ae7e58119d4ec842bf9c',
        'x_api2_crm_application_key': '7ae5b17008fb414d84981191cf3b66a476ef8bef',
        'x_api2_crm_native_enable': 'x_api2_crm_native_enable_example',
        'x_api2_crm_data_enable': 'x_api2_crm_data_enable_example',
        'x_api2_crm_data_build': 'x_api2_crm_data_build_example',
        'x_api2_crm_data_is_final': 'x_api2_crm_data_is_final_example',
        'x_api2_crm_data_strategy': 'x_api2_crm_data_strategy_example',
        'x_api2_crm_data_coherent_entities': 'x_api2_crm_data_coherent_entities_example',
        'x_api2_crm_data_always_actual': 'x_api2_crm_data_always_actual_example',
        'x_api2_crm_data_actual_at': '2013-10-20T19:20:30+01:00',
        'x_api2_crm_describe_lifetime': 'x_api2_crm_describe_lifetime_example',
    }
    response = await client.request(
        method='GET',
        path='/v1/application/entity/event/list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_event_count_collection(client):
    """Test case for get_event_count_collection

    COUNT for event
    """
    params = [('filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'x_api2_crm_user_key': 'e2a6379ab878ae7e58119d4ec842bf9c',
        'x_api2_crm_application_key': '7ae5b17008fb414d84981191cf3b66a476ef8bef',
        'x_api2_crm_data_enable': 'x_api2_crm_data_enable_example',
        'x_api2_crm_data_build': 'x_api2_crm_data_build_example',
        'x_api2_crm_data_is_final': 'x_api2_crm_data_is_final_example',
        'x_api2_crm_data_strategy': 'x_api2_crm_data_strategy_example',
        'x_api2_crm_data_coherent_entities': 'x_api2_crm_data_coherent_entities_example',
        'x_api2_crm_data_always_actual': 'x_api2_crm_data_always_actual_example',
        'x_api2_crm_data_actual_at': '2013-10-20T19:20:30+01:00',
    }
    response = await client.request(
        method='GET',
        path='/v1/application/entity/event/count',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_event_describe(client):
    """Test case for get_event_describe

    DESCRIBE for event
    """
    headers = { 
        'Accept': 'application/json',
        'x_api2_crm_user_key': 'e2a6379ab878ae7e58119d4ec842bf9c',
        'x_api2_crm_application_key': '7ae5b17008fb414d84981191cf3b66a476ef8bef',
        'x_api2_crm_data_enable': 'x_api2_crm_data_enable_example',
        'x_api2_crm_data_build': 'x_api2_crm_data_build_example',
        'x_api2_crm_data_is_final': 'x_api2_crm_data_is_final_example',
        'x_api2_crm_data_strategy': 'x_api2_crm_data_strategy_example',
        'x_api2_crm_data_coherent_entities': 'x_api2_crm_data_coherent_entities_example',
        'x_api2_crm_data_always_actual': 'x_api2_crm_data_always_actual_example',
        'x_api2_crm_data_actual_at': '2013-10-20T19:20:30+01:00',
        'x_api2_crm_describe_lifetime': 'x_api2_crm_describe_lifetime_example',
    }
    response = await client.request(
        method='GET',
        path='/v1/application/entity/event/describe',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_event_entity(client):
    """Test case for get_event_entity

    GET for event
    """
    params = [('expand', 'expand_example'),
                    ('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'x_api2_crm_user_key': 'e2a6379ab878ae7e58119d4ec842bf9c',
        'x_api2_crm_application_key': '7ae5b17008fb414d84981191cf3b66a476ef8bef',
        'x_api2_crm_native_enable': 'x_api2_crm_native_enable_example',
        'x_api2_crm_data_enable': 'x_api2_crm_data_enable_example',
        'x_api2_crm_data_build': 'x_api2_crm_data_build_example',
        'x_api2_crm_data_is_final': 'x_api2_crm_data_is_final_example',
        'x_api2_crm_data_strategy': 'x_api2_crm_data_strategy_example',
        'x_api2_crm_data_coherent_entities': 'x_api2_crm_data_coherent_entities_example',
        'x_api2_crm_data_always_actual': 'x_api2_crm_data_always_actual_example',
        'x_api2_crm_data_actual_at': '2013-10-20T19:20:30+01:00',
        'x_api2_crm_describe_lifetime': 'x_api2_crm_describe_lifetime_example',
    }
    response = await client.request(
        method='GET',
        path='/v1/application/entity/event/{event_id}'.format(event_id='event_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_event_entity(client):
    """Test case for update_event_entity

    PUT for event
    """
    body = {"updated_at":"2000-01-23T04:56:07.000+00:00","subject":"Subject of the event","created_at":"2000-01-23T04:56:07.000+00:00","description":"Description of the event","started_at":"2000-01-23T04:56:07.000+00:00","is_all_day":True,"location":"London","id":"21312411","ended_at":"2000-01-23T04:56:07.000+00:00","relation":{"note":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"project":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"priceBook":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"quote":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"attachment":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"post":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"contact":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"tag":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"event":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"meeting":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"case":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"email":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"product":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"ticket":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"opportunityProduct":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"opportunity":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"lead":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"call":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"priceBookItem":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"task":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"campaign":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"invoiceItem":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"quoteItem":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"comment":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"invoice":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"user":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"account":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}]},"status":"Held"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_api2_crm_user_key': 'e2a6379ab878ae7e58119d4ec842bf9c',
        'x_api2_crm_application_key': '7ae5b17008fb414d84981191cf3b66a476ef8bef',
        'x_api2_crm_native_enable': 'x_api2_crm_native_enable_example',
        'x_api2_crm_describe_lifetime': 'x_api2_crm_describe_lifetime_example',
    }
    response = await client.request(
        method='PUT',
        path='/v1/application/entity/event/{event_id}'.format(event_id='event_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_event_entity_bulk(client):
    """Test case for update_event_entity_bulk

    PUT bulk  for event
    """
    body = {"item":[null,null]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_api2_crm_user_key': 'e2a6379ab878ae7e58119d4ec842bf9c',
        'x_api2_crm_application_key': '7ae5b17008fb414d84981191cf3b66a476ef8bef',
        'x_api2_crm_native_enable': 'x_api2_crm_native_enable_example',
        'x_api2_crm_describe_lifetime': 'x_api2_crm_describe_lifetime_example',
    }
    response = await client.request(
        method='PUT',
        path='/v1/application/entity/event/bulk',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

