# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.action_rule import ActionRule
from openapi_server.models.action_rules_list import ActionRulesList
from openapi_server.models.alert import Alert
from openapi_server.models.alert_modification import AlertModification
from openapi_server.models.alerts_list import AlertsList
from openapi_server.models.alerts_meta_data import AlertsMetaData
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
    action_rule = {"properties":{"createdAt":"2000-01-23T04:56:07.000+00:00","lastModifiedAt":"2000-01-23T04:56:07.000+00:00","createdBy":"createdBy","lastModifiedBy":"lastModifiedBy","scope":{"scopeType":"ResourceGroup","values":["values","values"]},"description":"description","conditions":{"monitorCondition":{"values":["values","values"],"operator":"Equals"},"severity":{"values":["values","values"],"operator":"Equals"},"alertContext":{"values":["values","values"],"operator":"Equals"},"description":{"values":["values","values"],"operator":"Equals"},"monitorService":{"values":["values","values"],"operator":"Equals"},"alertRuleId":{"values":["values","values"],"operator":"Equals"},"targetResourceType":{"values":["values","values"],"operator":"Equals"}},"type":"Suppression","status":"Enabled"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AlertsManagement/actionRules/{action_rule_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', action_rule_name='action_rule_name_example'),
        headers=headers,
        json=action_rule,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_action_rules_delete(client):
    """Test case for action_rules_delete

    Delete action rule
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AlertsManagement/actionRules/{action_rule_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', action_rule_name='action_rule_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_action_rules_get_by_name(client):
    """Test case for action_rules_get_by_name

    Get action rule by name
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AlertsManagement/actionRules/{action_rule_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', action_rule_name='action_rule_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_action_rules_list_by_resource_group(client):
    """Test case for action_rules_list_by_resource_group

    Get all action rules created in a resource group
    """
    params = [('targetResourceGroup', 'target_resource_group_example'),
                    ('targetResourceType', 'target_resource_type_example'),
                    ('targetResource', 'target_resource_example'),
                    ('severity', 'severity_example'),
                    ('monitorService', 'monitor_service_example'),
                    ('impactedScope', 'impacted_scope_example'),
                    ('description', 'description_example'),
                    ('alertRuleId', 'alert_rule_id_example'),
                    ('actionGroup', 'action_group_example'),
                    ('name', 'name_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AlertsManagement/actionRules'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_action_rules_list_by_subscription(client):
    """Test case for action_rules_list_by_subscription

    Get all action rule in a given subscription
    """
    params = [('targetResourceGroup', 'target_resource_group_example'),
                    ('targetResourceType', 'target_resource_type_example'),
                    ('targetResource', 'target_resource_example'),
                    ('severity', 'severity_example'),
                    ('monitorService', 'monitor_service_example'),
                    ('impactedScope', 'impacted_scope_example'),
                    ('description', 'description_example'),
                    ('alertRuleId', 'alert_rule_id_example'),
                    ('actionGroup', 'action_group_example'),
                    ('name', 'name_example'),
                    ('api-version', 'api_version_example')]
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

async def test_action_rules_update(client):
    """Test case for action_rules_update

    Patch action rule
    """
    action_rule_patch = {"properties":{"status":"Enabled"},"tags":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AlertsManagement/actionRules/{action_rule_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', action_rule_name='action_rule_name_example'),
        headers=headers,
        json=action_rule_patch,
        params=params,
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
                    ('targetResourceType', 'target_resource_type_example'),
                    ('targetResourceGroup', 'target_resource_group_example'),
                    ('monitorService', 'monitor_service_example'),
                    ('monitorCondition', 'monitor_condition_example'),
                    ('severity', 'severity_example'),
                    ('alertState', 'alert_state_example'),
                    ('alertRule', 'alert_rule_example'),
                    ('smartGroupId', 'smart_group_id_example'),
                    ('includeContext', True),
                    ('includeEgressConfig', True),
                    ('pageCount', 56),
                    ('sortBy', 'sort_by_example'),
                    ('sortOrder', 'sort_order_example'),
                    ('select', 'select_example'),
                    ('timeRange', 'time_range_example'),
                    ('customTimeRange', 'custom_time_range_example'),
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
    params = [('groupby', 'groupby_example'),
                    ('includeSmartGroupsCount', True),
                    ('targetResource', 'target_resource_example'),
                    ('targetResourceType', 'target_resource_type_example'),
                    ('targetResourceGroup', 'target_resource_group_example'),
                    ('monitorService', 'monitor_service_example'),
                    ('monitorCondition', 'monitor_condition_example'),
                    ('severity', 'severity_example'),
                    ('alertState', 'alert_state_example'),
                    ('alertRule', 'alert_rule_example'),
                    ('timeRange', 'time_range_example'),
                    ('customTimeRange', 'custom_time_range_example'),
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

async def test_alerts_meta_data(client):
    """Test case for alerts_meta_data

    
    """
    params = [('api-version', 'api_version_example'),
                    ('identifier', 'identifier_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.AlertsManagement/alertsMetaData',
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

    Get all Smart Groups within a specified subscription
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

    Get information related to a specific Smart Group.
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

