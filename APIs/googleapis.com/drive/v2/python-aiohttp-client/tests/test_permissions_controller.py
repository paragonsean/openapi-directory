# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.permission import Permission
from openapi_server.models.permission_id import PermissionId
from openapi_server.models.permission_list import PermissionList


pytestmark = pytest.mark.asyncio

async def test_drive_permissions_delete(client):
    """Test case for drive_permissions_delete

    
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
                    ('supportsAllDrives', True),
                    ('supportsTeamDrives', True),
                    ('useDomainAdminAccess', True)]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/drive/v2/files/{file_id}/permissions/{permission_id}'.format(file_id='file_id_example', permission_id='permission_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drive_permissions_get(client):
    """Test case for drive_permissions_get

    
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
                    ('supportsAllDrives', True),
                    ('supportsTeamDrives', True),
                    ('useDomainAdminAccess', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/drive/v2/files/{file_id}/permissions/{permission_id}'.format(file_id='file_id_example', permission_id='permission_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drive_permissions_get_id_for_email(client):
    """Test case for drive_permissions_get_id_for_email

    
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
        path='/drive/v2/permissionIds/{email}'.format(email='email_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drive_permissions_insert(client):
    """Test case for drive_permissions_insert

    
    """
    body = {"authKey":"authKey","teamDrivePermissionDetails":[{"role":"role","inherited":True,"additionalRoles":["additionalRoles","additionalRoles"],"inheritedFrom":"inheritedFrom","teamDrivePermissionType":"teamDrivePermissionType"},{"role":"role","inherited":True,"additionalRoles":["additionalRoles","additionalRoles"],"inheritedFrom":"inheritedFrom","teamDrivePermissionType":"teamDrivePermissionType"}],"role":"role","pendingOwner":True,"kind":"drive#permission","additionalRoles":["additionalRoles","additionalRoles"],"withLink":True,"type":"type","selfLink":"selfLink","emailAddress":"emailAddress","view":"view","deleted":True,"permissionDetails":[{"permissionType":"permissionType","role":"role","inherited":True,"additionalRoles":["additionalRoles","additionalRoles"],"inheritedFrom":"inheritedFrom"},{"permissionType":"permissionType","role":"role","inherited":True,"additionalRoles":["additionalRoles","additionalRoles"],"inheritedFrom":"inheritedFrom"}],"domain":"domain","name":"name","etag":"etag","id":"id","photoLink":"photoLink","value":"value","expirationDate":"2000-01-23T04:56:07.000+00:00"}
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
                    ('emailMessage', 'email_message_example'),
                    ('enforceSingleParent', True),
                    ('moveToNewOwnersRoot', True),
                    ('sendNotificationEmails', True),
                    ('supportsAllDrives', True),
                    ('supportsTeamDrives', True),
                    ('useDomainAdminAccess', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/drive/v2/files/{file_id}/permissions'.format(file_id='file_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drive_permissions_list(client):
    """Test case for drive_permissions_list

    
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
                    ('includePermissionsForView', 'include_permissions_for_view_example'),
                    ('maxResults', 56),
                    ('pageToken', 'page_token_example'),
                    ('supportsAllDrives', True),
                    ('supportsTeamDrives', True),
                    ('useDomainAdminAccess', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/drive/v2/files/{file_id}/permissions'.format(file_id='file_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drive_permissions_patch(client):
    """Test case for drive_permissions_patch

    
    """
    body = {"authKey":"authKey","teamDrivePermissionDetails":[{"role":"role","inherited":True,"additionalRoles":["additionalRoles","additionalRoles"],"inheritedFrom":"inheritedFrom","teamDrivePermissionType":"teamDrivePermissionType"},{"role":"role","inherited":True,"additionalRoles":["additionalRoles","additionalRoles"],"inheritedFrom":"inheritedFrom","teamDrivePermissionType":"teamDrivePermissionType"}],"role":"role","pendingOwner":True,"kind":"drive#permission","additionalRoles":["additionalRoles","additionalRoles"],"withLink":True,"type":"type","selfLink":"selfLink","emailAddress":"emailAddress","view":"view","deleted":True,"permissionDetails":[{"permissionType":"permissionType","role":"role","inherited":True,"additionalRoles":["additionalRoles","additionalRoles"],"inheritedFrom":"inheritedFrom"},{"permissionType":"permissionType","role":"role","inherited":True,"additionalRoles":["additionalRoles","additionalRoles"],"inheritedFrom":"inheritedFrom"}],"domain":"domain","name":"name","etag":"etag","id":"id","photoLink":"photoLink","value":"value","expirationDate":"2000-01-23T04:56:07.000+00:00"}
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
                    ('removeExpiration', True),
                    ('supportsAllDrives', True),
                    ('supportsTeamDrives', True),
                    ('transferOwnership', True),
                    ('useDomainAdminAccess', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/drive/v2/files/{file_id}/permissions/{permission_id}'.format(file_id='file_id_example', permission_id='permission_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drive_permissions_update(client):
    """Test case for drive_permissions_update

    
    """
    body = {"authKey":"authKey","teamDrivePermissionDetails":[{"role":"role","inherited":True,"additionalRoles":["additionalRoles","additionalRoles"],"inheritedFrom":"inheritedFrom","teamDrivePermissionType":"teamDrivePermissionType"},{"role":"role","inherited":True,"additionalRoles":["additionalRoles","additionalRoles"],"inheritedFrom":"inheritedFrom","teamDrivePermissionType":"teamDrivePermissionType"}],"role":"role","pendingOwner":True,"kind":"drive#permission","additionalRoles":["additionalRoles","additionalRoles"],"withLink":True,"type":"type","selfLink":"selfLink","emailAddress":"emailAddress","view":"view","deleted":True,"permissionDetails":[{"permissionType":"permissionType","role":"role","inherited":True,"additionalRoles":["additionalRoles","additionalRoles"],"inheritedFrom":"inheritedFrom"},{"permissionType":"permissionType","role":"role","inherited":True,"additionalRoles":["additionalRoles","additionalRoles"],"inheritedFrom":"inheritedFrom"}],"domain":"domain","name":"name","etag":"etag","id":"id","photoLink":"photoLink","value":"value","expirationDate":"2000-01-23T04:56:07.000+00:00"}
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
                    ('removeExpiration', True),
                    ('supportsAllDrives', True),
                    ('supportsTeamDrives', True),
                    ('transferOwnership', True),
                    ('useDomainAdminAccess', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/drive/v2/files/{file_id}/permissions/{permission_id}'.format(file_id='file_id_example', permission_id='permission_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

