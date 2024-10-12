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
    body = {"lastModifyingUserName":"lastModifyingUserName","shareable":True,"copyRequiresWriterPermission":True,"labelInfo":{"labels":[{"revisionId":"revisionId","kind":"drive#label","id":"id","fields":{"key":{"selection":["selection","selection"],"kind":"drive#labelField","valueType":"valueType","dateString":["2000-01-23","2000-01-23"],"id":"id","integer":["integer","integer"],"text":["text","text"],"user":[{"permissionId":"permissionId","emailAddress":"emailAddress","isAuthenticatedUser":True,"displayName":"displayName","kind":"drive#user","picture":{"url":"url"}},{"permissionId":"permissionId","emailAddress":"emailAddress","isAuthenticatedUser":True,"displayName":"displayName","kind":"drive#user","picture":{"url":"url"}}]}}},{"revisionId":"revisionId","kind":"drive#label","id":"id","fields":{"key":{"selection":["selection","selection"],"kind":"drive#labelField","valueType":"valueType","dateString":["2000-01-23","2000-01-23"],"id":"id","integer":["integer","integer"],"text":["text","text"],"user":[{"permissionId":"permissionId","emailAddress":"emailAddress","isAuthenticatedUser":True,"displayName":"displayName","kind":"drive#user","picture":{"url":"url"}},{"permissionId":"permissionId","emailAddress":"emailAddress","isAuthenticatedUser":True,"displayName":"displayName","kind":"drive#user","picture":{"url":"url"}}]}}}]},"downloadUrl":"downloadUrl","owners":[{"permissionId":"permissionId","emailAddress":"emailAddress","isAuthenticatedUser":True,"displayName":"displayName","kind":"drive#user","picture":{"url":"url"}},{"permissionId":"permissionId","emailAddress":"emailAddress","isAuthenticatedUser":True,"displayName":"displayName","kind":"drive#user","picture":{"url":"url"}}],"mimeType":"mimeType","contentRestrictions":[{"reason":"reason","restrictionDate":"2000-01-23T04:56:07.000+00:00","readOnly":True,"ownerRestricted":True,"systemRestricted":True,"type":"type","restrictingUser":{"permissionId":"permissionId","emailAddress":"emailAddress","isAuthenticatedUser":True,"displayName":"displayName","kind":"drive#user","picture":{"url":"url"}}},{"reason":"reason","restrictionDate":"2000-01-23T04:56:07.000+00:00","readOnly":True,"ownerRestricted":True,"systemRestricted":True,"type":"type","restrictingUser":{"permissionId":"permissionId","emailAddress":"emailAddress","isAuthenticatedUser":True,"displayName":"displayName","kind":"drive#user","picture":{"url":"url"}}}],"copyable":True,"iconLink":"iconLink","indexableText":{"text":"text"},"permissions":[{"authKey":"authKey","teamDrivePermissionDetails":[{"role":"role","inherited":True,"additionalRoles":["additionalRoles","additionalRoles"],"inheritedFrom":"inheritedFrom","teamDrivePermissionType":"teamDrivePermissionType"},{"role":"role","inherited":True,"additionalRoles":["additionalRoles","additionalRoles"],"inheritedFrom":"inheritedFrom","teamDrivePermissionType":"teamDrivePermissionType"}],"role":"role","pendingOwner":True,"kind":"drive#permission","additionalRoles":["additionalRoles","additionalRoles"],"withLink":True,"type":"type","selfLink":"selfLink","emailAddress":"emailAddress","view":"view","deleted":True,"permissionDetails":[{"permissionType":"permissionType","role":"role","inherited":True,"additionalRoles":["additionalRoles","additionalRoles"],"inheritedFrom":"inheritedFrom"},{"permissionType":"permissionType","role":"role","inherited":True,"additionalRoles":["additionalRoles","additionalRoles"],"inheritedFrom":"inheritedFrom"}],"domain":"domain","name":"name","etag":"etag","id":"id","photoLink":"photoLink","value":"value","expirationDate":"2000-01-23T04:56:07.000+00:00"},{"authKey":"authKey","teamDrivePermissionDetails":[{"role":"role","inherited":True,"additionalRoles":["additionalRoles","additionalRoles"],"inheritedFrom":"inheritedFrom","teamDrivePermissionType":"teamDrivePermissionType"},{"role":"role","inherited":True,"additionalRoles":["additionalRoles","additionalRoles"],"inheritedFrom":"inheritedFrom","teamDrivePermissionType":"teamDrivePermissionType"}],"role":"role","pendingOwner":True,"kind":"drive#permission","additionalRoles":["additionalRoles","additionalRoles"],"withLink":True,"type":"type","selfLink":"selfLink","emailAddress":"emailAddress","view":"view","deleted":True,"permissionDetails":[{"permissionType":"permissionType","role":"role","inherited":True,"additionalRoles":["additionalRoles","additionalRoles"],"inheritedFrom":"inheritedFrom"},{"permissionType":"permissionType","role":"role","inherited":True,"additionalRoles":["additionalRoles","additionalRoles"],"inheritedFrom":"inheritedFrom"}],"domain":"domain","name":"name","etag":"etag","id":"id","photoLink":"photoLink","value":"value","expirationDate":"2000-01-23T04:56:07.000+00:00"}],"isAppAuthorized":True,"canComment":True,"id":"id","writersCanShare":True,"thumbnail":{"image":"image","mimeType":"mimeType"},"kind":"drive#file","webViewLink":"webViewLink","ownedByMe":True,"version":"version","labels":{"hidden":True,"starred":True,"restricted":True,"viewed":True,"modified":True,"trashed":True},"appDataContents":True,"explicitlyTrashed":True,"driveId":"driveId","fileSize":"fileSize","sharedWithMeDate":"2000-01-23T04:56:07.000+00:00","imageMediaMetadata":{"date":"date","meteringMode":"meteringMode","exposureTime":2.302136,"whiteBalance":"whiteBalance","rotation":1,"maxApertureValue":1.2315135,"lens":"lens","exposureBias":5.637377,"colorSpace":"colorSpace","aperture":5.962134,"flashUsed":True,"subjectDistance":1,"cameraModel":"cameraModel","width":6,"isoSpeed":3,"location":{"altitude":2.027123023002322,"latitude":4.145608029883936,"longitude":7.386281948385884},"sensor":"sensor","cameraMake":"cameraMake","exposureMode":"exposureMode","focalLength":7.0614014,"height":9},"modifiedDate":"2000-01-23T04:56:07.000+00:00","spaces":["spaces","spaces"],"etag":"etag","folderColorRgb":"folderColorRgb","headRevisionId":"headRevisionId","parents":[{"parentLink":"parentLink","isRoot":True,"kind":"drive#parentReference","id":"id","selfLink":"selfLink"},{"parentLink":"parentLink","isRoot":True,"kind":"drive#parentReference","id":"id","selfLink":"selfLink"}],"teamDriveId":"teamDriveId","canReadRevisions":True,"shared":True,"hasAugmentedPermissions":True,"trashedDate":"2000-01-23T04:56:07.000+00:00","description":"description","title":"title","trashingUser":{"permissionId":"permissionId","emailAddress":"emailAddress","isAuthenticatedUser":True,"displayName":"displayName","kind":"drive#user","picture":{"url":"url"}},"permissionIds":["permissionIds","permissionIds"],"thumbnailLink":"thumbnailLink","quotaBytesUsed":"quotaBytesUsed","lastModifyingUser":{"permissionId":"permissionId","emailAddress":"emailAddress","isAuthenticatedUser":True,"displayName":"displayName","kind":"drive#user","picture":{"url":"url"}},"md5Checksum":"md5Checksum","fileExtension":"fileExtension","linkShareMetadata":{"securityUpdateEnabled":True,"securityUpdateEligible":True},"alternateLink":"alternateLink","fullFileExtension":"fullFileExtension","modifiedByMeDate":"2000-01-23T04:56:07.000+00:00","lastViewedByMeDate":"2000-01-23T04:56:07.000+00:00","webContentLink":"webContentLink","shortcutDetails":{"targetId":"targetId","targetResourceKey":"targetResourceKey","targetMimeType":"targetMimeType"},"capabilities":{"canModifyLabels":True,"canReadRevisions":True,"canAcceptOwnership":True,"canMoveItemOutOfDrive":True,"canEdit":True,"canRename":True,"canAddMyDriveParent":True,"canMoveChildrenWithinTeamDrive":True,"canTrashChildren":True,"canModifyEditorContentRestriction":True,"canAddChildren":True,"canListChildren":True,"canTrash":True,"canChangeSecurityUpdateEnabled":True,"canMoveItemIntoTeamDrive":True,"canRemoveContentRestriction":True,"canRemoveMyDriveParent":True,"canCopy":True,"canModifyOwnerContentRestriction":True,"canDownload":True,"canReadLabels":True,"canDelete":True,"canAddFolderFromAnotherDrive":True,"canComment":True,"canUntrash":True,"canMoveItemOutOfTeamDrive":True,"canMoveChildrenWithinDrive":True,"canModifyContentRestriction":True,"canMoveTeamDriveItem":True,"canChangeCopyRequiresWriterPermission":True,"canMoveChildrenOutOfDrive":True,"canReadDrive":True,"canShare":True,"canDeleteChildren":True,"canMoveItemWithinDrive":True,"canChangeRestrictedDownload":True,"canMoveChildrenOutOfTeamDrive":True,"canMoveItemWithinTeamDrive":True,"canModifyContent":True,"canRemoveChildren":True,"canReadTeamDrive":True},"hasThumbnail":True,"resourceKey":"resourceKey","userPermission":{"authKey":"authKey","teamDrivePermissionDetails":[{"role":"role","inherited":True,"additionalRoles":["additionalRoles","additionalRoles"],"inheritedFrom":"inheritedFrom","teamDrivePermissionType":"teamDrivePermissionType"},{"role":"role","inherited":True,"additionalRoles":["additionalRoles","additionalRoles"],"inheritedFrom":"inheritedFrom","teamDrivePermissionType":"teamDrivePermissionType"}],"role":"role","pendingOwner":True,"kind":"drive#permission","additionalRoles":["additionalRoles","additionalRoles"],"withLink":True,"type":"type","selfLink":"selfLink","emailAddress":"emailAddress","view":"view","deleted":True,"permissionDetails":[{"permissionType":"permissionType","role":"role","inherited":True,"additionalRoles":["additionalRoles","additionalRoles"],"inheritedFrom":"inheritedFrom"},{"permissionType":"permissionType","role":"role","inherited":True,"additionalRoles":["additionalRoles","additionalRoles"],"inheritedFrom":"inheritedFrom"}],"domain":"domain","name":"name","etag":"etag","id":"id","photoLink":"photoLink","value":"value","expirationDate":"2000-01-23T04:56:07.000+00:00"},"defaultOpenWithLink":"defaultOpenWithLink","editable":True,"ownerNames":["ownerNames","ownerNames"],"selfLink":"selfLink","markedViewedByMeDate":"2000-01-23T04:56:07.000+00:00","openWithLinks":{"key":"openWithLinks"},"sha1Checksum":"sha1Checksum","embedLink":"embedLink","videoMediaMetadata":{"width":1,"durationMillis":"durationMillis","height":7},"createdDate":"2000-01-23T04:56:07.000+00:00","exportLinks":{"key":"exportLinks"},"thumbnailVersion":"thumbnailVersion","sha256Checksum":"sha256Checksum","sharingUser":{"permissionId":"permissionId","emailAddress":"emailAddress","isAuthenticatedUser":True,"displayName":"displayName","kind":"drive#user","picture":{"url":"url"}},"originalFilename":"originalFilename","properties":[{"visibility":"visibility","kind":"drive#property","etag":"etag","value":"value","key":"key","selfLink":"selfLink"},{"visibility":"visibility","kind":"drive#property","etag":"etag","value":"value","key":"key","selfLink":"selfLink"}]}
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
                    ('convert', True),
                    ('enforceSingleParent', True),
                    ('includeLabels', 'include_labels_example'),
                    ('includePermissionsForView', 'include_permissions_for_view_example'),
                    ('ocr', True),
                    ('ocrLanguage', 'ocr_language_example'),
                    ('pinned', True),
                    ('supportsAllDrives', True),
                    ('supportsTeamDrives', True),
                    ('timedTextLanguage', 'timed_text_language_example'),
                    ('timedTextTrackName', 'timed_text_track_name_example'),
                    ('visibility', 'visibility_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/drive/v2/files/{file_id}/copy'.format(file_id='file_id_example'),
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
        path='/drive/v2/files/{file_id}'.format(file_id='file_id_example'),
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
        path='/drive/v2/files/trash',
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
        path='/drive/v2/files/{file_id}/export'.format(file_id='file_id_example'),
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
                    ('maxResults', 56),
                    ('space', 'space_example'),
                    ('type', 'type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/drive/v2/files/generateIds',
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
                    ('projection', 'projection_example'),
                    ('revisionId', 'revision_id_example'),
                    ('supportsAllDrives', True),
                    ('supportsTeamDrives', True),
                    ('updateViewedDate', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/drive/v2/files/{file_id}'.format(file_id='file_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/octet-stream not supported by Connexion")
async def test_drive_files_insert(client):
    """Test case for drive_files_insert

    
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
                    ('convert', True),
                    ('enforceSingleParent', True),
                    ('includeLabels', 'include_labels_example'),
                    ('includePermissionsForView', 'include_permissions_for_view_example'),
                    ('ocr', True),
                    ('ocrLanguage', 'ocr_language_example'),
                    ('pinned', True),
                    ('supportsAllDrives', True),
                    ('supportsTeamDrives', True),
                    ('timedTextLanguage', 'timed_text_language_example'),
                    ('timedTextTrackName', 'timed_text_track_name_example'),
                    ('useContentAsIndexableText', True),
                    ('visibility', 'visibility_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/octet-stream',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/drive/v2/files',
        headers=headers,
        json=body,
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
                    ('maxResults', 56),
                    ('orderBy', 'order_by_example'),
                    ('pageToken', 'page_token_example'),
                    ('projection', 'projection_example'),
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
        path='/drive/v2/files',
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
        path='/drive/v2/files/{file_id}/listLabels'.format(file_id='file_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drive_files_modify_labels(client):
    """Test case for drive_files_modify_labels

    
    """
    body = {"kind":"drive#modifyLabelsRequest","labelModifications":[{"labelId":"labelId","kind":"drive#labelModification","removeLabel":True,"fieldModifications":[{"setUserValues":["setUserValues","setUserValues"],"kind":"drive#labelFieldModification","setSelectionValues":["setSelectionValues","setSelectionValues"],"setTextValues":["setTextValues","setTextValues"],"setDateValues":["2000-01-23","2000-01-23"],"setIntegerValues":["setIntegerValues","setIntegerValues"],"unsetValues":True,"fieldId":"fieldId"},{"setUserValues":["setUserValues","setUserValues"],"kind":"drive#labelFieldModification","setSelectionValues":["setSelectionValues","setSelectionValues"],"setTextValues":["setTextValues","setTextValues"],"setDateValues":["2000-01-23","2000-01-23"],"setIntegerValues":["setIntegerValues","setIntegerValues"],"unsetValues":True,"fieldId":"fieldId"}]},{"labelId":"labelId","kind":"drive#labelModification","removeLabel":True,"fieldModifications":[{"setUserValues":["setUserValues","setUserValues"],"kind":"drive#labelFieldModification","setSelectionValues":["setSelectionValues","setSelectionValues"],"setTextValues":["setTextValues","setTextValues"],"setDateValues":["2000-01-23","2000-01-23"],"setIntegerValues":["setIntegerValues","setIntegerValues"],"unsetValues":True,"fieldId":"fieldId"},{"setUserValues":["setUserValues","setUserValues"],"kind":"drive#labelFieldModification","setSelectionValues":["setSelectionValues","setSelectionValues"],"setTextValues":["setTextValues","setTextValues"],"setDateValues":["2000-01-23","2000-01-23"],"setIntegerValues":["setIntegerValues","setIntegerValues"],"unsetValues":True,"fieldId":"fieldId"}]}]}
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
        path='/drive/v2/files/{file_id}/modifyLabels'.format(file_id='file_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drive_files_patch(client):
    """Test case for drive_files_patch

    
    """
    body = {"lastModifyingUserName":"lastModifyingUserName","shareable":True,"copyRequiresWriterPermission":True,"labelInfo":{"labels":[{"revisionId":"revisionId","kind":"drive#label","id":"id","fields":{"key":{"selection":["selection","selection"],"kind":"drive#labelField","valueType":"valueType","dateString":["2000-01-23","2000-01-23"],"id":"id","integer":["integer","integer"],"text":["text","text"],"user":[{"permissionId":"permissionId","emailAddress":"emailAddress","isAuthenticatedUser":True,"displayName":"displayName","kind":"drive#user","picture":{"url":"url"}},{"permissionId":"permissionId","emailAddress":"emailAddress","isAuthenticatedUser":True,"displayName":"displayName","kind":"drive#user","picture":{"url":"url"}}]}}},{"revisionId":"revisionId","kind":"drive#label","id":"id","fields":{"key":{"selection":["selection","selection"],"kind":"drive#labelField","valueType":"valueType","dateString":["2000-01-23","2000-01-23"],"id":"id","integer":["integer","integer"],"text":["text","text"],"user":[{"permissionId":"permissionId","emailAddress":"emailAddress","isAuthenticatedUser":True,"displayName":"displayName","kind":"drive#user","picture":{"url":"url"}},{"permissionId":"permissionId","emailAddress":"emailAddress","isAuthenticatedUser":True,"displayName":"displayName","kind":"drive#user","picture":{"url":"url"}}]}}}]},"downloadUrl":"downloadUrl","owners":[{"permissionId":"permissionId","emailAddress":"emailAddress","isAuthenticatedUser":True,"displayName":"displayName","kind":"drive#user","picture":{"url":"url"}},{"permissionId":"permissionId","emailAddress":"emailAddress","isAuthenticatedUser":True,"displayName":"displayName","kind":"drive#user","picture":{"url":"url"}}],"mimeType":"mimeType","contentRestrictions":[{"reason":"reason","restrictionDate":"2000-01-23T04:56:07.000+00:00","readOnly":True,"ownerRestricted":True,"systemRestricted":True,"type":"type","restrictingUser":{"permissionId":"permissionId","emailAddress":"emailAddress","isAuthenticatedUser":True,"displayName":"displayName","kind":"drive#user","picture":{"url":"url"}}},{"reason":"reason","restrictionDate":"2000-01-23T04:56:07.000+00:00","readOnly":True,"ownerRestricted":True,"systemRestricted":True,"type":"type","restrictingUser":{"permissionId":"permissionId","emailAddress":"emailAddress","isAuthenticatedUser":True,"displayName":"displayName","kind":"drive#user","picture":{"url":"url"}}}],"copyable":True,"iconLink":"iconLink","indexableText":{"text":"text"},"permissions":[{"authKey":"authKey","teamDrivePermissionDetails":[{"role":"role","inherited":True,"additionalRoles":["additionalRoles","additionalRoles"],"inheritedFrom":"inheritedFrom","teamDrivePermissionType":"teamDrivePermissionType"},{"role":"role","inherited":True,"additionalRoles":["additionalRoles","additionalRoles"],"inheritedFrom":"inheritedFrom","teamDrivePermissionType":"teamDrivePermissionType"}],"role":"role","pendingOwner":True,"kind":"drive#permission","additionalRoles":["additionalRoles","additionalRoles"],"withLink":True,"type":"type","selfLink":"selfLink","emailAddress":"emailAddress","view":"view","deleted":True,"permissionDetails":[{"permissionType":"permissionType","role":"role","inherited":True,"additionalRoles":["additionalRoles","additionalRoles"],"inheritedFrom":"inheritedFrom"},{"permissionType":"permissionType","role":"role","inherited":True,"additionalRoles":["additionalRoles","additionalRoles"],"inheritedFrom":"inheritedFrom"}],"domain":"domain","name":"name","etag":"etag","id":"id","photoLink":"photoLink","value":"value","expirationDate":"2000-01-23T04:56:07.000+00:00"},{"authKey":"authKey","teamDrivePermissionDetails":[{"role":"role","inherited":True,"additionalRoles":["additionalRoles","additionalRoles"],"inheritedFrom":"inheritedFrom","teamDrivePermissionType":"teamDrivePermissionType"},{"role":"role","inherited":True,"additionalRoles":["additionalRoles","additionalRoles"],"inheritedFrom":"inheritedFrom","teamDrivePermissionType":"teamDrivePermissionType"}],"role":"role","pendingOwner":True,"kind":"drive#permission","additionalRoles":["additionalRoles","additionalRoles"],"withLink":True,"type":"type","selfLink":"selfLink","emailAddress":"emailAddress","view":"view","deleted":True,"permissionDetails":[{"permissionType":"permissionType","role":"role","inherited":True,"additionalRoles":["additionalRoles","additionalRoles"],"inheritedFrom":"inheritedFrom"},{"permissionType":"permissionType","role":"role","inherited":True,"additionalRoles":["additionalRoles","additionalRoles"],"inheritedFrom":"inheritedFrom"}],"domain":"domain","name":"name","etag":"etag","id":"id","photoLink":"photoLink","value":"value","expirationDate":"2000-01-23T04:56:07.000+00:00"}],"isAppAuthorized":True,"canComment":True,"id":"id","writersCanShare":True,"thumbnail":{"image":"image","mimeType":"mimeType"},"kind":"drive#file","webViewLink":"webViewLink","ownedByMe":True,"version":"version","labels":{"hidden":True,"starred":True,"restricted":True,"viewed":True,"modified":True,"trashed":True},"appDataContents":True,"explicitlyTrashed":True,"driveId":"driveId","fileSize":"fileSize","sharedWithMeDate":"2000-01-23T04:56:07.000+00:00","imageMediaMetadata":{"date":"date","meteringMode":"meteringMode","exposureTime":2.302136,"whiteBalance":"whiteBalance","rotation":1,"maxApertureValue":1.2315135,"lens":"lens","exposureBias":5.637377,"colorSpace":"colorSpace","aperture":5.962134,"flashUsed":True,"subjectDistance":1,"cameraModel":"cameraModel","width":6,"isoSpeed":3,"location":{"altitude":2.027123023002322,"latitude":4.145608029883936,"longitude":7.386281948385884},"sensor":"sensor","cameraMake":"cameraMake","exposureMode":"exposureMode","focalLength":7.0614014,"height":9},"modifiedDate":"2000-01-23T04:56:07.000+00:00","spaces":["spaces","spaces"],"etag":"etag","folderColorRgb":"folderColorRgb","headRevisionId":"headRevisionId","parents":[{"parentLink":"parentLink","isRoot":True,"kind":"drive#parentReference","id":"id","selfLink":"selfLink"},{"parentLink":"parentLink","isRoot":True,"kind":"drive#parentReference","id":"id","selfLink":"selfLink"}],"teamDriveId":"teamDriveId","canReadRevisions":True,"shared":True,"hasAugmentedPermissions":True,"trashedDate":"2000-01-23T04:56:07.000+00:00","description":"description","title":"title","trashingUser":{"permissionId":"permissionId","emailAddress":"emailAddress","isAuthenticatedUser":True,"displayName":"displayName","kind":"drive#user","picture":{"url":"url"}},"permissionIds":["permissionIds","permissionIds"],"thumbnailLink":"thumbnailLink","quotaBytesUsed":"quotaBytesUsed","lastModifyingUser":{"permissionId":"permissionId","emailAddress":"emailAddress","isAuthenticatedUser":True,"displayName":"displayName","kind":"drive#user","picture":{"url":"url"}},"md5Checksum":"md5Checksum","fileExtension":"fileExtension","linkShareMetadata":{"securityUpdateEnabled":True,"securityUpdateEligible":True},"alternateLink":"alternateLink","fullFileExtension":"fullFileExtension","modifiedByMeDate":"2000-01-23T04:56:07.000+00:00","lastViewedByMeDate":"2000-01-23T04:56:07.000+00:00","webContentLink":"webContentLink","shortcutDetails":{"targetId":"targetId","targetResourceKey":"targetResourceKey","targetMimeType":"targetMimeType"},"capabilities":{"canModifyLabels":True,"canReadRevisions":True,"canAcceptOwnership":True,"canMoveItemOutOfDrive":True,"canEdit":True,"canRename":True,"canAddMyDriveParent":True,"canMoveChildrenWithinTeamDrive":True,"canTrashChildren":True,"canModifyEditorContentRestriction":True,"canAddChildren":True,"canListChildren":True,"canTrash":True,"canChangeSecurityUpdateEnabled":True,"canMoveItemIntoTeamDrive":True,"canRemoveContentRestriction":True,"canRemoveMyDriveParent":True,"canCopy":True,"canModifyOwnerContentRestriction":True,"canDownload":True,"canReadLabels":True,"canDelete":True,"canAddFolderFromAnotherDrive":True,"canComment":True,"canUntrash":True,"canMoveItemOutOfTeamDrive":True,"canMoveChildrenWithinDrive":True,"canModifyContentRestriction":True,"canMoveTeamDriveItem":True,"canChangeCopyRequiresWriterPermission":True,"canMoveChildrenOutOfDrive":True,"canReadDrive":True,"canShare":True,"canDeleteChildren":True,"canMoveItemWithinDrive":True,"canChangeRestrictedDownload":True,"canMoveChildrenOutOfTeamDrive":True,"canMoveItemWithinTeamDrive":True,"canModifyContent":True,"canRemoveChildren":True,"canReadTeamDrive":True},"hasThumbnail":True,"resourceKey":"resourceKey","userPermission":{"authKey":"authKey","teamDrivePermissionDetails":[{"role":"role","inherited":True,"additionalRoles":["additionalRoles","additionalRoles"],"inheritedFrom":"inheritedFrom","teamDrivePermissionType":"teamDrivePermissionType"},{"role":"role","inherited":True,"additionalRoles":["additionalRoles","additionalRoles"],"inheritedFrom":"inheritedFrom","teamDrivePermissionType":"teamDrivePermissionType"}],"role":"role","pendingOwner":True,"kind":"drive#permission","additionalRoles":["additionalRoles","additionalRoles"],"withLink":True,"type":"type","selfLink":"selfLink","emailAddress":"emailAddress","view":"view","deleted":True,"permissionDetails":[{"permissionType":"permissionType","role":"role","inherited":True,"additionalRoles":["additionalRoles","additionalRoles"],"inheritedFrom":"inheritedFrom"},{"permissionType":"permissionType","role":"role","inherited":True,"additionalRoles":["additionalRoles","additionalRoles"],"inheritedFrom":"inheritedFrom"}],"domain":"domain","name":"name","etag":"etag","id":"id","photoLink":"photoLink","value":"value","expirationDate":"2000-01-23T04:56:07.000+00:00"},"defaultOpenWithLink":"defaultOpenWithLink","editable":True,"ownerNames":["ownerNames","ownerNames"],"selfLink":"selfLink","markedViewedByMeDate":"2000-01-23T04:56:07.000+00:00","openWithLinks":{"key":"openWithLinks"},"sha1Checksum":"sha1Checksum","embedLink":"embedLink","videoMediaMetadata":{"width":1,"durationMillis":"durationMillis","height":7},"createdDate":"2000-01-23T04:56:07.000+00:00","exportLinks":{"key":"exportLinks"},"thumbnailVersion":"thumbnailVersion","sha256Checksum":"sha256Checksum","sharingUser":{"permissionId":"permissionId","emailAddress":"emailAddress","isAuthenticatedUser":True,"displayName":"displayName","kind":"drive#user","picture":{"url":"url"}},"originalFilename":"originalFilename","properties":[{"visibility":"visibility","kind":"drive#property","etag":"etag","value":"value","key":"key","selfLink":"selfLink"},{"visibility":"visibility","kind":"drive#property","etag":"etag","value":"value","key":"key","selfLink":"selfLink"}]}
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
                    ('convert', True),
                    ('enforceSingleParent', True),
                    ('includeLabels', 'include_labels_example'),
                    ('includePermissionsForView', 'include_permissions_for_view_example'),
                    ('modifiedDateBehavior', 'modified_date_behavior_example'),
                    ('newRevision', True),
                    ('ocr', True),
                    ('ocrLanguage', 'ocr_language_example'),
                    ('pinned', True),
                    ('removeParents', 'remove_parents_example'),
                    ('setModifiedDate', True),
                    ('supportsAllDrives', True),
                    ('supportsTeamDrives', True),
                    ('timedTextLanguage', 'timed_text_language_example'),
                    ('timedTextTrackName', 'timed_text_track_name_example'),
                    ('updateViewedDate', True),
                    ('useContentAsIndexableText', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/drive/v2/files/{file_id}'.format(file_id='file_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drive_files_touch(client):
    """Test case for drive_files_touch

    
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
        method='POST',
        path='/drive/v2/files/{file_id}/touch'.format(file_id='file_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drive_files_trash(client):
    """Test case for drive_files_trash

    
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
        method='POST',
        path='/drive/v2/files/{file_id}/trash'.format(file_id='file_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drive_files_untrash(client):
    """Test case for drive_files_untrash

    
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
        method='POST',
        path='/drive/v2/files/{file_id}/untrash'.format(file_id='file_id_example'),
        headers=headers,
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
                    ('convert', True),
                    ('enforceSingleParent', True),
                    ('includeLabels', 'include_labels_example'),
                    ('includePermissionsForView', 'include_permissions_for_view_example'),
                    ('modifiedDateBehavior', 'modified_date_behavior_example'),
                    ('newRevision', True),
                    ('ocr', True),
                    ('ocrLanguage', 'ocr_language_example'),
                    ('pinned', True),
                    ('removeParents', 'remove_parents_example'),
                    ('setModifiedDate', True),
                    ('supportsAllDrives', True),
                    ('supportsTeamDrives', True),
                    ('timedTextLanguage', 'timed_text_language_example'),
                    ('timedTextTrackName', 'timed_text_track_name_example'),
                    ('updateViewedDate', True),
                    ('useContentAsIndexableText', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/octet-stream',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/drive/v2/files/{file_id}'.format(file_id='file_id_example'),
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
                    ('projection', 'projection_example'),
                    ('revisionId', 'revision_id_example'),
                    ('supportsAllDrives', True),
                    ('supportsTeamDrives', True),
                    ('updateViewedDate', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/drive/v2/files/{file_id}/watch'.format(file_id='file_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

