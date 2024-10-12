# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_email_get_collection200_response import ApiTransportEmailGetCollection200Response
from openapi_server.models.transport_email_get import TransportEmailGet
from openapi_server.models.transport_email_jsonld_get import TransportEmailJsonldGet
from openapi_server.models.transport_email_jsonld_post import TransportEmailJsonldPost
from openapi_server.models.transport_email_jsonld_put import TransportEmailJsonldPut
from openapi_server.models.transport_email_patch import TransportEmailPatch
from openapi_server.models.transport_email_post import TransportEmailPost
from openapi_server.models.transport_email_put import TransportEmailPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_email_get_collection(client):
    """Test case for api_transport_email_get_collection

    Retrieves the collection of TransportEmail resources.
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
        path='/api/transport-email',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_email_id_delete(client):
    """Test case for api_transport_email_id_delete

    Removes the TransportEmail resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-email/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_email_id_get(client):
    """Test case for api_transport_email_id_get

    Retrieves a TransportEmail resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-email/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_email_id_patch(client):
    """Test case for api_transport_email_id_patch

    Updates the TransportEmail resource.
    """
    body = openapi_server.TransportEmailPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-email/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_email_id_put(client):
    """Test case for api_transport_email_id_put

    Replaces the TransportEmail resource.
    """
    body = openapi_server.TransportEmailPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-email/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_email_post(client):
    """Test case for api_transport_email_post

    Creates a TransportEmail resource.
    """
    body = openapi_server.TransportEmailPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-email',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

