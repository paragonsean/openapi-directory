# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.create_item_response import CreateItemResponse
from openapi_server.models.delete_item_response import DeleteItemResponse
from openapi_server.models.get_item_response import GetItemResponse
from openapi_server.models.get_items_response import GetItemsResponse
from openapi_server.models.item import Item
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.payment_required_response import PaymentRequiredResponse
from openapi_server.models.unauthorized_response import UnauthorizedResponse
from openapi_server.models.unexpected_error_response import UnexpectedErrorResponse
from openapi_server.models.unprocessable_response import UnprocessableResponse
from openapi_server.models.update_item_response import UpdateItemResponse


pytestmark = pytest.mark.asyncio

async def test_items_add(client):
    """Test case for items_add

    Create Item
    """
    body = {"code":"11910345","hidden":True,"tax_ids":["12345","67890"],"absent_at_location_ids":["12345","67890"],"available":True,"created_at":"2020-09-30T07:43:32Z","description":"Hot Chocolate","custom_mappings":"{}","present_at_all_locations":False,"use_default_tax_rates":False,"updated_at":"2020-09-30T07:43:32Z","variations":[{"id":"12345","image_ids":["12345","67890"],"item_id":"12345","name":"Food","price_amount":10,"price_currency":"USD","pricing_type":"fixed","sequence":0,"sku":"11910345"}],"options":[{"attribute_id":"12345","name":"Option 1","id":"12345"},{"attribute_id":"12345","name":"Option 1","id":"12345"}],"idempotency_key":"random_string","categories":[{"id":"12345","image_ids":["12345","67890"],"name":"Food"}],"id":"#cocoa","sku":"11910345","price_currency":"USD","cost":2,"modifier_groups":[{"id":"12345"}],"price_amount":10,"abbreviation":"Ch","created_by":"12345","version":"12345","pricing_type":"fixed","deleted":True,"product_type":"regular","name":"Cocoa","updated_by":"12345","is_revenue":False,"available_for_pickup":False,"available_online":False}
    params = [('raw', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pos/items',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_items_all(client):
    """Test case for items_all

    List Items
    """
    params = [('raw', False),
                    ('cursor', 'cursor_example'),
                    ('limit', 20),
                    ('fields', 'id,updated_at')]
    headers = { 
        'Accept': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pos/items',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_items_delete(client):
    """Test case for items_delete

    Delete Item
    """
    params = [('raw', False)]
    headers = { 
        'Accept': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/pos/items/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_items_one(client):
    """Test case for items_one

    Get Item
    """
    params = [('raw', False),
                    ('fields', 'id,updated_at')]
    headers = { 
        'Accept': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pos/items/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_items_update(client):
    """Test case for items_update

    Update Item
    """
    body = {"code":"11910345","hidden":True,"tax_ids":["12345","67890"],"absent_at_location_ids":["12345","67890"],"available":True,"created_at":"2020-09-30T07:43:32Z","description":"Hot Chocolate","custom_mappings":"{}","present_at_all_locations":False,"use_default_tax_rates":False,"updated_at":"2020-09-30T07:43:32Z","variations":[{"id":"12345","image_ids":["12345","67890"],"item_id":"12345","name":"Food","price_amount":10,"price_currency":"USD","pricing_type":"fixed","sequence":0,"sku":"11910345"}],"options":[{"attribute_id":"12345","name":"Option 1","id":"12345"},{"attribute_id":"12345","name":"Option 1","id":"12345"}],"idempotency_key":"random_string","categories":[{"id":"12345","image_ids":["12345","67890"],"name":"Food"}],"id":"#cocoa","sku":"11910345","price_currency":"USD","cost":2,"modifier_groups":[{"id":"12345"}],"price_amount":10,"abbreviation":"Ch","created_by":"12345","version":"12345","pricing_type":"fixed","deleted":True,"product_type":"regular","name":"Cocoa","updated_by":"12345","is_revenue":False,"available_for_pickup":False,"available_online":False}
    params = [('raw', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/pos/items/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

