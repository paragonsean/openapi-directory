# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_globalwinescores_latest_get(client):
    """Test case for globalwinescores_latest_get

    List all latest GWS
    """
    params = [('wine_id', [[114959,114952]]),
                    ('vintage', '2000'),
                    ('color', 'color_example'),
                    ('is_primeurs', False),
                    ('lwin', '1014033'),
                    ('lwin_11', '10140332000'),
                    ('limit', 100),
                    ('offset', 100),
                    ('ordering', -date)]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Token <YOUR-API-TOKEN>',
        'TokenAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/globalwinescores/latest/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_historical_gws(client):
    """Test case for list_historical_gws

    List all historical GWS
    """
    params = [('wine_id', [[114959,114952]]),
                    ('vintage', '2000'),
                    ('color', 'color_example'),
                    ('is_primeurs', False),
                    ('lwin', '1014033'),
                    ('lwin_11', '10140332000'),
                    ('limit', 100),
                    ('offset', 100),
                    ('ordering', -date)]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Token <YOUR-API-TOKEN>',
        'TokenAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/globalwinescores/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

