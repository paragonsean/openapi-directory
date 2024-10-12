# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_mastodon_get_collection200_response import ApiTransportMastodonGetCollection200Response
from openapi_server.models.transport_mastodon_get import TransportMastodonGet
from openapi_server.models.transport_mastodon_jsonld_get import TransportMastodonJsonldGet
from openapi_server.models.transport_mastodon_jsonld_post import TransportMastodonJsonldPost
from openapi_server.models.transport_mastodon_jsonld_put import TransportMastodonJsonldPut
from openapi_server.models.transport_mastodon_patch import TransportMastodonPatch
from openapi_server.models.transport_mastodon_post import TransportMastodonPost
from openapi_server.models.transport_mastodon_put import TransportMastodonPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_mastodon_get_collection(client):
    """Test case for api_transport_mastodon_get_collection

    Retrieves the collection of TransportMastodon resources.
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
        path='/api/transport-mastodon',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_mastodon_id_delete(client):
    """Test case for api_transport_mastodon_id_delete

    Removes the TransportMastodon resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-mastodon/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_mastodon_id_get(client):
    """Test case for api_transport_mastodon_id_get

    Retrieves a TransportMastodon resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-mastodon/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_mastodon_id_patch(client):
    """Test case for api_transport_mastodon_id_patch

    Updates the TransportMastodon resource.
    """
    body = openapi_server.TransportMastodonPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-mastodon/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_mastodon_id_put(client):
    """Test case for api_transport_mastodon_id_put

    Replaces the TransportMastodon resource.
    """
    body = openapi_server.TransportMastodonPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-mastodon/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_mastodon_post(client):
    """Test case for api_transport_mastodon_post

    Creates a TransportMastodon resource.
    """
    body = openapi_server.TransportMastodonPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-mastodon',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

