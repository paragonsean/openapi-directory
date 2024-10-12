# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_expo_get_collection200_response import ApiTransportExpoGetCollection200Response
from openapi_server.models.transport_expo_get import TransportExpoGet
from openapi_server.models.transport_expo_jsonld_get import TransportExpoJsonldGet
from openapi_server.models.transport_expo_jsonld_post import TransportExpoJsonldPost
from openapi_server.models.transport_expo_jsonld_put import TransportExpoJsonldPut
from openapi_server.models.transport_expo_patch import TransportExpoPatch
from openapi_server.models.transport_expo_post import TransportExpoPost
from openapi_server.models.transport_expo_put import TransportExpoPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_expo_get_collection(client):
    """Test case for api_transport_expo_get_collection

    Retrieves the collection of TransportExpo resources.
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
        path='/api/transport-expo',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_expo_id_delete(client):
    """Test case for api_transport_expo_id_delete

    Removes the TransportExpo resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-expo/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_expo_id_get(client):
    """Test case for api_transport_expo_id_get

    Retrieves a TransportExpo resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-expo/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_expo_id_patch(client):
    """Test case for api_transport_expo_id_patch

    Updates the TransportExpo resource.
    """
    body = openapi_server.TransportExpoPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-expo/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_expo_id_put(client):
    """Test case for api_transport_expo_id_put

    Replaces the TransportExpo resource.
    """
    body = openapi_server.TransportExpoPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-expo/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_expo_post(client):
    """Test case for api_transport_expo_post

    Creates a TransportExpo resource.
    """
    body = openapi_server.TransportExpoPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-expo',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

