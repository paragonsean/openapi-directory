# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.application_insights_component_proactive_detection_configuration import ApplicationInsightsComponentProactiveDetectionConfiguration


pytestmark = pytest.mark.asyncio

async def test_proactive_detection_configurations_get(client):
    """Test case for proactive_detection_configurations_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Insights/components/{resource_name}/ProactiveDetectionConfigs/{configuration_id}'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', resource_name='resource_name_example', configuration_id='configuration_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_proactive_detection_configurations_list(client):
    """Test case for proactive_detection_configurations_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Insights/components/{resource_name}/ProactiveDetectionConfigs'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', resource_name='resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_proactive_detection_configurations_update(client):
    """Test case for proactive_detection_configurations_update

    
    """
    proactive_detection_properties = {"name":"name","location":"location","id":"id","type":"type","properties":{"CustomEmails":["CustomEmails","CustomEmails"],"SendEmailsToSubscriptionOwners":True,"Enabled":True,"LastUpdatedTime":"LastUpdatedTime","RuleDefinitions":{"IsHidden":True,"IsInPreview":True,"SupportsEmailNotifications":True,"Description":"Description","DisplayName":"DisplayName","IsEnabledByDefault":True,"HelpUrl":"HelpUrl","Name":"Name"},"Name":"Name"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Insights/components/{resource_name}/ProactiveDetectionConfigs/{configuration_id}'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', resource_name='resource_name_example', configuration_id='configuration_id_example'),
        headers=headers,
        json=proactive_detection_properties,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

