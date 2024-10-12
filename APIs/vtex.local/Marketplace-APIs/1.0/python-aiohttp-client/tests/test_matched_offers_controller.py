# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_matched_offers_response import GetMatchedOffersResponse


pytestmark = pytest.mark.asyncio

async def test_get_productoffers(client):
    """Test case for get_productoffers

    Get Matched Offer's Data by Product ID
    """
    params = [('accountName', 'apiexamples'),
                    ('environment', 'vtexcommercestable')]
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/offer-manager/pvt/product/{product_id}'.format(product_id='123456'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sk_uoffers(client):
    """Test case for get_sk_uoffers

    Get Matched Offer's Data by SKU ID
    """
    params = [('accountName', 'apiexamples'),
                    ('environment', 'vtexcommercestable')]
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/offer-manager/pvt/product/{product_id}/sku/{sku_id}'.format(product_id='123456', sku_id='1234'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getofferslist(client):
    """Test case for getofferslist

    Get Matched Offers List
    """
    params = [('sort', 'availability,desc'),
                    ('rows', 20),
                    ('start', 21),
                    ('fq', 'skuId:172'),
                    ('accountName', 'apiexamples'),
                    ('environment', 'vtexcommercestable')]
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/offer-manager/pvt/offers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

