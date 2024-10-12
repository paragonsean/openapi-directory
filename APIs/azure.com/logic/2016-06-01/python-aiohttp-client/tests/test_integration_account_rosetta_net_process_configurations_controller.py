# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.integration_account_rosetta_net_process_configuration import IntegrationAccountRosettaNetProcessConfiguration
from openapi_server.models.integration_account_rosetta_net_process_configuration_list_result import IntegrationAccountRosettaNetProcessConfigurationListResult


pytestmark = pytest.mark.asyncio

async def test_rosetta_net_process_configurations_create_or_update(client):
    """Test case for rosetta_net_process_configurations_create_or_update

    
    """
    rosetta_net_process_configuration = {"properties":{"metadata":{"key":"metadata"},"initiatorRoleSettings":{"role":"role","service":"service","action":"action","description":"description","businessDocument":{"name":"name","description":"description","version":"version"},"roleType":"NotSpecified","serviceClassification":"serviceClassification"},"processName":"processName","processCode":"processCode","createdTime":"2000-01-23T04:56:07.000+00:00","description":"description","activitySettings":{"activityBehavior":{"actionType":"NotSpecified","responseType":"NotSpecified","nonRepudiationOfOriginAndContent":True,"retryCount":6,"isAuthorizationRequired":True,"timeToPerformInSeconds":1,"isSecuredTransportRequired":True,"persistentConfidentialityScope":"NotSpecified"},"acknowledgmentOfReceiptSettings":{"timeToAcknowledgeInSeconds":0,"isNonRepudiationRequired":True},"activityType":"NotSpecified"},"changedTime":"2000-01-23T04:56:07.000+00:00","responderRoleSettings":{"role":"role","service":"service","action":"action","description":"description","businessDocument":{"name":"name","description":"description","version":"version"},"roleType":"NotSpecified","serviceClassification":"serviceClassification"},"processVersion":"processVersion"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/integrationAccounts/{integration_account_name}/rosettanetprocessconfigurations/{rosetta_net_process_configuration_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', integration_account_name='integration_account_name_example', rosetta_net_process_configuration_name='rosetta_net_process_configuration_name_example'),
        headers=headers,
        json=rosetta_net_process_configuration,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rosetta_net_process_configurations_delete(client):
    """Test case for rosetta_net_process_configurations_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/integrationAccounts/{integration_account_name}/rosettanetprocessconfigurations/{rosetta_net_process_configuration_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', integration_account_name='integration_account_name_example', rosetta_net_process_configuration_name='rosetta_net_process_configuration_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rosetta_net_process_configurations_get(client):
    """Test case for rosetta_net_process_configurations_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/integrationAccounts/{integration_account_name}/rosettanetprocessconfigurations/{rosetta_net_process_configuration_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', integration_account_name='integration_account_name_example', rosetta_net_process_configuration_name='rosetta_net_process_configuration_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rosetta_net_process_configurations_list_by_integration_accounts(client):
    """Test case for rosetta_net_process_configurations_list_by_integration_accounts

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$top', 56),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/integrationAccounts/{integration_account_name}/rosettanetprocessconfigurations'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', integration_account_name='integration_account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

