# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_dish_pairing_for_wine200_response import GetDishPairingForWine200Response
from openapi_server.models.get_wine_description200_response import GetWineDescription200Response
from openapi_server.models.get_wine_pairing200_response import GetWinePairing200Response
from openapi_server.models.get_wine_recommendation200_response import GetWineRecommendation200Response


pytestmark = pytest.mark.asyncio

async def test_get_dish_pairing_for_wine(client):
    """Test case for get_dish_pairing_for_wine

    Dish Pairing for Wine
    """
    params = [('wine', 'malbec')]
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/food/wine/dishes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_wine_description(client):
    """Test case for get_wine_description

    Wine Description
    """
    params = [('wine', 'merlot')]
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/food/wine/description',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_wine_pairing(client):
    """Test case for get_wine_pairing

    Wine Pairing
    """
    params = [('food', 'steak'),
                    ('maxPrice', 50)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/food/wine/pairing',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_wine_recommendation(client):
    """Test case for get_wine_recommendation

    Wine Recommendation
    """
    params = [('wine', 'merlot'),
                    ('maxPrice', 50),
                    ('minRating', 0.7),
                    ('number', 10)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/food/wine/recommendation',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

