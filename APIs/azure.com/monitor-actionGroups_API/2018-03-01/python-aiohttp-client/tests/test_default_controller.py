# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.action_group_list import ActionGroupList
from openapi_server.models.action_group_patch_body import ActionGroupPatchBody
from openapi_server.models.action_group_resource import ActionGroupResource
from openapi_server.models.enable_request import EnableRequest
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_action_groups_create_or_update(client):
    """Test case for action_groups_create_or_update

    
    """
    action_group = {"properties":{"logicAppReceivers":[{"resourceId":"resourceId","name":"name","callbackUrl":"callbackUrl"},{"resourceId":"resourceId","name":"name","callbackUrl":"callbackUrl"}],"smsReceivers":[{"phoneNumber":"phoneNumber","countryCode":"countryCode","name":"name"},{"phoneNumber":"phoneNumber","countryCode":"countryCode","name":"name"}],"voiceReceivers":[{"phoneNumber":"phoneNumber","countryCode":"countryCode","name":"name"},{"phoneNumber":"phoneNumber","countryCode":"countryCode","name":"name"}],"groupShortName":"groupShortName","azureFunctionReceivers":[{"httpTriggerUrl":"httpTriggerUrl","functionName":"functionName","name":"name","functionAppResourceId":"functionAppResourceId"},{"httpTriggerUrl":"httpTriggerUrl","functionName":"functionName","name":"name","functionAppResourceId":"functionAppResourceId"}],"webhookReceivers":[{"serviceUri":"serviceUri","name":"name"},{"serviceUri":"serviceUri","name":"name"}],"emailReceivers":[{"emailAddress":"emailAddress","name":"name","status":"NotSpecified"},{"emailAddress":"emailAddress","name":"name","status":"NotSpecified"}],"enabled":True,"itsmReceivers":[{"name":"name","connectionId":"connectionId","region":"region","ticketConfiguration":"ticketConfiguration","workspaceId":"workspaceId"},{"name":"name","connectionId":"connectionId","region":"region","ticketConfiguration":"ticketConfiguration","workspaceId":"workspaceId"}],"automationRunbookReceivers":[{"serviceUri":"serviceUri","webhookResourceId":"webhookResourceId","runbookName":"runbookName","name":"name","automationAccountId":"automationAccountId","isGlobalRunbook":True},{"serviceUri":"serviceUri","webhookResourceId":"webhookResourceId","runbookName":"runbookName","name":"name","automationAccountId":"automationAccountId","isGlobalRunbook":True}],"azureAppPushReceivers":[{"emailAddress":"emailAddress","name":"name"},{"emailAddress":"emailAddress","name":"name"}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/microsoft.insights/actionGroups/{action_group_name}'.format(resource_group_name='resource_group_name_example', action_group_name='action_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=action_group,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_action_groups_delete(client):
    """Test case for action_groups_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/microsoft.insights/actionGroups/{action_group_name}'.format(resource_group_name='resource_group_name_example', action_group_name='action_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_action_groups_enable_receiver(client):
    """Test case for action_groups_enable_receiver

    
    """
    enable_request = {"receiverName":"receiverName"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/microsoft.insights/actionGroups/{action_group_name}/subscribe'.format(resource_group_name='resource_group_name_example', action_group_name='action_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=enable_request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_action_groups_get(client):
    """Test case for action_groups_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/microsoft.insights/actionGroups/{action_group_name}'.format(resource_group_name='resource_group_name_example', action_group_name='action_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_action_groups_list_by_resource_group(client):
    """Test case for action_groups_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/microsoft.insights/actionGroups'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_action_groups_list_by_subscription_id(client):
    """Test case for action_groups_list_by_subscription_id

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/microsoft.insights/actionGroups'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_action_groups_update(client):
    """Test case for action_groups_update

    
    """
    action_group_patch = {"properties":{"enabled":True},"tags":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/microsoft.insights/actionGroups/{action_group_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', action_group_name='action_group_name_example'),
        headers=headers,
        json=action_group_patch,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

