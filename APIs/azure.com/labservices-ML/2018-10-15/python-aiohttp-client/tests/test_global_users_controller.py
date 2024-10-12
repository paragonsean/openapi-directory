# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.environment_operations_payload import EnvironmentOperationsPayload
from openapi_server.models.get_environment_response import GetEnvironmentResponse
from openapi_server.models.get_personal_preferences_response import GetPersonalPreferencesResponse
from openapi_server.models.list_environments_payload import ListEnvironmentsPayload
from openapi_server.models.list_environments_response import ListEnvironmentsResponse
from openapi_server.models.list_labs_response import ListLabsResponse
from openapi_server.models.operation_batch_status_payload import OperationBatchStatusPayload
from openapi_server.models.operation_batch_status_response import OperationBatchStatusResponse
from openapi_server.models.operation_status_payload import OperationStatusPayload
from openapi_server.models.operation_status_response import OperationStatusResponse
from openapi_server.models.personal_preferences_operations_payload import PersonalPreferencesOperationsPayload
from openapi_server.models.register_payload import RegisterPayload
from openapi_server.models.reset_password_payload import ResetPasswordPayload


pytestmark = pytest.mark.asyncio

async def test_global_users_get_environment(client):
    """Test case for global_users_get_environment

    
    """
    environment_operations_payload = {"environmentId":"environmentId"}
    params = [('$expand', 'expand_example'),
                    ('api-version', '2018-10-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.LabServices/users/{user_name}/getEnvironment'.format(user_name='user_name_example'),
        headers=headers,
        json=environment_operations_payload,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_global_users_get_operation_batch_status(client):
    """Test case for global_users_get_operation_batch_status

    
    """
    operation_batch_status_payload = {"urls":["urls","urls"]}
    params = [('api-version', '2018-10-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.LabServices/users/{user_name}/getOperationBatchStatus'.format(user_name='user_name_example'),
        headers=headers,
        json=operation_batch_status_payload,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_global_users_get_operation_status(client):
    """Test case for global_users_get_operation_status

    
    """
    operation_status_payload = {"operationUrl":"operationUrl"}
    params = [('api-version', '2018-10-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.LabServices/users/{user_name}/getOperationStatus'.format(user_name='user_name_example'),
        headers=headers,
        json=operation_status_payload,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_global_users_get_personal_preferences(client):
    """Test case for global_users_get_personal_preferences

    
    """
    personal_preferences_operations_payload = {"addRemove":"Add","labAccountResourceId":"labAccountResourceId","labResourceId":"labResourceId"}
    params = [('api-version', '2018-10-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.LabServices/users/{user_name}/getPersonalPreferences'.format(user_name='user_name_example'),
        headers=headers,
        json=personal_preferences_operations_payload,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_global_users_list_environments(client):
    """Test case for global_users_list_environments

    
    """
    list_environments_payload = {"labId":"labId"}
    params = [('api-version', '2018-10-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.LabServices/users/{user_name}/listEnvironments'.format(user_name='user_name_example'),
        headers=headers,
        json=list_environments_payload,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_global_users_list_labs(client):
    """Test case for global_users_list_labs

    
    """
    params = [('api-version', '2018-10-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.LabServices/users/{user_name}/listLabs'.format(user_name='user_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_global_users_register(client):
    """Test case for global_users_register

    
    """
    register_payload = {"registrationCode":"registrationCode"}
    params = [('api-version', '2018-10-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.LabServices/users/{user_name}/register'.format(user_name='user_name_example'),
        headers=headers,
        json=register_payload,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_global_users_reset_password(client):
    """Test case for global_users_reset_password

    
    """
    reset_password_payload = {"password":"password","environmentId":"environmentId","username":"username"}
    params = [('api-version', '2018-10-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.LabServices/users/{user_name}/resetPassword'.format(user_name='user_name_example'),
        headers=headers,
        json=reset_password_payload,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_global_users_start_environment(client):
    """Test case for global_users_start_environment

    
    """
    environment_operations_payload = {"environmentId":"environmentId"}
    params = [('api-version', '2018-10-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.LabServices/users/{user_name}/startEnvironment'.format(user_name='user_name_example'),
        headers=headers,
        json=environment_operations_payload,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_global_users_stop_environment(client):
    """Test case for global_users_stop_environment

    
    """
    environment_operations_payload = {"environmentId":"environmentId"}
    params = [('api-version', '2018-10-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.LabServices/users/{user_name}/stopEnvironment'.format(user_name='user_name_example'),
        headers=headers,
        json=environment_operations_payload,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

