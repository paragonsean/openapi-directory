# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_user_account_get_collection200_response import ApiUserAccountGetCollection200Response
from openapi_server.models.user_account_get import UserAccountGet
from openapi_server.models.user_account_jsonld_get import UserAccountJsonldGet
from openapi_server.models.user_account_jsonld_put import UserAccountJsonldPut
from openapi_server.models.user_account_patch import UserAccountPatch
from openapi_server.models.user_account_put import UserAccountPut


pytestmark = pytest.mark.asyncio

async def test_api_user_account_get_collection(client):
    """Test case for api_user_account_get_collection

    Retrieves the collection of UserAccount resources.
    """
    params = [('page', 1),
                    ('properties[]', ['properties_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/user-account',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_user_account_id_get(client):
    """Test case for api_user_account_id_get

    Retrieves a UserAccount resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/user-account/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_user_account_id_patch(client):
    """Test case for api_user_account_id_patch

    Updates the UserAccount resource.
    """
    body = openapi_server.UserAccountPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/user-account/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_user_account_id_put(client):
    """Test case for api_user_account_id_put

    Replaces the UserAccount resource.
    """
    body = openapi_server.UserAccountPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/user-account/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

