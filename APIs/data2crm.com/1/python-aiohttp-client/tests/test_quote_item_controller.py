# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.aggregate import Aggregate
from openapi_server.models.bulk_entity import BulkEntity
from openapi_server.models.bulk_entity_relation import BulkEntityRelation
from openapi_server.models.count import Count
from openapi_server.models.quote_item_describe import QuoteItemDescribe
from openapi_server.models.quote_item_entity import QuoteItemEntity
from openapi_server.models.quote_item_entity_relation import QuoteItemEntityRelation


pytestmark = pytest.mark.asyncio

async def test_create_quote_item_entity(client):
    """Test case for create_quote_item_entity

    POST for quoteItem
    """
    body = {"quantity":4235.91,"total_price":4235.91,"created_at":"2000-01-23T04:56:07.000+00:00","description":"Description","discount":[{"percent_value":4235.91,"type":"Work","value":4235.91},{"percent_value":4235.91,"type":"Work","value":4235.91}],"tax":[{"percent_value":4235.91,"type":"Work","value":4235.91},{"percent_value":4235.91,"type":"Work","value":4235.91}],"list_price":4235.91,"relation":{"note":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"project":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"priceBook":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"quote":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"attachment":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"post":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"contact":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"tag":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"event":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"meeting":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"case":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"email":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"product":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"ticket":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"opportunityProduct":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"opportunity":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"lead":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"call":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"priceBookItem":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"task":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"campaign":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"invoiceItem":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"quoteItem":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"comment":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"invoice":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"user":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"account":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}]},"number":"21312411","unit":"kg","updated_at":"2000-01-23T04:56:07.000+00:00","subtotal":4235.91,"sales_price":4235.91,"id":"21312411"}
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
        path='/v1/application/entity/quoteItem',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_quote_item_entity_bulk(client):
    """Test case for create_quote_item_entity_bulk

    POST bulk  for quoteItem
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
        path='/v1/application/entity/quoteItem/bulk',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_quote_item_collection_bulk(client):
    """Test case for delete_quote_item_collection_bulk

    DELETE bulk  for quoteItem
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
        path='/v1/application/entity/quoteItem/bulk',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_quote_item_entity(client):
    """Test case for delete_quote_item_entity

    DELETE for quoteItem
    """
    headers = { 
        'x_api2_crm_user_key': 'e2a6379ab878ae7e58119d4ec842bf9c',
        'x_api2_crm_application_key': '7ae5b17008fb414d84981191cf3b66a476ef8bef',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/application/entity/quoteItem/{quote_item_id}'.format(quote_item_id='quote_item_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_quote_item_aggregate(client):
    """Test case for get_quote_item_aggregate

    AGGREGATE for quoteItem
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
        path='/v1/application/entity/quoteItem/aggregate',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_quote_item_collection(client):
    """Test case for get_quote_item_collection

    GET for quoteItem
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
        path='/v1/application/entity/quoteItem/list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_quote_item_count_collection(client):
    """Test case for get_quote_item_count_collection

    COUNT for quoteItem
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
        path='/v1/application/entity/quoteItem/count',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_quote_item_describe(client):
    """Test case for get_quote_item_describe

    DESCRIBE for quoteItem
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
        path='/v1/application/entity/quoteItem/describe',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_quote_item_entity(client):
    """Test case for get_quote_item_entity

    GET for quoteItem
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
        path='/v1/application/entity/quoteItem/{quote_item_id}'.format(quote_item_id='quote_item_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_quote_item_entity(client):
    """Test case for update_quote_item_entity

    PUT for quoteItem
    """
    body = {"quantity":4235.91,"total_price":4235.91,"created_at":"2000-01-23T04:56:07.000+00:00","description":"Description","discount":[{"percent_value":4235.91,"type":"Work","value":4235.91},{"percent_value":4235.91,"type":"Work","value":4235.91}],"tax":[{"percent_value":4235.91,"type":"Work","value":4235.91},{"percent_value":4235.91,"type":"Work","value":4235.91}],"list_price":4235.91,"relation":{"note":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"project":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"priceBook":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"quote":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"attachment":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"post":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"contact":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"tag":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"event":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"meeting":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"case":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"email":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"product":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"ticket":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"opportunityProduct":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"opportunity":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"lead":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"call":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"priceBookItem":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"task":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"campaign":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"invoiceItem":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"quoteItem":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"comment":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"invoice":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"user":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"account":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}]},"number":"21312411","unit":"kg","updated_at":"2000-01-23T04:56:07.000+00:00","subtotal":4235.91,"sales_price":4235.91,"id":"21312411"}
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
        path='/v1/application/entity/quoteItem/{quote_item_id}'.format(quote_item_id='quote_item_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_quote_item_entity_bulk(client):
    """Test case for update_quote_item_entity_bulk

    PUT bulk  for quoteItem
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
        path='/v1/application/entity/quoteItem/bulk',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

