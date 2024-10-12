# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_zulip_get_collection200_response import ApiTransportZulipGetCollection200Response
from openapi_server.models.transport_zulip_get import TransportZulipGet
from openapi_server.models.transport_zulip_jsonld_get import TransportZulipJsonldGet
from openapi_server.models.transport_zulip_jsonld_post import TransportZulipJsonldPost
from openapi_server.models.transport_zulip_jsonld_put import TransportZulipJsonldPut
from openapi_server.models.transport_zulip_patch import TransportZulipPatch
from openapi_server.models.transport_zulip_post import TransportZulipPost
from openapi_server.models.transport_zulip_put import TransportZulipPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_zulip_get_collection(client):
    """Test case for api_transport_zulip_get_collection

    Retrieves the collection of TransportZulip resources.
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
        path='/api/transport-zulip',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_zulip_id_delete(client):
    """Test case for api_transport_zulip_id_delete

    Removes the TransportZulip resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-zulip/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_zulip_id_get(client):
    """Test case for api_transport_zulip_id_get

    Retrieves a TransportZulip resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-zulip/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_zulip_id_patch(client):
    """Test case for api_transport_zulip_id_patch

    Updates the TransportZulip resource.
    """
    body = openapi_server.TransportZulipPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-zulip/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_zulip_id_put(client):
    """Test case for api_transport_zulip_id_put

    Replaces the TransportZulip resource.
    """
    body = openapi_server.TransportZulipPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-zulip/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_zulip_post(client):
    """Test case for api_transport_zulip_post

    Creates a TransportZulip resource.
    """
    body = openapi_server.TransportZulipPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-zulip',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

