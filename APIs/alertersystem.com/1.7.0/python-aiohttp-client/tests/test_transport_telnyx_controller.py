# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_telnyx_get_collection200_response import ApiTransportTelnyxGetCollection200Response
from openapi_server.models.transport_telnyx_get import TransportTelnyxGet
from openapi_server.models.transport_telnyx_jsonld_get import TransportTelnyxJsonldGet
from openapi_server.models.transport_telnyx_jsonld_post import TransportTelnyxJsonldPost
from openapi_server.models.transport_telnyx_jsonld_put import TransportTelnyxJsonldPut
from openapi_server.models.transport_telnyx_patch import TransportTelnyxPatch
from openapi_server.models.transport_telnyx_post import TransportTelnyxPost
from openapi_server.models.transport_telnyx_put import TransportTelnyxPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_telnyx_get_collection(client):
    """Test case for api_transport_telnyx_get_collection

    Retrieves the collection of TransportTelnyx resources.
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
        path='/api/transport-telnyx',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_telnyx_id_delete(client):
    """Test case for api_transport_telnyx_id_delete

    Removes the TransportTelnyx resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-telnyx/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_telnyx_id_get(client):
    """Test case for api_transport_telnyx_id_get

    Retrieves a TransportTelnyx resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-telnyx/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_telnyx_id_patch(client):
    """Test case for api_transport_telnyx_id_patch

    Updates the TransportTelnyx resource.
    """
    body = openapi_server.TransportTelnyxPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-telnyx/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_telnyx_id_put(client):
    """Test case for api_transport_telnyx_id_put

    Replaces the TransportTelnyx resource.
    """
    body = openapi_server.TransportTelnyxPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-telnyx/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_telnyx_post(client):
    """Test case for api_transport_telnyx_post

    Creates a TransportTelnyx resource.
    """
    body = openapi_server.TransportTelnyxPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-telnyx',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

