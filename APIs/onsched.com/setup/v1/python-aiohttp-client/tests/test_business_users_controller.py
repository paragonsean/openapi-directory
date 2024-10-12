# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.authorized_company_list_view_model import AuthorizedCompanyListViewModel
from openapi_server.models.business_permission_list_view_model import BusinessPermissionListViewModel
from openapi_server.models.business_user_input_model import BusinessUserInputModel
from openapi_server.models.business_user_list_view_model import BusinessUserListViewModel
from openapi_server.models.business_user_update_model import BusinessUserUpdateModel
from openapi_server.models.business_user_view_model import BusinessUserViewModel


pytestmark = pytest.mark.asyncio

async def test_setup_v1_businessusers_email_companies_get(client):
    """Test case for setup_v1_businessusers_email_companies_get

    List User Companies
    """
    params = [('searchText', 'search_text_example'),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/businessusers/{email}/companies'.format(email='email_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_businessusers_get(client):
    """Test case for setup_v1_businessusers_get

    List Users
    """
    params = [('locationId', 'location_id_example'),
                    ('email', 'email_example'),
                    ('role', 'role_example'),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/businessusers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_businessusers_id_delete(client):
    """Test case for setup_v1_businessusers_id_delete

    Delete User
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/setup/v1/businessusers/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_businessusers_id_get(client):
    """Test case for setup_v1_businessusers_id_get

    Get User
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/businessusers/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_setup_v1_businessusers_id_put(client):
    """Test case for setup_v1_businessusers_id_put

    Update User
    """
    body = {"resourceId":"resourceId","role":"role","name":"name","email":"email","sendRegistrationInvite":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/setup/v1/businessusers/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_businessusers_permissions_get(client):
    """Test case for setup_v1_businessusers_permissions_get

    List User Permissions
    """
    params = [('role', 'role_example'),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/businessusers/permissions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_setup_v1_businessusers_post(client):
    """Test case for setup_v1_businessusers_post

    Create User
    """
    body = {"resourceId":"resourceId","role":"role","locationId":"locationId","name":"name","email":"email","sendRegistrationInvite":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/setup/v1/businessusers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

