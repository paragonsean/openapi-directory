# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.action_rule import ActionRule
from openapi_server.models.action_rules_list import ActionRulesList
from openapi_server.models.alert import Alert
from openapi_server.models.alert_modification import AlertModification
from openapi_server.models.alerts_list import AlertsList
from openapi_server.models.alerts_summary import AlertsSummary
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.operations_list import OperationsList
from openapi_server.models.patch_object import PatchObject
from openapi_server.models.smart_group import SmartGroup
from openapi_server.models.smart_group_modification import SmartGroupModification
from openapi_server.models.smart_groups_list import SmartGroupsList


pytestmark = pytest.mark.asyncio

async def test_action_rules_create_update(client):
    """Test case for action_rules_create_update

    Create/update an action rule
    """
    action_rule = openapi_server.ActionRule()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.AlertsManagement/actionRules/{action_rule_name}'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', action_rule_name='action_rule_name_example'),
        headers=headers,
        json=action_rule,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_action_rules_delete(client):
    """Test case for action_rules_delete

    Delete action rule
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.AlertsManagement/actionRules/{action_rule_name}'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', action_rule_name='action_rule_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_action_rules_get_all_resource_group(client):
    """Test case for action_rules_get_all_resource_group

    Get all action rules created in a resource group
    """
    params = [('targetResourceGroup', 'target_resource_group_example'),
                    ('targetResourceType', 'target_resource_type_example'),
                    ('targetResource', 'target_resource_example'),
                    ('severity', 'severity_example'),
                    ('monitorService', 'monitor_service_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.AlertsManagement/actionRules'.format(subscription_id='subscription_id_example', resource_group='resource_group_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_action_rules_get_all_subscription(client):
    """Test case for action_rules_get_all_subscription

    Get all action rule in a given subscription
    """
    params = [('targetResourceGroup', 'target_resource_group_example'),
                    ('targetResourceType', 'target_resource_type_example'),
                    ('targetResource', 'target_resource_example'),
                    ('severity', 'severity_example'),
                    ('monitorService', 'monitor_service_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.AlertsManagement/actionRules'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_action_rules_get_by_name(client):
    """Test case for action_rules_get_by_name

    Get action rule by name
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.AlertsManagement/actionRules/{action_rule_name}'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', action_rule_name='action_rule_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_action_rules_patch(client):
    """Test case for action_rules_patch

    Patch action rule
    """
    action_rule_patch = openapi_server.PatchObject()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.AlertsManagement/actionRules/{action_rule_name}'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', action_rule_name='action_rule_name_example'),
        headers=headers,
        json=action_rule_patch,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alerts_change_state(client):
    """Test case for alerts_change_state

    
    """
    params = [('api-version', 'api_version_example'),
                    ('newState', 'new_state_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.AlertsManagement/alerts/{alert_id}/changestate'.format(subscription_id='subscription_id_example', alert_id='alert_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alerts_get_all(client):
    """Test case for alerts_get_all

    
    """
    params = [('targetResource', 'target_resource_example'),
                    ('targetResourceGroup', 'target_resource_group_example'),
                    ('targetResourceType', 'target_resource_type_example'),
                    ('monitorService', 'monitor_service_example'),
                    ('monitorCondition', 'monitor_condition_example'),
                    ('severity', 'severity_example'),
                    ('alertState', 'alert_state_example'),
                    ('smartGroupId', 'smart_group_id_example'),
                    ('includePayload', True),
                    ('pageCount', 56),
                    ('sortBy', 'sort_by_example'),
                    ('sortOrder', 'sort_order_example'),
                    ('timeRange', 'time_range_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.AlertsManagement/alerts'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alerts_get_by_id(client):
    """Test case for alerts_get_by_id

    Get a specific alert.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.AlertsManagement/alerts/{alert_id}'.format(subscription_id='subscription_id_example', alert_id='alert_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alerts_get_history(client):
    """Test case for alerts_get_history

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.AlertsManagement/alerts/{alert_id}/history'.format(subscription_id='subscription_id_example', alert_id='alert_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alerts_get_summary(client):
    """Test case for alerts_get_summary

    
    """
    params = [('targetResourceGroup', 'target_resource_group_example'),
                    ('timeRange', 'time_range_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.AlertsManagement/alertsSummary'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_operations_list(client):
    """Test case for operations_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.AlertsManagement/operations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_smart_groups_change_state(client):
    """Test case for smart_groups_change_state

    
    """
    params = [('api-version', 'api_version_example'),
                    ('newState', 'new_state_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.AlertsManagement/smartGroups/{smart_group_id}/changeState'.format(subscription_id='subscription_id_example', smart_group_id='smart_group_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_smart_groups_get_all(client):
    """Test case for smart_groups_get_all

    Get all smartGroups within the subscription
    """
    params = [('targetResource', 'target_resource_example'),
                    ('targetResourceGroup', 'target_resource_group_example'),
                    ('targetResourceType', 'target_resource_type_example'),
                    ('monitorService', 'monitor_service_example'),
                    ('monitorCondition', 'monitor_condition_example'),
                    ('severity', 'severity_example'),
                    ('smartGroupState', 'smart_group_state_example'),
                    ('timeRange', 'time_range_example'),
                    ('pageCount', 56),
                    ('sortBy', 'sort_by_example'),
                    ('sortOrder', 'sort_order_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.AlertsManagement/smartGroups'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_smart_groups_get_by_id(client):
    """Test case for smart_groups_get_by_id

    Get information of smart alerts group.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.AlertsManagement/smartGroups/{smart_group_id}'.format(subscription_id='subscription_id_example', smart_group_id='smart_group_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_smart_groups_get_history(client):
    """Test case for smart_groups_get_history

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.AlertsManagement/smartGroups/{smart_group_id}/history'.format(subscription_id='subscription_id_example', smart_group_id='smart_group_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

