# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_help_scout_get_collection200_response import ApiTransportHelpScoutGetCollection200Response
from openapi_server.models.transport_help_scout_get import TransportHelpScoutGet
from openapi_server.models.transport_help_scout_jsonld_get import TransportHelpScoutJsonldGet
from openapi_server.models.transport_help_scout_jsonld_post import TransportHelpScoutJsonldPost
from openapi_server.models.transport_help_scout_jsonld_put import TransportHelpScoutJsonldPut
from openapi_server.models.transport_help_scout_patch import TransportHelpScoutPatch
from openapi_server.models.transport_help_scout_post import TransportHelpScoutPost
from openapi_server.models.transport_help_scout_put import TransportHelpScoutPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_help_scout_get_collection(client):
    """Test case for api_transport_help_scout_get_collection

    Retrieves the collection of TransportHelpScout resources.
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
        path='/api/transport-help-scout',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_help_scout_id_delete(client):
    """Test case for api_transport_help_scout_id_delete

    Removes the TransportHelpScout resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-help-scout/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_help_scout_id_get(client):
    """Test case for api_transport_help_scout_id_get

    Retrieves a TransportHelpScout resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-help-scout/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_help_scout_id_patch(client):
    """Test case for api_transport_help_scout_id_patch

    Updates the TransportHelpScout resource.
    """
    body = openapi_server.TransportHelpScoutPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-help-scout/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_help_scout_id_put(client):
    """Test case for api_transport_help_scout_id_put

    Replaces the TransportHelpScout resource.
    """
    body = openapi_server.TransportHelpScoutPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-help-scout/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_help_scout_post(client):
    """Test case for api_transport_help_scout_post

    Creates a TransportHelpScout resource.
    """
    body = openapi_server.TransportHelpScoutPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-help-scout',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

