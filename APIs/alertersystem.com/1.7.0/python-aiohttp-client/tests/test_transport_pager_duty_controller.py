# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_pager_duty_get_collection200_response import ApiTransportPagerDutyGetCollection200Response
from openapi_server.models.transport_pager_duty_get import TransportPagerDutyGet
from openapi_server.models.transport_pager_duty_jsonld_get import TransportPagerDutyJsonldGet
from openapi_server.models.transport_pager_duty_jsonld_post import TransportPagerDutyJsonldPost
from openapi_server.models.transport_pager_duty_jsonld_put import TransportPagerDutyJsonldPut
from openapi_server.models.transport_pager_duty_patch import TransportPagerDutyPatch
from openapi_server.models.transport_pager_duty_post import TransportPagerDutyPost
from openapi_server.models.transport_pager_duty_put import TransportPagerDutyPut


pytestmark = pytest.mark.asyncio

async def test_api_transport_pager_duty_get_collection(client):
    """Test case for api_transport_pager_duty_get_collection

    Retrieves the collection of TransportPagerDuty resources.
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
        path='/api/transport-pager-duty',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_pager_duty_id_delete(client):
    """Test case for api_transport_pager_duty_id_delete

    Removes the TransportPagerDuty resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-pager-duty/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_pager_duty_id_get(client):
    """Test case for api_transport_pager_duty_id_get

    Retrieves a TransportPagerDuty resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-pager-duty/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_pager_duty_id_patch(client):
    """Test case for api_transport_pager_duty_id_patch

    Updates the TransportPagerDuty resource.
    """
    body = openapi_server.TransportPagerDutyPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-pager-duty/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_pager_duty_id_put(client):
    """Test case for api_transport_pager_duty_id_put

    Replaces the TransportPagerDuty resource.
    """
    body = openapi_server.TransportPagerDutyPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-pager-duty/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_pager_duty_post(client):
    """Test case for api_transport_pager_duty_post

    Creates a TransportPagerDuty resource.
    """
    body = openapi_server.TransportPagerDutyPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-pager-duty',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

