# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.not_found import NotFound
from openapi_server.models.promotion import Promotion
from openapi_server.models.promotion_edit import PromotionEdit


pytestmark = pytest.mark.asyncio

async def test_promotions_id_json_delete(client):
    """Test case for promotions_id_json_delete

    Delete an existing Promotion.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/promotions/{id_jso}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_promotions_id_json_get(client):
    """Test case for promotions_id_json_get

    Retrieve a single Promotion.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/promotions/{id_jso}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_promotions_id_json_put(client):
    """Test case for promotions_id_json_put

    Update a Promotion.
    """
    body = {"promotion":{"products_x":[{"id":0},{"id":0}],"customer_categories":[{"id":0},{"id":0}],"discount_amount_percent":5.962134,"lasts":"lasts","code":"code","max_times_used":5,"quantity_x":2,"condition_qty":6,"cumulative":False,"type":"type","condition_price":0.8008282,"enabled":True,"products":[{"id":0},{"id":0}],"discount_amount_fix":1.4658129,"begins_at":"begins_at","expires_at":"expires_at","buys_at_least":"buys_at_least","name":"name","categories":[{"id":0},{"id":0}],"customers":"customers","discount_target":"discount_target"}}
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/promotions/{id_jso}'.format(id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_promotions_json_get(client):
    """Test case for promotions_json_get

    Retrieve all Promotions.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example'),
                    ('limit', 56),
                    ('page', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/promotions.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_promotions_json_post(client):
    """Test case for promotions_json_post

    Create a new Promotion.
    """
    body = {"promotion":{"products_x":[{"id":0},{"id":0}],"customer_categories":[{"id":0},{"id":0}],"discount_amount_percent":5.962134,"lasts":"lasts","code":"code","max_times_used":5,"quantity_x":2,"condition_qty":6,"cumulative":False,"type":"type","condition_price":0.8008282,"enabled":True,"products":[{"id":0},{"id":0}],"discount_amount_fix":1.4658129,"begins_at":"begins_at","expires_at":"expires_at","buys_at_least":"buys_at_least","name":"name","categories":[{"id":0},{"id":0}],"customers":"customers","discount_target":"discount_target"}}
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/promotions.json',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

