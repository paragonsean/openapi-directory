# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_ovh_cloud_get_collection200_response import ApiTransportOvhCloudGetCollection200Response
from openapi_server.models.transport_ovh_cloud_get import TransportOvhCloudGet
from openapi_server.models.transport_ovh_cloud_jsonld_get import TransportOvhCloudJsonldGet
from openapi_server.models.transport_ovh_cloud_jsonld_post import TransportOvhCloudJsonldPost
from openapi_server.models.transport_ovh_cloud_jsonld_put import TransportOvhCloudJsonldPut
from openapi_server.models.transport_ovh_cloud_patch import TransportOvhCloudPatch
from openapi_server.models.transport_ovh_cloud_post import TransportOvhCloudPost
from openapi_server.models.transport_ovh_cloud_put import TransportOvhCloudPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_ovh_cloud_get_collection(client):
    """Test case for api_transport_ovh_cloud_get_collection

    Retrieves the collection of TransportOvhCloud resources.
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
        path='/api/transport-ovh-cloud',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_ovh_cloud_id_delete(client):
    """Test case for api_transport_ovh_cloud_id_delete

    Removes the TransportOvhCloud resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-ovh-cloud/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_ovh_cloud_id_get(client):
    """Test case for api_transport_ovh_cloud_id_get

    Retrieves a TransportOvhCloud resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-ovh-cloud/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_ovh_cloud_id_patch(client):
    """Test case for api_transport_ovh_cloud_id_patch

    Updates the TransportOvhCloud resource.
    """
    body = openapi_server.TransportOvhCloudPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-ovh-cloud/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_ovh_cloud_id_put(client):
    """Test case for api_transport_ovh_cloud_id_put

    Replaces the TransportOvhCloud resource.
    """
    body = openapi_server.TransportOvhCloudPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-ovh-cloud/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_ovh_cloud_post(client):
    """Test case for api_transport_ovh_cloud_post

    Creates a TransportOvhCloud resource.
    """
    body = openapi_server.TransportOvhCloudPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-ovh-cloud',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

