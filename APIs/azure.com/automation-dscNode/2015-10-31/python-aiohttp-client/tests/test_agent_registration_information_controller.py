# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.agent_registration import AgentRegistration
from openapi_server.models.agent_registration_information_get_default_response import AgentRegistrationInformationGetDefaultResponse
from openapi_server.models.agent_registration_regenerate_key_parameter import AgentRegistrationRegenerateKeyParameter


pytestmark = pytest.mark.asyncio

async def test_agent_registration_information_get(client):
    """Test case for agent_registration_information_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/agentRegistrationInformation'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_agent_registration_information_regenerate_key(client):
    """Test case for agent_registration_information_regenerate_key

    
    """
    parameters = {"keyName":"primary","name":"name","location":"location","tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/agentRegistrationInformation/regenerateKey'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

