# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.import_read import ImportRead
from openapi_server.models.import_write import ImportWrite


pytestmark = pytest.mark.asyncio

async def test_get_import_collection(client):
    """Test case for get_import_collection

    Retrieves the collection of Import resources.
    """
    params = [('projectId', 'project_id_example'),
                    ('page', 56)]
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/imports',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_import_item(client):
    """Test case for get_import_item

    Retrieves a Import resource.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/imports/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_post_import_collection(client):
    """Test case for post_import_collection

    Creates a Import resource.
    """
    _import = openapi_server.ImportWrite()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/ld+json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/imports',
        headers=headers,
        json=_import,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

