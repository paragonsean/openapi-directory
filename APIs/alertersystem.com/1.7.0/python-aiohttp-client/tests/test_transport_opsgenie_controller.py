# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_opsgenie_get_collection200_response import ApiTransportOpsgenieGetCollection200Response
from openapi_server.models.transport_opsgenie_get import TransportOpsgenieGet
from openapi_server.models.transport_opsgenie_jsonld_get import TransportOpsgenieJsonldGet
from openapi_server.models.transport_opsgenie_jsonld_post import TransportOpsgenieJsonldPost
from openapi_server.models.transport_opsgenie_jsonld_put import TransportOpsgenieJsonldPut
from openapi_server.models.transport_opsgenie_patch import TransportOpsgeniePatch
from openapi_server.models.transport_opsgenie_post import TransportOpsgeniePost
from openapi_server.models.transport_opsgenie_put import TransportOpsgeniePut


pytestmark = pytest.mark.asyncio

async def test_api_transport_opsgenie_get_collection(client):
    """Test case for api_transport_opsgenie_get_collection

    Retrieves the collection of TransportOpsgenie resources.
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
        path='/api/transport-opsgenie',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_opsgenie_id_delete(client):
    """Test case for api_transport_opsgenie_id_delete

    Removes the TransportOpsgenie resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-opsgenie/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_opsgenie_id_get(client):
    """Test case for api_transport_opsgenie_id_get

    Retrieves a TransportOpsgenie resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-opsgenie/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_opsgenie_id_patch(client):
    """Test case for api_transport_opsgenie_id_patch

    Updates the TransportOpsgenie resource.
    """
    body = openapi_server.TransportOpsgeniePatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-opsgenie/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_opsgenie_id_put(client):
    """Test case for api_transport_opsgenie_id_put

    Replaces the TransportOpsgenie resource.
    """
    body = openapi_server.TransportOpsgeniePut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-opsgenie/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_opsgenie_post(client):
    """Test case for api_transport_opsgenie_post

    Creates a TransportOpsgenie resource.
    """
    body = openapi_server.TransportOpsgeniePost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-opsgenie',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

