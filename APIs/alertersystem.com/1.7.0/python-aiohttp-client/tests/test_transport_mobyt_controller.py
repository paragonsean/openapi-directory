# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_mobyt_get_collection200_response import ApiTransportMobytGetCollection200Response
from openapi_server.models.transport_mobyt_get import TransportMobytGet
from openapi_server.models.transport_mobyt_jsonld_get import TransportMobytJsonldGet
from openapi_server.models.transport_mobyt_jsonld_post import TransportMobytJsonldPost
from openapi_server.models.transport_mobyt_jsonld_put import TransportMobytJsonldPut
from openapi_server.models.transport_mobyt_patch import TransportMobytPatch
from openapi_server.models.transport_mobyt_post import TransportMobytPost
from openapi_server.models.transport_mobyt_put import TransportMobytPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_mobyt_get_collection(client):
    """Test case for api_transport_mobyt_get_collection

    Retrieves the collection of TransportMobyt resources.
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
        path='/api/transport-mobyt',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_mobyt_id_delete(client):
    """Test case for api_transport_mobyt_id_delete

    Removes the TransportMobyt resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-mobyt/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_mobyt_id_get(client):
    """Test case for api_transport_mobyt_id_get

    Retrieves a TransportMobyt resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-mobyt/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_mobyt_id_patch(client):
    """Test case for api_transport_mobyt_id_patch

    Updates the TransportMobyt resource.
    """
    body = openapi_server.TransportMobytPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-mobyt/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_mobyt_id_put(client):
    """Test case for api_transport_mobyt_id_put

    Replaces the TransportMobyt resource.
    """
    body = openapi_server.TransportMobytPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-mobyt/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_mobyt_post(client):
    """Test case for api_transport_mobyt_post

    Creates a TransportMobyt resource.
    """
    body = openapi_server.TransportMobytPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-mobyt',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

