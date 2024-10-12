# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.getdataentityfields import Getdataentityfields
from openapi_server.models.listdataentity import Listdataentity


pytestmark = pytest.mark.asyncio

async def test_getdataentitystructure(client):
    """Test case for getdataentitystructure

    Get data entity structure
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/vnd.vtex.ds.v10+json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dataentities/{acronym}'.format(acronym='{{acronym}}'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listdataentities(client):
    """Test case for listdataentities

    List data entities
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/vnd.vtex.ds.v10+json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dataentities',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

