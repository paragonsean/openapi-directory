# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.persona import Persona
from openapi_server.models.personas_get200_response import PersonasGet200Response


pytestmark = pytest.mark.asyncio

async def test_personas_get(client):
    """Test case for personas_get

    Get Personas
    """
    params = [('name', 'name_example'),
                    ('count', 20),
                    ('page', 56),
                    ('fields', ['fields_example']),
                    ('expand', ['expand_example'])]
    headers = { 
        'Accept': 'application/json',
        'accessToken': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/personas',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_personas_id_get(client):
    """Test case for personas_id_get

    Get Persona by id
    """
    params = [('fields', ['fields_example']),
                    ('expand', ['expand_example'])]
    headers = { 
        'Accept': 'application/json',
        'accessToken': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/personas/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

