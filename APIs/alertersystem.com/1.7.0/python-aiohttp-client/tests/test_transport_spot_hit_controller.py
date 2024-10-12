# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_spot_hit_get_collection200_response import ApiTransportSpotHitGetCollection200Response
from openapi_server.models.transport_spot_hit_get import TransportSpotHitGet
from openapi_server.models.transport_spot_hit_jsonld_get import TransportSpotHitJsonldGet
from openapi_server.models.transport_spot_hit_jsonld_post import TransportSpotHitJsonldPost
from openapi_server.models.transport_spot_hit_jsonld_put import TransportSpotHitJsonldPut
from openapi_server.models.transport_spot_hit_patch import TransportSpotHitPatch
from openapi_server.models.transport_spot_hit_post import TransportSpotHitPost
from openapi_server.models.transport_spot_hit_put import TransportSpotHitPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_spot_hit_get_collection(client):
    """Test case for api_transport_spot_hit_get_collection

    Retrieves the collection of TransportSpotHit resources.
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
        path='/api/transport-spot-hit',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_spot_hit_id_delete(client):
    """Test case for api_transport_spot_hit_id_delete

    Removes the TransportSpotHit resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-spot-hit/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_spot_hit_id_get(client):
    """Test case for api_transport_spot_hit_id_get

    Retrieves a TransportSpotHit resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-spot-hit/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_spot_hit_id_patch(client):
    """Test case for api_transport_spot_hit_id_patch

    Updates the TransportSpotHit resource.
    """
    body = openapi_server.TransportSpotHitPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-spot-hit/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_spot_hit_id_put(client):
    """Test case for api_transport_spot_hit_id_put

    Replaces the TransportSpotHit resource.
    """
    body = openapi_server.TransportSpotHitPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-spot-hit/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_spot_hit_post(client):
    """Test case for api_transport_spot_hit_post

    Creates a TransportSpotHit resource.
    """
    body = openapi_server.TransportSpotHitPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-spot-hit',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

