# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_update_price_or_fixed_price_request import CreateUpdatePriceOrFixedPriceRequest
from openapi_server.models.createorupdatefixedpricesonpricetableortradepolicy_request_inner import CreateorupdatefixedpricesonpricetableortradepolicyRequestInner
from openapi_server.models.fixed_price import FixedPrice
from openapi_server.models.getcomputedprice import Getcomputedprice
from openapi_server.models.getprice import Getprice


pytestmark = pytest.mark.asyncio

async def test_create_update_price_or_fixed_price(client):
    """Test case for create_update_price_or_fixed_price

    Create or Update Base Price or Fixed Prices
    """
    body = openapi_server.CreateUpdatePriceOrFixedPriceRequest()
    headers = { 
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/pricing/prices/{item_id}'.format(item_id=1),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_createorupdatefixedpricesonpricetableortradepolicy(client):
    """Test case for createorupdatefixedpricesonpricetableortradepolicy

    Create or Update Fixed Prices on a price table or trade policy
    """
    body = [openapi_server.CreateorupdatefixedpricesonpricetableortradepolicyRequestInner()]
    headers = { 
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pricing/prices/{item_id}/fixed/{price_table_id}'.format(item_id=1, price_table_id='priceTableA'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_price(client):
    """Test case for delete_price

    Delete Price
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/pricing/prices/{item_id}'.format(item_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deletefixedpricesonapricetableortradepolicy(client):
    """Test case for deletefixedpricesonapricetableortradepolicy

    Delete Fixed Prices on a price table or trade policy
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/pricing/prices/{item_id}/fixed/{price_table_id}'.format(item_id=1, price_table_id='gold'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_computed_pricebypricetable(client):
    """Test case for get_computed_pricebypricetable

    Get Computed Price by price table or trade policy
    """
    params = [('categoryIds', 1),
                    ('brandId', 3),
                    ('quantity', 2)]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pricing/prices/{item_id}/computed/{price_table_id}'.format(item_id=1, price_table_id='gold'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_fixed_prices(client):
    """Test case for get_fixed_prices

    Get Fixed Prices
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pricing/prices/{item_id}/fixed'.format(item_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_fixed_pricesonapricetable(client):
    """Test case for get_fixed_pricesonapricetable

    Get Fixed Prices on a price table or trade policy
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pricing/prices/{item_id}/fixed/{price_table_id}'.format(item_id=1, price_table_id='gold'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_price(client):
    """Test case for get_price

    Get Price
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pricing/prices/{item_id}'.format(item_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

