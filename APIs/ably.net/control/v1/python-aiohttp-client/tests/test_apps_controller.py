# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.app_patch import AppPatch
from openapi_server.models.app_post import AppPost
from openapi_server.models.app_response import AppResponse
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_accounts_account_id_apps_get(client):
    """Test case for accounts_account_id_apps_get

    Lists account apps
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/accounts/{account_id}/apps'.format(account_id='account_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accounts_account_id_apps_post(client):
    """Test case for accounts_account_id_apps_post

    Creates an app
    """
    body = openapi_server.AppPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/accounts/{account_id}/apps'.format(account_id='account_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_id_delete(client):
    """Test case for apps_id_delete

    Deletes an app
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/apps/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_id_patch(client):
    """Test case for apps_id_patch

    Updates an app
    """
    body = openapi_server.AppPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/apps/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_apps_id_pkcs12_post(client):
    """Test case for apps_id_pkcs12_post

    Updates app's APNS info from a .p12 file
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('p12_file', '/path/to/file')
    data.add_field('p12_pass', 'p12_pass_example')
    response = await client.request(
        method='POST',
        path='/v1/apps/{id}/pkcs12'.format(id='id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

