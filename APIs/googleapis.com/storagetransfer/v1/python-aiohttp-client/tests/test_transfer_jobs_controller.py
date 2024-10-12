# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_transfer_jobs_response import ListTransferJobsResponse
from openapi_server.models.operation import Operation
from openapi_server.models.run_transfer_job_request import RunTransferJobRequest
from openapi_server.models.transfer_job import TransferJob
from openapi_server.models.update_transfer_job_request import UpdateTransferJobRequest


pytestmark = pytest.mark.asyncio

async def test_storagetransfer_transfer_jobs_create(client):
    """Test case for storagetransfer_transfer_jobs_create

    
    """
    body = {"creationTime":"creationTime","lastModificationTime":"lastModificationTime","description":"description","deletionTime":"deletionTime","schedule":{"scheduleEndDate":{"month":2,"year":7,"day":5},"scheduleStartDate":{"month":2,"year":7,"day":5},"repeatInterval":"repeatInterval","endTimeOfDay":{"hours":0,"seconds":5,"nanos":1,"minutes":6},"startTimeOfDay":{"hours":0,"seconds":5,"nanos":1,"minutes":6}},"loggingConfig":{"logActions":["LOGGABLE_ACTION_UNSPECIFIED","LOGGABLE_ACTION_UNSPECIFIED"],"enableOnpremGcsTransferLogs":True,"logActionStates":["LOGGABLE_ACTION_STATE_UNSPECIFIED","LOGGABLE_ACTION_STATE_UNSPECIFIED"]},"eventStream":{"eventStreamExpirationTime":"eventStreamExpirationTime","eventStreamStartTime":"eventStreamStartTime","name":"name"},"name":"name","transferSpec":{"sinkAgentPoolName":"sinkAgentPoolName","awsS3CompatibleDataSource":{"bucketName":"bucketName","path":"path","endpoint":"endpoint","s3Metadata":{"protocol":"NETWORK_PROTOCOL_UNSPECIFIED","listApi":"LIST_API_UNSPECIFIED","requestModel":"REQUEST_MODEL_UNSPECIFIED","authMethod":"AUTH_METHOD_UNSPECIFIED"},"region":"region"},"azureBlobStorageDataSource":{"container":"container","path":"path","credentialsSecret":"credentialsSecret","azureCredentials":{"sasToken":"sasToken"},"storageAccount":"storageAccount"},"posixDataSink":{"rootDirectory":"rootDirectory"},"awsS3DataSource":{"bucketName":"bucketName","path":"path","awsAccessKey":{"accessKeyId":"accessKeyId","secretAccessKey":"secretAccessKey"},"credentialsSecret":"credentialsSecret","roleArn":"roleArn","cloudfrontDomain":"cloudfrontDomain"},"sourceAgentPoolName":"sourceAgentPoolName","gcsDataSource":{"bucketName":"bucketName","path":"path","managedFolderTransferEnabled":True},"gcsDataSink":{"bucketName":"bucketName","path":"path","managedFolderTransferEnabled":True},"posixDataSource":{"rootDirectory":"rootDirectory"},"hdfsDataSource":{"path":"path"},"objectConditions":{"minTimeElapsedSinceLastModification":"minTimeElapsedSinceLastModification","includePrefixes":["includePrefixes","includePrefixes"],"lastModifiedBefore":"lastModifiedBefore","lastModifiedSince":"lastModifiedSince","excludePrefixes":["excludePrefixes","excludePrefixes"],"maxTimeElapsedSinceLastModification":"maxTimeElapsedSinceLastModification"},"gcsIntermediateDataLocation":{"bucketName":"bucketName","path":"path","managedFolderTransferEnabled":True},"httpDataSource":{"listUrl":"listUrl"},"transferManifest":{"location":"location"},"transferOptions":{"deleteObjectsUniqueInSink":True,"overwriteObjectsAlreadyExistingInSink":True,"metadataOptions":{"mode":"MODE_UNSPECIFIED","uid":"UID_UNSPECIFIED","storageClass":"STORAGE_CLASS_UNSPECIFIED","gid":"GID_UNSPECIFIED","kmsKey":"KMS_KEY_UNSPECIFIED","symlink":"SYMLINK_UNSPECIFIED","temporaryHold":"TEMPORARY_HOLD_UNSPECIFIED","timeCreated":"TIME_CREATED_UNSPECIFIED","acl":"ACL_UNSPECIFIED"},"deleteObjectsFromSourceAfterTransfer":True,"overwriteWhen":"OVERWRITE_WHEN_UNSPECIFIED"}},"notificationConfig":{"eventTypes":["EVENT_TYPE_UNSPECIFIED","EVENT_TYPE_UNSPECIFIED"],"pubsubTopic":"pubsubTopic","payloadFormat":"PAYLOAD_FORMAT_UNSPECIFIED"},"projectId":"projectId","latestOperationName":"latestOperationName","status":"STATUS_UNSPECIFIED"}
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
        path='/v1/transferJobs',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storagetransfer_transfer_jobs_delete(client):
    """Test case for storagetransfer_transfer_jobs_delete

    
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
                    ('projectId', 'project_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/{job_name}'.format(job_name='job_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storagetransfer_transfer_jobs_get(client):
    """Test case for storagetransfer_transfer_jobs_get

    
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
                    ('projectId', 'project_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{job_name}'.format(job_name='job_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storagetransfer_transfer_jobs_list(client):
    """Test case for storagetransfer_transfer_jobs_list

    
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
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/transferJobs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storagetransfer_transfer_jobs_patch(client):
    """Test case for storagetransfer_transfer_jobs_patch

    
    """
    body = {"transferJob":{"creationTime":"creationTime","lastModificationTime":"lastModificationTime","description":"description","deletionTime":"deletionTime","schedule":{"scheduleEndDate":{"month":2,"year":7,"day":5},"scheduleStartDate":{"month":2,"year":7,"day":5},"repeatInterval":"repeatInterval","endTimeOfDay":{"hours":0,"seconds":5,"nanos":1,"minutes":6},"startTimeOfDay":{"hours":0,"seconds":5,"nanos":1,"minutes":6}},"loggingConfig":{"logActions":["LOGGABLE_ACTION_UNSPECIFIED","LOGGABLE_ACTION_UNSPECIFIED"],"enableOnpremGcsTransferLogs":True,"logActionStates":["LOGGABLE_ACTION_STATE_UNSPECIFIED","LOGGABLE_ACTION_STATE_UNSPECIFIED"]},"eventStream":{"eventStreamExpirationTime":"eventStreamExpirationTime","eventStreamStartTime":"eventStreamStartTime","name":"name"},"name":"name","transferSpec":{"sinkAgentPoolName":"sinkAgentPoolName","awsS3CompatibleDataSource":{"bucketName":"bucketName","path":"path","endpoint":"endpoint","s3Metadata":{"protocol":"NETWORK_PROTOCOL_UNSPECIFIED","listApi":"LIST_API_UNSPECIFIED","requestModel":"REQUEST_MODEL_UNSPECIFIED","authMethod":"AUTH_METHOD_UNSPECIFIED"},"region":"region"},"azureBlobStorageDataSource":{"container":"container","path":"path","credentialsSecret":"credentialsSecret","azureCredentials":{"sasToken":"sasToken"},"storageAccount":"storageAccount"},"posixDataSink":{"rootDirectory":"rootDirectory"},"awsS3DataSource":{"bucketName":"bucketName","path":"path","awsAccessKey":{"accessKeyId":"accessKeyId","secretAccessKey":"secretAccessKey"},"credentialsSecret":"credentialsSecret","roleArn":"roleArn","cloudfrontDomain":"cloudfrontDomain"},"sourceAgentPoolName":"sourceAgentPoolName","gcsDataSource":{"bucketName":"bucketName","path":"path","managedFolderTransferEnabled":True},"gcsDataSink":{"bucketName":"bucketName","path":"path","managedFolderTransferEnabled":True},"posixDataSource":{"rootDirectory":"rootDirectory"},"hdfsDataSource":{"path":"path"},"objectConditions":{"minTimeElapsedSinceLastModification":"minTimeElapsedSinceLastModification","includePrefixes":["includePrefixes","includePrefixes"],"lastModifiedBefore":"lastModifiedBefore","lastModifiedSince":"lastModifiedSince","excludePrefixes":["excludePrefixes","excludePrefixes"],"maxTimeElapsedSinceLastModification":"maxTimeElapsedSinceLastModification"},"gcsIntermediateDataLocation":{"bucketName":"bucketName","path":"path","managedFolderTransferEnabled":True},"httpDataSource":{"listUrl":"listUrl"},"transferManifest":{"location":"location"},"transferOptions":{"deleteObjectsUniqueInSink":True,"overwriteObjectsAlreadyExistingInSink":True,"metadataOptions":{"mode":"MODE_UNSPECIFIED","uid":"UID_UNSPECIFIED","storageClass":"STORAGE_CLASS_UNSPECIFIED","gid":"GID_UNSPECIFIED","kmsKey":"KMS_KEY_UNSPECIFIED","symlink":"SYMLINK_UNSPECIFIED","temporaryHold":"TEMPORARY_HOLD_UNSPECIFIED","timeCreated":"TIME_CREATED_UNSPECIFIED","acl":"ACL_UNSPECIFIED"},"deleteObjectsFromSourceAfterTransfer":True,"overwriteWhen":"OVERWRITE_WHEN_UNSPECIFIED"}},"notificationConfig":{"eventTypes":["EVENT_TYPE_UNSPECIFIED","EVENT_TYPE_UNSPECIFIED"],"pubsubTopic":"pubsubTopic","payloadFormat":"PAYLOAD_FORMAT_UNSPECIFIED"},"projectId":"projectId","latestOperationName":"latestOperationName","status":"STATUS_UNSPECIFIED"},"projectId":"projectId","updateTransferJobFieldMask":"updateTransferJobFieldMask"}
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
        method='PATCH',
        path='/v1/{job_name}'.format(job_name='job_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storagetransfer_transfer_jobs_run(client):
    """Test case for storagetransfer_transfer_jobs_run

    
    """
    body = {"projectId":"projectId"}
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
        path='/v1/{job_nameru}'.format(job_name='job_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

