# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_firebase_get_collection200_response import ApiTransportFirebaseGetCollection200Response
from openapi_server.models.transport_firebase_get import TransportFirebaseGet
from openapi_server.models.transport_firebase_jsonld_get import TransportFirebaseJsonldGet
from openapi_server.models.transport_firebase_jsonld_post import TransportFirebaseJsonldPost
from openapi_server.models.transport_firebase_jsonld_put import TransportFirebaseJsonldPut
from openapi_server.models.transport_firebase_patch import TransportFirebasePatch
from openapi_server.models.transport_firebase_post import TransportFirebasePost
from openapi_server.models.transport_firebase_put import TransportFirebasePut


pytestmark = pytest.mark.asyncio

async def test_api_transport_firebase_get_collection(client):
    """Test case for api_transport_firebase_get_collection

    Retrieves the collection of TransportFirebase resources.
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
        path='/api/transport-firebase',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_firebase_id_delete(client):
    """Test case for api_transport_firebase_id_delete

    Removes the TransportFirebase resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-firebase/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_firebase_id_get(client):
    """Test case for api_transport_firebase_id_get

    Retrieves a TransportFirebase resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-firebase/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_firebase_id_patch(client):
    """Test case for api_transport_firebase_id_patch

    Updates the TransportFirebase resource.
    """
    body = openapi_server.TransportFirebasePatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-firebase/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_firebase_id_put(client):
    """Test case for api_transport_firebase_id_put

    Replaces the TransportFirebase resource.
    """
    body = openapi_server.TransportFirebasePut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-firebase/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_firebase_post(client):
    """Test case for api_transport_firebase_post

    Creates a TransportFirebase resource.
    """
    body = openapi_server.TransportFirebasePost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-firebase',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

