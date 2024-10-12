# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.drive import Drive
from openapi_server.models.drive_list import DriveList


pytestmark = pytest.mark.asyncio

async def test_drive_drives_delete(client):
    """Test case for drive_drives_delete

    
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
                    ('allowItemDeletion', True),
                    ('useDomainAdminAccess', True)]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/drive/v2/drives/{drive_id}'.format(drive_id='drive_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drive_drives_get(client):
    """Test case for drive_drives_get

    
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
                    ('useDomainAdminAccess', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/drive/v2/drives/{drive_id}'.format(drive_id='drive_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drive_drives_hide(client):
    """Test case for drive_drives_hide

    
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
        method='POST',
        path='/drive/v2/drives/{drive_id}/hide'.format(drive_id='drive_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drive_drives_insert(client):
    """Test case for drive_drives_insert

    
    """
    body = {"capabilities":{"canDeleteDrive":True,"canReadRevisions":True,"canEdit":True,"canShare":True,"canRename":True,"canDeleteChildren":True,"canChangeCopyRequiresWriterPermissionRestriction":True,"canChangeDriveBackground":True,"canTrashChildren":True,"canChangeSharingFoldersRequiresOrganizerPermissionRestriction":True,"canResetDriveRestrictions":True,"canAddChildren":True,"canChangeDriveMembersOnlyRestriction":True,"canListChildren":True,"canChangeDomainUsersOnlyRestriction":True,"canManageMembers":True,"canRenameDrive":True,"canCopy":True,"canDownload":True,"canComment":True},"createdDate":"2000-01-23T04:56:07.000+00:00","backgroundImageFile":{"xCoordinate":6.0274563,"yCoordinate":1.4658129,"width":0.8008282,"id":"id"},"hidden":True,"kind":"drive#drive","backgroundImageLink":"backgroundImageLink","name":"name","restrictions":{"adminManagedRestrictions":True,"copyRequiresWriterPermission":True,"sharingFoldersRequiresOrganizerPermission":True,"domainUsersOnly":True,"driveMembersOnly":True},"themeId":"themeId","id":"id","orgUnitId":"orgUnitId","colorRgb":"colorRgb"}
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
                    ('requestId', 'request_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/drive/v2/drives',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drive_drives_list(client):
    """Test case for drive_drives_list

    
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
                    ('maxResults', 56),
                    ('pageToken', 'page_token_example'),
                    ('q', 'q_example'),
                    ('useDomainAdminAccess', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/drive/v2/drives',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drive_drives_unhide(client):
    """Test case for drive_drives_unhide

    
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
        method='POST',
        path='/drive/v2/drives/{drive_id}/unhide'.format(drive_id='drive_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drive_drives_update(client):
    """Test case for drive_drives_update

    
    """
    body = {"capabilities":{"canDeleteDrive":True,"canReadRevisions":True,"canEdit":True,"canShare":True,"canRename":True,"canDeleteChildren":True,"canChangeCopyRequiresWriterPermissionRestriction":True,"canChangeDriveBackground":True,"canTrashChildren":True,"canChangeSharingFoldersRequiresOrganizerPermissionRestriction":True,"canResetDriveRestrictions":True,"canAddChildren":True,"canChangeDriveMembersOnlyRestriction":True,"canListChildren":True,"canChangeDomainUsersOnlyRestriction":True,"canManageMembers":True,"canRenameDrive":True,"canCopy":True,"canDownload":True,"canComment":True},"createdDate":"2000-01-23T04:56:07.000+00:00","backgroundImageFile":{"xCoordinate":6.0274563,"yCoordinate":1.4658129,"width":0.8008282,"id":"id"},"hidden":True,"kind":"drive#drive","backgroundImageLink":"backgroundImageLink","name":"name","restrictions":{"adminManagedRestrictions":True,"copyRequiresWriterPermission":True,"sharingFoldersRequiresOrganizerPermission":True,"domainUsersOnly":True,"driveMembersOnly":True},"themeId":"themeId","id":"id","orgUnitId":"orgUnitId","colorRgb":"colorRgb"}
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
                    ('useDomainAdminAccess', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/drive/v2/drives/{drive_id}'.format(drive_id='drive_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

