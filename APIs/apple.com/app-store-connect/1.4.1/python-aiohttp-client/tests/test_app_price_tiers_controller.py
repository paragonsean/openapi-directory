# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.app_price_points_response import AppPricePointsResponse
from openapi_server.models.app_price_tier_response import AppPriceTierResponse
from openapi_server.models.app_price_tiers_response import AppPriceTiersResponse
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_app_price_tiers_get_collection(client):
    """Test case for app_price_tiers_get_collection

    
    """
    params = [('filter[id]', ['filter_id_example']),
                    ('fields[appPriceTiers]', ['fields_app_price_tiers_example']),
                    ('limit', 56),
                    ('include', ['include_example']),
                    ('fields[appPricePoints]', ['fields_app_price_points_example']),
                    ('limit[pricePoints]', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appPriceTiers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_price_tiers_get_instance(client):
    """Test case for app_price_tiers_get_instance

    
    """
    params = [('fields[appPriceTiers]', ['fields_app_price_tiers_example']),
                    ('include', ['include_example']),
                    ('fields[appPricePoints]', ['fields_app_price_points_example']),
                    ('limit[pricePoints]', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appPriceTiers/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_price_tiers_price_points_get_to_many_related(client):
    """Test case for app_price_tiers_price_points_get_to_many_related

    
    """
    params = [('fields[appPricePoints]', ['fields_app_price_points_example']),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appPriceTiers/{id}/pricePoints'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

