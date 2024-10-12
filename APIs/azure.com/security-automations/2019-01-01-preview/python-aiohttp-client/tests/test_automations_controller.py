# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.automation import Automation
from openapi_server.models.automation_list import AutomationList
from openapi_server.models.automation_validation_status import AutomationValidationStatus
from openapi_server.models.automations_list_default_response import AutomationsListDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_automations_create_or_update(client):
    """Test case for automations_create_or_update

    
    """
    automation = {"properties":{"sources":[{"eventSource":"Assessments","ruleSets":[{"rules":[{"propertyType":"String","expectedValue":"expectedValue","operator":"Equals","propertyJPath":"propertyJPath"},{"propertyType":"String","expectedValue":"expectedValue","operator":"Equals","propertyJPath":"propertyJPath"}]},{"rules":[{"propertyType":"String","expectedValue":"expectedValue","operator":"Equals","propertyJPath":"propertyJPath"},{"propertyType":"String","expectedValue":"expectedValue","operator":"Equals","propertyJPath":"propertyJPath"}]}]},{"eventSource":"Assessments","ruleSets":[{"rules":[{"propertyType":"String","expectedValue":"expectedValue","operator":"Equals","propertyJPath":"propertyJPath"},{"propertyType":"String","expectedValue":"expectedValue","operator":"Equals","propertyJPath":"propertyJPath"}]},{"rules":[{"propertyType":"String","expectedValue":"expectedValue","operator":"Equals","propertyJPath":"propertyJPath"},{"propertyType":"String","expectedValue":"expectedValue","operator":"Equals","propertyJPath":"propertyJPath"}]}]}],"isEnabled":True,"description":"description","scopes":[{"scopePath":"scopePath","description":"description"},{"scopePath":"scopePath","description":"description"}],"actions":[{"actionType":"LogicApp"},{"actionType":"LogicApp"}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Security/automations/{automation_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', automation_name='automation_name_example'),
        headers=headers,
        json=automation,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_automations_delete(client):
    """Test case for automations_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Security/automations/{automation_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', automation_name='automation_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_automations_get(client):
    """Test case for automations_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Security/automations/{automation_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', automation_name='automation_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_automations_list(client):
    """Test case for automations_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Security/automations'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_automations_list_by_resource_group(client):
    """Test case for automations_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Security/automations'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_automations_validate(client):
    """Test case for automations_validate

    
    """
    automation = {"properties":{"sources":[{"eventSource":"Assessments","ruleSets":[{"rules":[{"propertyType":"String","expectedValue":"expectedValue","operator":"Equals","propertyJPath":"propertyJPath"},{"propertyType":"String","expectedValue":"expectedValue","operator":"Equals","propertyJPath":"propertyJPath"}]},{"rules":[{"propertyType":"String","expectedValue":"expectedValue","operator":"Equals","propertyJPath":"propertyJPath"},{"propertyType":"String","expectedValue":"expectedValue","operator":"Equals","propertyJPath":"propertyJPath"}]}]},{"eventSource":"Assessments","ruleSets":[{"rules":[{"propertyType":"String","expectedValue":"expectedValue","operator":"Equals","propertyJPath":"propertyJPath"},{"propertyType":"String","expectedValue":"expectedValue","operator":"Equals","propertyJPath":"propertyJPath"}]},{"rules":[{"propertyType":"String","expectedValue":"expectedValue","operator":"Equals","propertyJPath":"propertyJPath"},{"propertyType":"String","expectedValue":"expectedValue","operator":"Equals","propertyJPath":"propertyJPath"}]}]}],"isEnabled":True,"description":"description","scopes":[{"scopePath":"scopePath","description":"description"},{"scopePath":"scopePath","description":"description"}],"actions":[{"actionType":"LogicApp"},{"actionType":"LogicApp"}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Security/automations/{automation_name}/validate'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', automation_name='automation_name_example'),
        headers=headers,
        json=automation,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

