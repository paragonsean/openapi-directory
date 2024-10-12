# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_sinch_get_collection200_response import ApiTransportSinchGetCollection200Response
from openapi_server.models.transport_sinch_get import TransportSinchGet
from openapi_server.models.transport_sinch_jsonld_get import TransportSinchJsonldGet
from openapi_server.models.transport_sinch_jsonld_post import TransportSinchJsonldPost
from openapi_server.models.transport_sinch_jsonld_put import TransportSinchJsonldPut
from openapi_server.models.transport_sinch_patch import TransportSinchPatch
from openapi_server.models.transport_sinch_post import TransportSinchPost
from openapi_server.models.transport_sinch_put import TransportSinchPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_sinch_get_collection(client):
    """Test case for api_transport_sinch_get_collection

    Retrieves the collection of TransportSinch resources.
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
        path='/api/transport-sinch',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_sinch_id_delete(client):
    """Test case for api_transport_sinch_id_delete

    Removes the TransportSinch resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-sinch/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_sinch_id_get(client):
    """Test case for api_transport_sinch_id_get

    Retrieves a TransportSinch resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-sinch/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_sinch_id_patch(client):
    """Test case for api_transport_sinch_id_patch

    Updates the TransportSinch resource.
    """
    body = openapi_server.TransportSinchPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-sinch/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_sinch_id_put(client):
    """Test case for api_transport_sinch_id_put

    Replaces the TransportSinch resource.
    """
    body = openapi_server.TransportSinchPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-sinch/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_sinch_post(client):
    """Test case for api_transport_sinch_post

    Creates a TransportSinch resource.
    """
    body = openapi_server.TransportSinchPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-sinch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

