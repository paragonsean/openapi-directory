# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_bandwidth_get_collection200_response import ApiTransportBandwidthGetCollection200Response
from openapi_server.models.transport_bandwidth_get import TransportBandwidthGet
from openapi_server.models.transport_bandwidth_jsonld_get import TransportBandwidthJsonldGet
from openapi_server.models.transport_bandwidth_jsonld_post import TransportBandwidthJsonldPost
from openapi_server.models.transport_bandwidth_jsonld_put import TransportBandwidthJsonldPut
from openapi_server.models.transport_bandwidth_patch import TransportBandwidthPatch
from openapi_server.models.transport_bandwidth_post import TransportBandwidthPost
from openapi_server.models.transport_bandwidth_put import TransportBandwidthPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_bandwidth_get_collection(client):
    """Test case for api_transport_bandwidth_get_collection

    Retrieves the collection of TransportBandwidth resources.
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
        path='/api/transport-bandwidth',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_bandwidth_id_delete(client):
    """Test case for api_transport_bandwidth_id_delete

    Removes the TransportBandwidth resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-bandwidth/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_bandwidth_id_get(client):
    """Test case for api_transport_bandwidth_id_get

    Retrieves a TransportBandwidth resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-bandwidth/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_bandwidth_id_patch(client):
    """Test case for api_transport_bandwidth_id_patch

    Updates the TransportBandwidth resource.
    """
    body = openapi_server.TransportBandwidthPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-bandwidth/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_bandwidth_id_put(client):
    """Test case for api_transport_bandwidth_id_put

    Replaces the TransportBandwidth resource.
    """
    body = openapi_server.TransportBandwidthPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-bandwidth/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_bandwidth_post(client):
    """Test case for api_transport_bandwidth_post

    Creates a TransportBandwidth resource.
    """
    body = openapi_server.TransportBandwidthPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-bandwidth',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

