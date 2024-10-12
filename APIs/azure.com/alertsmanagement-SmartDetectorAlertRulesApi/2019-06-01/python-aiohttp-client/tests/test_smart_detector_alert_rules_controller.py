# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.alert_rule import AlertRule
from openapi_server.models.alert_rule_patch_object import AlertRulePatchObject
from openapi_server.models.alert_rules_list import AlertRulesList
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_smart_detector_alert_rules_create_or_update(client):
    """Test case for smart_detector_alert_rules_create_or_update

    
    """
    parameters = {"properties":{"severity":"Sev0","throttling":{"duration":"duration"},"actionGroups":{"groupIds":["groupIds","groupIds"],"customWebhookPayload":"customWebhookPayload","customEmailSubject":"customEmailSubject"},"scope":["scope","scope"],"description":"description","state":"Enabled","detector":{"supportedResourceTypes":["supportedResourceTypes","supportedResourceTypes"],"imagePaths":["imagePaths","imagePaths"],"name":"name","description":"description","id":"id","parameters":{"key":"{}"}},"frequency":"frequency"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/microsoft.alertsManagement/smartDetectorAlertRules/{alert_rule_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', alert_rule_name='alert_rule_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_smart_detector_alert_rules_delete(client):
    """Test case for smart_detector_alert_rules_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/microsoft.alertsManagement/smartDetectorAlertRules/{alert_rule_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', alert_rule_name='alert_rule_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_smart_detector_alert_rules_get(client):
    """Test case for smart_detector_alert_rules_get

    
    """
    params = [('api-version', 'api_version_example'),
                    ('expandDetector', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/microsoft.alertsManagement/smartDetectorAlertRules/{alert_rule_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', alert_rule_name='alert_rule_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_smart_detector_alert_rules_list(client):
    """Test case for smart_detector_alert_rules_list

    
    """
    params = [('api-version', 'api_version_example'),
                    ('expandDetector', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/microsoft.alertsManagement/smartDetectorAlertRules'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_smart_detector_alert_rules_list_by_resource_group(client):
    """Test case for smart_detector_alert_rules_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example'),
                    ('expandDetector', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/microsoft.alertsManagement/smartDetectorAlertRules'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_smart_detector_alert_rules_patch(client):
    """Test case for smart_detector_alert_rules_patch

    
    """
    parameters = {"name":"name","id":"id","type":"type","properties":{"severity":"Sev0","throttling":{"duration":"duration"},"actionGroups":{"groupIds":["groupIds","groupIds"],"customWebhookPayload":"customWebhookPayload","customEmailSubject":"customEmailSubject"},"description":"description","state":"Enabled","frequency":"frequency"},"tags":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/microsoft.alertsManagement/smartDetectorAlertRules/{alert_rule_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', alert_rule_name='alert_rule_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

