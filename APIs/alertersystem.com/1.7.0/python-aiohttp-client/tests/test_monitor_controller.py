# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_monitor_get_collection200_response import ApiMonitorGetCollection200Response
from openapi_server.models.monitor_get import MonitorGet
from openapi_server.models.monitor_jsonld_get import MonitorJsonldGet
from openapi_server.models.monitor_jsonld_post import MonitorJsonldPost
from openapi_server.models.monitor_jsonld_put import MonitorJsonldPut
from openapi_server.models.monitor_patch import MonitorPatch
from openapi_server.models.monitor_post import MonitorPost
from openapi_server.models.monitor_put import MonitorPut


pytestmark = pytest.mark.asyncio

async def test_api_monitor_get_collection(client):
    """Test case for api_monitor_get_collection

    Retrieves the collection of Monitor resources.
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
        path='/api/monitor',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_monitor_id_delete(client):
    """Test case for api_monitor_id_delete

    Removes the Monitor resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/monitor/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_monitor_id_get(client):
    """Test case for api_monitor_id_get

    Retrieves a Monitor resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/monitor/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_monitor_id_patch(client):
    """Test case for api_monitor_id_patch

    Updates the Monitor resource.
    """
    body = openapi_server.MonitorPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/monitor/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_monitor_id_put(client):
    """Test case for api_monitor_id_put

    Replaces the Monitor resource.
    """
    body = openapi_server.MonitorPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/monitor/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_monitor_post(client):
    """Test case for api_monitor_post

    Creates a Monitor resource.
    """
    body = openapi_server.MonitorPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/monitor',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

