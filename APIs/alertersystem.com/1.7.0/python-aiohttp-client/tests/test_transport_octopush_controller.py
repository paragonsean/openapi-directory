# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_octopush_get_collection200_response import ApiTransportOctopushGetCollection200Response
from openapi_server.models.transport_octopush_get import TransportOctopushGet
from openapi_server.models.transport_octopush_jsonld_get import TransportOctopushJsonldGet
from openapi_server.models.transport_octopush_jsonld_post import TransportOctopushJsonldPost
from openapi_server.models.transport_octopush_jsonld_put import TransportOctopushJsonldPut
from openapi_server.models.transport_octopush_patch import TransportOctopushPatch
from openapi_server.models.transport_octopush_post import TransportOctopushPost
from openapi_server.models.transport_octopush_put import TransportOctopushPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_octopush_get_collection(client):
    """Test case for api_transport_octopush_get_collection

    Retrieves the collection of TransportOctopush resources.
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
        path='/api/transport-octopush',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_octopush_id_delete(client):
    """Test case for api_transport_octopush_id_delete

    Removes the TransportOctopush resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-octopush/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_octopush_id_get(client):
    """Test case for api_transport_octopush_id_get

    Retrieves a TransportOctopush resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-octopush/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_octopush_id_patch(client):
    """Test case for api_transport_octopush_id_patch

    Updates the TransportOctopush resource.
    """
    body = openapi_server.TransportOctopushPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-octopush/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_octopush_id_put(client):
    """Test case for api_transport_octopush_id_put

    Replaces the TransportOctopush resource.
    """
    body = openapi_server.TransportOctopushPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-octopush/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_octopush_post(client):
    """Test case for api_transport_octopush_post

    Creates a TransportOctopush resource.
    """
    body = openapi_server.TransportOctopushPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-octopush',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

