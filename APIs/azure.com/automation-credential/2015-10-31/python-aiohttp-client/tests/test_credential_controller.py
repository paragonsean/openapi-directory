# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.credential import Credential
from openapi_server.models.credential_create_or_update_parameters import CredentialCreateOrUpdateParameters
from openapi_server.models.credential_get_default_response import CredentialGetDefaultResponse
from openapi_server.models.credential_list_result import CredentialListResult
from openapi_server.models.credential_update_parameters import CredentialUpdateParameters


pytestmark = pytest.mark.asyncio

async def test_credential_create_or_update(client):
    """Test case for credential_create_or_update

    
    """
    parameters = {"name":"name","properties":{"password":"password","description":"description","userName":"userName"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/credentials/{credential_name}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', credential_name='credential_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_credential_delete(client):
    """Test case for credential_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/credentials/{credential_name}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', credential_name='credential_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_credential_get(client):
    """Test case for credential_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/credentials/{credential_name}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', credential_name='credential_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_credential_list_by_automation_account(client):
    """Test case for credential_list_by_automation_account

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/credentials'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_credential_update(client):
    """Test case for credential_update

    
    """
    parameters = {"name":"name","properties":{"password":"password","description":"description","userName":"userName"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/credentials/{credential_name}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', credential_name='credential_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

