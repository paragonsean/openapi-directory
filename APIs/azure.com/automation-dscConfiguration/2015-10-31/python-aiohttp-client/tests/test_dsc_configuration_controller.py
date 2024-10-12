# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.dsc_configuration import DscConfiguration
from openapi_server.models.dsc_configuration_create_or_update_parameters import DscConfigurationCreateOrUpdateParameters
from openapi_server.models.dsc_configuration_list_by_automation_account_default_response import DscConfigurationListByAutomationAccountDefaultResponse
from openapi_server.models.dsc_configuration_list_result import DscConfigurationListResult
from openapi_server.models.dsc_configuration_update_parameters import DscConfigurationUpdateParameters


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_dsc_configuration_create_or_update(client):
    """Test case for dsc_configuration_create_or_update

    
    """
    parameters = {"name":"name","location":"location","properties":{"logVerbose":True,"description":"description","logProgress":True,"source":{"type":"embeddedContent","value":"value","version":"version","hash":{"value":"value","algorithm":"algorithm"}},"parameters":{"key":{"defaultValue":"defaultValue","position":5,"type":"type","isMandatory":True}}},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/configurations/{configuration_name}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', configuration_name='configuration_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dsc_configuration_delete(client):
    """Test case for dsc_configuration_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/configurations/{configuration_name}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', configuration_name='configuration_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dsc_configuration_get(client):
    """Test case for dsc_configuration_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/configurations/{configuration_name}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', configuration_name='configuration_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dsc_configuration_get_content(client):
    """Test case for dsc_configuration_get_content

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'text/powershell',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/configurations/{configuration_name}/content'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', configuration_name='configuration_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dsc_configuration_list_by_automation_account(client):
    """Test case for dsc_configuration_list_by_automation_account

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$skip', 56),
                    ('$top', 56),
                    ('$inlinecount', 'inlinecount_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/configurations'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_dsc_configuration_update(client):
    """Test case for dsc_configuration_update

    
    """
    parameters = {"name":"name","properties":{"logVerbose":True,"description":"description","logProgress":True,"source":{"type":"embeddedContent","value":"value","version":"version","hash":{"value":"value","algorithm":"algorithm"}},"parameters":{"key":{"defaultValue":"defaultValue","position":5,"type":"type","isMandatory":True}}},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/configurations/{configuration_name}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', configuration_name='configuration_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

