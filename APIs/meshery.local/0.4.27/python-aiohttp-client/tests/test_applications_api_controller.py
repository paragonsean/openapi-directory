# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.applications_api_response import ApplicationsAPIResponse
from openapi_server.models.meshery_application import MesheryApplication


pytestmark = pytest.mark.asyncio

async def test_id_delete_application_file(client):
    """Test case for id_delete_application_file

    Handle DELETE request for Application File Deploy
    """
    headers = { 
        'token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/application/deploy',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_delete_meshery_application_file(client):
    """Test case for id_delete_meshery_application_file

    Handle Delete for a Meshery Application File
    """
    headers = { 
        'token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/application/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_get_application_file_request(client):
    """Test case for id_get_application_file_request

    Handle GET request for Application Files
    """
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/application/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_get_meshery_application(client):
    """Test case for id_get_meshery_application

    Handle GET request for Meshery Application with the given id
    """
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/application/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_post_application_file_request(client):
    """Test case for id_post_application_file_request

    Handle POST request for Application Files
    """
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/application/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_id_post_deploy_application_file(client):
    """Test case for id_post_deploy_application_file

    Handle POST request for Application File Deploy
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'token': 'special-key',
    }
    data = FormData()
    data.add_field('upload_yaml_yml_file', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/api/application/deploy',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

