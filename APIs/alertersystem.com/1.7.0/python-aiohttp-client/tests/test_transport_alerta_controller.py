# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_alerta_get_collection200_response import ApiTransportAlertaGetCollection200Response
from openapi_server.models.transport_alerta_get import TransportAlertaGet
from openapi_server.models.transport_alerta_jsonld_get import TransportAlertaJsonldGet
from openapi_server.models.transport_alerta_jsonld_post import TransportAlertaJsonldPost
from openapi_server.models.transport_alerta_jsonld_put import TransportAlertaJsonldPut
from openapi_server.models.transport_alerta_patch import TransportAlertaPatch
from openapi_server.models.transport_alerta_post import TransportAlertaPost
from openapi_server.models.transport_alerta_put import TransportAlertaPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_alerta_get_collection(client):
    """Test case for api_transport_alerta_get_collection

    Retrieves the collection of TransportAlerta resources.
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
        path='/api/transport-alerta',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_alerta_id_delete(client):
    """Test case for api_transport_alerta_id_delete

    Removes the TransportAlerta resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-alerta/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_alerta_id_get(client):
    """Test case for api_transport_alerta_id_get

    Retrieves a TransportAlerta resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-alerta/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_alerta_id_patch(client):
    """Test case for api_transport_alerta_id_patch

    Updates the TransportAlerta resource.
    """
    body = openapi_server.TransportAlertaPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-alerta/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_alerta_id_put(client):
    """Test case for api_transport_alerta_id_put

    Replaces the TransportAlerta resource.
    """
    body = openapi_server.TransportAlertaPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-alerta/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_alerta_post(client):
    """Test case for api_transport_alerta_post

    Creates a TransportAlerta resource.
    """
    body = openapi_server.TransportAlertaPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-alerta',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

