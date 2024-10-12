# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.change_node_comment_request import ChangeNodeCommentRequest
from openapi_server.models.chunk_upload_response import ChunkUploadResponse
from openapi_server.models.comment import Comment
from openapi_server.models.comment_list import CommentList
from openapi_server.models.complete_s3_file_upload_request import CompleteS3FileUploadRequest
from openapi_server.models.complete_upload_request import CompleteUploadRequest
from openapi_server.models.config_room_request import ConfigRoomRequest
from openapi_server.models.copy_nodes_request import CopyNodesRequest
from openapi_server.models.create_file_upload_request import CreateFileUploadRequest
from openapi_server.models.create_file_upload_response import CreateFileUploadResponse
from openapi_server.models.create_folder_request import CreateFolderRequest
from openapi_server.models.create_key_pair_request import CreateKeyPairRequest
from openapi_server.models.create_node_comment_request import CreateNodeCommentRequest
from openapi_server.models.create_room_request import CreateRoomRequest
from openapi_server.models.delete_deleted_nodes_request import DeleteDeletedNodesRequest
from openapi_server.models.delete_nodes_request import DeleteNodesRequest
from openapi_server.models.deleted_node import DeletedNode
from openapi_server.models.deleted_node_summary_list import DeletedNodeSummaryList
from openapi_server.models.deleted_node_versions_list import DeletedNodeVersionsList
from openapi_server.models.download_token_generate_response import DownloadTokenGenerateResponse
from openapi_server.models.encrypt_room_request import EncryptRoomRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.file_key import FileKey
from openapi_server.models.file_version_list import FileVersionList
from openapi_server.models.generate_presigned_urls_request import GeneratePresignedUrlsRequest
from openapi_server.models.log_event_list import LogEventList
from openapi_server.models.missing_keys_response import MissingKeysResponse
from openapi_server.models.move_nodes_request import MoveNodesRequest
from openapi_server.models.node import Node
from openapi_server.models.node_list import NodeList
from openapi_server.models.node_parent_list import NodeParentList
from openapi_server.models.pending_assignment_list import PendingAssignmentList
from openapi_server.models.pending_assignments_request import PendingAssignmentsRequest
from openapi_server.models.presigned_url_list import PresignedUrlList
from openapi_server.models.restore_deleted_nodes_request import RestoreDeletedNodesRequest
from openapi_server.models.room_group_list import RoomGroupList
from openapi_server.models.room_groups_add_batch_request import RoomGroupsAddBatchRequest
from openapi_server.models.room_groups_delete_batch_request import RoomGroupsDeleteBatchRequest
from openapi_server.models.room_guest_user_add_request import RoomGuestUserAddRequest
from openapi_server.models.room_policies import RoomPolicies
from openapi_server.models.room_policies_request import RoomPoliciesRequest
from openapi_server.models.room_user_list import RoomUserList
from openapi_server.models.room_users_add_batch_request import RoomUsersAddBatchRequest
from openapi_server.models.room_users_delete_batch_request import RoomUsersDeleteBatchRequest
from openapi_server.models.room_webhook_list import RoomWebhookList
from openapi_server.models.s3_file_upload_status import S3FileUploadStatus
from openapi_server.models.s3_tag_ids import S3TagIds
from openapi_server.models.s3_tag_list import S3TagList
from openapi_server.models.update_favorites_bulk_request import UpdateFavoritesBulkRequest
from openapi_server.models.update_file_request import UpdateFileRequest
from openapi_server.models.update_files_bulk_request import UpdateFilesBulkRequest
from openapi_server.models.update_folder_request import UpdateFolderRequest
from openapi_server.models.update_room_request import UpdateRoomRequest
from openapi_server.models.update_room_webhook_request import UpdateRoomWebhookRequest
from openapi_server.models.user_file_key_set_batch_request import UserFileKeySetBatchRequest
from openapi_server.models.user_key_pair_container import UserKeyPairContainer
from openapi_server.models.zip_download_request import ZipDownloadRequest


