# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.application import Application
from openapi_server.models.application_data import ApplicationData
from openapi_server.models.application_error import ApplicationError
from openapi_server.models.not_found import NotFound


pytestmark = pytest.mark.asyncio

async def test_oauth_application_create(client):
    """Test case for oauth_application_create

    Create a new OAuth2 application
    """
    application_data = {"name":"name","authorization_grant_type":"authorization-code","client_type":"confidential","redirect_uris":"redirect_uris"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{namespace}/oauth/applications'.format(namespace='namespace_example'),
        headers=headers,
        json=application_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_oauth_application_delete(client):
    """Test case for oauth_application_delete

    Delete an application by id
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/{namespace}/oauth/applications/{application}'.format(namespace='namespace_example', application='application_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_oauth_application_read(client):
    """Test case for oauth_application_read

    Get an application by id
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{namespace}/oauth/applications/{application}'.format(namespace='namespace_example', application='application_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_oauth_application_replace(client):
    """Test case for oauth_application_replace

    Replace an application by id
    """
    oauth_application_data = {"name":"name","authorization_grant_type":"authorization-code","client_type":"confidential","redirect_uris":"redirect_uris"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/{namespace}/oauth/applications/{application}'.format(namespace='namespace_example', application='application_example'),
        headers=headers,
        json=oauth_application_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_oauth_application_update(client):
    """Test case for oauth_application_update

    Update an application by id
    """
    application_data = {"name":"name","authorization_grant_type":"authorization-code","client_type":"confidential","redirect_uris":"redirect_uris"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/{namespace}/oauth/applications/{application}'.format(namespace='namespace_example', application='application_example'),
        headers=headers,
        json=application_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_oauth_applications_list(client):
    """Test case for oauth_applications_list

    Retrieve oauth applications
    """
    params = [('limit', 'limit_example'),
                    ('offset', 'offset_example'),
                    ('ordering', 'ordering_example')]
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{namespace}/oauth/applications'.format(namespace='namespace_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

