# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.runbook import Runbook
from openapi_server.models.runbook_create_or_update_parameters import RunbookCreateOrUpdateParameters
from openapi_server.models.runbook_list_by_automation_account_default_response import RunbookListByAutomationAccountDefaultResponse
from openapi_server.models.runbook_list_result import RunbookListResult
from openapi_server.models.runbook_update_parameters import RunbookUpdateParameters


pytestmark = pytest.mark.asyncio

async def test_runbook_create_or_update(client):
    """Test case for runbook_create_or_update

    
    """
    parameters = {"name":"name","location":"location","properties":{"runbookType":"Script","publishContentLink":{"uri":"uri","version":"version","contentHash":{"value":"value","algorithm":"algorithm"}},"draft":{"draftContentLink":{"uri":"uri","version":"version","contentHash":{"value":"value","algorithm":"algorithm"}},"lastModifiedTime":"2000-01-23T04:56:07.000+00:00","creationTime":"2000-01-23T04:56:07.000+00:00","inEdit":True,"outputTypes":["outputTypes","outputTypes"],"parameters":{"key":{"defaultValue":"defaultValue","position":0,"type":"type","isMandatory":True}}},"logVerbose":True,"description":"description","logProgress":True,"logActivityTrace":0},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/runbooks/{runbook_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', runbook_name='runbook_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_runbook_delete(client):
    """Test case for runbook_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/runbooks/{runbook_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', runbook_name='runbook_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_runbook_get(client):
    """Test case for runbook_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/runbooks/{runbook_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', runbook_name='runbook_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_runbook_get_content(client):
    """Test case for runbook_get_content

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'text/powershell',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/runbooks/{runbook_name}/content'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', runbook_name='runbook_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_runbook_list_by_automation_account(client):
    """Test case for runbook_list_by_automation_account

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/runbooks'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_runbook_update(client):
    """Test case for runbook_update

    
    """
    parameters = {"name":"name","location":"location","properties":{"logVerbose":True,"description":"description","logProgress":True,"logActivityTrace":0},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/runbooks/{runbook_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', runbook_name='runbook_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