pytestmark = pytest.mark.asyncio

async def test_add_favorite(client):
    """Test case for add_favorite

    Mark a node (room, folder or file) as favorite
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/nodes/{node_id}/favorite'.format(node_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_room_guest_users(client):
    """Test case for add_room_guest_users

    Add guest users to a room
    """
    body = {"roomGuestInvitations":[{"firstName":"firstName","lastName":"lastName","email":"email"},{"firstName":"firstName","lastName":"lastName","email":"email"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/nodes/rooms/{room_id}/guest_users'.format(room_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cancel_file_upload(client):
    """Test case for cancel_file_upload

    Cancel file upload
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/nodes/files/uploads/{upload_id}'.format(upload_id='upload_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_change_pending_assignments(client):
    """Test case for change_pending_assignments

    Handle user-room assignments per group
    """
    body = {"items":[{"groupId":0,"state":"ACCEPTED","userId":1,"roomId":6,"roomName":"roomName"},{"groupId":0,"state":"ACCEPTED","userId":1,"roomId":6,"roomName":"roomName"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/nodes/rooms/pending',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_complete_file_upload(client):
    """Test case for complete_file_upload

    Complete file upload
    """
    body = {"resolutionStrategy":"autorename","fileName":"fileName","keepShareLinks":False,"userFileKeyList":{"items":[{"fileKey":{"tag":"tag","iv":"iv","version":"version","key":"key"},"userId":0},{"fileKey":{"tag":"tag","iv":"iv","version":"version","key":"key"},"userId":0}]},"fileKey":{"tag":"tag","iv":"iv","version":"version","key":"key"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/nodes/files/uploads/{upload_id}'.format(upload_id='upload_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_complete_s3_file_upload(client):
    """Test case for complete_s3_file_upload

    Complete S3 file upload
    """
    body = {"resolutionStrategy":"autorename","fileName":"fileName","keepShareLinks":False,"parts":[{"partEtag":"partEtag","partNumber":0},{"partEtag":"partEtag","partNumber":0}],"fileKey":{"tag":"tag","iv":"iv","version":"version","key":"key"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/nodes/files/uploads/{upload_id}/s3'.format(upload_id='upload_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_configure_room(client):
    """Test case for configure_room

    Configure room
    """
    body = {"adminGroupIds":[0,0],"hasActivitiesLog":True,"adminIds":[6,6],"takeOverPermissions":True,"recycleBinRetentionPeriod":5961,"inheritPermissions":True,"classification":1,"newGroupMemberAcceptance":"autoallow"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/nodes/rooms/{room_id}/config'.format(room_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_copy_nodes(client):
    """Test case for copy_nodes

    Copy node(s)
    """
    body = {"nodeIds":[6,6],"resolutionStrategy":"autorename","keepShareLinks":False,"items":[{"timestampModification":"2000-01-23T04:56:07.000+00:00","name":"name","timestampCreation":"2000-01-23T04:56:07.000+00:00","id":0},{"timestampModification":"2000-01-23T04:56:07.000+00:00","name":"name","timestampCreation":"2000-01-23T04:56:07.000+00:00","id":0}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/nodes/{node_id}/copy_to'.format(node_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_and_preserve_room_rescue_key_pair(client):
    """Test case for create_and_preserve_room_rescue_key_pair

    Create key pair and preserve copy of old private key
    """
    body = {"privateKeyContainer":{"createdAt":"2000-01-23T04:56:07.000+00:00","privateKey":"privateKey","createdBy":0,"version":"version"},"previousPrivateKey":{"createdAt":"2000-01-23T04:56:07.000+00:00","privateKey":"privateKey","createdBy":0,"version":"version"},"publicKeyContainer":{"createdAt":"2000-01-23T04:56:07.000+00:00","createdBy":5,"publicKey":"publicKey","version":"version"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/nodes/rooms/{room_id}/keypairs'.format(room_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_file_upload_channel(client):
    """Test case for create_file_upload_channel

    Create new file upload channel
    """
    body = {"timestampModification":"2000-01-23T04:56:07.000+00:00","notes":"notes","size":1,"name":"name","timestampCreation":"2000-01-23T04:56:07.000+00:00","expiration":{"enableExpiration":True,"expireAt":"2000-01-23T04:56:07.000+00:00"},"classification":0,"directS3Upload":False,"parentId":6}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/nodes/files/uploads',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_folder(client):
    """Test case for create_folder

    Create new folder
    """
    body = {"timestampModification":"2000-01-23T04:56:07.000+00:00","notes":"notes","name":"name","timestampCreation":"2000-01-23T04:56:07.000+00:00","classification":0,"parentId":6}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/nodes/folders',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_node_comment(client):
    """Test case for create_node_comment

    Create node comment
    """
    body = {"text":"text"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/nodes/{node_id}/comments'.format(node_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_room(client):
    """Test case for create_room

    Create new room
    """
    body = {"timestampModification":"2000-01-23T04:56:07.000+00:00","notes":"notes","inheritPermissions":True,"classification":1,"hasRecycleBin":True,"parentId":5,"adminGroupIds":[0,0],"hasActivitiesLog":True,"adminIds":[6,6],"quota":5,"name":"name","timestampCreation":"2000-01-23T04:56:07.000+00:00","recycleBinRetentionPeriod":2301,"newGroupMemberAcceptance":"autoallow"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/nodes/rooms',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_download_zip_archive(client):
    """Test case for download_zip_archive

    Download files / folders as ZIP archive
    """
    body = {"nodeIds":[0,0]}
    headers = { 
        'Accept': 'application/octet-stream',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/nodes/zip/download',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_empty_deleted_nodes(client):
    """Test case for empty_deleted_nodes

    Empty recycle bin
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/nodes/{node_id}/deleted_nodes'.format(node_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_encrypt_room(client):
    """Test case for encrypt_room

    Encrypt room
    """
    body = {"dataRoomRescueKey":{"privateKeyContainer":{"createdAt":"2000-01-23T04:56:07.000+00:00","privateKey":"privateKey","createdBy":0,"version":"version"},"publicKeyContainer":{"createdAt":"2000-01-23T04:56:07.000+00:00","createdBy":5,"publicKey":"publicKey","version":"version"}},"useDataSpaceRescueKey":True,"isEncrypted":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/nodes/rooms/{room_id}/encrypt'.format(room_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_generate_download_url(client):
    """Test case for generate_download_url

    Generate download URL
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/nodes/files/{file_id}/downloads'.format(file_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_generate_download_url_for_zip_archive(client):
    """Test case for generate_download_url_for_zip_archive

    Generate download URL for ZIP download
    """
    body = {"nodeIds":[0,0]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/nodes/zip',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_generate_presigned_urls_files(client):
    """Test case for generate_presigned_urls_files

    Generate presigned URLs for S3 file upload
    """
    body = {"size":1,"lastPartNumber":6,"firstPartNumber":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/nodes/files/uploads/{upload_id}/s3_urls'.format(upload_id='upload_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_handle_room_webhook_assignments(client):
    """Test case for handle_room_webhook_assignments

    Assign or unassign webhooks to room
    """
    body = {"items":[{"isAssigned":True,"webhookId":0},{"isAssigned":True,"webhookId":0}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/nodes/rooms/{room_id}/webhooks'.format(room_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_move_nodes(client):
    """Test case for move_nodes

    Move node(s)
    """
    body = {"nodeIds":[6,6],"resolutionStrategy":"autorename","keepShareLinks":False,"items":[{"timestampModification":"2000-01-23T04:56:07.000+00:00","name":"name","timestampCreation":"2000-01-23T04:56:07.000+00:00","id":0},{"timestampModification":"2000-01-23T04:56:07.000+00:00","name":"name","timestampCreation":"2000-01-23T04:56:07.000+00:00","id":0}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/nodes/{node_id}/move_to'.format(node_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_deleted_nodes(client):
    """Test case for remove_deleted_nodes

    Remove nodes from recycle bin
    """
    body = {"deletedNodeIds":[0,0]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/nodes/deleted_nodes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_favorite(client):
    """Test case for remove_favorite

    Unmark a node (room, folder or file) as favorite
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/nodes/{node_id}/favorite'.format(node_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_node(client):
    """Test case for remove_node

    Remove node
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/nodes/{node_id}'.format(node_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_node_comment(client):
    """Test case for remove_node_comment

    Remove node comment
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/nodes/comments/{comment_id}'.format(comment_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_nodes(client):
    """Test case for remove_nodes

    Remove nodes
    """
    body = {"nodeIds":[0,0]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/nodes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_room_rescue_key_pair(client):
    """Test case for remove_room_rescue_key_pair

    Remove rooms's rescue key pair
    """
    params = [('version', 'version_example')]
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/nodes/rooms/{room_id}/keypair'.format(room_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_deleted_node(client):
    """Test case for request_deleted_node

    Request deleted node
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/nodes/deleted_nodes/{deleted_node_id}'.format(deleted_node_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_deleted_node_versions(client):
    """Test case for request_deleted_node_versions

    Request deleted versions of nodes
    """
    params = [('type', 'type_example'),
                    ('name', 'name_example'),
                    ('sort', 'sort_example'),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/nodes/{node_id}/deleted_nodes/versions'.format(node_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_deleted_nodes_summary(client):
    """Test case for request_deleted_nodes_summary

    Request list of deleted nodes
    """
    params = [('filter', 'filter_example'),
                    ('sort', 'sort_example'),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/nodes/{node_id}/deleted_nodes'.format(node_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_file_version_list(client):
    """Test case for request_file_version_list

    Request list of file versions
    """
    params = [('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/nodes/files/versions/{reference_id}'.format(reference_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_list_of_webhooks_for_room(client):
    """Test case for request_list_of_webhooks_for_room

    Request list of webhooks that are assigned or can be assigned to this room
    """
    params = [('offset', 56),
                    ('limit', 56),
                    ('filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/nodes/rooms/{room_id}/webhooks'.format(room_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_missing_file_keys(client):
    """Test case for request_missing_file_keys

    Request files without user's file key
    """
    params = [('offset', 56),
                    ('limit', 56),
                    ('room_id', 56),
                    ('file_id', 56),
                    ('user_id', 56),
                    ('use_key', 'use_key_example')]
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/nodes/missingFileKeys',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_node(client):
    """Test case for request_node

    Request node
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/nodes/{node_id}'.format(node_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_node_comments(client):
    """Test case for request_node_comments

    Request list of node comments
    """
    params = [('offset', 56),
                    ('limit', 56),
                    ('hide_deleted', True)]
    headers = { 
        'Accept': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/nodes/{node_id}/comments'.format(node_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_node_parents(client):
    """Test case for request_node_parents

    Request list of parent nodes
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/nodes/{node_id}/parents'.format(node_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_nodes(client):
    """Test case for request_nodes

    Request list of nodes
    """
    params = [('depth_level', 56),
                    ('parent_id', 56),
                    ('room_manager', True),
                    ('filter', 'filter_example'),
                    ('sort', 'sort_example'),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/nodes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_pending_assignments(client):
    """Test case for request_pending_assignments

    Request user-room assignments per group
    """
    params = [('offset', 56),
                    ('limit', 56),
                    ('filter', 'filter_example'),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/nodes/rooms/pending',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_room_activities_log_as_json(client):
    """Test case for request_room_activities_log_as_json

    Request events of a room
    """
    params = [('sort', 'sort_example'),
                    ('offset', 56),
                    ('limit', 56),
                    ('date_start', 'date_start_example'),
                    ('date_end', 'date_end_example'),
                    ('type', 56),
                    ('user_id', 56),
                    ('status', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/nodes/rooms/{room_id}/events'.format(room_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_room_groups(client):
    """Test case for request_room_groups

    Request room granted group(s) or / and group(s) that can be granted
    """
    params = [('offset', 56),
                    ('limit', 56),
                    ('filter', 'filter_example'),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/nodes/rooms/{room_id}/groups'.format(room_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_room_policies(client):
    """Test case for request_room_policies

    Request Room Policies
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/nodes/rooms/{room_id}/policies'.format(room_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_room_rescue_key(client):
    """Test case for request_room_rescue_key

    Request room rescue key
    """
    params = [('version', 'version_example')]
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/nodes/files/{file_id}/data_room_file_key'.format(file_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_room_rescue_key_pair(client):
    """Test case for request_room_rescue_key_pair

    Request room rescue key
    """
    params = [('version', 'version_example')]
    headers = { 
        'Accept': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/nodes/rooms/{room_id}/keypair'.format(room_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_room_rescue_key_pairs(client):
    """Test case for request_room_rescue_key_pairs

    Request all room rescue key pairs
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/nodes/rooms/{room_id}/keypairs'.format(room_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_room_s3_tags(client):
    """Test case for request_room_s3_tags

    Request list of all assigned S3 tags to the room
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/nodes/rooms/{room_id}/s3_tags'.format(room_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_room_users(client):
    """Test case for request_room_users

    Request room granted user(s) or / and user(s) that can be granted
    """
    params = [('offset', 56),
                    ('limit', 56),
                    ('filter', 'filter_example'),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/nodes/rooms/{room_id}/users'.format(room_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_system_rescue_key(client):
    """Test case for request_system_rescue_key

    Request system rescue key
    """
    params = [('version', 'version_example')]
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/nodes/files/{file_id}/data_space_file_key'.format(file_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_upload_status_files(client):
    """Test case for request_upload_status_files

    Request status of S3 file upload
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/nodes/files/uploads/{upload_id}'.format(upload_id='upload_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_user_file_key(client):
    """Test case for request_user_file_key

    Request user's file key
    """
    params = [('version', 'version_example')]
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/nodes/files/{file_id}/user_file_key'.format(file_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_restore_nodes(client):
    """Test case for restore_nodes

    Restore deleted nodes
    """
    body = {"deletedNodeIds":[0,0],"resolutionStrategy":"autorename","keepShareLinks":False,"parentId":6}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/nodes/deleted_nodes/actions/restore',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_revoke_room_groups(client):
    """Test case for revoke_room_groups

    Revoke granted group(s) from room
    """
    body = {"ids":[0,0]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/nodes/rooms/{room_id}/groups'.format(room_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_revoke_room_users(client):
    """Test case for revoke_room_users

    Revoke granted user(s) from room
    """
    body = {"ids":[0,0]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/nodes/rooms/{room_id}/users'.format(room_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_nodes(client):
    """Test case for search_nodes

    Search nodes
    """
    params = [('search_string', 'search_string_example'),
                    ('depth_level', 56),
                    ('parent_id', 56),
                    ('filter', 'filter_example'),
                    ('sort', 'sort_example'),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/nodes/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_room_policies(client):
    """Test case for set_room_policies

    Set room policies
    """
    body = {"defaultExpirationPeriod":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/nodes/rooms/{room_id}/policies'.format(room_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_room_rescue_key_pair(client):
    """Test case for set_room_rescue_key_pair

    Set room's rescue key pair
    """
    body = {"privateKeyContainer":{"createdAt":"2000-01-23T04:56:07.000+00:00","privateKey":"privateKey","createdBy":0,"version":"version"},"publicKeyContainer":{"createdAt":"2000-01-23T04:56:07.000+00:00","createdBy":5,"publicKey":"publicKey","version":"version"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/nodes/rooms/{room_id}/keypair'.format(room_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_room_s3_tags(client):
    """Test case for set_room_s3_tags

    Set S3 tags for a room
    """
    body = {"ids":[0,0]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/nodes/rooms/{room_id}/s3_tags'.format(room_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_user_file_keys(client):
    """Test case for set_user_file_keys

    Set file keys for a list of users and files
    """
    body = {"items":[{"fileKey":{"tag":"tag","iv":"iv","version":"version","key":"key"},"userId":6,"fileId":0},{"fileKey":{"tag":"tag","iv":"iv","version":"version","key":"key"},"userId":6,"fileId":0}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/nodes/files/keys',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_favorites(client):
    """Test case for update_favorites

    Mark or unmark a list of nodes (room, folder or file) as favorite
    """
    body = {"isFavorite":True,"objectIds":[0,0]}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/nodes/favorites',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_file(client):
    """Test case for update_file

    Updates a file’s metadata
    """
    body = {"timestampModification":"2000-01-23T04:56:07.000+00:00","notes":"notes","name":"name","timestampCreation":"2000-01-23T04:56:07.000+00:00","expiration":{"enableExpiration":True,"expireAt":"2000-01-23T04:56:07.000+00:00"},"classification":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/nodes/files/{file_id}'.format(file_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_files(client):
    """Test case for update_files

    Updates a list of  file’s metadata
    """
    body = {"expiration":{"enableExpiration":True,"expireAt":"2000-01-23T04:56:07.000+00:00"},"classification":0,"objectIds":[6,6]}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/nodes/files',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_folder(client):
    """Test case for update_folder

    Updates folder’s metadata
    """
    body = {"timestampModification":"2000-01-23T04:56:07.000+00:00","notes":"notes","name":"name","timestampCreation":"2000-01-23T04:56:07.000+00:00","classification":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/nodes/folders/{folder_id}'.format(folder_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_node_comment(client):
    """Test case for update_node_comment

    Edit node comment
    """
    body = {"text":"text"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/nodes/comments/{comment_id}'.format(comment_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_room(client):
    """Test case for update_room

    Updates room’s metadata
    """
    body = {"timestampModification":"2000-01-23T04:56:07.000+00:00","notes":"notes","quota":0,"name":"name","timestampCreation":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/nodes/rooms/{room_id}'.format(room_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_room_groups(client):
    """Test case for update_room_groups

    Add or change room granted group(s)
    """
    body = {"items":[{"permissions":{"manageDownloadShare":True,"read":True,"manageUploadShare":True,"restoreRecycleBin":True,"change":True,"create":True,"deleteRecycleBin":True,"delete":True,"readRecycleBin":True,"manage":True},"id":0,"newGroupMemberAcceptance":"autoallow"},{"permissions":{"manageDownloadShare":True,"read":True,"manageUploadShare":True,"restoreRecycleBin":True,"change":True,"create":True,"deleteRecycleBin":True,"delete":True,"readRecycleBin":True,"manage":True},"id":0,"newGroupMemberAcceptance":"autoallow"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/nodes/rooms/{room_id}/groups'.format(room_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_room_users(client):
    """Test case for update_room_users

    Add or change room granted user(s)
    """
    body = {"items":[{"permissions":{"manageDownloadShare":True,"read":True,"manageUploadShare":True,"restoreRecycleBin":True,"change":True,"create":True,"deleteRecycleBin":True,"delete":True,"readRecycleBin":True,"manage":True},"id":0},{"permissions":{"manageDownloadShare":True,"read":True,"manageUploadShare":True,"restoreRecycleBin":True,"change":True,"create":True,"deleteRecycleBin":True,"delete":True,"readRecycleBin":True,"manage":True},"id":0}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/nodes/rooms/{room_id}/users'.format(room_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_upload_file_as_multipart(client):
    """Test case for upload_file_as_multipart

    Upload file
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'content_range': 'content_range_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/api/v4/nodes/files/uploads/{upload_id}'.format(upload_id='upload_id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

