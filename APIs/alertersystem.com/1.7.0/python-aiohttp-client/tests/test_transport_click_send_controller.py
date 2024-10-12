# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_click_send_get_collection200_response import ApiTransportClickSendGetCollection200Response
from openapi_server.models.transport_click_send_get import TransportClickSendGet
from openapi_server.models.transport_click_send_jsonld_get import TransportClickSendJsonldGet
from openapi_server.models.transport_click_send_jsonld_post import TransportClickSendJsonldPost
from openapi_server.models.transport_click_send_jsonld_put import TransportClickSendJsonldPut
from openapi_server.models.transport_click_send_patch import TransportClickSendPatch
from openapi_server.models.transport_click_send_post import TransportClickSendPost
from openapi_server.models.transport_click_send_put import TransportClickSendPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_click_send_get_collection(client):
    """Test case for api_transport_click_send_get_collection

    Retrieves the collection of TransportClickSend resources.
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
        path='/api/transport-click-send',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_click_send_id_delete(client):
    """Test case for api_transport_click_send_id_delete

    Removes the TransportClickSend resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-click-send/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_click_send_id_get(client):
    """Test case for api_transport_click_send_id_get

    Retrieves a TransportClickSend resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-click-send/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_click_send_id_patch(client):
    """Test case for api_transport_click_send_id_patch

    Updates the TransportClickSend resource.
    """
    body = openapi_server.TransportClickSendPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-click-send/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_click_send_id_put(client):
    """Test case for api_transport_click_send_id_put

    Replaces the TransportClickSend resource.
    """
    body = openapi_server.TransportClickSendPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-click-send/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_click_send_post(client):
    """Test case for api_transport_click_send_post

    Creates a TransportClickSend resource.
    """
    body = openapi_server.TransportClickSendPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-click-send',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

