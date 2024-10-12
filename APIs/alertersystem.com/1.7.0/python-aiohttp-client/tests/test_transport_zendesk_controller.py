# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_zendesk_get_collection200_response import ApiTransportZendeskGetCollection200Response
from openapi_server.models.transport_zendesk_get import TransportZendeskGet
from openapi_server.models.transport_zendesk_jsonld_get import TransportZendeskJsonldGet
from openapi_server.models.transport_zendesk_jsonld_post import TransportZendeskJsonldPost
from openapi_server.models.transport_zendesk_jsonld_put import TransportZendeskJsonldPut
from openapi_server.models.transport_zendesk_patch import TransportZendeskPatch
from openapi_server.models.transport_zendesk_post import TransportZendeskPost
from openapi_server.models.transport_zendesk_put import TransportZendeskPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_zendesk_get_collection(client):
    """Test case for api_transport_zendesk_get_collection

    Retrieves the collection of TransportZendesk resources.
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
        path='/api/transport-zendesk',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_zendesk_id_delete(client):
    """Test case for api_transport_zendesk_id_delete

    Removes the TransportZendesk resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-zendesk/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_zendesk_id_get(client):
    """Test case for api_transport_zendesk_id_get

    Retrieves a TransportZendesk resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-zendesk/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_zendesk_id_patch(client):
    """Test case for api_transport_zendesk_id_patch

    Updates the TransportZendesk resource.
    """
    body = openapi_server.TransportZendeskPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-zendesk/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_zendesk_id_put(client):
    """Test case for api_transport_zendesk_id_put

    Replaces the TransportZendesk resource.
    """
    body = openapi_server.TransportZendeskPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-zendesk/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_zendesk_post(client):
    """Test case for api_transport_zendesk_post

    Creates a TransportZendesk resource.
    """
    body = openapi_server.TransportZendeskPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-zendesk',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

