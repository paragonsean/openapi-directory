# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_forty_six_elks_get_collection200_response import ApiTransportFortySixElksGetCollection200Response
from openapi_server.models.transport_forty_six_elks_get import TransportFortySixElksGet
from openapi_server.models.transport_forty_six_elks_jsonld_get import TransportFortySixElksJsonldGet
from openapi_server.models.transport_forty_six_elks_jsonld_post import TransportFortySixElksJsonldPost
from openapi_server.models.transport_forty_six_elks_jsonld_put import TransportFortySixElksJsonldPut
from openapi_server.models.transport_forty_six_elks_patch import TransportFortySixElksPatch
from openapi_server.models.transport_forty_six_elks_post import TransportFortySixElksPost
from openapi_server.models.transport_forty_six_elks_put import TransportFortySixElksPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_forty_six_elks_get_collection(client):
    """Test case for api_transport_forty_six_elks_get_collection

    Retrieves the collection of TransportFortySixElks resources.
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
        path='/api/transport-forty-six-elks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_forty_six_elks_id_delete(client):
    """Test case for api_transport_forty_six_elks_id_delete

    Removes the TransportFortySixElks resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-forty-six-elks/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_forty_six_elks_id_get(client):
    """Test case for api_transport_forty_six_elks_id_get

    Retrieves a TransportFortySixElks resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-forty-six-elks/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_forty_six_elks_id_patch(client):
    """Test case for api_transport_forty_six_elks_id_patch

    Updates the TransportFortySixElks resource.
    """
    body = openapi_server.TransportFortySixElksPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-forty-six-elks/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_forty_six_elks_id_put(client):
    """Test case for api_transport_forty_six_elks_id_put

    Replaces the TransportFortySixElks resource.
    """
    body = openapi_server.TransportFortySixElksPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-forty-six-elks/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_forty_six_elks_post(client):
    """Test case for api_transport_forty_six_elks_post

    Creates a TransportFortySixElks resource.
    """
    body = openapi_server.TransportFortySixElksPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-forty-six-elks',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

