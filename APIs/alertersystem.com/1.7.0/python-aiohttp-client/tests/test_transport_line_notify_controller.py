# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_line_notify_get_collection200_response import ApiTransportLineNotifyGetCollection200Response
from openapi_server.models.transport_line_notify_get import TransportLineNotifyGet
from openapi_server.models.transport_line_notify_jsonld_get import TransportLineNotifyJsonldGet
from openapi_server.models.transport_line_notify_jsonld_post import TransportLineNotifyJsonldPost
from openapi_server.models.transport_line_notify_jsonld_put import TransportLineNotifyJsonldPut
from openapi_server.models.transport_line_notify_patch import TransportLineNotifyPatch
from openapi_server.models.transport_line_notify_post import TransportLineNotifyPost
from openapi_server.models.transport_line_notify_put import TransportLineNotifyPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_line_notify_get_collection(client):
    """Test case for api_transport_line_notify_get_collection

    Retrieves the collection of TransportLineNotify resources.
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
        path='/api/transport-line-notify',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_line_notify_id_delete(client):
    """Test case for api_transport_line_notify_id_delete

    Removes the TransportLineNotify resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-line-notify/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_line_notify_id_get(client):
    """Test case for api_transport_line_notify_id_get

    Retrieves a TransportLineNotify resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-line-notify/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_line_notify_id_patch(client):
    """Test case for api_transport_line_notify_id_patch

    Updates the TransportLineNotify resource.
    """
    body = openapi_server.TransportLineNotifyPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-line-notify/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_line_notify_id_put(client):
    """Test case for api_transport_line_notify_id_put

    Replaces the TransportLineNotify resource.
    """
    body = openapi_server.TransportLineNotifyPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-line-notify/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_line_notify_post(client):
    """Test case for api_transport_line_notify_post

    Creates a TransportLineNotify resource.
    """
    body = openapi_server.TransportLineNotifyPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-line-notify',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

