# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.bulk_action_request_body import BulkActionRequestBody
from openapi_server.models.clocking_records_clocking_record_id_put200_response import ClockingRecordsClockingRecordIdPut200Response
from openapi_server.models.clocking_records_post201_response import ClockingRecordsPost201Response
from openapi_server.models.companies_company_id_integration_settings_post_request import CompaniesCompanyIdIntegrationSettingsPostRequest
from openapi_server.models.create_success_response import CreateSuccessResponse
from openapi_server.models.empty_success_response import EmptySuccessResponse
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.forbidden_error import ForbiddenError
from openapi_server.models.projects_project_id_users_get200_response import ProjectsProjectIdUsersGet200Response
from openapi_server.models.projects_project_id_users_user_id_get200_response import ProjectsProjectIdUsersUserIdGet200Response
from openapi_server.models.users_post_request import UsersPostRequest
from openapi_server.models.users_resend_welcome_sms_get200_response import UsersResendWelcomeSmsGet200Response
from openapi_server.models.users_user_id_integration_settings_get200_response import UsersUserIdIntegrationSettingsGet200Response
from openapi_server.models.users_user_id_integration_settings_integration_settings_user_id_get200_response import UsersUserIdIntegrationSettingsIntegrationSettingsUserIdGet200Response


pytestmark = pytest.mark.asyncio

async def test_users_bulk_activate(client):
    """Test case for users_bulk_activate

    Activate multiple users
    """
    body = {"id":["id","id"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/users/bulkActivate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_bulk_deactivate(client):
    """Test case for users_bulk_deactivate

    Deactivate multiple users
    """
    body = {"id":["id","id"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/users/bulkDeactivate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_get(client):
    """Test case for users_get

    Get list of users in company
    """
    params = [('first_name', 'first_name_example'),
                    ('last_name', 'last_name_example'),
                    ('email', 'email_example'),
                    ('stock_location_id', 'stock_location_id_example'),
                    ('is_active', True)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/users',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_post(client):
    """Test case for users_post

    Add user to company
    """
    body = openapi_server.UsersPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/users',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_resend_welcome_sms_get(client):
    """Test case for users_resend_welcome_sms_get

    Resend Welcome SMS to the user
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/users/resendWelcomeSms',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_user_id_delete(client):
    """Test case for users_user_id_delete

    Delete user
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/users/{user_id}'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_user_id_get(client):
    """Test case for users_user_id_get

    View user
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/users/{user_id}'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_user_id_integration_settings_get(client):
    """Test case for users_user_id_integration_settings_get

    Get a list of user integration settings
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/users/{user_id}/integration_settings'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_user_id_integration_settings_integration_settings_user_id_delete(client):
    """Test case for users_user_id_integration_settings_integration_settings_user_id_delete

    Delete a user integration setting
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/users/{user_id}/integration_settings/{integration_settings_user_id}'.format(user_id='user_id_example', integration_settings_user_id='integration_settings_user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_user_id_integration_settings_integration_settings_user_id_get(client):
    """Test case for users_user_id_integration_settings_integration_settings_user_id_get

    Get a user integration setting
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/users/{user_id}/integration_settings/{integration_settings_user_id}'.format(user_id='user_id_example', integration_settings_user_id='integration_settings_user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_user_id_integration_settings_integration_settings_user_id_put(client):
    """Test case for users_user_id_integration_settings_integration_settings_user_id_put

    Edit a user integration setting
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/users/{user_id}/integration_settings/{integration_settings_user_id}'.format(user_id='user_id_example', integration_settings_user_id='integration_settings_user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_user_id_integration_settings_post(client):
    """Test case for users_user_id_integration_settings_post

    Add a user integration setting
    """
    body = openapi_server.CompaniesCompanyIdIntegrationSettingsPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/users/{user_id}/integration_settings'.format(user_id='user_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_user_id_put(client):
    """Test case for users_user_id_put

    Edit user
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/users/{user_id}'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_users_user_id_upload_image_post(client):
    """Test case for users_user_id_upload_image_post

    Upload a new image to a user
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    data = FormData()
    data.add_field('image', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/api/v1/users/{user_id}/uploadImage'.format(user_id='user_id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

