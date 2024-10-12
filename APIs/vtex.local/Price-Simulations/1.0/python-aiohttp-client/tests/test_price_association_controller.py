# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.request_body import RequestBody
from openapi_server.models.v_custom_prices_rules_post200_response import VCustomPricesRulesPost200Response
from openapi_server.models.v_custom_prices_rules_post_request import VCustomPricesRulesPostRequest


pytestmark = pytest.mark.asyncio

async def test_v_custom_prices_rules_post(client):
    """Test case for v_custom_prices_rules_post

    Create price association
    """
    body = openapi_server.VCustomPricesRulesPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/_v/custom-prices/rules',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v_custom_prices_rules_price_association_id_delete(client):
    """Test case for v_custom_prices_rules_price_association_id_delete

    Disassociate price association by ID
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/_v/custom-prices/rules/{price_association_id}'.format(price_association_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v_custom_prices_rules_price_association_id_get(client):
    """Test case for v_custom_prices_rules_price_association_id_get

    Get price association by ID
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/_v/custom-prices/rules/{price_association_id}'.format(price_association_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v_custom_prices_rules_price_association_id_put(client):
    """Test case for v_custom_prices_rules_price_association_id_put

    Update price association by ID
    """
    body = openapi_server.RequestBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/_v/custom-prices/rules/{price_association_id}'.format(price_association_id=1),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

