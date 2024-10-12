# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_one_signal_get_collection200_response import ApiTransportOneSignalGetCollection200Response
from openapi_server.models.transport_one_signal_get import TransportOneSignalGet
from openapi_server.models.transport_one_signal_jsonld_get import TransportOneSignalJsonldGet
from openapi_server.models.transport_one_signal_jsonld_post import TransportOneSignalJsonldPost
from openapi_server.models.transport_one_signal_jsonld_put import TransportOneSignalJsonldPut
from openapi_server.models.transport_one_signal_patch import TransportOneSignalPatch
from openapi_server.models.transport_one_signal_post import TransportOneSignalPost
from openapi_server.models.transport_one_signal_put import TransportOneSignalPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_one_signal_get_collection(client):
    """Test case for api_transport_one_signal_get_collection

    Retrieves the collection of TransportOneSignal resources.
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
        path='/api/transport-one-signal',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_one_signal_id_delete(client):
    """Test case for api_transport_one_signal_id_delete

    Removes the TransportOneSignal resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-one-signal/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_one_signal_id_get(client):
    """Test case for api_transport_one_signal_id_get

    Retrieves a TransportOneSignal resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-one-signal/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_one_signal_id_patch(client):
    """Test case for api_transport_one_signal_id_patch

    Updates the TransportOneSignal resource.
    """
    body = openapi_server.TransportOneSignalPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-one-signal/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_one_signal_id_put(client):
    """Test case for api_transport_one_signal_id_put

    Replaces the TransportOneSignal resource.
    """
    body = openapi_server.TransportOneSignalPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-one-signal/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_one_signal_post(client):
    """Test case for api_transport_one_signal_post

    Creates a TransportOneSignal resource.
    """
    body = openapi_server.TransportOneSignalPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-one-signal',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

