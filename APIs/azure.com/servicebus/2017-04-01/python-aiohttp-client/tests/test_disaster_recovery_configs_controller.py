# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.access_keys import AccessKeys
from openapi_server.models.arm_disaster_recovery import ArmDisasterRecovery
from openapi_server.models.arm_disaster_recovery_list_result import ArmDisasterRecoveryListResult
from openapi_server.models.check_name_availability import CheckNameAvailability
from openapi_server.models.check_name_availability_result import CheckNameAvailabilityResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.sb_authorization_rule import SBAuthorizationRule
from openapi_server.models.sb_authorization_rule_list_result import SBAuthorizationRuleListResult


pytestmark = pytest.mark.asyncio

async def test_disaster_recovery_configs_break_pairing(client):
    """Test case for disaster_recovery_configs_break_pairing

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceBus/namespaces/{namespace_name}/disasterRecoveryConfigs/{alias}/breakPairing'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', alias='alias_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disaster_recovery_configs_check_name_availability(client):
    """Test case for disaster_recovery_configs_check_name_availability

    
    """
    parameters = {"name":"name"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceBus/namespaces/{namespace_name}/disasterRecoveryConfigs/CheckNameAvailability'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disaster_recovery_configs_create_or_update(client):
    """Test case for disaster_recovery_configs_create_or_update

    
    """
    parameters = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceBus/namespaces/{namespace_name}/disasterRecoveryConfigs/{alias}'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', alias='alias_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disaster_recovery_configs_delete(client):
    """Test case for disaster_recovery_configs_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceBus/namespaces/{namespace_name}/disasterRecoveryConfigs/{alias}'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', alias='alias_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disaster_recovery_configs_fail_over(client):
    """Test case for disaster_recovery_configs_fail_over

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceBus/namespaces/{namespace_name}/disasterRecoveryConfigs/{alias}/failover'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', alias='alias_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disaster_recovery_configs_get(client):
    """Test case for disaster_recovery_configs_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceBus/namespaces/{namespace_name}/disasterRecoveryConfigs/{alias}'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', alias='alias_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disaster_recovery_configs_get_authorization_rule(client):
    """Test case for disaster_recovery_configs_get_authorization_rule

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceBus/namespaces/{namespace_name}/disasterRecoveryConfigs/{alias}/AuthorizationRules/{authorization_rule_name}'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', alias='alias_example', authorization_rule_name='authorization_rule_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disaster_recovery_configs_list(client):
    """Test case for disaster_recovery_configs_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceBus/namespaces/{namespace_name}/disasterRecoveryConfigs'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disaster_recovery_configs_list_authorization_rules(client):
    """Test case for disaster_recovery_configs_list_authorization_rules

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceBus/namespaces/{namespace_name}/disasterRecoveryConfigs/{alias}/AuthorizationRules'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', alias='alias_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disaster_recovery_configs_list_keys(client):
    """Test case for disaster_recovery_configs_list_keys

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceBus/namespaces/{namespace_name}/disasterRecoveryConfigs/{alias}/AuthorizationRules/{authorization_rule_name}/listKeys'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', alias='alias_example', authorization_rule_name='authorization_rule_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

