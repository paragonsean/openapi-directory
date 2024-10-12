# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.deletescorebyfield_request import DeletescorebyfieldRequest
from openapi_server.models.putscorebyfield_request import PutscorebyfieldRequest
from openapi_server.models.putscores_request import PutscoresRequest


pytestmark = pytest.mark.asyncio

async def test_deletescorebyfield(client):
    """Test case for deletescorebyfield

    Delete score by field
    """
    body = {"key":"first key"}
    headers = { 
        'Content-Type': 'application/json',
        'accept': 'application/vnd.vtex.ds.v10+json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dataentities/{acronym}/documents/{id}/score/{field_name}'.format(acronym='{{acronym}}', id='{{id}}', field_name='{{field-name}}'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_putscorebyfield(client):
    """Test case for putscorebyfield

    Put score by field
    """
    body = {"key":"first key","point":1,"until":"10m"}
    headers = { 
        'Content-Type': 'application/json',
        'accept': 'application/vnd.vtex.ds.v10+json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dataentities/{acronym}/documents/{id}/score/{field_name}'.format(acronym='{{acronym}}', id='{{id}}', field_name='{{field-name}}'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_putscores(client):
    """Test case for putscores

    Put scores
    """
    body = {"field":"carttag","key":"Payment","point":1,"until":"10m"}
    headers = { 
        'Content-Type': 'application/json',
        'accept': 'application/vnd.vtex.ds.v10+json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dataentities/{acronym}/documents/{id}/score'.format(acronym='{{acronym}}', id='{{id}}'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

