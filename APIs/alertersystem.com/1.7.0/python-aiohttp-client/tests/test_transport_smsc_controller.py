# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_smsc_get_collection200_response import ApiTransportSmscGetCollection200Response
from openapi_server.models.transport_smsc_get import TransportSmscGet
from openapi_server.models.transport_smsc_jsonld_get import TransportSmscJsonldGet
from openapi_server.models.transport_smsc_jsonld_post import TransportSmscJsonldPost
from openapi_server.models.transport_smsc_jsonld_put import TransportSmscJsonldPut
from openapi_server.models.transport_smsc_patch import TransportSmscPatch
from openapi_server.models.transport_smsc_post import TransportSmscPost
from openapi_server.models.transport_smsc_put import TransportSmscPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_smsc_get_collection(client):
    """Test case for api_transport_smsc_get_collection

    Retrieves the collection of TransportSmsc resources.
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
        path='/api/transport-smsc',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_smsc_id_delete(client):
    """Test case for api_transport_smsc_id_delete

    Removes the TransportSmsc resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-smsc/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_smsc_id_get(client):
    """Test case for api_transport_smsc_id_get

    Retrieves a TransportSmsc resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-smsc/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_smsc_id_patch(client):
    """Test case for api_transport_smsc_id_patch

    Updates the TransportSmsc resource.
    """
    body = openapi_server.TransportSmscPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-smsc/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_smsc_id_put(client):
    """Test case for api_transport_smsc_id_put

    Replaces the TransportSmsc resource.
    """
    body = openapi_server.TransportSmscPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-smsc/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_smsc_post(client):
    """Test case for api_transport_smsc_post

    Creates a TransportSmsc resource.
    """
    body = openapi_server.TransportSmscPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-smsc',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

