# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_targeting_request import AddTargetingRequest
from openapi_server.models.app_recovery_action import AppRecoveryAction
from openapi_server.models.create_draft_app_recovery_request import CreateDraftAppRecoveryRequest


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_apprecovery_add_targeting(client):
    """Test case for androidpublisher_apprecovery_add_targeting

    
    """
    body = {"targetingUpdate":{"regions":{"regionCode":["regionCode","regionCode"]},"allUsers":{"isAllUsersRequested":True},"androidSdks":{"sdkLevels":["sdkLevels","sdkLevels"]}}}
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
        path='/androidpublisher/v3/applications/{package_name}/appRecoveries/{app_recovery_idadd_targetin}'.format(package_name='package_name_example', app_recovery_id='app_recovery_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_apprecovery_cancel(client):
    """Test case for androidpublisher_apprecovery_cancel

    
    """
    body = None
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
        path='/androidpublisher/v3/applications/{package_name}/appRecoveries/{app_recovery_idcance}'.format(package_name='package_name_example', app_recovery_id='app_recovery_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_apprecovery_create(client):
    """Test case for androidpublisher_apprecovery_create

    
    """
    body = {"targeting":{"versionRange":{"versionCodeStart":"versionCodeStart","versionCodeEnd":"versionCodeEnd"},"regions":{"regionCode":["regionCode","regionCode"]},"allUsers":{"isAllUsersRequested":True},"androidSdks":{"sdkLevels":["sdkLevels","sdkLevels"]},"versionList":{"versionCodes":["versionCodes","versionCodes"]}},"remoteInAppUpdate":{"isRemoteInAppUpdateRequested":True}}
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
        path='/androidpublisher/v3/applications/{package_name}/appRecoveries'.format(package_name='package_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_apprecovery_deploy(client):
    """Test case for androidpublisher_apprecovery_deploy

    
    """
    body = None
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
        path='/androidpublisher/v3/applications/{package_name}/appRecoveries/{app_recovery_iddeplo}'.format(package_name='package_name_example', app_recovery_id='app_recovery_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

