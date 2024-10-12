# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_twitter_get_collection200_response import ApiTransportTwitterGetCollection200Response
from openapi_server.models.transport_twitter_get import TransportTwitterGet
from openapi_server.models.transport_twitter_jsonld_get import TransportTwitterJsonldGet
from openapi_server.models.transport_twitter_jsonld_post import TransportTwitterJsonldPost
from openapi_server.models.transport_twitter_jsonld_put import TransportTwitterJsonldPut
from openapi_server.models.transport_twitter_patch import TransportTwitterPatch
from openapi_server.models.transport_twitter_post import TransportTwitterPost
from openapi_server.models.transport_twitter_put import TransportTwitterPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_twitter_get_collection(client):
    """Test case for api_transport_twitter_get_collection

    Retrieves the collection of TransportTwitter resources.
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
        path='/api/transport-twitter',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_twitter_id_delete(client):
    """Test case for api_transport_twitter_id_delete

    Removes the TransportTwitter resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-twitter/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_twitter_id_get(client):
    """Test case for api_transport_twitter_id_get

    Retrieves a TransportTwitter resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-twitter/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_twitter_id_patch(client):
    """Test case for api_transport_twitter_id_patch

    Updates the TransportTwitter resource.
    """
    body = openapi_server.TransportTwitterPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-twitter/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_twitter_id_put(client):
    """Test case for api_transport_twitter_id_put

    Replaces the TransportTwitter resource.
    """
    body = openapi_server.TransportTwitterPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-twitter/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_twitter_post(client):
    """Test case for api_transport_twitter_post

    Creates a TransportTwitter resource.
    """
    body = openapi_server.TransportTwitterPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-twitter',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

