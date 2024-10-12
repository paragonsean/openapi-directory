# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.getversion import Getversion
from openapi_server.models.listversion import Listversion
from openapi_server.models.putversion import Putversion


pytestmark = pytest.mark.asyncio

async def test_getversion(client):
    """Test case for getversion

    Get version
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
        path='/api/dataentities/{acronym}/documents/{id}/versions/{version_id}'.format(acronym='{{acronym}}', id='{{id}}', version_id='{{versionId}}'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listversions(client):
    """Test case for listversions

    List versions
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
        path='/api/dataentities/{acronym}/documents/{id}/versions'.format(acronym='{{acronym}}', id='{{id}}'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_putversion(client):
    """Test case for putversion

    Put version
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/vnd.vtex.ds.v10+json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dataentities/{acronym}/documents/{id}/versions/{version_id}'.format(acronym='{{acronym}}', id='{{id}}', version_id='{{versionId}}'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

