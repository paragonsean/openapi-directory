# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_pushover_get_collection200_response import ApiTransportPushoverGetCollection200Response
from openapi_server.models.transport_pushover_get import TransportPushoverGet
from openapi_server.models.transport_pushover_jsonld_get import TransportPushoverJsonldGet
from openapi_server.models.transport_pushover_jsonld_post import TransportPushoverJsonldPost
from openapi_server.models.transport_pushover_jsonld_put import TransportPushoverJsonldPut
from openapi_server.models.transport_pushover_patch import TransportPushoverPatch
from openapi_server.models.transport_pushover_post import TransportPushoverPost
from openapi_server.models.transport_pushover_put import TransportPushoverPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_pushover_get_collection(client):
    """Test case for api_transport_pushover_get_collection

    Retrieves the collection of TransportPushover resources.
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
        path='/api/transport-pushover',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_pushover_id_delete(client):
    """Test case for api_transport_pushover_id_delete

    Removes the TransportPushover resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-pushover/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_pushover_id_get(client):
    """Test case for api_transport_pushover_id_get

    Retrieves a TransportPushover resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-pushover/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_pushover_id_patch(client):
    """Test case for api_transport_pushover_id_patch

    Updates the TransportPushover resource.
    """
    body = openapi_server.TransportPushoverPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-pushover/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_pushover_id_put(client):
    """Test case for api_transport_pushover_id_put

    Replaces the TransportPushover resource.
    """
    body = openapi_server.TransportPushoverPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-pushover/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_pushover_post(client):
    """Test case for api_transport_pushover_post

    Creates a TransportPushover resource.
    """
    body = openapi_server.TransportPushoverPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-pushover',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

