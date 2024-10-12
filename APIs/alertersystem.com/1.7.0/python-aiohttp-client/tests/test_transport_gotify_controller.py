# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_gotify_get_collection200_response import ApiTransportGotifyGetCollection200Response
from openapi_server.models.transport_gotify_get import TransportGotifyGet
from openapi_server.models.transport_gotify_jsonld_get import TransportGotifyJsonldGet
from openapi_server.models.transport_gotify_jsonld_post import TransportGotifyJsonldPost
from openapi_server.models.transport_gotify_jsonld_put import TransportGotifyJsonldPut
from openapi_server.models.transport_gotify_patch import TransportGotifyPatch
from openapi_server.models.transport_gotify_post import TransportGotifyPost
from openapi_server.models.transport_gotify_put import TransportGotifyPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_gotify_get_collection(client):
    """Test case for api_transport_gotify_get_collection

    Retrieves the collection of TransportGotify resources.
    """
    params = [('page', 1),
                    ('dataSegmentCode', 'data_segment_code_example'),
                    ('dataSegmentCode[]', ['data_segment_code_example']),
                    ('partition', 'partition_example'),
                    ('partition[]', ['partition_example']),
                    ('properties[]', ['properties_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-gotify',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_gotify_id_delete(client):
    """Test case for api_transport_gotify_id_delete

    Removes the TransportGotify resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-gotify/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_gotify_id_get(client):
    """Test case for api_transport_gotify_id_get

    Retrieves a TransportGotify resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-gotify/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_gotify_id_patch(client):
    """Test case for api_transport_gotify_id_patch

    Updates the TransportGotify resource.
    """
    body = openapi_server.TransportGotifyPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-gotify/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_gotify_id_put(client):
    """Test case for api_transport_gotify_id_put

    Replaces the TransportGotify resource.
    """
    body = openapi_server.TransportGotifyPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-gotify/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_gotify_post(client):
    """Test case for api_transport_gotify_post

    Creates a TransportGotify resource.
    """
    body = openapi_server.TransportGotifyPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-gotify',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

