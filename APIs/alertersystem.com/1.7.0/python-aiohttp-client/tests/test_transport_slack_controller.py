# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_slack_get_collection200_response import ApiTransportSlackGetCollection200Response
from openapi_server.models.transport_slack_get import TransportSlackGet
from openapi_server.models.transport_slack_jsonld_get import TransportSlackJsonldGet
from openapi_server.models.transport_slack_jsonld_post import TransportSlackJsonldPost
from openapi_server.models.transport_slack_jsonld_put import TransportSlackJsonldPut
from openapi_server.models.transport_slack_patch import TransportSlackPatch
from openapi_server.models.transport_slack_post import TransportSlackPost
from openapi_server.models.transport_slack_put import TransportSlackPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_slack_get_collection(client):
    """Test case for api_transport_slack_get_collection

    Retrieves the collection of TransportSlack resources.
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
        path='/api/transport-slack',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_slack_id_delete(client):
    """Test case for api_transport_slack_id_delete

    Removes the TransportSlack resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-slack/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_slack_id_get(client):
    """Test case for api_transport_slack_id_get

    Retrieves a TransportSlack resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-slack/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_slack_id_patch(client):
    """Test case for api_transport_slack_id_patch

    Updates the TransportSlack resource.
    """
    body = openapi_server.TransportSlackPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-slack/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_slack_id_put(client):
    """Test case for api_transport_slack_id_put

    Replaces the TransportSlack resource.
    """
    body = openapi_server.TransportSlackPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-slack/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_slack_post(client):
    """Test case for api_transport_slack_post

    Creates a TransportSlack resource.
    """
    body = openapi_server.TransportSlackPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-slack',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

