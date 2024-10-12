# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_mattermost_get_collection200_response import ApiTransportMattermostGetCollection200Response
from openapi_server.models.transport_mattermost_get import TransportMattermostGet
from openapi_server.models.transport_mattermost_jsonld_get import TransportMattermostJsonldGet
from openapi_server.models.transport_mattermost_jsonld_post import TransportMattermostJsonldPost
from openapi_server.models.transport_mattermost_jsonld_put import TransportMattermostJsonldPut
from openapi_server.models.transport_mattermost_patch import TransportMattermostPatch
from openapi_server.models.transport_mattermost_post import TransportMattermostPost
from openapi_server.models.transport_mattermost_put import TransportMattermostPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_mattermost_get_collection(client):
    """Test case for api_transport_mattermost_get_collection

    Retrieves the collection of TransportMattermost resources.
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
        path='/api/transport-mattermost',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_mattermost_id_delete(client):
    """Test case for api_transport_mattermost_id_delete

    Removes the TransportMattermost resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-mattermost/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_mattermost_id_get(client):
    """Test case for api_transport_mattermost_id_get

    Retrieves a TransportMattermost resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-mattermost/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_mattermost_id_patch(client):
    """Test case for api_transport_mattermost_id_patch

    Updates the TransportMattermost resource.
    """
    body = openapi_server.TransportMattermostPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-mattermost/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_mattermost_id_put(client):
    """Test case for api_transport_mattermost_id_put

    Replaces the TransportMattermost resource.
    """
    body = openapi_server.TransportMattermostPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-mattermost/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_mattermost_post(client):
    """Test case for api_transport_mattermost_post

    Creates a TransportMattermost resource.
    """
    body = openapi_server.TransportMattermostPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-mattermost',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

