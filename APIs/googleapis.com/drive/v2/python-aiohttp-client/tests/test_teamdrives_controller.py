# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.team_drive import TeamDrive
from openapi_server.models.team_drive_list import TeamDriveList


pytestmark = pytest.mark.asyncio

async def test_drive_teamdrives_delete(client):
    """Test case for drive_teamdrives_delete

    
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
        method='DELETE',
        path='/drive/v2/teamdrives/{team_drive_id}'.format(team_drive_id='team_drive_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drive_teamdrives_get(client):
    """Test case for drive_teamdrives_get

    
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
        path='/drive/v2/teamdrives/{team_drive_id}'.format(team_drive_id='team_drive_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drive_teamdrives_insert(client):
    """Test case for drive_teamdrives_insert

    
    """
    body = {"capabilities":{"canChangeTeamDriveBackground":True,"canReadRevisions":True,"canDeleteTeamDrive":True,"canEdit":True,"canShare":True,"canRename":True,"canDeleteChildren":True,"canChangeCopyRequiresWriterPermissionRestriction":True,"canTrashChildren":True,"canChangeSharingFoldersRequiresOrganizerPermissionRestriction":True,"canRenameTeamDrive":True,"canResetTeamDriveRestrictions":True,"canAddChildren":True,"canChangeTeamMembersOnlyRestriction":True,"canListChildren":True,"canChangeDomainUsersOnlyRestriction":True,"canManageMembers":True,"canRemoveChildren":True,"canCopy":True,"canDownload":True,"canComment":True},"createdDate":"2000-01-23T04:56:07.000+00:00","backgroundImageFile":{"xCoordinate":5.025005,"yCoordinate":9.965781,"width":4.9652185,"id":"id"},"kind":"drive#teamDrive","backgroundImageLink":"backgroundImageLink","name":"name","restrictions":{"adminManagedRestrictions":True,"copyRequiresWriterPermission":True,"sharingFoldersRequiresOrganizerPermission":True,"domainUsersOnly":True,"teamMembersOnly":True},"themeId":"themeId","id":"id","orgUnitId":"orgUnitId","colorRgb":"colorRgb"}
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
        path='/drive/v2/teamdrives',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drive_teamdrives_list(client):
    """Test case for drive_teamdrives_list

    
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
        path='/drive/v2/teamdrives',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drive_teamdrives_update(client):
    """Test case for drive_teamdrives_update

    
    """
    body = {"capabilities":{"canChangeTeamDriveBackground":True,"canReadRevisions":True,"canDeleteTeamDrive":True,"canEdit":True,"canShare":True,"canRename":True,"canDeleteChildren":True,"canChangeCopyRequiresWriterPermissionRestriction":True,"canTrashChildren":True,"canChangeSharingFoldersRequiresOrganizerPermissionRestriction":True,"canRenameTeamDrive":True,"canResetTeamDriveRestrictions":True,"canAddChildren":True,"canChangeTeamMembersOnlyRestriction":True,"canListChildren":True,"canChangeDomainUsersOnlyRestriction":True,"canManageMembers":True,"canRemoveChildren":True,"canCopy":True,"canDownload":True,"canComment":True},"createdDate":"2000-01-23T04:56:07.000+00:00","backgroundImageFile":{"xCoordinate":5.025005,"yCoordinate":9.965781,"width":4.9652185,"id":"id"},"kind":"drive#teamDrive","backgroundImageLink":"backgroundImageLink","name":"name","restrictions":{"adminManagedRestrictions":True,"copyRequiresWriterPermission":True,"sharingFoldersRequiresOrganizerPermission":True,"domainUsersOnly":True,"teamMembersOnly":True},"themeId":"themeId","id":"id","orgUnitId":"orgUnitId","colorRgb":"colorRgb"}
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
        path='/drive/v2/teamdrives/{team_drive_id}'.format(team_drive_id='team_drive_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

