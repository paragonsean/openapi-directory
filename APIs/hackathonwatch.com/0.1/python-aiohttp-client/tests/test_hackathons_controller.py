# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_g_et_hackathons_coming_format(client):
    """Test case for g_et_hackathons_coming_format

    Return a list of coming hackathons
    """
    params = [('page', 1)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/hackathons/coming.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_hackathons_id_format(client):
    """Test case for g_et_hackathons_id_format

    Return the detail of a given hackathon
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/hackathons/{id_jso}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

