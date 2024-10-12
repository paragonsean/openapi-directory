# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_contact_everyone_get_collection200_response import ApiTransportContactEveryoneGetCollection200Response
from openapi_server.models.transport_contact_everyone_get import TransportContactEveryoneGet
from openapi_server.models.transport_contact_everyone_jsonld_get import TransportContactEveryoneJsonldGet
from openapi_server.models.transport_contact_everyone_jsonld_post import TransportContactEveryoneJsonldPost
from openapi_server.models.transport_contact_everyone_jsonld_put import TransportContactEveryoneJsonldPut
from openapi_server.models.transport_contact_everyone_patch import TransportContactEveryonePatch
from openapi_server.models.transport_contact_everyone_post import TransportContactEveryonePost
from openapi_server.models.transport_contact_everyone_put import TransportContactEveryonePut


pytestmark = pytest.mark.asyncio

async def test_api_transport_contact_everyone_get_collection(client):
    """Test case for api_transport_contact_everyone_get_collection

    Retrieves the collection of TransportContactEveryone resources.
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
        path='/api/transport-contact-everyone',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_contact_everyone_id_delete(client):
    """Test case for api_transport_contact_everyone_id_delete

    Removes the TransportContactEveryone resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-contact-everyone/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_contact_everyone_id_get(client):
    """Test case for api_transport_contact_everyone_id_get

    Retrieves a TransportContactEveryone resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-contact-everyone/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_contact_everyone_id_patch(client):
    """Test case for api_transport_contact_everyone_id_patch

    Updates the TransportContactEveryone resource.
    """
    body = openapi_server.TransportContactEveryonePatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-contact-everyone/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_contact_everyone_id_put(client):
    """Test case for api_transport_contact_everyone_id_put

    Replaces the TransportContactEveryone resource.
    """
    body = openapi_server.TransportContactEveryonePut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-contact-everyone/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_contact_everyone_post(client):
    """Test case for api_transport_contact_everyone_post

    Creates a TransportContactEveryone resource.
    """
    body = openapi_server.TransportContactEveryonePost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-contact-everyone',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

