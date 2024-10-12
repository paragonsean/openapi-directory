# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.isos_get200_response import IsosGet200Response
from openapi_server.models.isos_id_get200_response import IsosIdGet200Response


pytestmark = pytest.mark.asyncio

async def test_isos_get(client):
    """Test case for isos_get

    Get all ISOs
    """
    params = [('name', 'name_example'),
                    ('architecture', 'architecture_example'),
                    ('include_architecture_wildcard', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/isos',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_isos_id_get(client):
    """Test case for isos_id_get

    Get an ISO
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/isos/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

