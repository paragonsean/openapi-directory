# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_telegram_get_collection200_response import ApiTransportTelegramGetCollection200Response
from openapi_server.models.transport_telegram_get import TransportTelegramGet
from openapi_server.models.transport_telegram_jsonld_get import TransportTelegramJsonldGet
from openapi_server.models.transport_telegram_jsonld_post import TransportTelegramJsonldPost
from openapi_server.models.transport_telegram_jsonld_put import TransportTelegramJsonldPut
from openapi_server.models.transport_telegram_patch import TransportTelegramPatch
from openapi_server.models.transport_telegram_post import TransportTelegramPost
from openapi_server.models.transport_telegram_put import TransportTelegramPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_telegram_get_collection(client):
    """Test case for api_transport_telegram_get_collection

    Retrieves the collection of TransportTelegram resources.
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
        path='/api/transport-telegram',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_telegram_id_delete(client):
    """Test case for api_transport_telegram_id_delete

    Removes the TransportTelegram resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-telegram/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_telegram_id_get(client):
    """Test case for api_transport_telegram_id_get

    Retrieves a TransportTelegram resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-telegram/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_telegram_id_patch(client):
    """Test case for api_transport_telegram_id_patch

    Updates the TransportTelegram resource.
    """
    body = openapi_server.TransportTelegramPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-telegram/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_telegram_id_put(client):
    """Test case for api_transport_telegram_id_put

    Replaces the TransportTelegram resource.
    """
    body = openapi_server.TransportTelegramPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-telegram/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_telegram_post(client):
    """Test case for api_transport_telegram_post

    Creates a TransportTelegram resource.
    """
    body = openapi_server.TransportTelegramPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-telegram',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

