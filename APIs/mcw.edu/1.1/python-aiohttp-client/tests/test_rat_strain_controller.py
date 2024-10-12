# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.strain import Strain


pytestmark = pytest.mark.asyncio

async def test_get_all_strains_using_get(client):
    """Test case for get_all_strains_using_get

    Return all active strains in RGD
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/strains/all',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_strain_by_rgd_id_using_get(client):
    """Test case for get_strain_by_rgd_id_using_get

    Return a strain by RGD ID
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/strains/{rgd_id}'.format(rgd_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_strains_by_position_using_get(client):
    """Test case for get_strains_by_position_using_get

    Return all active strains by position
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/strains/{chr}/{start}/{stop}/{map_key}'.format(chr='chr_example', start=56, stop=56, map_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

