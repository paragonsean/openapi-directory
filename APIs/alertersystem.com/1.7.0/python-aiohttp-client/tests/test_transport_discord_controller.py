# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_discord_get_collection200_response import ApiTransportDiscordGetCollection200Response
from openapi_server.models.transport_discord_get import TransportDiscordGet
from openapi_server.models.transport_discord_jsonld_get import TransportDiscordJsonldGet
from openapi_server.models.transport_discord_jsonld_post import TransportDiscordJsonldPost
from openapi_server.models.transport_discord_jsonld_put import TransportDiscordJsonldPut
from openapi_server.models.transport_discord_patch import TransportDiscordPatch
from openapi_server.models.transport_discord_post import TransportDiscordPost
from openapi_server.models.transport_discord_put import TransportDiscordPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_discord_get_collection(client):
    """Test case for api_transport_discord_get_collection

    Retrieves the collection of TransportDiscord resources.
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
        path='/api/transport-discord',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_discord_id_delete(client):
    """Test case for api_transport_discord_id_delete

    Removes the TransportDiscord resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-discord/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_discord_id_get(client):
    """Test case for api_transport_discord_id_get

    Retrieves a TransportDiscord resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-discord/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_discord_id_patch(client):
    """Test case for api_transport_discord_id_patch

    Updates the TransportDiscord resource.
    """
    body = openapi_server.TransportDiscordPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-discord/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_discord_id_put(client):
    """Test case for api_transport_discord_id_put

    Replaces the TransportDiscord resource.
    """
    body = openapi_server.TransportDiscordPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-discord/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_discord_post(client):
    """Test case for api_transport_discord_post

    Creates a TransportDiscord resource.
    """
    body = openapi_server.TransportDiscordPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-discord',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

