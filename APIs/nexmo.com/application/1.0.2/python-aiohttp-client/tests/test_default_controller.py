# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.application import Application
from openapi_server.models.application_created import ApplicationCreated
from openapi_server.models.applications import Applications
from openapi_server.models.create_application_request import CreateApplicationRequest
from openapi_server.models.update_application_request import UpdateApplicationRequest


pytestmark = pytest.mark.asyncio

async def test_create_application(client):
    """Test case for create_application

    Create Application
    """
    body = openapi_server.CreateApplicationRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/applications/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_application(client):
    """Test case for delete_application

    Destroy Application
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v1/applications/{app_id}'.format(app_id='aaaaaaaa-bbbb-cccc-dddd-0123456789ab'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_application(client):
    """Test case for retrieve_application

    Retrieve Application
    """
    params = [('api_key', 'api_key_example'),
                    ('api_secret', 'api_secret_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/applications/{app_id}'.format(app_id='aaaaaaaa-bbbb-cccc-dddd-0123456789ab'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_applications(client):
    """Test case for retrieve_applications

    Retrieve all Applications
    """
    params = [('api_key', 'api_key_example'),
                    ('api_secret', 'api_secret_example'),
                    ('page_size', 10),
                    ('page_index', 0)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/applications/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_application(client):
    """Test case for update_application

    Update Application
    """
    body = openapi_server.UpdateApplicationRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/applications/{app_id}'.format(app_id='aaaaaaaa-bbbb-cccc-dddd-0123456789ab'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

