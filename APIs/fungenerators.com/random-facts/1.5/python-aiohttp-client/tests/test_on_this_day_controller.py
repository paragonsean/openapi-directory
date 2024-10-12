# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_fact_onthisday_born_get(client):
    """Test case for fact_onthisday_born_get

    
    """
    params = [('month', 'month_example'),
                    ('day', 'day_example')]
    headers = { 
        'Accept': 'application/json',
        'X-Fungenerators-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/fact/onthisday/born',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fact_onthisday_died_get(client):
    """Test case for fact_onthisday_died_get

    
    """
    params = [('month', 'month_example'),
                    ('day', 'day_example')]
    headers = { 
        'Accept': 'application/json',
        'X-Fungenerators-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/fact/onthisday/died',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fact_onthisday_event_get(client):
    """Test case for fact_onthisday_event_get

    
    """
    params = [('month', 'month_example'),
                    ('day', 'day_example')]
    headers = { 
        'Accept': 'application/json',
        'X-Fungenerators-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/fact/onthisday/event',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

