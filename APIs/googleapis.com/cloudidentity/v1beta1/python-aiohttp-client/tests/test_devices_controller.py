# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.approve_device_user_request import ApproveDeviceUserRequest
from openapi_server.models.block_device_user_request import BlockDeviceUserRequest
from openapi_server.models.cancel_wipe_device_user_request import CancelWipeDeviceUserRequest
from openapi_server.models.create_device_request import CreateDeviceRequest
from openapi_server.models.list_device_users_response import ListDeviceUsersResponse
from openapi_server.models.list_devices_response import ListDevicesResponse
from openapi_server.models.lookup_self_device_users_response import LookupSelfDeviceUsersResponse
from openapi_server.models.operation import Operation
from openapi_server.models.wipe_device_user_request import WipeDeviceUserRequest


pytestmark = pytest.mark.asyncio

async def test_cloudidentity_devices_create(client):
    """Test case for cloudidentity_devices_create

    
    """
    body = {"device":{"meid":"meid","ownerType":"DEVICE_OWNERSHIP_UNSPECIFIED","encryptionState":"ENCRYPTION_STATE_UNSPECIFIED","lastSyncTime":"lastSyncTime","networkOperator":"networkOperator","assetTag":"assetTag","buildNumber":"buildNumber","deviceId":"deviceId","manufacturer":"manufacturer","bootloaderVersion":"bootloaderVersion","hostname":"hostname","osVersion":"osVersion","compromisedState":"COMPROMISED_STATE_UNSPECIFIED","endpointVerificationSpecificAttributes":{"additionalSignals":{"key":""},"certificateAttributes":[{"certificateTemplate":{"id":"id","majorVersion":0,"minorVersion":6},"serialNumber":"serialNumber","subject":"subject","validityExpirationTime":"validityExpirationTime","fingerprint":"fingerprint","thumbprint":"thumbprint","validityStartTime":"validityStartTime","issuer":"issuer","validationState":"CERTIFICATE_VALIDATION_STATE_UNSPECIFIED"},{"certificateTemplate":{"id":"id","majorVersion":0,"minorVersion":6},"serialNumber":"serialNumber","subject":"subject","validityExpirationTime":"validityExpirationTime","fingerprint":"fingerprint","thumbprint":"thumbprint","validityStartTime":"validityStartTime","issuer":"issuer","validationState":"CERTIFICATE_VALIDATION_STATE_UNSPECIFIED"}],"browserAttributes":[{"lastProfileSyncTime":"lastProfileSyncTime","chromeBrowserInfo":{"isRealtimeUrlCheckEnabled":True,"isThirdPartyBlockingEnabled":True,"passwordProtectionWarningTrigger":"PASSWORD_PROTECTION_TRIGGER_UNSPECIFIED","isBulkDataEntryAnalysisEnabled":True,"isSiteIsolationEnabled":True,"safeBrowsingProtectionLevel":"SAFE_BROWSING_LEVEL_UNSPECIFIED","isFileUploadAnalysisEnabled":True,"browserManagementState":"UNSPECIFIED","isSecurityEventAnalysisEnabled":True,"browserVersion":"browserVersion","isChromeRemoteDesktopAppBlocked":True,"isFileDownloadAnalysisEnabled":True,"isBuiltInDnsClientEnabled":True,"isChromeCleanupEnabled":True},"chromeProfileId":"chromeProfileId"},{"lastProfileSyncTime":"lastProfileSyncTime","chromeBrowserInfo":{"isRealtimeUrlCheckEnabled":True,"isThirdPartyBlockingEnabled":True,"passwordProtectionWarningTrigger":"PASSWORD_PROTECTION_TRIGGER_UNSPECIFIED","isBulkDataEntryAnalysisEnabled":True,"isSiteIsolationEnabled":True,"safeBrowsingProtectionLevel":"SAFE_BROWSING_LEVEL_UNSPECIFIED","isFileUploadAnalysisEnabled":True,"browserManagementState":"UNSPECIFIED","isSecurityEventAnalysisEnabled":True,"browserVersion":"browserVersion","isChromeRemoteDesktopAppBlocked":True,"isFileDownloadAnalysisEnabled":True,"isBuiltInDnsClientEnabled":True,"isChromeCleanupEnabled":True},"chromeProfileId":"chromeProfileId"}]},"basebandVersion":"basebandVersion","model":"model","androidSpecificAttributes":{"hasPotentiallyHarmfulApps":True,"verifyAppsEnabled":True,"ctsProfileMatch":True,"enabledUnknownSources":True,"ownerProfileAccount":True,"verifiedBoot":True,"ownershipPrivilege":"OWNERSHIP_PRIVILEGE_UNSPECIFIED","supportsWorkProfile":True},"brand":"brand","deviceType":"DEVICE_TYPE_UNSPECIFIED","clientTypes":["CLIENT_TYPE_UNSPECIFIED","CLIENT_TYPE_UNSPECIFIED"],"serialNumber":"serialNumber","releaseVersion":"releaseVersion","enabledDeveloperOptions":True,"securityPatchTime":"securityPatchTime","wifiMacAddresses":["wifiMacAddresses","wifiMacAddresses"],"enabledUsbDebugging":True,"otherAccounts":["otherAccounts","otherAccounts"],"createTime":"createTime","kernelVersion":"kernelVersion","name":"name","imei":"imei","managementState":"MANAGEMENT_STATE_UNSPECIFIED"},"customer":"customer"}
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
        method='POST',
        path='/v1beta1/devices',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudidentity_devices_device_users_approve(client):
    """Test case for cloudidentity_devices_device_users_approve

    
    """
    body = {"customer":"customer"}
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
        method='POST',
        path='/v1beta1/{nameapprov}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudidentity_devices_device_users_block(client):
    """Test case for cloudidentity_devices_device_users_block

    
    """
    body = {"customer":"customer"}
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
        method='POST',
        path='/v1beta1/{namebloc}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudidentity_devices_device_users_cancel_wipe(client):
    """Test case for cloudidentity_devices_device_users_cancel_wipe

    
    """
    body = {"customer":"customer"}
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
        method='POST',
        path='/v1beta1/{namecancel_wip}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudidentity_devices_device_users_list(client):
    """Test case for cloudidentity_devices_device_users_list

    
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
                    ('uploadType', 'upload_type_example'),
                    ('customer', 'customer_example'),
                    ('filter', 'filter_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/deviceUsers'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudidentity_devices_device_users_lookup(client):
    """Test case for cloudidentity_devices_device_users_lookup

    
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
                    ('uploadType', 'upload_type_example'),
                    ('androidId', 'android_id_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('rawResourceId', 'raw_resource_id_example'),
                    ('userId', 'user_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parentlooku}'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudidentity_devices_device_users_wipe(client):
    """Test case for cloudidentity_devices_device_users_wipe

    
    """
    body = {"customer":"customer"}
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
        method='POST',
        path='/v1beta1/{namewip}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudidentity_devices_list(client):
    """Test case for cloudidentity_devices_list

    
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
                    ('uploadType', 'upload_type_example'),
                    ('customer', 'customer_example'),
                    ('filter', 'filter_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/devices',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

