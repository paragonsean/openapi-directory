# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.logical_server_security_alert_policy_list_result import LogicalServerSecurityAlertPolicyListResult
from openapi_server.models.server_security_alert_policy import ServerSecurityAlertPolicy


pytestmark = pytest.mark.asyncio

async def test_server_security_alert_policies_create_or_update(client):
    """Test case for server_security_alert_policies_create_or_update

    
    """
    parameters = {"properties":{"disabledAlerts":["disabledAlerts","disabledAlerts"],"storageEndpoint":"storageEndpoint","emailAddresses":["emailAddresses","emailAddresses"],"creationTime":"2000-01-23T04:56:07.000+00:00","emailAccountAdmins":True,"retentionDays":0,"storageAccountAccessKey":"storageAccountAccessKey","state":"New"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/securityAlertPolicies/{security_alert_policy_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', security_alert_policy_name='security_alert_policy_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_server_security_alert_policies_get(client):
    """Test case for server_security_alert_policies_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/securityAlertPolicies/{security_alert_policy_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', security_alert_policy_name='security_alert_policy_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_server_security_alert_policies_list_by_server(client):
    """Test case for server_security_alert_policies_list_by_server

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/securityAlertPolicies'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

