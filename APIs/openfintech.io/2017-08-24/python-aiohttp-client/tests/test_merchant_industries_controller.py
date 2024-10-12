# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.merchant_industries_response import MerchantIndustriesResponse
from openapi_server.models.merchant_industry_response import MerchantIndustryResponse


pytestmark = pytest.mark.asyncio

async def test_merchant_industries_get(client):
    """Test case for merchant_industries_get

    List of merchant industries
    """
    params = [('page[number]', 56),
                    ('page[size]', 56),
                    ('filter[name]', 'filter_name_example')]
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/v1/merchant-industries',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_merchant_industries_id_get(client):
    """Test case for merchant_industries_id_get

    Merchant industry by ID
    """
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/v1/merchant-industries/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

