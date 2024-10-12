# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_freshdesk_get_collection200_response import ApiTransportFreshdeskGetCollection200Response
from openapi_server.models.transport_freshdesk_get import TransportFreshdeskGet
from openapi_server.models.transport_freshdesk_jsonld_get import TransportFreshdeskJsonldGet
from openapi_server.models.transport_freshdesk_jsonld_post import TransportFreshdeskJsonldPost
from openapi_server.models.transport_freshdesk_jsonld_put import TransportFreshdeskJsonldPut
from openapi_server.models.transport_freshdesk_patch import TransportFreshdeskPatch
from openapi_server.models.transport_freshdesk_post import TransportFreshdeskPost
from openapi_server.models.transport_freshdesk_put import TransportFreshdeskPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_freshdesk_get_collection(client):
    """Test case for api_transport_freshdesk_get_collection

    Retrieves the collection of TransportFreshdesk resources.
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
        path='/api/transport-freshdesk',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_freshdesk_id_delete(client):
    """Test case for api_transport_freshdesk_id_delete

    Removes the TransportFreshdesk resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-freshdesk/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_freshdesk_id_get(client):
    """Test case for api_transport_freshdesk_id_get

    Retrieves a TransportFreshdesk resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-freshdesk/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_freshdesk_id_patch(client):
    """Test case for api_transport_freshdesk_id_patch

    Updates the TransportFreshdesk resource.
    """
    body = openapi_server.TransportFreshdeskPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-freshdesk/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_freshdesk_id_put(client):
    """Test case for api_transport_freshdesk_id_put

    Replaces the TransportFreshdesk resource.
    """
    body = openapi_server.TransportFreshdeskPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-freshdesk/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_freshdesk_post(client):
    """Test case for api_transport_freshdesk_post

    Creates a TransportFreshdesk resource.
    """
    body = openapi_server.TransportFreshdeskPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-freshdesk',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

