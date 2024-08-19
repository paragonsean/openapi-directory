# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.aggregate import Aggregate
from openapi_server.models.bulk_entity import BulkEntity
from openapi_server.models.bulk_entity_relation import BulkEntityRelation
from openapi_server.models.count import Count
from openapi_server.models.quote_describe import QuoteDescribe
from openapi_server.models.quote_entity import QuoteEntity
from openapi_server.models.quote_entity_relation import QuoteEntityRelation


pytestmark = pytest.mark.asyncio

async def test_create_quote_entity(client):
    """Test case for create_quote_entity

    POST for quote
    """
    body = {"shipping_and_handling":4235.91,"address":[{"zip":"47212","country":"USA","city":"Brandenburg","street":"NY","state":"NY","type":"billing"},{"zip":"47212","country":"USA","city":"Brandenburg","street":"NY","state":"NY","type":"billing"}],"total_price":4235.91,"subject":"Sales","created_at":"2000-01-23T04:56:07.000+00:00","description":"Description","discount":[{"percent_value":4235.91,"type":"Work","value":4235.91},{"percent_value":4235.91,"type":"Work","value":4235.91}],"tax":[{"percent_value":4235.91,"type":"Work","value":4235.91},{"percent_value":4235.91,"type":"Work","value":4235.91}],"expiration_date":"1982-11-28","payment_terms":"Net 60","relation":{"note":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"project":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"priceBook":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"quote":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"attachment":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"post":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"contact":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"tag":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"event":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"meeting":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"case":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"email":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"product":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"ticket":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"opportunityProduct":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"opportunity":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"lead":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"call":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"priceBookItem":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"task":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"campaign":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"invoiceItem":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"quoteItem":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"comment":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"invoice":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"user":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"account":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}]},"terms_and_conditions":"Conditions","number":"21312411","carrier":"DHL","updated_at":"2000-01-23T04:56:07.000+00:00","subtotal":4235.91,"adjustment":4235.91,"currency":{"code":"USD"},"grand_total":4235.91,"id":"21312411","status":"active"}
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
        path='/v1/application/entity/quote',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_quote_entity_bulk(client):
    """Test case for create_quote_entity_bulk

    POST bulk  for quote
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
        path='/v1/application/entity/quote/bulk',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_quote_collection_bulk(client):
    """Test case for delete_quote_collection_bulk

    DELETE bulk  for quote
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
        path='/v1/application/entity/quote/bulk',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_quote_entity(client):
    """Test case for delete_quote_entity

    DELETE for quote
    """
    headers = { 
        'x_api2_crm_user_key': 'e2a6379ab878ae7e58119d4ec842bf9c',
        'x_api2_crm_application_key': '7ae5b17008fb414d84981191cf3b66a476ef8bef',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/application/entity/quote/{quote_id}'.format(quote_id='quote_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_quote_aggregate(client):
    """Test case for get_quote_aggregate

    AGGREGATE for quote
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
        path='/v1/application/entity/quote/aggregate',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_quote_collection(client):
    """Test case for get_quote_collection

    GET for quote
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
        path='/v1/application/entity/quote/list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_quote_count_collection(client):
    """Test case for get_quote_count_collection

    COUNT for quote
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
        path='/v1/application/entity/quote/count',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_quote_describe(client):
    """Test case for get_quote_describe

    DESCRIBE for quote
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
        path='/v1/application/entity/quote/describe',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_quote_entity(client):
    """Test case for get_quote_entity

    GET for quote
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
        path='/v1/application/entity/quote/{quote_id}'.format(quote_id='quote_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_quote_entity(client):
    """Test case for update_quote_entity

    PUT for quote
    """
    body = {"shipping_and_handling":4235.91,"address":[{"zip":"47212","country":"USA","city":"Brandenburg","street":"NY","state":"NY","type":"billing"},{"zip":"47212","country":"USA","city":"Brandenburg","street":"NY","state":"NY","type":"billing"}],"total_price":4235.91,"subject":"Sales","created_at":"2000-01-23T04:56:07.000+00:00","description":"Description","discount":[{"percent_value":4235.91,"type":"Work","value":4235.91},{"percent_value":4235.91,"type":"Work","value":4235.91}],"tax":[{"percent_value":4235.91,"type":"Work","value":4235.91},{"percent_value":4235.91,"type":"Work","value":4235.91}],"expiration_date":"1982-11-28","payment_terms":"Net 60","relation":{"note":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"project":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"priceBook":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"quote":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"attachment":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"post":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"contact":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"tag":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"event":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"meeting":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"case":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"email":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"product":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"ticket":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"opportunityProduct":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"opportunity":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"lead":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"call":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"priceBookItem":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"task":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"campaign":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"invoiceItem":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"quoteItem":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"comment":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"invoice":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"user":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}],"account":[{"type":"General","entity":{"id":"21312411"}},{"type":"General","entity":{"id":"21312411"}}]},"terms_and_conditions":"Conditions","number":"21312411","carrier":"DHL","updated_at":"2000-01-23T04:56:07.000+00:00","subtotal":4235.91,"adjustment":4235.91,"currency":{"code":"USD"},"grand_total":4235.91,"id":"21312411","status":"active"}
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
        path='/v1/application/entity/quote/{quote_id}'.format(quote_id='quote_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_quote_entity_bulk(client):
    """Test case for update_quote_entity_bulk

    PUT bulk  for quote
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
        path='/v1/application/entity/quote/bulk',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

