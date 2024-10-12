# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.device import Device
from openapi_server.models.device_state import DeviceState
from openapi_server.models.devices_list_response import DevicesListResponse


pytestmark = pytest.mark.asyncio

async def test_androidenterprise_devices_force_report_upload(client):
    """Test case for androidenterprise_devices_force_report_upload

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/androidenterprise/v1/enterprises/{enterprise_id}/users/{user_id}/devices/{device_id}/forceReportUpload'.format(enterprise_id='enterprise_id_example', user_id='user_id_example', device_id='device_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidenterprise_devices_get(client):
    """Test case for androidenterprise_devices_get

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/androidenterprise/v1/enterprises/{enterprise_id}/users/{user_id}/devices/{device_id}'.format(enterprise_id='enterprise_id_example', user_id='user_id_example', device_id='device_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidenterprise_devices_get_state(client):
    """Test case for androidenterprise_devices_get_state

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/androidenterprise/v1/enterprises/{enterprise_id}/users/{user_id}/devices/{device_id}/state'.format(enterprise_id='enterprise_id_example', user_id='user_id_example', device_id='device_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidenterprise_devices_list(client):
    """Test case for androidenterprise_devices_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/androidenterprise/v1/enterprises/{enterprise_id}/users/{user_id}/devices'.format(enterprise_id='enterprise_id_example', user_id='user_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidenterprise_devices_set_state(client):
    """Test case for androidenterprise_devices_set_state

    
    """
    body = {"accountState":"enabled"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/androidenterprise/v1/enterprises/{enterprise_id}/users/{user_id}/devices/{device_id}/state'.format(enterprise_id='enterprise_id_example', user_id='user_id_example', device_id='device_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidenterprise_devices_update(client):
    """Test case for androidenterprise_devices_update

    
    """
    body = {"product":"product","retailBrand":"retailBrand","latestBuildFingerprint":"latestBuildFingerprint","report":{"appState":[{"keyedAppState":[{"severity":"severityUnknown","data":"data","message":"message","key":"key","stateTimestampMillis":"stateTimestampMillis"},{"severity":"severityUnknown","data":"data","message":"message","key":"key","stateTimestampMillis":"stateTimestampMillis"}],"packageName":"packageName"},{"keyedAppState":[{"severity":"severityUnknown","data":"data","message":"message","key":"key","stateTimestampMillis":"stateTimestampMillis"},{"severity":"severityUnknown","data":"data","message":"message","key":"key","stateTimestampMillis":"stateTimestampMillis"}],"packageName":"packageName"}],"lastUpdatedTimestampMillis":"lastUpdatedTimestampMillis"},"maker":"maker","model":"model","sdkVersion":5,"device":"device","androidId":"androidId","managementType":"managedDevice","policy":{"deviceReportPolicy":"deviceReportPolicyUnspecified","maintenanceWindow":{"durationMs":"durationMs","startTimeAfterMidnightMs":"startTimeAfterMidnightMs"},"productAvailabilityPolicy":"productAvailabilityPolicyUnspecified","productPolicy":[{"enterpriseAuthenticationAppLinkConfigs":[{"uri":"uri"},{"uri":"uri"}],"autoUpdateMode":"autoUpdateModeUnspecified","productId":"productId","trackIds":["trackIds","trackIds"],"autoInstallPolicy":{"autoInstallPriority":0,"autoInstallConstraint":[{"deviceIdleStateConstraint":"deviceIdleStateConstraintUnspecified","networkTypeConstraint":"networkTypeConstraintUnspecified","chargingStateConstraint":"chargingStateConstraintUnspecified"},{"deviceIdleStateConstraint":"deviceIdleStateConstraintUnspecified","networkTypeConstraint":"networkTypeConstraintUnspecified","chargingStateConstraint":"chargingStateConstraintUnspecified"}],"minimumVersionCode":6,"autoInstallMode":"autoInstallModeUnspecified"},"managedConfiguration":{"productId":"productId","kind":"kind","managedProperty":[{"valueBundle":{"managedProperty":[null,null]},"valueStringArray":["valueStringArray","valueStringArray"],"valueString":"valueString","valueBundleArray":[{"managedProperty":[null,null]},{"managedProperty":[null,null]}],"valueInteger":1,"key":"key","valueBool":True},{"valueBundle":{"managedProperty":[null,null]},"valueStringArray":["valueStringArray","valueStringArray"],"valueString":"valueString","valueBundleArray":[{"managedProperty":[null,null]},{"managedProperty":[null,null]}],"valueInteger":1,"key":"key","valueBool":True}],"configurationVariables":{"mcmId":"mcmId","variableSet":[{"userValue":"userValue","placeholder":"placeholder"},{"userValue":"userValue","placeholder":"placeholder"}]}},"tracks":["appTrackUnspecified","appTrackUnspecified"]},{"enterpriseAuthenticationAppLinkConfigs":[{"uri":"uri"},{"uri":"uri"}],"autoUpdateMode":"autoUpdateModeUnspecified","productId":"productId","trackIds":["trackIds","trackIds"],"autoInstallPolicy":{"autoInstallPriority":0,"autoInstallConstraint":[{"deviceIdleStateConstraint":"deviceIdleStateConstraintUnspecified","networkTypeConstraint":"networkTypeConstraintUnspecified","chargingStateConstraint":"chargingStateConstraintUnspecified"},{"deviceIdleStateConstraint":"deviceIdleStateConstraintUnspecified","networkTypeConstraint":"networkTypeConstraintUnspecified","chargingStateConstraint":"chargingStateConstraintUnspecified"}],"minimumVersionCode":6,"autoInstallMode":"autoInstallModeUnspecified"},"managedConfiguration":{"productId":"productId","kind":"kind","managedProperty":[{"valueBundle":{"managedProperty":[null,null]},"valueStringArray":["valueStringArray","valueStringArray"],"valueString":"valueString","valueBundleArray":[{"managedProperty":[null,null]},{"managedProperty":[null,null]}],"valueInteger":1,"key":"key","valueBool":True},{"valueBundle":{"managedProperty":[null,null]},"valueStringArray":["valueStringArray","valueStringArray"],"valueString":"valueString","valueBundleArray":[{"managedProperty":[null,null]},{"managedProperty":[null,null]}],"valueInteger":1,"key":"key","valueBool":True}],"configurationVariables":{"mcmId":"mcmId","variableSet":[{"userValue":"userValue","placeholder":"placeholder"},{"userValue":"userValue","placeholder":"placeholder"}]}},"tracks":["appTrackUnspecified","appTrackUnspecified"]}],"autoUpdatePolicy":"autoUpdatePolicyUnspecified"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('updateMask', 'update_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/androidenterprise/v1/enterprises/{enterprise_id}/users/{user_id}/devices/{device_id}'.format(enterprise_id='enterprise_id_example', user_id='user_id_example', device_id='device_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

