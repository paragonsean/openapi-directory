# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.marker import Marker
from openapi_server.models.marker_write import MarkerWrite


pytestmark = pytest.mark.asyncio

async def test_delete_marker_item(client):
    """Test case for delete_marker_item

    Removes the Marker resource.
    """
    headers = { 
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/markers/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_marker_item(client):
    """Test case for get_marker_item

    Retrieves a Marker resource.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/markers/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_post_marker_collection(client):
    """Test case for post_marker_collection

    Creates a Marker resource.
    """
    marker = openapi_server.MarkerWrite()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/ld+json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/markers',
        headers=headers,
        json=marker,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_put_marker_item(client):
    """Test case for put_marker_item

    Replaces the Marker resource.
    """
    marker = {"maximumOccurrence":0,"minimumOccurrence":6,"regex":"regex","transformers":["transformers","transformers"],"name":"name","options":["options","options"],"id":"id","type":"type"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/ld+json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/markers/{id}'.format(id='id_example'),
        headers=headers,
        json=marker,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

