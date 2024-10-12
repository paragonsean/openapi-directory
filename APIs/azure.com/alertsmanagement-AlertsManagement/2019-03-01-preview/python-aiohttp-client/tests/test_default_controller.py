# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.alert import Alert
from openapi_server.models.alert_modification import AlertModification
from openapi_server.models.alerts_list import AlertsList
from openapi_server.models.alerts_summary import AlertsSummary
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.operations_list import OperationsList
from openapi_server.models.smart_group import SmartGroup
from openapi_server.models.smart_group_modification import SmartGroupModification
from openapi_server.models.smart_groups_list import SmartGroupsList


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
        path='/{scope}/providers/Microsoft.AlertsManagement/alerts/{alert_id}/changestate'.format(scope='scope_example', alert_id='alert_id_example'),
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
        path='/{scope}/providers/Microsoft.AlertsManagement/alerts'.format(scope='scope_example'),
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
        path='/{scope}/providers/Microsoft.AlertsManagement/alerts/{alert_id}'.format(scope='scope_example', alert_id='alert_id_example'),
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
        path='/{scope}/providers/Microsoft.AlertsManagement/alerts/{alert_id}/history'.format(scope='scope_example', alert_id='alert_id_example'),
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
        path='/{scope}/providers/Microsoft.AlertsManagement/alertsSummary'.format(scope='scope_example'),
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

