# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_vonage_get_collection200_response import ApiTransportVonageGetCollection200Response
from openapi_server.models.transport_vonage_get import TransportVonageGet
from openapi_server.models.transport_vonage_jsonld_get import TransportVonageJsonldGet
from openapi_server.models.transport_vonage_jsonld_post import TransportVonageJsonldPost
from openapi_server.models.transport_vonage_jsonld_put import TransportVonageJsonldPut
from openapi_server.models.transport_vonage_patch import TransportVonagePatch
from openapi_server.models.transport_vonage_post import TransportVonagePost
from openapi_server.models.transport_vonage_put import TransportVonagePut


pytestmark = pytest.mark.asyncio

async def test_api_transport_vonage_get_collection(client):
    """Test case for api_transport_vonage_get_collection

    Retrieves the collection of TransportVonage resources.
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
        path='/api/transport-vonage',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_vonage_id_delete(client):
    """Test case for api_transport_vonage_id_delete

    Removes the TransportVonage resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-vonage/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_vonage_id_get(client):
    """Test case for api_transport_vonage_id_get

    Retrieves a TransportVonage resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-vonage/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_vonage_id_patch(client):
    """Test case for api_transport_vonage_id_patch

    Updates the TransportVonage resource.
    """
    body = openapi_server.TransportVonagePatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-vonage/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_vonage_id_put(client):
    """Test case for api_transport_vonage_id_put

    Replaces the TransportVonage resource.
    """
    body = openapi_server.TransportVonagePut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-vonage/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_vonage_post(client):
    """Test case for api_transport_vonage_post

    Creates a TransportVonage resource.
    """
    body = openapi_server.TransportVonagePost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-vonage',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

