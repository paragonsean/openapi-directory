# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.awards import Awards


pytestmark = pytest.mark.asyncio

async def test_awards_get(client):
    """Test case for awards_get

    Gets all awards for requested year
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Awards/ByYear/{year}'.format(year='year_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_awardsby_winner_get(client):
    """Test case for awardsby_winner_get

    Gets all awards by nominiee
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Awards/ByWinner/{access_token}/{nominee}'.format(access_token='access_token_example', nominee='nominee_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

