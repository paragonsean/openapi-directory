# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.alert_service_get import AlertServiceGet
from openapi_server.models.alert_service_jsonld_get import AlertServiceJsonldGet
from openapi_server.models.alert_service_jsonld_post import AlertServiceJsonldPost
from openapi_server.models.alert_service_jsonld_put import AlertServiceJsonldPut
from openapi_server.models.alert_service_patch import AlertServicePatch
from openapi_server.models.alert_service_post import AlertServicePost
from openapi_server.models.alert_service_put import AlertServicePut
from openapi_server.models.api_alert_service_get_collection200_response import ApiAlertServiceGetCollection200Response


pytestmark = pytest.mark.asyncio

async def test_api_alert_service_get_collection(client):
    """Test case for api_alert_service_get_collection

    Retrieves the collection of AlertService resources.
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
        path='/api/alert-service',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_alert_service_id_delete(client):
    """Test case for api_alert_service_id_delete

    Removes the AlertService resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/alert-service/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_alert_service_id_get(client):
    """Test case for api_alert_service_id_get

    Retrieves a AlertService resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/alert-service/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_alert_service_id_patch(client):
    """Test case for api_alert_service_id_patch

    Updates the AlertService resource.
    """
    body = openapi_server.AlertServicePatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/alert-service/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_alert_service_id_put(client):
    """Test case for api_alert_service_id_put

    Replaces the AlertService resource.
    """
    body = openapi_server.AlertServicePut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/alert-service/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_alert_service_post(client):
    """Test case for api_alert_service_post

    Creates a AlertService resource.
    """
    body = openapi_server.AlertServicePost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/alert-service',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

