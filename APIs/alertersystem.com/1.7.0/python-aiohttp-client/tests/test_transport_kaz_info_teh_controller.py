# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_kaz_info_teh_get_collection200_response import ApiTransportKazInfoTehGetCollection200Response
from openapi_server.models.transport_kaz_info_teh_get import TransportKazInfoTehGet
from openapi_server.models.transport_kaz_info_teh_jsonld_get import TransportKazInfoTehJsonldGet
from openapi_server.models.transport_kaz_info_teh_jsonld_post import TransportKazInfoTehJsonldPost
from openapi_server.models.transport_kaz_info_teh_jsonld_put import TransportKazInfoTehJsonldPut
from openapi_server.models.transport_kaz_info_teh_patch import TransportKazInfoTehPatch
from openapi_server.models.transport_kaz_info_teh_post import TransportKazInfoTehPost
from openapi_server.models.transport_kaz_info_teh_put import TransportKazInfoTehPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_kaz_info_teh_get_collection(client):
    """Test case for api_transport_kaz_info_teh_get_collection

    Retrieves the collection of TransportKazInfoTeh resources.
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
        path='/api/transport-kaz-info-teh',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_kaz_info_teh_id_delete(client):
    """Test case for api_transport_kaz_info_teh_id_delete

    Removes the TransportKazInfoTeh resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-kaz-info-teh/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_kaz_info_teh_id_get(client):
    """Test case for api_transport_kaz_info_teh_id_get

    Retrieves a TransportKazInfoTeh resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-kaz-info-teh/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_kaz_info_teh_id_patch(client):
    """Test case for api_transport_kaz_info_teh_id_patch

    Updates the TransportKazInfoTeh resource.
    """
    body = openapi_server.TransportKazInfoTehPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-kaz-info-teh/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_kaz_info_teh_id_put(client):
    """Test case for api_transport_kaz_info_teh_id_put

    Replaces the TransportKazInfoTeh resource.
    """
    body = openapi_server.TransportKazInfoTehPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-kaz-info-teh/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_kaz_info_teh_post(client):
    """Test case for api_transport_kaz_info_teh_post

    Creates a TransportKazInfoTeh resource.
    """
    body = openapi_server.TransportKazInfoTehPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-kaz-info-teh',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

