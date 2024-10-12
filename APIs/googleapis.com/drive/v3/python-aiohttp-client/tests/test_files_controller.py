# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.channel import Channel
from openapi_server.models.file import File
from openapi_server.models.file_list import FileList
from openapi_server.models.generated_ids import GeneratedIds
from openapi_server.models.label_list import LabelList
from openapi_server.models.modify_labels_request import ModifyLabelsRequest
from openapi_server.models.modify_labels_response import ModifyLabelsResponse


pytestmark = pytest.mark.asyncio

async def test_drive_files_copy(client):
    """Test case for drive_files_copy

    
    """
    body = {"modifiedTime":"2000-01-23T04:56:07.000+00:00","copyRequiresWriterPermission":True,"labelInfo":{"labels":[{"revisionId":"revisionId","kind":"kind","id":"id","fields":{"key":{"selection":["selection","selection"],"kind":"kind","valueType":"valueType","dateString":["2000-01-23","2000-01-23"],"id":"id","integer":["integer","integer"],"text":["text","text"],"user":[{"permissionId":"permissionId","emailAddress":"emailAddress","displayName":"displayName","kind":"drive#user","me":True,"photoLink":"photoLink"},{"permissionId":"permissionId","emailAddress":"emailAddress","displayName":"displayName","kind":"drive#user","me":True,"photoLink":"photoLink"}]}}},{"revisionId":"revisionId","kind":"kind","id":"id","fields":{"key":{"selection":["selection","selection"],"kind":"kind","valueType":"valueType","dateString":["2000-01-23","2000-01-23"],"id":"id","integer":["integer","integer"],"text":["text","text"],"user":[{"permissionId":"permissionId","emailAddress":"emailAddress","displayName":"displayName","kind":"drive#user","me":True,"photoLink":"photoLink"},{"permissionId":"permissionId","emailAddress":"emailAddress","displayName":"displayName","kind":"drive#user","me":True,"photoLink":"photoLink"}]}}}]},"owners":[{"permissionId":"permissionId","emailAddress":"emailAddress","displayName":"displayName","kind":"drive#user","me":True,"photoLink":"photoLink"},{"permissionId":"permissionId","emailAddress":"emailAddress","displayName":"displayName","kind":"drive#user","me":True,"photoLink":"photoLink"}],"mimeType":"mimeType","contentRestrictions":[{"reason":"reason","readOnly":True,"ownerRestricted":True,"systemRestricted":True,"restrictionTime":"2000-01-23T04:56:07.000+00:00","type":"type","restrictingUser":{"permissionId":"permissionId","emailAddress":"emailAddress","displayName":"displayName","kind":"drive#user","me":True,"photoLink":"photoLink"}},{"reason":"reason","readOnly":True,"ownerRestricted":True,"systemRestricted":True,"restrictionTime":"2000-01-23T04:56:07.000+00:00","type":"type","restrictingUser":{"permissionId":"permissionId","emailAddress":"emailAddress","displayName":"displayName","kind":"drive#user","me":True,"photoLink":"photoLink"}}],"iconLink":"iconLink","starred":True,"permissions":[{"teamDrivePermissionDetails":[{"role":"role","inherited":True,"inheritedFrom":"inheritedFrom","teamDrivePermissionType":"teamDrivePermissionType"},{"role":"role","inherited":True,"inheritedFrom":"inheritedFrom","teamDrivePermissionType":"teamDrivePermissionType"}],"role":"role","pendingOwner":True,"displayName":"displayName","kind":"drive#permission","type":"type","emailAddress":"emailAddress","view":"view","deleted":True,"permissionDetails":[{"permissionType":"permissionType","role":"role","inherited":True,"inheritedFrom":"inheritedFrom"},{"permissionType":"permissionType","role":"role","inherited":True,"inheritedFrom":"inheritedFrom"}],"expirationTime":"2000-01-23T04:56:07.000+00:00","domain":"domain","id":"id","photoLink":"photoLink","allowFileDiscovery":True},{"teamDrivePermissionDetails":[{"role":"role","inherited":True,"inheritedFrom":"inheritedFrom","teamDrivePermissionType":"teamDrivePermissionType"},{"role":"role","inherited":True,"inheritedFrom":"inheritedFrom","teamDrivePermissionType":"teamDrivePermissionType"}],"role":"role","pendingOwner":True,"displayName":"displayName","kind":"drive#permission","type":"type","emailAddress":"emailAddress","view":"view","deleted":True,"permissionDetails":[{"permissionType":"permissionType","role":"role","inherited":True,"inheritedFrom":"inheritedFrom"},{"permissionType":"permissionType","role":"role","inherited":True,"inheritedFrom":"inheritedFrom"}],"expirationTime":"2000-01-23T04:56:07.000+00:00","domain":"domain","id":"id","photoLink":"photoLink","allowFileDiscovery":True}],"modifiedByMe":True,"contentHints":{"thumbnail":{"image":"image","mimeType":"mimeType"},"indexableText":"indexableText"},"isAppAuthorized":True,"createdTime":"2000-01-23T04:56:07.000+00:00","id":"id","sharedWithMeTime":"2000-01-23T04:56:07.000+00:00","writersCanShare":True,"kind":"drive#file","viewersCanCopyContent":True,"webViewLink":"webViewLink","ownedByMe":True,"version":"version","explicitlyTrashed":True,"trashedTime":"2000-01-23T04:56:07.000+00:00","viewedByMe":True,"driveId":"driveId","size":"size","imageMediaMetadata":{"meteringMode":"meteringMode","exposureTime":2.302136,"whiteBalance":"whiteBalance","rotation":1,"maxApertureValue":1.2315135,"lens":"lens","exposureBias":5.637377,"colorSpace":"colorSpace","aperture":5.962134,"flashUsed":True,"subjectDistance":1,"cameraModel":"cameraModel","width":6,"isoSpeed":3,"location":{"altitude":2.027123023002322,"latitude":4.145608029883936,"longitude":7.386281948385884},"sensor":"sensor","time":"time","cameraMake":"cameraMake","exposureMode":"exposureMode","focalLength":7.0614014,"height":9},"name":"name","spaces":["spaces","spaces"],"appProperties":{"key":"appProperties"},"folderColorRgb":"folderColorRgb","headRevisionId":"headRevisionId","parents":["parents","parents"],"teamDriveId":"teamDriveId","trashed":True,"modifiedByMeTime":"2000-01-23T04:56:07.000+00:00","shared":True,"hasAugmentedPermissions":True,"description":"description","trashingUser":{"permissionId":"permissionId","emailAddress":"emailAddress","displayName":"displayName","kind":"drive#user","me":True,"photoLink":"photoLink"},"permissionIds":["permissionIds","permissionIds"],"thumbnailLink":"thumbnailLink","quotaBytesUsed":"quotaBytesUsed","lastModifyingUser":{"permissionId":"permissionId","emailAddress":"emailAddress","displayName":"displayName","kind":"drive#user","me":True,"photoLink":"photoLink"},"md5Checksum":"md5Checksum","fileExtension":"fileExtension","linkShareMetadata":{"securityUpdateEnabled":True,"securityUpdateEligible":True},"fullFileExtension":"fullFileExtension","webContentLink":"webContentLink","shortcutDetails":{"targetId":"targetId","targetResourceKey":"targetResourceKey","targetMimeType":"targetMimeType"},"capabilities":{"canModifyLabels":True,"canReadRevisions":True,"canAcceptOwnership":True,"canMoveItemOutOfDrive":True,"canEdit":True,"canRename":True,"canAddMyDriveParent":True,"canMoveChildrenWithinTeamDrive":True,"canTrashChildren":True,"canModifyEditorContentRestriction":True,"canAddChildren":True,"canListChildren":True,"canTrash":True,"canChangeSecurityUpdateEnabled":True,"canMoveItemIntoTeamDrive":True,"canRemoveContentRestriction":True,"canRemoveMyDriveParent":True,"canCopy":True,"canModifyOwnerContentRestriction":True,"canDownload":True,"canReadLabels":True,"canDelete":True,"canAddFolderFromAnotherDrive":True,"canComment":True,"canUntrash":True,"canMoveItemOutOfTeamDrive":True,"canMoveChildrenWithinDrive":True,"canModifyContentRestriction":True,"canMoveTeamDriveItem":True,"canChangeCopyRequiresWriterPermission":True,"canMoveChildrenOutOfDrive":True,"canReadDrive":True,"canShare":True,"canDeleteChildren":True,"canMoveItemWithinDrive":True,"canMoveChildrenOutOfTeamDrive":True,"canMoveItemWithinTeamDrive":True,"canModifyContent":True,"canRemoveChildren":True,"canChangeViewersCanCopyContent":True,"canReadTeamDrive":True},"hasThumbnail":True,"resourceKey":"resourceKey","viewedByMeTime":"2000-01-23T04:56:07.000+00:00","sha1Checksum":"sha1Checksum","videoMediaMetadata":{"width":1,"durationMillis":"durationMillis","height":7},"exportLinks":{"key":"exportLinks"},"thumbnailVersion":"thumbnailVersion","sha256Checksum":"sha256Checksum","sharingUser":{"permissionId":"permissionId","emailAddress":"emailAddress","displayName":"displayName","kind":"drive#user","me":True,"photoLink":"photoLink"},"originalFilename":"originalFilename","properties":{"key":"properties"}}
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
                    ('enforceSingleParent', True),
                    ('ignoreDefaultVisibility', True),
                    ('includeLabels', 'include_labels_example'),
                    ('includePermissionsForView', 'include_permissions_for_view_example'),
                    ('keepRevisionForever', True),
                    ('ocrLanguage', 'ocr_language_example'),
                    ('supportsAllDrives', True),
                    ('supportsTeamDrives', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/drive/v3/files/{file_id}/copy'.format(file_id='file_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/octet-stream not supported by Connexion")
async def test_drive_files_create(client):
    """Test case for drive_files_create

    
    """
    body = '/path/to/file'
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
                    ('enforceSingleParent', True),
                    ('ignoreDefaultVisibility', True),
                    ('includeLabels', 'include_labels_example'),
                    ('includePermissionsForView', 'include_permissions_for_view_example'),
                    ('keepRevisionForever', True),
                    ('ocrLanguage', 'ocr_language_example'),
                    ('supportsAllDrives', True),
                    ('supportsTeamDrives', True),
                    ('useContentAsIndexableText', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/octet-stream',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/drive/v3/files',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drive_files_delete(client):
    """Test case for drive_files_delete

    
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
                    ('enforceSingleParent', True),
                    ('supportsAllDrives', True),
                    ('supportsTeamDrives', True)]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/drive/v3/files/{file_id}'.format(file_id='file_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drive_files_empty_trash(client):
    """Test case for drive_files_empty_trash

    
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
                    ('driveId', 'drive_id_example'),
                    ('enforceSingleParent', True)]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/drive/v3/files/trash',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drive_files_export(client):
    """Test case for drive_files_export

    
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
                    ('mimeType', 'mime_type_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/drive/v3/files/{file_id}/export'.format(file_id='file_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drive_files_generate_ids(client):
    """Test case for drive_files_generate_ids

    
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
                    ('count', 56),
                    ('space', 'space_example'),
                    ('type', 'type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/drive/v3/files/generateIds',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drive_files_get(client):
    """Test case for drive_files_get

    
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
                    ('acknowledgeAbuse', True),
                    ('includeLabels', 'include_labels_example'),
                    ('includePermissionsForView', 'include_permissions_for_view_example'),
                    ('supportsAllDrives', True),
                    ('supportsTeamDrives', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/drive/v3/files/{file_id}'.format(file_id='file_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drive_files_list(client):
    """Test case for drive_files_list

    
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
                    ('corpora', 'corpora_example'),
                    ('corpus', 'corpus_example'),
                    ('driveId', 'drive_id_example'),
                    ('includeItemsFromAllDrives', True),
                    ('includeLabels', 'include_labels_example'),
                    ('includePermissionsForView', 'include_permissions_for_view_example'),
                    ('includeTeamDriveItems', True),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('q', 'q_example'),
                    ('spaces', 'spaces_example'),
                    ('supportsAllDrives', True),
                    ('supportsTeamDrives', True),
                    ('teamDriveId', 'team_drive_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/drive/v3/files',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drive_files_list_labels(client):
    """Test case for drive_files_list_labels

    
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
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/drive/v3/files/{file_id}/listLabels'.format(file_id='file_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drive_files_modify_labels(client):
    """Test case for drive_files_modify_labels

    
    """
    body = {"kind":"kind","labelModifications":[{"labelId":"labelId","kind":"kind","removeLabel":True,"fieldModifications":[{"setUserValues":["setUserValues","setUserValues"],"kind":"kind","setSelectionValues":["setSelectionValues","setSelectionValues"],"setTextValues":["setTextValues","setTextValues"],"setDateValues":["2000-01-23","2000-01-23"],"setIntegerValues":["setIntegerValues","setIntegerValues"],"unsetValues":True,"fieldId":"fieldId"},{"setUserValues":["setUserValues","setUserValues"],"kind":"kind","setSelectionValues":["setSelectionValues","setSelectionValues"],"setTextValues":["setTextValues","setTextValues"],"setDateValues":["2000-01-23","2000-01-23"],"setIntegerValues":["setIntegerValues","setIntegerValues"],"unsetValues":True,"fieldId":"fieldId"}]},{"labelId":"labelId","kind":"kind","removeLabel":True,"fieldModifications":[{"setUserValues":["setUserValues","setUserValues"],"kind":"kind","setSelectionValues":["setSelectionValues","setSelectionValues"],"setTextValues":["setTextValues","setTextValues"],"setDateValues":["2000-01-23","2000-01-23"],"setIntegerValues":["setIntegerValues","setIntegerValues"],"unsetValues":True,"fieldId":"fieldId"},{"setUserValues":["setUserValues","setUserValues"],"kind":"kind","setSelectionValues":["setSelectionValues","setSelectionValues"],"setTextValues":["setTextValues","setTextValues"],"setDateValues":["2000-01-23","2000-01-23"],"setIntegerValues":["setIntegerValues","setIntegerValues"],"unsetValues":True,"fieldId":"fieldId"}]}]}
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
        path='/drive/v3/files/{file_id}/modifyLabels'.format(file_id='file_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/octet-stream not supported by Connexion")
async def test_drive_files_update(client):
    """Test case for drive_files_update

    
    """
    body = '/path/to/file'
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
                    ('addParents', 'add_parents_example'),
                    ('enforceSingleParent', True),
                    ('includeLabels', 'include_labels_example'),
                    ('includePermissionsForView', 'include_permissions_for_view_example'),
                    ('keepRevisionForever', True),
                    ('ocrLanguage', 'ocr_language_example'),
                    ('removeParents', 'remove_parents_example'),
                    ('supportsAllDrives', True),
                    ('supportsTeamDrives', True),
                    ('useContentAsIndexableText', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/octet-stream',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/drive/v3/files/{file_id}'.format(file_id='file_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drive_files_watch(client):
    """Test case for drive_files_watch

    
    """
    body = {"resourceId":"resourceId","address":"address","payload":True,"kind":"api#channel","expiration":"expiration","id":"id","resourceUri":"resourceUri","params":{"key":"params"},"type":"type","token":"token"}
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
                    ('acknowledgeAbuse', True),
                    ('includeLabels', 'include_labels_example'),
                    ('includePermissionsForView', 'include_permissions_for_view_example'),
                    ('supportsAllDrives', True),
                    ('supportsTeamDrives', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/drive/v3/files/{file_id}/watch'.format(file_id='file_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

