# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_job_from_template_request import CreateJobFromTemplateRequest
from openapi_server.models.get_debug_config_request import GetDebugConfigRequest
from openapi_server.models.get_debug_config_response import GetDebugConfigResponse
from openapi_server.models.get_template_response import GetTemplateResponse
from openapi_server.models.job import Job
from openapi_server.models.job_execution_details import JobExecutionDetails
from openapi_server.models.job_metrics import JobMetrics
from openapi_server.models.launch_flex_template_request import LaunchFlexTemplateRequest
from openapi_server.models.launch_flex_template_response import LaunchFlexTemplateResponse
from openapi_server.models.launch_template_parameters import LaunchTemplateParameters
from openapi_server.models.launch_template_response import LaunchTemplateResponse
from openapi_server.models.lease_work_item_request import LeaseWorkItemRequest
from openapi_server.models.lease_work_item_response import LeaseWorkItemResponse
from openapi_server.models.list_job_messages_response import ListJobMessagesResponse
from openapi_server.models.list_jobs_response import ListJobsResponse
from openapi_server.models.list_snapshots_response import ListSnapshotsResponse
from openapi_server.models.report_work_item_status_request import ReportWorkItemStatusRequest
from openapi_server.models.report_work_item_status_response import ReportWorkItemStatusResponse
from openapi_server.models.send_debug_capture_request import SendDebugCaptureRequest
from openapi_server.models.send_worker_messages_request import SendWorkerMessagesRequest
from openapi_server.models.send_worker_messages_response import SendWorkerMessagesResponse
from openapi_server.models.snapshot import Snapshot
from openapi_server.models.snapshot_job_request import SnapshotJobRequest
from openapi_server.models.stage_execution_details import StageExecutionDetails


pytestmark = pytest.mark.asyncio

async def test_dataflow_projects_delete_snapshots(client):
    """Test case for dataflow_projects_delete_snapshots

    
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
                    ('location', 'location_example'),
                    ('snapshotId', 'snapshot_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1b3/projects/{project_id}/snapshots'.format(project_id='project_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataflow_projects_jobs_aggregated(client):
    """Test case for dataflow_projects_jobs_aggregated

    
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
                    ('location', 'location_example'),
                    ('name', 'name_example'),
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
        path='/v1b3/projects/{project_id}/jobs:aggregated'.format(project_id='project_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataflow_projects_jobs_create(client):
    """Test case for dataflow_projects_jobs_create

    
    """
    body = {"transformNameMapping":{"key":"transformNameMapping"},"currentStateTime":"currentStateTime","jobMetadata":{"bigTableDetails":[{"instanceId":"instanceId","tableId":"tableId","projectId":"projectId"},{"instanceId":"instanceId","tableId":"tableId","projectId":"projectId"}],"datastoreDetails":[{"namespace":"namespace","projectId":"projectId"},{"namespace":"namespace","projectId":"projectId"}],"fileDetails":[{"filePattern":"filePattern"},{"filePattern":"filePattern"}],"pubsubDetails":[{"topic":"topic","subscription":"subscription"},{"topic":"topic","subscription":"subscription"}],"bigqueryDetails":[{"query":"query","dataset":"dataset","projectId":"projectId","table":"table"},{"query":"query","dataset":"dataset","projectId":"projectId","table":"table"}],"sdkVersion":{"bugs":[{"severity":"SEVERITY_UNSPECIFIED","type":"TYPE_UNSPECIFIED","uri":"uri"},{"severity":"SEVERITY_UNSPECIFIED","type":"TYPE_UNSPECIFIED","uri":"uri"}],"sdkSupportStatus":"UNKNOWN","version":"version","versionDisplayName":"versionDisplayName"},"userDisplayProperties":{"key":"userDisplayProperties"},"spannerDetails":[{"instanceId":"instanceId","databaseId":"databaseId","projectId":"projectId"},{"instanceId":"instanceId","databaseId":"databaseId","projectId":"projectId"}]},"tempFiles":["tempFiles","tempFiles"],"satisfiesPzs":True,"replacedByJobId":"replacedByJobId","type":"JOB_TYPE_UNKNOWN","createdFromSnapshotId":"createdFromSnapshotId","executionInfo":{"stages":{"key":{"stepName":["stepName","stepName"]}}},"startTime":"startTime","id":"id","stepsLocation":"stepsLocation","requestedState":"JOB_STATE_UNKNOWN","clientRequestId":"clientRequestId","steps":[{"kind":"kind","name":"name","properties":{"key":""}},{"kind":"kind","name":"name","properties":{"key":""}}],"labels":{"key":"labels"},"runtimeUpdatableParams":{"minNumWorkers":9,"maxNumWorkers":7,"workerUtilizationHint":3.616076749251911},"environment":{"workerRegion":"workerRegion","experiments":["experiments","experiments"],"sdkPipelineOptions":{"key":""},"streamingMode":"STREAMING_MODE_UNSPECIFIED","userAgent":{"key":""},"flexResourceSchedulingGoal":"FLEXRS_UNSPECIFIED","serviceOptions":["serviceOptions","serviceOptions"],"version":{"key":""},"serviceKmsKeyName":"serviceKmsKeyName","workerPools":[{"metadata":{"key":"metadata"},"onHostMaintenance":"onHostMaintenance","kind":"kind","poolArgs":{"key":""},"packages":[{"name":"name","location":"location"},{"name":"name","location":"location"}],"diskSourceImage":"diskSourceImage","numThreadsPerWorker":5,"workerHarnessContainerImage":"workerHarnessContainerImage","network":"network","zone":"zone","ipConfiguration":"WORKER_IP_UNSPECIFIED","teardownPolicy":"TEARDOWN_POLICY_UNKNOWN","sdkHarnessContainerImages":[{"useSingleCorePerContainer":True,"capabilities":["capabilities","capabilities"],"environmentId":"environmentId","containerImage":"containerImage"},{"useSingleCorePerContainer":True,"capabilities":["capabilities","capabilities"],"environmentId":"environmentId","containerImage":"containerImage"}],"subnetwork":"subnetwork","numWorkers":5,"autoscalingSettings":{"maxNumWorkers":0,"algorithm":"AUTOSCALING_ALGORITHM_UNKNOWN"},"dataDisks":[{"sizeGb":6,"mountPoint":"mountPoint","diskType":"diskType"},{"sizeGb":6,"mountPoint":"mountPoint","diskType":"diskType"}],"diskType":"diskType","taskrunnerSettings":{"logUploadLocation":"logUploadLocation","alsologtostderr":True,"vmId":"vmId","workflowFileName":"workflowFileName","harnessCommand":"harnessCommand","continueOnException":True,"oauthScopes":["oauthScopes","oauthScopes"],"commandlinesFileName":"commandlinesFileName","taskGroup":"taskGroup","baseUrl":"baseUrl","parallelWorkerSettings":{"reportingEnabled":True,"baseUrl":"baseUrl","shuffleServicePath":"shuffleServicePath","workerId":"workerId","servicePath":"servicePath","tempStoragePrefix":"tempStoragePrefix"},"languageHint":"languageHint","dataflowApiVersion":"dataflowApiVersion","baseTaskDir":"baseTaskDir","streamingWorkerMainClass":"streamingWorkerMainClass","logToSerialconsole":True,"logDir":"logDir","taskUser":"taskUser","tempStoragePrefix":"tempStoragePrefix"},"machineType":"machineType","defaultPackageSet":"DEFAULT_PACKAGE_SET_UNKNOWN","diskSizeGb":1},{"metadata":{"key":"metadata"},"onHostMaintenance":"onHostMaintenance","kind":"kind","poolArgs":{"key":""},"packages":[{"name":"name","location":"location"},{"name":"name","location":"location"}],"diskSourceImage":"diskSourceImage","numThreadsPerWorker":5,"workerHarnessContainerImage":"workerHarnessContainerImage","network":"network","zone":"zone","ipConfiguration":"WORKER_IP_UNSPECIFIED","teardownPolicy":"TEARDOWN_POLICY_UNKNOWN","sdkHarnessContainerImages":[{"useSingleCorePerContainer":True,"capabilities":["capabilities","capabilities"],"environmentId":"environmentId","containerImage":"containerImage"},{"useSingleCorePerContainer":True,"capabilities":["capabilities","capabilities"],"environmentId":"environmentId","containerImage":"containerImage"}],"subnetwork":"subnetwork","numWorkers":5,"autoscalingSettings":{"maxNumWorkers":0,"algorithm":"AUTOSCALING_ALGORITHM_UNKNOWN"},"dataDisks":[{"sizeGb":6,"mountPoint":"mountPoint","diskType":"diskType"},{"sizeGb":6,"mountPoint":"mountPoint","diskType":"diskType"}],"diskType":"diskType","taskrunnerSettings":{"logUploadLocation":"logUploadLocation","alsologtostderr":True,"vmId":"vmId","workflowFileName":"workflowFileName","harnessCommand":"harnessCommand","continueOnException":True,"oauthScopes":["oauthScopes","oauthScopes"],"commandlinesFileName":"commandlinesFileName","taskGroup":"taskGroup","baseUrl":"baseUrl","parallelWorkerSettings":{"reportingEnabled":True,"baseUrl":"baseUrl","shuffleServicePath":"shuffleServicePath","workerId":"workerId","servicePath":"servicePath","tempStoragePrefix":"tempStoragePrefix"},"languageHint":"languageHint","dataflowApiVersion":"dataflowApiVersion","baseTaskDir":"baseTaskDir","streamingWorkerMainClass":"streamingWorkerMainClass","logToSerialconsole":True,"logDir":"logDir","taskUser":"taskUser","tempStoragePrefix":"tempStoragePrefix"},"machineType":"machineType","defaultPackageSet":"DEFAULT_PACKAGE_SET_UNKNOWN","diskSizeGb":1}],"clusterManagerApiService":"clusterManagerApiService","debugOptions":{"enableHotKeyLogging":True,"dataSampling":{"behaviors":["DATA_SAMPLING_BEHAVIOR_UNSPECIFIED","DATA_SAMPLING_BEHAVIOR_UNSPECIFIED"]}},"workerZone":"workerZone","serviceAccountEmail":"serviceAccountEmail","internalExperiments":{"key":""},"shuffleMode":"SHUFFLE_MODE_UNSPECIFIED","dataset":"dataset","useStreamingEngineResourceBasedBilling":True,"tempStoragePrefix":"tempStoragePrefix"},"pipelineDescription":{"stepNamesHash":"stepNamesHash","displayData":[{"int64Value":"int64Value","shortStrValue":"shortStrValue","durationValue":"durationValue","timestampValue":"timestampValue","namespace":"namespace","floatValue":2.302136,"boolValue":True,"javaClassValue":"javaClassValue","label":"label","strValue":"strValue","key":"key","url":"url"},{"int64Value":"int64Value","shortStrValue":"shortStrValue","durationValue":"durationValue","timestampValue":"timestampValue","namespace":"namespace","floatValue":2.302136,"boolValue":True,"javaClassValue":"javaClassValue","label":"label","strValue":"strValue","key":"key","url":"url"}],"originalPipelineTransform":[{"outputCollectionName":["outputCollectionName","outputCollectionName"],"inputCollectionName":["inputCollectionName","inputCollectionName"],"kind":"UNKNOWN_KIND","name":"name","displayData":[{"int64Value":"int64Value","shortStrValue":"shortStrValue","durationValue":"durationValue","timestampValue":"timestampValue","namespace":"namespace","floatValue":2.302136,"boolValue":True,"javaClassValue":"javaClassValue","label":"label","strValue":"strValue","key":"key","url":"url"},{"int64Value":"int64Value","shortStrValue":"shortStrValue","durationValue":"durationValue","timestampValue":"timestampValue","namespace":"namespace","floatValue":2.302136,"boolValue":True,"javaClassValue":"javaClassValue","label":"label","strValue":"strValue","key":"key","url":"url"}],"id":"id"},{"outputCollectionName":["outputCollectionName","outputCollectionName"],"inputCollectionName":["inputCollectionName","inputCollectionName"],"kind":"UNKNOWN_KIND","name":"name","displayData":[{"int64Value":"int64Value","shortStrValue":"shortStrValue","durationValue":"durationValue","timestampValue":"timestampValue","namespace":"namespace","floatValue":2.302136,"boolValue":True,"javaClassValue":"javaClassValue","label":"label","strValue":"strValue","key":"key","url":"url"},{"int64Value":"int64Value","shortStrValue":"shortStrValue","durationValue":"durationValue","timestampValue":"timestampValue","namespace":"namespace","floatValue":2.302136,"boolValue":True,"javaClassValue":"javaClassValue","label":"label","strValue":"strValue","key":"key","url":"url"}],"id":"id"}],"executionPipelineStage":[{"prerequisiteStage":["prerequisiteStage","prerequisiteStage"],"kind":"UNKNOWN_KIND","name":"name","outputSource":[{"originalTransformOrCollection":"originalTransformOrCollection","name":"name","userName":"userName","sizeBytes":"sizeBytes"},{"originalTransformOrCollection":"originalTransformOrCollection","name":"name","userName":"userName","sizeBytes":"sizeBytes"}],"componentTransform":[{"originalTransform":"originalTransform","name":"name","userName":"userName"},{"originalTransform":"originalTransform","name":"name","userName":"userName"}],"id":"id","inputSource":[{"originalTransformOrCollection":"originalTransformOrCollection","name":"name","userName":"userName","sizeBytes":"sizeBytes"},{"originalTransformOrCollection":"originalTransformOrCollection","name":"name","userName":"userName","sizeBytes":"sizeBytes"}],"componentSource":[{"originalTransformOrCollection":"originalTransformOrCollection","name":"name","userName":"userName"},{"originalTransformOrCollection":"originalTransformOrCollection","name":"name","userName":"userName"}]},{"prerequisiteStage":["prerequisiteStage","prerequisiteStage"],"kind":"UNKNOWN_KIND","name":"name","outputSource":[{"originalTransformOrCollection":"originalTransformOrCollection","name":"name","userName":"userName","sizeBytes":"sizeBytes"},{"originalTransformOrCollection":"originalTransformOrCollection","name":"name","userName":"userName","sizeBytes":"sizeBytes"}],"componentTransform":[{"originalTransform":"originalTransform","name":"name","userName":"userName"},{"originalTransform":"originalTransform","name":"name","userName":"userName"}],"id":"id","inputSource":[{"originalTransformOrCollection":"originalTransformOrCollection","name":"name","userName":"userName","sizeBytes":"sizeBytes"},{"originalTransformOrCollection":"originalTransformOrCollection","name":"name","userName":"userName","sizeBytes":"sizeBytes"}],"componentSource":[{"originalTransformOrCollection":"originalTransformOrCollection","name":"name","userName":"userName"},{"originalTransformOrCollection":"originalTransformOrCollection","name":"name","userName":"userName"}]}]},"stageStates":[{"executionStageName":"executionStageName","executionStageState":"JOB_STATE_UNKNOWN","currentStateTime":"currentStateTime"},{"executionStageName":"executionStageName","executionStageState":"JOB_STATE_UNKNOWN","currentStateTime":"currentStateTime"}],"createTime":"createTime","replaceJobId":"replaceJobId","name":"name","location":"location","currentState":"JOB_STATE_UNKNOWN","satisfiesPzi":True,"projectId":"projectId"}
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
                    ('location', 'location_example'),
                    ('replaceJobId', 'replace_job_id_example'),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1b3/projects/{project_id}/jobs'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataflow_projects_jobs_debug_get_config(client):
    """Test case for dataflow_projects_jobs_debug_get_config

    
    """
    body = {"workerId":"workerId","componentId":"componentId","location":"location"}
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
        path='/v1b3/projects/{project_id}/jobs/{job_id}/debug/getConfig'.format(project_id='project_id_example', job_id='job_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataflow_projects_jobs_debug_send_capture(client):
    """Test case for dataflow_projects_jobs_debug_send_capture

    
    """
    body = {"workerId":"workerId","componentId":"componentId","data":"data","dataFormat":"DATA_FORMAT_UNSPECIFIED","location":"location"}
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
        path='/v1b3/projects/{project_id}/jobs/{job_id}/debug/sendCapture'.format(project_id='project_id_example', job_id='job_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataflow_projects_jobs_get(client):
    """Test case for dataflow_projects_jobs_get

    
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
                    ('location', 'location_example'),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1b3/projects/{project_id}/jobs/{job_id}'.format(project_id='project_id_example', job_id='job_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataflow_projects_jobs_get_metrics(client):
    """Test case for dataflow_projects_jobs_get_metrics

    
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
                    ('location', 'location_example'),
                    ('startTime', 'start_time_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1b3/projects/{project_id}/jobs/{job_id}/metrics'.format(project_id='project_id_example', job_id='job_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataflow_projects_jobs_list(client):
    """Test case for dataflow_projects_jobs_list

    
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
                    ('location', 'location_example'),
                    ('name', 'name_example'),
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
        path='/v1b3/projects/{project_id}/jobs'.format(project_id='project_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataflow_projects_jobs_messages_list(client):
    """Test case for dataflow_projects_jobs_messages_list

    
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
                    ('endTime', 'end_time_example'),
                    ('location', 'location_example'),
                    ('minimumImportance', 'minimum_importance_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('startTime', 'start_time_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1b3/projects/{project_id}/jobs/{job_id}/messages'.format(project_id='project_id_example', job_id='job_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataflow_projects_jobs_snapshot(client):
    """Test case for dataflow_projects_jobs_snapshot

    
    """
    body = {"snapshotSources":True,"description":"description","location":"location","ttl":"ttl"}
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
        path='/v1b3/projects/{project_id}/jobs/{job_idsnapsho}'.format(project_id='project_id_example', job_id='job_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataflow_projects_jobs_update(client):
    """Test case for dataflow_projects_jobs_update

    
    """
    body = {"transformNameMapping":{"key":"transformNameMapping"},"currentStateTime":"currentStateTime","jobMetadata":{"bigTableDetails":[{"instanceId":"instanceId","tableId":"tableId","projectId":"projectId"},{"instanceId":"instanceId","tableId":"tableId","projectId":"projectId"}],"datastoreDetails":[{"namespace":"namespace","projectId":"projectId"},{"namespace":"namespace","projectId":"projectId"}],"fileDetails":[{"filePattern":"filePattern"},{"filePattern":"filePattern"}],"pubsubDetails":[{"topic":"topic","subscription":"subscription"},{"topic":"topic","subscription":"subscription"}],"bigqueryDetails":[{"query":"query","dataset":"dataset","projectId":"projectId","table":"table"},{"query":"query","dataset":"dataset","projectId":"projectId","table":"table"}],"sdkVersion":{"bugs":[{"severity":"SEVERITY_UNSPECIFIED","type":"TYPE_UNSPECIFIED","uri":"uri"},{"severity":"SEVERITY_UNSPECIFIED","type":"TYPE_UNSPECIFIED","uri":"uri"}],"sdkSupportStatus":"UNKNOWN","version":"version","versionDisplayName":"versionDisplayName"},"userDisplayProperties":{"key":"userDisplayProperties"},"spannerDetails":[{"instanceId":"instanceId","databaseId":"databaseId","projectId":"projectId"},{"instanceId":"instanceId","databaseId":"databaseId","projectId":"projectId"}]},"tempFiles":["tempFiles","tempFiles"],"satisfiesPzs":True,"replacedByJobId":"replacedByJobId","type":"JOB_TYPE_UNKNOWN","createdFromSnapshotId":"createdFromSnapshotId","executionInfo":{"stages":{"key":{"stepName":["stepName","stepName"]}}},"startTime":"startTime","id":"id","stepsLocation":"stepsLocation","requestedState":"JOB_STATE_UNKNOWN","clientRequestId":"clientRequestId","steps":[{"kind":"kind","name":"name","properties":{"key":""}},{"kind":"kind","name":"name","properties":{"key":""}}],"labels":{"key":"labels"},"runtimeUpdatableParams":{"minNumWorkers":9,"maxNumWorkers":7,"workerUtilizationHint":3.616076749251911},"environment":{"workerRegion":"workerRegion","experiments":["experiments","experiments"],"sdkPipelineOptions":{"key":""},"streamingMode":"STREAMING_MODE_UNSPECIFIED","userAgent":{"key":""},"flexResourceSchedulingGoal":"FLEXRS_UNSPECIFIED","serviceOptions":["serviceOptions","serviceOptions"],"version":{"key":""},"serviceKmsKeyName":"serviceKmsKeyName","workerPools":[{"metadata":{"key":"metadata"},"onHostMaintenance":"onHostMaintenance","kind":"kind","poolArgs":{"key":""},"packages":[{"name":"name","location":"location"},{"name":"name","location":"location"}],"diskSourceImage":"diskSourceImage","numThreadsPerWorker":5,"workerHarnessContainerImage":"workerHarnessContainerImage","network":"network","zone":"zone","ipConfiguration":"WORKER_IP_UNSPECIFIED","teardownPolicy":"TEARDOWN_POLICY_UNKNOWN","sdkHarnessContainerImages":[{"useSingleCorePerContainer":True,"capabilities":["capabilities","capabilities"],"environmentId":"environmentId","containerImage":"containerImage"},{"useSingleCorePerContainer":True,"capabilities":["capabilities","capabilities"],"environmentId":"environmentId","containerImage":"containerImage"}],"subnetwork":"subnetwork","numWorkers":5,"autoscalingSettings":{"maxNumWorkers":0,"algorithm":"AUTOSCALING_ALGORITHM_UNKNOWN"},"dataDisks":[{"sizeGb":6,"mountPoint":"mountPoint","diskType":"diskType"},{"sizeGb":6,"mountPoint":"mountPoint","diskType":"diskType"}],"diskType":"diskType","taskrunnerSettings":{"logUploadLocation":"logUploadLocation","alsologtostderr":True,"vmId":"vmId","workflowFileName":"workflowFileName","harnessCommand":"harnessCommand","continueOnException":True,"oauthScopes":["oauthScopes","oauthScopes"],"commandlinesFileName":"commandlinesFileName","taskGroup":"taskGroup","baseUrl":"baseUrl","parallelWorkerSettings":{"reportingEnabled":True,"baseUrl":"baseUrl","shuffleServicePath":"shuffleServicePath","workerId":"workerId","servicePath":"servicePath","tempStoragePrefix":"tempStoragePrefix"},"languageHint":"languageHint","dataflowApiVersion":"dataflowApiVersion","baseTaskDir":"baseTaskDir","streamingWorkerMainClass":"streamingWorkerMainClass","logToSerialconsole":True,"logDir":"logDir","taskUser":"taskUser","tempStoragePrefix":"tempStoragePrefix"},"machineType":"machineType","defaultPackageSet":"DEFAULT_PACKAGE_SET_UNKNOWN","diskSizeGb":1},{"metadata":{"key":"metadata"},"onHostMaintenance":"onHostMaintenance","kind":"kind","poolArgs":{"key":""},"packages":[{"name":"name","location":"location"},{"name":"name","location":"location"}],"diskSourceImage":"diskSourceImage","numThreadsPerWorker":5,"workerHarnessContainerImage":"workerHarnessContainerImage","network":"network","zone":"zone","ipConfiguration":"WORKER_IP_UNSPECIFIED","teardownPolicy":"TEARDOWN_POLICY_UNKNOWN","sdkHarnessContainerImages":[{"useSingleCorePerContainer":True,"capabilities":["capabilities","capabilities"],"environmentId":"environmentId","containerImage":"containerImage"},{"useSingleCorePerContainer":True,"capabilities":["capabilities","capabilities"],"environmentId":"environmentId","containerImage":"containerImage"}],"subnetwork":"subnetwork","numWorkers":5,"autoscalingSettings":{"maxNumWorkers":0,"algorithm":"AUTOSCALING_ALGORITHM_UNKNOWN"},"dataDisks":[{"sizeGb":6,"mountPoint":"mountPoint","diskType":"diskType"},{"sizeGb":6,"mountPoint":"mountPoint","diskType":"diskType"}],"diskType":"diskType","taskrunnerSettings":{"logUploadLocation":"logUploadLocation","alsologtostderr":True,"vmId":"vmId","workflowFileName":"workflowFileName","harnessCommand":"harnessCommand","continueOnException":True,"oauthScopes":["oauthScopes","oauthScopes"],"commandlinesFileName":"commandlinesFileName","taskGroup":"taskGroup","baseUrl":"baseUrl","parallelWorkerSettings":{"reportingEnabled":True,"baseUrl":"baseUrl","shuffleServicePath":"shuffleServicePath","workerId":"workerId","servicePath":"servicePath","tempStoragePrefix":"tempStoragePrefix"},"languageHint":"languageHint","dataflowApiVersion":"dataflowApiVersion","baseTaskDir":"baseTaskDir","streamingWorkerMainClass":"streamingWorkerMainClass","logToSerialconsole":True,"logDir":"logDir","taskUser":"taskUser","tempStoragePrefix":"tempStoragePrefix"},"machineType":"machineType","defaultPackageSet":"DEFAULT_PACKAGE_SET_UNKNOWN","diskSizeGb":1}],"clusterManagerApiService":"clusterManagerApiService","debugOptions":{"enableHotKeyLogging":True,"dataSampling":{"behaviors":["DATA_SAMPLING_BEHAVIOR_UNSPECIFIED","DATA_SAMPLING_BEHAVIOR_UNSPECIFIED"]}},"workerZone":"workerZone","serviceAccountEmail":"serviceAccountEmail","internalExperiments":{"key":""},"shuffleMode":"SHUFFLE_MODE_UNSPECIFIED","dataset":"dataset","useStreamingEngineResourceBasedBilling":True,"tempStoragePrefix":"tempStoragePrefix"},"pipelineDescription":{"stepNamesHash":"stepNamesHash","displayData":[{"int64Value":"int64Value","shortStrValue":"shortStrValue","durationValue":"durationValue","timestampValue":"timestampValue","namespace":"namespace","floatValue":2.302136,"boolValue":True,"javaClassValue":"javaClassValue","label":"label","strValue":"strValue","key":"key","url":"url"},{"int64Value":"int64Value","shortStrValue":"shortStrValue","durationValue":"durationValue","timestampValue":"timestampValue","namespace":"namespace","floatValue":2.302136,"boolValue":True,"javaClassValue":"javaClassValue","label":"label","strValue":"strValue","key":"key","url":"url"}],"originalPipelineTransform":[{"outputCollectionName":["outputCollectionName","outputCollectionName"],"inputCollectionName":["inputCollectionName","inputCollectionName"],"kind":"UNKNOWN_KIND","name":"name","displayData":[{"int64Value":"int64Value","shortStrValue":"shortStrValue","durationValue":"durationValue","timestampValue":"timestampValue","namespace":"namespace","floatValue":2.302136,"boolValue":True,"javaClassValue":"javaClassValue","label":"label","strValue":"strValue","key":"key","url":"url"},{"int64Value":"int64Value","shortStrValue":"shortStrValue","durationValue":"durationValue","timestampValue":"timestampValue","namespace":"namespace","floatValue":2.302136,"boolValue":True,"javaClassValue":"javaClassValue","label":"label","strValue":"strValue","key":"key","url":"url"}],"id":"id"},{"outputCollectionName":["outputCollectionName","outputCollectionName"],"inputCollectionName":["inputCollectionName","inputCollectionName"],"kind":"UNKNOWN_KIND","name":"name","displayData":[{"int64Value":"int64Value","shortStrValue":"shortStrValue","durationValue":"durationValue","timestampValue":"timestampValue","namespace":"namespace","floatValue":2.302136,"boolValue":True,"javaClassValue":"javaClassValue","label":"label","strValue":"strValue","key":"key","url":"url"},{"int64Value":"int64Value","shortStrValue":"shortStrValue","durationValue":"durationValue","timestampValue":"timestampValue","namespace":"namespace","floatValue":2.302136,"boolValue":True,"javaClassValue":"javaClassValue","label":"label","strValue":"strValue","key":"key","url":"url"}],"id":"id"}],"executionPipelineStage":[{"prerequisiteStage":["prerequisiteStage","prerequisiteStage"],"kind":"UNKNOWN_KIND","name":"name","outputSource":[{"originalTransformOrCollection":"originalTransformOrCollection","name":"name","userName":"userName","sizeBytes":"sizeBytes"},{"originalTransformOrCollection":"originalTransformOrCollection","name":"name","userName":"userName","sizeBytes":"sizeBytes"}],"componentTransform":[{"originalTransform":"originalTransform","name":"name","userName":"userName"},{"originalTransform":"originalTransform","name":"name","userName":"userName"}],"id":"id","inputSource":[{"originalTransformOrCollection":"originalTransformOrCollection","name":"name","userName":"userName","sizeBytes":"sizeBytes"},{"originalTransformOrCollection":"originalTransformOrCollection","name":"name","userName":"userName","sizeBytes":"sizeBytes"}],"componentSource":[{"originalTransformOrCollection":"originalTransformOrCollection","name":"name","userName":"userName"},{"originalTransformOrCollection":"originalTransformOrCollection","name":"name","userName":"userName"}]},{"prerequisiteStage":["prerequisiteStage","prerequisiteStage"],"kind":"UNKNOWN_KIND","name":"name","outputSource":[{"originalTransformOrCollection":"originalTransformOrCollection","name":"name","userName":"userName","sizeBytes":"sizeBytes"},{"originalTransformOrCollection":"originalTransformOrCollection","name":"name","userName":"userName","sizeBytes":"sizeBytes"}],"componentTransform":[{"originalTransform":"originalTransform","name":"name","userName":"userName"},{"originalTransform":"originalTransform","name":"name","userName":"userName"}],"id":"id","inputSource":[{"originalTransformOrCollection":"originalTransformOrCollection","name":"name","userName":"userName","sizeBytes":"sizeBytes"},{"originalTransformOrCollection":"originalTransformOrCollection","name":"name","userName":"userName","sizeBytes":"sizeBytes"}],"componentSource":[{"originalTransformOrCollection":"originalTransformOrCollection","name":"name","userName":"userName"},{"originalTransformOrCollection":"originalTransformOrCollection","name":"name","userName":"userName"}]}]},"stageStates":[{"executionStageName":"executionStageName","executionStageState":"JOB_STATE_UNKNOWN","currentStateTime":"currentStateTime"},{"executionStageName":"executionStageName","executionStageState":"JOB_STATE_UNKNOWN","currentStateTime":"currentStateTime"}],"createTime":"createTime","replaceJobId":"replaceJobId","name":"name","location":"location","currentState":"JOB_STATE_UNKNOWN","satisfiesPzi":True,"projectId":"projectId"}
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
                    ('location', 'location_example'),
                    ('updateMask', 'update_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1b3/projects/{project_id}/jobs/{job_id}'.format(project_id='project_id_example', job_id='job_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataflow_projects_jobs_work_items_lease(client):
    """Test case for dataflow_projects_jobs_work_items_lease

    
    """
    body = {"currentWorkerTime":"currentWorkerTime","unifiedWorkerRequest":{"key":""},"workerId":"workerId","workItemTypes":["workItemTypes","workItemTypes"],"location":"location","requestedLeaseDuration":"requestedLeaseDuration","workerCapabilities":["workerCapabilities","workerCapabilities"]}
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
        path='/v1b3/projects/{project_id}/jobs/{job_id}/workItems:lease'.format(project_id='project_id_example', job_id='job_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataflow_projects_jobs_work_items_report_status(client):
    """Test case for dataflow_projects_jobs_work_items_report_status

    
    """
    body = {"currentWorkerTime":"currentWorkerTime","unifiedWorkerRequest":{"key":""},"workerId":"workerId","workItemStatuses":[{"metricUpdates":[{"gauge":"","internal":"","scalar":"","set":"","meanCount":"","kind":"kind","name":{"origin":"origin","context":{"key":"context"},"name":"name"},"updateTime":"updateTime","cumulative":True,"distribution":"","meanSum":""},{"gauge":"","internal":"","scalar":"","set":"","meanCount":"","kind":"kind","name":{"origin":"origin","context":{"key":"context"},"name":"name"},"updateTime":"updateTime","cumulative":True,"distribution":"","meanSum":""}],"sourceFork":{"primarySource":{"derivationMode":"SOURCE_DERIVATION_MODE_UNKNOWN","source":{"codec":{"key":""},"metadata":{"infinite":True,"estimatedSizeBytes":"estimatedSizeBytes","producesSortedKeys":True},"baseSpecs":[{"key":""},{"key":""}],"doesNotNeedSplitting":True,"spec":{"key":""}}},"residual":{"derivationMode":"SOURCE_DERIVATION_MODE_UNKNOWN","source":{"codec":{"key":""},"metadata":{"infinite":True,"estimatedSizeBytes":"estimatedSizeBytes","producesSortedKeys":True},"baseSpecs":[{"key":""},{"key":""}],"doesNotNeedSplitting":True,"spec":{"key":""}}},"primary":{"derivationMode":"SOURCE_DERIVATION_MODE_UNKNOWN","source":{"codec":{"key":""},"metadata":{"infinite":True,"estimatedSizeBytes":"estimatedSizeBytes","producesSortedKeys":True},"baseSpecs":[{"key":""},{"key":""}],"doesNotNeedSplitting":True,"spec":{"key":""}}},"residualSource":{"derivationMode":"SOURCE_DERIVATION_MODE_UNKNOWN","source":{"codec":{"key":""},"metadata":{"infinite":True,"estimatedSizeBytes":"estimatedSizeBytes","producesSortedKeys":True},"baseSpecs":[{"key":""},{"key":""}],"doesNotNeedSplitting":True,"spec":{"key":""}}}},"stopPosition":{"concatPosition":{"index":5},"byteOffset":"byteOffset","end":True,"recordIndex":"recordIndex","key":"key","shufflePosition":"shufflePosition"},"dynamicSourceSplit":{"residual":{"derivationMode":"SOURCE_DERIVATION_MODE_UNKNOWN","source":{"codec":{"key":""},"metadata":{"infinite":True,"estimatedSizeBytes":"estimatedSizeBytes","producesSortedKeys":True},"baseSpecs":[{"key":""},{"key":""}],"doesNotNeedSplitting":True,"spec":{"key":""}}},"primary":{"derivationMode":"SOURCE_DERIVATION_MODE_UNKNOWN","source":{"codec":{"key":""},"metadata":{"infinite":True,"estimatedSizeBytes":"estimatedSizeBytes","producesSortedKeys":True},"baseSpecs":[{"key":""},{"key":""}],"doesNotNeedSplitting":True,"spec":{"key":""}}}},"completed":True,"reportIndex":"reportIndex","workItemId":"workItemId","sourceOperationResponse":{"getMetadata":{"metadata":{"infinite":True,"estimatedSizeBytes":"estimatedSizeBytes","producesSortedKeys":True}},"split":{"shards":[{"derivationMode":"SOURCE_DERIVATION_MODE_UNKNOWN","source":{"codec":{"key":""},"metadata":{"infinite":True,"estimatedSizeBytes":"estimatedSizeBytes","producesSortedKeys":True},"baseSpecs":[{"key":""},{"key":""}],"doesNotNeedSplitting":True,"spec":{"key":""}}},{"derivationMode":"SOURCE_DERIVATION_MODE_UNKNOWN","source":{"codec":{"key":""},"metadata":{"infinite":True,"estimatedSizeBytes":"estimatedSizeBytes","producesSortedKeys":True},"baseSpecs":[{"key":""},{"key":""}],"doesNotNeedSplitting":True,"spec":{"key":""}}}],"bundles":[{"derivationMode":"SOURCE_DERIVATION_MODE_UNKNOWN","source":{"codec":{"key":""},"metadata":{"infinite":True,"estimatedSizeBytes":"estimatedSizeBytes","producesSortedKeys":True},"baseSpecs":[{"key":""},{"key":""}],"doesNotNeedSplitting":True,"spec":{"key":""}}},{"derivationMode":"SOURCE_DERIVATION_MODE_UNKNOWN","source":{"codec":{"key":""},"metadata":{"infinite":True,"estimatedSizeBytes":"estimatedSizeBytes","producesSortedKeys":True},"baseSpecs":[{"key":""},{"key":""}],"doesNotNeedSplitting":True,"spec":{"key":""}}}],"outcome":"SOURCE_SPLIT_OUTCOME_UNKNOWN"}},"counterUpdates":[{"nameAndKind":{"kind":"INVALID","name":"name"},"shortId":"shortId","internal":"","integerList":{"elements":[{"highBits":0,"lowBits":6},{"highBits":0,"lowBits":6}]},"floatingPoint":5.637376656633329,"floatingPointList":{"elements":[2.3021358869347655,2.3021358869347655]},"integer":{"highBits":0,"lowBits":6},"cumulative":True,"distribution":{"histogram":{"bucketCounts":["bucketCounts","bucketCounts"],"firstBucketOffset":1},"sumOfSquares":5.962133916683182,"min":{"highBits":0,"lowBits":6},"max":{"highBits":0,"lowBits":6},"count":{"highBits":0,"lowBits":6},"sum":{"highBits":0,"lowBits":6}},"floatingPointMean":{"count":{"highBits":0,"lowBits":6},"sum":7.061401241503109},"integerGauge":{"value":{"highBits":0,"lowBits":6},"timestamp":"timestamp"},"boolean":True,"stringList":{"elements":["elements","elements"]},"integerMean":{"count":{"highBits":0,"lowBits":6},"sum":{"highBits":0,"lowBits":6}},"structuredNameAndMetadata":{"metadata":{"kind":"INVALID","standardUnits":"BYTES","description":"description","otherUnits":"otherUnits"},"name":{"workerId":"workerId","componentStepName":"componentStepName","inputIndex":9,"origin":"SYSTEM","portion":"ALL","name":"name","originalRequestingStepName":"originalRequestingStepName","executionStepName":"executionStepName","originNamespace":"originNamespace","originalStepName":"originalStepName"}}},{"nameAndKind":{"kind":"INVALID","name":"name"},"shortId":"shortId","internal":"","integerList":{"elements":[{"highBits":0,"lowBits":6},{"highBits":0,"lowBits":6}]},"floatingPoint":5.637376656633329,"floatingPointList":{"elements":[2.3021358869347655,2.3021358869347655]},"integer":{"highBits":0,"lowBits":6},"cumulative":True,"distribution":{"histogram":{"bucketCounts":["bucketCounts","bucketCounts"],"firstBucketOffset":1},"sumOfSquares":5.962133916683182,"min":{"highBits":0,"lowBits":6},"max":{"highBits":0,"lowBits":6},"count":{"highBits":0,"lowBits":6},"sum":{"highBits":0,"lowBits":6}},"floatingPointMean":{"count":{"highBits":0,"lowBits":6},"sum":7.061401241503109},"integerGauge":{"value":{"highBits":0,"lowBits":6},"timestamp":"timestamp"},"boolean":True,"stringList":{"elements":["elements","elements"]},"integerMean":{"count":{"highBits":0,"lowBits":6},"sum":{"highBits":0,"lowBits":6}},"structuredNameAndMetadata":{"metadata":{"kind":"INVALID","standardUnits":"BYTES","description":"description","otherUnits":"otherUnits"},"name":{"workerId":"workerId","componentStepName":"componentStepName","inputIndex":9,"origin":"SYSTEM","portion":"ALL","name":"name","originalRequestingStepName":"originalRequestingStepName","executionStepName":"executionStepName","originNamespace":"originNamespace","originalStepName":"originalStepName"}}}],"progress":{"percentComplete":2.302136,"position":{"concatPosition":{"index":5},"byteOffset":"byteOffset","end":True,"recordIndex":"recordIndex","key":"key","shufflePosition":"shufflePosition"},"remainingTime":"remainingTime"},"totalThrottlerWaitTimeSeconds":4.145608029883936,"requestedLeaseDuration":"requestedLeaseDuration","errors":[{"code":0,"details":[{"key":""},{"key":""}],"message":"message"},{"code":0,"details":[{"key":""},{"key":""}],"message":"message"}],"reportedProgress":{"remainingParallelism":{"isInfinite":True,"value":3.616076749251911},"position":{"concatPosition":{"index":5},"byteOffset":"byteOffset","end":True,"recordIndex":"recordIndex","key":"key","shufflePosition":"shufflePosition"},"fractionConsumed":2.027123023002322,"consumedParallelism":{"isInfinite":True,"value":3.616076749251911}}},{"metricUpdates":[{"gauge":"","internal":"","scalar":"","set":"","meanCount":"","kind":"kind","name":{"origin":"origin","context":{"key":"context"},"name":"name"},"updateTime":"updateTime","cumulative":True,"distribution":"","meanSum":""},{"gauge":"","internal":"","scalar":"","set":"","meanCount":"","kind":"kind","name":{"origin":"origin","context":{"key":"context"},"name":"name"},"updateTime":"updateTime","cumulative":True,"distribution":"","meanSum":""}],"sourceFork":{"primarySource":{"derivationMode":"SOURCE_DERIVATION_MODE_UNKNOWN","source":{"codec":{"key":""},"metadata":{"infinite":True,"estimatedSizeBytes":"estimatedSizeBytes","producesSortedKeys":True},"baseSpecs":[{"key":""},{"key":""}],"doesNotNeedSplitting":True,"spec":{"key":""}}},"residual":{"derivationMode":"SOURCE_DERIVATION_MODE_UNKNOWN","source":{"codec":{"key":""},"metadata":{"infinite":True,"estimatedSizeBytes":"estimatedSizeBytes","producesSortedKeys":True},"baseSpecs":[{"key":""},{"key":""}],"doesNotNeedSplitting":True,"spec":{"key":""}}},"primary":{"derivationMode":"SOURCE_DERIVATION_MODE_UNKNOWN","source":{"codec":{"key":""},"metadata":{"infinite":True,"estimatedSizeBytes":"estimatedSizeBytes","producesSortedKeys":True},"baseSpecs":[{"key":""},{"key":""}],"doesNotNeedSplitting":True,"spec":{"key":""}}},"residualSource":{"derivationMode":"SOURCE_DERIVATION_MODE_UNKNOWN","source":{"codec":{"key":""},"metadata":{"infinite":True,"estimatedSizeBytes":"estimatedSizeBytes","producesSortedKeys":True},"baseSpecs":[{"key":""},{"key":""}],"doesNotNeedSplitting":True,"spec":{"key":""}}}},"stopPosition":{"concatPosition":{"index":5},"byteOffset":"byteOffset","end":True,"recordIndex":"recordIndex","key":"key","shufflePosition":"shufflePosition"},"dynamicSourceSplit":{"residual":{"derivationMode":"SOURCE_DERIVATION_MODE_UNKNOWN","source":{"codec":{"key":""},"metadata":{"infinite":True,"estimatedSizeBytes":"estimatedSizeBytes","producesSortedKeys":True},"baseSpecs":[{"key":""},{"key":""}],"doesNotNeedSplitting":True,"spec":{"key":""}}},"primary":{"derivationMode":"SOURCE_DERIVATION_MODE_UNKNOWN","source":{"codec":{"key":""},"metadata":{"infinite":True,"estimatedSizeBytes":"estimatedSizeBytes","producesSortedKeys":True},"baseSpecs":[{"key":""},{"key":""}],"doesNotNeedSplitting":True,"spec":{"key":""}}}},"completed":True,"reportIndex":"reportIndex","workItemId":"workItemId","sourceOperationResponse":{"getMetadata":{"metadata":{"infinite":True,"estimatedSizeBytes":"estimatedSizeBytes","producesSortedKeys":True}},"split":{"shards":[{"derivationMode":"SOURCE_DERIVATION_MODE_UNKNOWN","source":{"codec":{"key":""},"metadata":{"infinite":True,"estimatedSizeBytes":"estimatedSizeBytes","producesSortedKeys":True},"baseSpecs":[{"key":""},{"key":""}],"doesNotNeedSplitting":True,"spec":{"key":""}}},{"derivationMode":"SOURCE_DERIVATION_MODE_UNKNOWN","source":{"codec":{"key":""},"metadata":{"infinite":True,"estimatedSizeBytes":"estimatedSizeBytes","producesSortedKeys":True},"baseSpecs":[{"key":""},{"key":""}],"doesNotNeedSplitting":True,"spec":{"key":""}}}],"bundles":[{"derivationMode":"SOURCE_DERIVATION_MODE_UNKNOWN","source":{"codec":{"key":""},"metadata":{"infinite":True,"estimatedSizeBytes":"estimatedSizeBytes","producesSortedKeys":True},"baseSpecs":[{"key":""},{"key":""}],"doesNotNeedSplitting":True,"spec":{"key":""}}},{"derivationMode":"SOURCE_DERIVATION_MODE_UNKNOWN","source":{"codec":{"key":""},"metadata":{"infinite":True,"estimatedSizeBytes":"estimatedSizeBytes","producesSortedKeys":True},"baseSpecs":[{"key":""},{"key":""}],"doesNotNeedSplitting":True,"spec":{"key":""}}}],"outcome":"SOURCE_SPLIT_OUTCOME_UNKNOWN"}},"counterUpdates":[{"nameAndKind":{"kind":"INVALID","name":"name"},"shortId":"shortId","internal":"","integerList":{"elements":[{"highBits":0,"lowBits":6},{"highBits":0,"lowBits":6}]},"floatingPoint":5.637376656633329,"floatingPointList":{"elements":[2.3021358869347655,2.3021358869347655]},"integer":{"highBits":0,"lowBits":6},"cumulative":True,"distribution":{"histogram":{"bucketCounts":["bucketCounts","bucketCounts"],"firstBucketOffset":1},"sumOfSquares":5.962133916683182,"min":{"highBits":0,"lowBits":6},"max":{"highBits":0,"lowBits":6},"count":{"highBits":0,"lowBits":6},"sum":{"highBits":0,"lowBits":6}},"floatingPointMean":{"count":{"highBits":0,"lowBits":6},"sum":7.061401241503109},"integerGauge":{"value":{"highBits":0,"lowBits":6},"timestamp":"timestamp"},"boolean":True,"stringList":{"elements":["elements","elements"]},"integerMean":{"count":{"highBits":0,"lowBits":6},"sum":{"highBits":0,"lowBits":6}},"structuredNameAndMetadata":{"metadata":{"kind":"INVALID","standardUnits":"BYTES","description":"description","otherUnits":"otherUnits"},"name":{"workerId":"workerId","componentStepName":"componentStepName","inputIndex":9,"origin":"SYSTEM","portion":"ALL","name":"name","originalRequestingStepName":"originalRequestingStepName","executionStepName":"executionStepName","originNamespace":"originNamespace","originalStepName":"originalStepName"}}},{"nameAndKind":{"kind":"INVALID","name":"name"},"shortId":"shortId","internal":"","integerList":{"elements":[{"highBits":0,"lowBits":6},{"highBits":0,"lowBits":6}]},"floatingPoint":5.637376656633329,"floatingPointList":{"elements":[2.3021358869347655,2.3021358869347655]},"integer":{"highBits":0,"lowBits":6},"cumulative":True,"distribution":{"histogram":{"bucketCounts":["bucketCounts","bucketCounts"],"firstBucketOffset":1},"sumOfSquares":5.962133916683182,"min":{"highBits":0,"lowBits":6},"max":{"highBits":0,"lowBits":6},"count":{"highBits":0,"lowBits":6},"sum":{"highBits":0,"lowBits":6}},"floatingPointMean":{"count":{"highBits":0,"lowBits":6},"sum":7.061401241503109},"integerGauge":{"value":{"highBits":0,"lowBits":6},"timestamp":"timestamp"},"boolean":True,"stringList":{"elements":["elements","elements"]},"integerMean":{"count":{"highBits":0,"lowBits":6},"sum":{"highBits":0,"lowBits":6}},"structuredNameAndMetadata":{"metadata":{"kind":"INVALID","standardUnits":"BYTES","description":"description","otherUnits":"otherUnits"},"name":{"workerId":"workerId","componentStepName":"componentStepName","inputIndex":9,"origin":"SYSTEM","portion":"ALL","name":"name","originalRequestingStepName":"originalRequestingStepName","executionStepName":"executionStepName","originNamespace":"originNamespace","originalStepName":"originalStepName"}}}],"progress":{"percentComplete":2.302136,"position":{"concatPosition":{"index":5},"byteOffset":"byteOffset","end":True,"recordIndex":"recordIndex","key":"key","shufflePosition":"shufflePosition"},"remainingTime":"remainingTime"},"totalThrottlerWaitTimeSeconds":4.145608029883936,"requestedLeaseDuration":"requestedLeaseDuration","errors":[{"code":0,"details":[{"key":""},{"key":""}],"message":"message"},{"code":0,"details":[{"key":""},{"key":""}],"message":"message"}],"reportedProgress":{"remainingParallelism":{"isInfinite":True,"value":3.616076749251911},"position":{"concatPosition":{"index":5},"byteOffset":"byteOffset","end":True,"recordIndex":"recordIndex","key":"key","shufflePosition":"shufflePosition"},"fractionConsumed":2.027123023002322,"consumedParallelism":{"isInfinite":True,"value":3.616076749251911}}}],"location":"location"}
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
        path='/v1b3/projects/{project_id}/jobs/{job_id}/workItems:reportStatus'.format(project_id='project_id_example', job_id='job_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataflow_projects_locations_flex_templates_launch(client):
    """Test case for dataflow_projects_locations_flex_templates_launch

    
    """
    body = {"validateOnly":True,"launchParameter":{"containerSpec":{"imageRepositoryPasswordSecretId":"imageRepositoryPasswordSecretId","image":"image","imageRepositoryCertPath":"imageRepositoryCertPath","defaultEnvironment":{"launcherMachineType":"launcherMachineType","workerRegion":"workerRegion","enableLauncherVmSerialPortLogging":True,"streamingMode":"STREAMING_MODE_UNSPECIFIED","flexrsGoal":"FLEXRS_UNSPECIFIED","network":"network","dumpHeapOnOom":True,"workerZone":"workerZone","maxWorkers":6,"serviceAccountEmail":"serviceAccountEmail","zone":"zone","ipConfiguration":"WORKER_IP_UNSPECIFIED","numWorkers":1,"machineType":"machineType","autoscalingAlgorithm":"AUTOSCALING_ALGORITHM_UNKNOWN","additionalUserLabels":{"key":"additionalUserLabels"},"stagingLocation":"stagingLocation","kmsKeyName":"kmsKeyName","additionalExperiments":["additionalExperiments","additionalExperiments"],"enableStreamingEngine":True,"tempLocation":"tempLocation","saveHeapDumpsToGcsPath":"saveHeapDumpsToGcsPath","subnetwork":"subnetwork","sdkContainerImage":"sdkContainerImage","diskSizeGb":0},"metadata":{"streaming":True,"supportsExactlyOnce":True,"name":"name","description":"description","parameters":[{"helpText":"helpText","hiddenUi":True,"defaultValue":"defaultValue","isOptional":True,"label":"label","regexes":["regexes","regexes"],"paramType":"DEFAULT","enumOptions":[{"description":"description","label":"label","value":"value"},{"description":"description","label":"label","value":"value"}],"groupName":"groupName","parentName":"parentName","customMetadata":{"key":"customMetadata"},"name":"name","parentTriggerValues":["parentTriggerValues","parentTriggerValues"]},{"helpText":"helpText","hiddenUi":True,"defaultValue":"defaultValue","isOptional":True,"label":"label","regexes":["regexes","regexes"],"paramType":"DEFAULT","enumOptions":[{"description":"description","label":"label","value":"value"},{"description":"description","label":"label","value":"value"}],"groupName":"groupName","parentName":"parentName","customMetadata":{"key":"customMetadata"},"name":"name","parentTriggerValues":["parentTriggerValues","parentTriggerValues"]}],"supportsAtLeastOnce":True},"imageRepositoryUsernameSecretId":"imageRepositoryUsernameSecretId","sdkInfo":{"language":"UNKNOWN","version":"version"}},"jobName":"jobName","launchOptions":{"key":"launchOptions"},"environment":{"launcherMachineType":"launcherMachineType","workerRegion":"workerRegion","enableLauncherVmSerialPortLogging":True,"streamingMode":"STREAMING_MODE_UNSPECIFIED","flexrsGoal":"FLEXRS_UNSPECIFIED","network":"network","dumpHeapOnOom":True,"workerZone":"workerZone","maxWorkers":6,"serviceAccountEmail":"serviceAccountEmail","zone":"zone","ipConfiguration":"WORKER_IP_UNSPECIFIED","numWorkers":1,"machineType":"machineType","autoscalingAlgorithm":"AUTOSCALING_ALGORITHM_UNKNOWN","additionalUserLabels":{"key":"additionalUserLabels"},"stagingLocation":"stagingLocation","kmsKeyName":"kmsKeyName","additionalExperiments":["additionalExperiments","additionalExperiments"],"enableStreamingEngine":True,"tempLocation":"tempLocation","saveHeapDumpsToGcsPath":"saveHeapDumpsToGcsPath","subnetwork":"subnetwork","sdkContainerImage":"sdkContainerImage","diskSizeGb":0},"transformNameMappings":{"key":"transformNameMappings"},"update":True,"containerSpecGcsPath":"containerSpecGcsPath","parameters":{"key":"parameters"}}}
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
        path='/v1b3/projects/{project_id}/locations/{location}/flexTemplates:launch'.format(project_id='project_id_example', location='location_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataflow_projects_locations_jobs_create(client):
    """Test case for dataflow_projects_locations_jobs_create

    
    """
    body = {"transformNameMapping":{"key":"transformNameMapping"},"currentStateTime":"currentStateTime","jobMetadata":{"bigTableDetails":[{"instanceId":"instanceId","tableId":"tableId","projectId":"projectId"},{"instanceId":"instanceId","tableId":"tableId","projectId":"projectId"}],"datastoreDetails":[{"namespace":"namespace","projectId":"projectId"},{"namespace":"namespace","projectId":"projectId"}],"fileDetails":[{"filePattern":"filePattern"},{"filePattern":"filePattern"}],"pubsubDetails":[{"topic":"topic","subscription":"subscription"},{"topic":"topic","subscription":"subscription"}],"bigqueryDetails":[{"query":"query","dataset":"dataset","projectId":"projectId","table":"table"},{"query":"query","dataset":"dataset","projectId":"projectId","table":"table"}],"sdkVersion":{"bugs":[{"severity":"SEVERITY_UNSPECIFIED","type":"TYPE_UNSPECIFIED","uri":"uri"},{"severity":"SEVERITY_UNSPECIFIED","type":"TYPE_UNSPECIFIED","uri":"uri"}],"sdkSupportStatus":"UNKNOWN","version":"version","versionDisplayName":"versionDisplayName"},"userDisplayProperties":{"key":"userDisplayProperties"},"spannerDetails":[{"instanceId":"instanceId","databaseId":"databaseId","projectId":"projectId"},{"instanceId":"instanceId","databaseId":"databaseId","projectId":"projectId"}]},"tempFiles":["tempFiles","tempFiles"],"satisfiesPzs":True,"replacedByJobId":"replacedByJobId","type":"JOB_TYPE_UNKNOWN","createdFromSnapshotId":"createdFromSnapshotId","executionInfo":{"stages":{"key":{"stepName":["stepName","stepName"]}}},"startTime":"startTime","id":"id","stepsLocation":"stepsLocation","requestedState":"JOB_STATE_UNKNOWN","clientRequestId":"clientRequestId","steps":[{"kind":"kind","name":"name","properties":{"key":""}},{"kind":"kind","name":"name","properties":{"key":""}}],"labels":{"key":"labels"},"runtimeUpdatableParams":{"minNumWorkers":9,"maxNumWorkers":7,"workerUtilizationHint":3.616076749251911},"environment":{"workerRegion":"workerRegion","experiments":["experiments","experiments"],"sdkPipelineOptions":{"key":""},"streamingMode":"STREAMING_MODE_UNSPECIFIED","userAgent":{"key":""},"flexResourceSchedulingGoal":"FLEXRS_UNSPECIFIED","serviceOptions":["serviceOptions","serviceOptions"],"version":{"key":""},"serviceKmsKeyName":"serviceKmsKeyName","workerPools":[{"metadata":{"key":"metadata"},"onHostMaintenance":"onHostMaintenance","kind":"kind","poolArgs":{"key":""},"packages":[{"name":"name","location":"location"},{"name":"name","location":"location"}],"diskSourceImage":"diskSourceImage","numThreadsPerWorker":5,"workerHarnessContainerImage":"workerHarnessContainerImage","network":"network","zone":"zone","ipConfiguration":"WORKER_IP_UNSPECIFIED","teardownPolicy":"TEARDOWN_POLICY_UNKNOWN","sdkHarnessContainerImages":[{"useSingleCorePerContainer":True,"capabilities":["capabilities","capabilities"],"environmentId":"environmentId","containerImage":"containerImage"},{"useSingleCorePerContainer":True,"capabilities":["capabilities","capabilities"],"environmentId":"environmentId","containerImage":"containerImage"}],"subnetwork":"subnetwork","numWorkers":5,"autoscalingSettings":{"maxNumWorkers":0,"algorithm":"AUTOSCALING_ALGORITHM_UNKNOWN"},"dataDisks":[{"sizeGb":6,"mountPoint":"mountPoint","diskType":"diskType"},{"sizeGb":6,"mountPoint":"mountPoint","diskType":"diskType"}],"diskType":"diskType","taskrunnerSettings":{"logUploadLocation":"logUploadLocation","alsologtostderr":True,"vmId":"vmId","workflowFileName":"workflowFileName","harnessCommand":"harnessCommand","continueOnException":True,"oauthScopes":["oauthScopes","oauthScopes"],"commandlinesFileName":"commandlinesFileName","taskGroup":"taskGroup","baseUrl":"baseUrl","parallelWorkerSettings":{"reportingEnabled":True,"baseUrl":"baseUrl","shuffleServicePath":"shuffleServicePath","workerId":"workerId","servicePath":"servicePath","tempStoragePrefix":"tempStoragePrefix"},"languageHint":"languageHint","dataflowApiVersion":"dataflowApiVersion","baseTaskDir":"baseTaskDir","streamingWorkerMainClass":"streamingWorkerMainClass","logToSerialconsole":True,"logDir":"logDir","taskUser":"taskUser","tempStoragePrefix":"tempStoragePrefix"},"machineType":"machineType","defaultPackageSet":"DEFAULT_PACKAGE_SET_UNKNOWN","diskSizeGb":1},{"metadata":{"key":"metadata"},"onHostMaintenance":"onHostMaintenance","kind":"kind","poolArgs":{"key":""},"packages":[{"name":"name","location":"location"},{"name":"name","location":"location"}],"diskSourceImage":"diskSourceImage","numThreadsPerWorker":5,"workerHarnessContainerImage":"workerHarnessContainerImage","network":"network","zone":"zone","ipConfiguration":"WORKER_IP_UNSPECIFIED","teardownPolicy":"TEARDOWN_POLICY_UNKNOWN","sdkHarnessContainerImages":[{"useSingleCorePerContainer":True,"capabilities":["capabilities","capabilities"],"environmentId":"environmentId","containerImage":"containerImage"},{"useSingleCorePerContainer":True,"capabilities":["capabilities","capabilities"],"environmentId":"environmentId","containerImage":"containerImage"}],"subnetwork":"subnetwork","numWorkers":5,"autoscalingSettings":{"maxNumWorkers":0,"algorithm":"AUTOSCALING_ALGORITHM_UNKNOWN"},"dataDisks":[{"sizeGb":6,"mountPoint":"mountPoint","diskType":"diskType"},{"sizeGb":6,"mountPoint":"mountPoint","diskType":"diskType"}],"diskType":"diskType","taskrunnerSettings":{"logUploadLocation":"logUploadLocation","alsologtostderr":True,"vmId":"vmId","workflowFileName":"workflowFileName","harnessCommand":"harnessCommand","continueOnException":True,"oauthScopes":["oauthScopes","oauthScopes"],"commandlinesFileName":"commandlinesFileName","taskGroup":"taskGroup","baseUrl":"baseUrl","parallelWorkerSettings":{"reportingEnabled":True,"baseUrl":"baseUrl","shuffleServicePath":"shuffleServicePath","workerId":"workerId","servicePath":"servicePath","tempStoragePrefix":"tempStoragePrefix"},"languageHint":"languageHint","dataflowApiVersion":"dataflowApiVersion","baseTaskDir":"baseTaskDir","streamingWorkerMainClass":"streamingWorkerMainClass","logToSerialconsole":True,"logDir":"logDir","taskUser":"taskUser","tempStoragePrefix":"tempStoragePrefix"},"machineType":"machineType","defaultPackageSet":"DEFAULT_PACKAGE_SET_UNKNOWN","diskSizeGb":1}],"clusterManagerApiService":"clusterManagerApiService","debugOptions":{"enableHotKeyLogging":True,"dataSampling":{"behaviors":["DATA_SAMPLING_BEHAVIOR_UNSPECIFIED","DATA_SAMPLING_BEHAVIOR_UNSPECIFIED"]}},"workerZone":"workerZone","serviceAccountEmail":"serviceAccountEmail","internalExperiments":{"key":""},"shuffleMode":"SHUFFLE_MODE_UNSPECIFIED","dataset":"dataset","useStreamingEngineResourceBasedBilling":True,"tempStoragePrefix":"tempStoragePrefix"},"pipelineDescription":{"stepNamesHash":"stepNamesHash","displayData":[{"int64Value":"int64Value","shortStrValue":"shortStrValue","durationValue":"durationValue","timestampValue":"timestampValue","namespace":"namespace","floatValue":2.302136,"boolValue":True,"javaClassValue":"javaClassValue","label":"label","strValue":"strValue","key":"key","url":"url"},{"int64Value":"int64Value","shortStrValue":"shortStrValue","durationValue":"durationValue","timestampValue":"timestampValue","namespace":"namespace","floatValue":2.302136,"boolValue":True,"javaClassValue":"javaClassValue","label":"label","strValue":"strValue","key":"key","url":"url"}],"originalPipelineTransform":[{"outputCollectionName":["outputCollectionName","outputCollectionName"],"inputCollectionName":["inputCollectionName","inputCollectionName"],"kind":"UNKNOWN_KIND","name":"name","displayData":[{"int64Value":"int64Value","shortStrValue":"shortStrValue","durationValue":"durationValue","timestampValue":"timestampValue","namespace":"namespace","floatValue":2.302136,"boolValue":True,"javaClassValue":"javaClassValue","label":"label","strValue":"strValue","key":"key","url":"url"},{"int64Value":"int64Value","shortStrValue":"shortStrValue","durationValue":"durationValue","timestampValue":"timestampValue","namespace":"namespace","floatValue":2.302136,"boolValue":True,"javaClassValue":"javaClassValue","label":"label","strValue":"strValue","key":"key","url":"url"}],"id":"id"},{"outputCollectionName":["outputCollectionName","outputCollectionName"],"inputCollectionName":["inputCollectionName","inputCollectionName"],"kind":"UNKNOWN_KIND","name":"name","displayData":[{"int64Value":"int64Value","shortStrValue":"shortStrValue","durationValue":"durationValue","timestampValue":"timestampValue","namespace":"namespace","floatValue":2.302136,"boolValue":True,"javaClassValue":"javaClassValue","label":"label","strValue":"strValue","key":"key","url":"url"},{"int64Value":"int64Value","shortStrValue":"shortStrValue","durationValue":"durationValue","timestampValue":"timestampValue","namespace":"namespace","floatValue":2.302136,"boolValue":True,"javaClassValue":"javaClassValue","label":"label","strValue":"strValue","key":"key","url":"url"}],"id":"id"}],"executionPipelineStage":[{"prerequisiteStage":["prerequisiteStage","prerequisiteStage"],"kind":"UNKNOWN_KIND","name":"name","outputSource":[{"originalTransformOrCollection":"originalTransformOrCollection","name":"name","userName":"userName","sizeBytes":"sizeBytes"},{"originalTransformOrCollection":"originalTransformOrCollection","name":"name","userName":"userName","sizeBytes":"sizeBytes"}],"componentTransform":[{"originalTransform":"originalTransform","name":"name","userName":"userName"},{"originalTransform":"originalTransform","name":"name","userName":"userName"}],"id":"id","inputSource":[{"originalTransformOrCollection":"originalTransformOrCollection","name":"name","userName":"userName","sizeBytes":"sizeBytes"},{"originalTransformOrCollection":"originalTransformOrCollection","name":"name","userName":"userName","sizeBytes":"sizeBytes"}],"componentSource":[{"originalTransformOrCollection":"originalTransformOrCollection","name":"name","userName":"userName"},{"originalTransformOrCollection":"originalTransformOrCollection","name":"name","userName":"userName"}]},{"prerequisiteStage":["prerequisiteStage","prerequisiteStage"],"kind":"UNKNOWN_KIND","name":"name","outputSource":[{"originalTransformOrCollection":"originalTransformOrCollection","name":"name","userName":"userName","sizeBytes":"sizeBytes"},{"originalTransformOrCollection":"originalTransformOrCollection","name":"name","userName":"userName","sizeBytes":"sizeBytes"}],"componentTransform":[{"originalTransform":"originalTransform","name":"name","userName":"userName"},{"originalTransform":"originalTransform","name":"name","userName":"userName"}],"id":"id","inputSource":[{"originalTransformOrCollection":"originalTransformOrCollection","name":"name","userName":"userName","sizeBytes":"sizeBytes"},{"originalTransformOrCollection":"originalTransformOrCollection","name":"name","userName":"userName","sizeBytes":"sizeBytes"}],"componentSource":[{"originalTransformOrCollection":"originalTransformOrCollection","name":"name","userName":"userName"},{"originalTransformOrCollection":"originalTransformOrCollection","name":"name","userName":"userName"}]}]},"stageStates":[{"executionStageName":"executionStageName","executionStageState":"JOB_STATE_UNKNOWN","currentStateTime":"currentStateTime"},{"executionStageName":"executionStageName","executionStageState":"JOB_STATE_UNKNOWN","currentStateTime":"currentStateTime"}],"createTime":"createTime","replaceJobId":"replaceJobId","name":"name","location":"location","currentState":"JOB_STATE_UNKNOWN","satisfiesPzi":True,"projectId":"projectId"}
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
                    ('replaceJobId', 'replace_job_id_example'),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1b3/projects/{project_id}/locations/{location}/jobs'.format(project_id='project_id_example', location='location_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataflow_projects_locations_jobs_debug_get_config(client):
    """Test case for dataflow_projects_locations_jobs_debug_get_config

    
    """
    body = {"workerId":"workerId","componentId":"componentId","location":"location"}
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
        path='/v1b3/projects/{project_id}/locations/{location}/jobs/{job_id}/debug/getConfig'.format(project_id='project_id_example', location='location_example', job_id='job_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataflow_projects_locations_jobs_debug_send_capture(client):
    """Test case for dataflow_projects_locations_jobs_debug_send_capture

    
    """
    body = {"workerId":"workerId","componentId":"componentId","data":"data","dataFormat":"DATA_FORMAT_UNSPECIFIED","location":"location"}
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
        path='/v1b3/projects/{project_id}/locations/{location}/jobs/{job_id}/debug/sendCapture'.format(project_id='project_id_example', location='location_example', job_id='job_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataflow_projects_locations_jobs_get(client):
    """Test case for dataflow_projects_locations_jobs_get

    
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
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1b3/projects/{project_id}/locations/{location}/jobs/{job_id}'.format(project_id='project_id_example', location='location_example', job_id='job_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataflow_projects_locations_jobs_get_execution_details(client):
    """Test case for dataflow_projects_locations_jobs_get_execution_details

    
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
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1b3/projects/{project_id}/locations/{location}/jobs/{job_id}/executionDetails'.format(project_id='project_id_example', location='location_example', job_id='job_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataflow_projects_locations_jobs_get_metrics(client):
    """Test case for dataflow_projects_locations_jobs_get_metrics

    
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
                    ('startTime', 'start_time_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1b3/projects/{project_id}/locations/{location}/jobs/{job_id}/metrics'.format(project_id='project_id_example', location='location_example', job_id='job_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataflow_projects_locations_jobs_list(client):
    """Test case for dataflow_projects_locations_jobs_list

    
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
                    ('name', 'name_example'),
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
        path='/v1b3/projects/{project_id}/locations/{location}/jobs'.format(project_id='project_id_example', location='location_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataflow_projects_locations_jobs_messages_list(client):
    """Test case for dataflow_projects_locations_jobs_messages_list

    
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
                    ('endTime', 'end_time_example'),
                    ('minimumImportance', 'minimum_importance_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('startTime', 'start_time_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1b3/projects/{project_id}/locations/{location}/jobs/{job_id}/messages'.format(project_id='project_id_example', location='location_example', job_id='job_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataflow_projects_locations_jobs_snapshot(client):
    """Test case for dataflow_projects_locations_jobs_snapshot

    
    """
    body = {"snapshotSources":True,"description":"description","location":"location","ttl":"ttl"}
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
        path='/v1b3/projects/{project_id}/locations/{location}/jobs/{job_idsnapsho}'.format(project_id='project_id_example', location='location_example', job_id='job_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataflow_projects_locations_jobs_snapshots_list(client):
    """Test case for dataflow_projects_locations_jobs_snapshots_list

    
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
        path='/v1b3/projects/{project_id}/locations/{location}/jobs/{job_id}/snapshots'.format(project_id='project_id_example', location='location_example', job_id='job_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataflow_projects_locations_jobs_stages_get_execution_details(client):
    """Test case for dataflow_projects_locations_jobs_stages_get_execution_details

    
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
                    ('endTime', 'end_time_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('startTime', 'start_time_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1b3/projects/{project_id}/locations/{location}/jobs/{job_id}/stages/{stage_id}/executionDetails'.format(project_id='project_id_example', location='location_example', job_id='job_id_example', stage_id='stage_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataflow_projects_locations_jobs_update(client):
    """Test case for dataflow_projects_locations_jobs_update

    
    """
    body = {"transformNameMapping":{"key":"transformNameMapping"},"currentStateTime":"currentStateTime","jobMetadata":{"bigTableDetails":[{"instanceId":"instanceId","tableId":"tableId","projectId":"projectId"},{"instanceId":"instanceId","tableId":"tableId","projectId":"projectId"}],"datastoreDetails":[{"namespace":"namespace","projectId":"projectId"},{"namespace":"namespace","projectId":"projectId"}],"fileDetails":[{"filePattern":"filePattern"},{"filePattern":"filePattern"}],"pubsubDetails":[{"topic":"topic","subscription":"subscription"},{"topic":"topic","subscription":"subscription"}],"bigqueryDetails":[{"query":"query","dataset":"dataset","projectId":"projectId","table":"table"},{"query":"query","dataset":"dataset","projectId":"projectId","table":"table"}],"sdkVersion":{"bugs":[{"severity":"SEVERITY_UNSPECIFIED","type":"TYPE_UNSPECIFIED","uri":"uri"},{"severity":"SEVERITY_UNSPECIFIED","type":"TYPE_UNSPECIFIED","uri":"uri"}],"sdkSupportStatus":"UNKNOWN","version":"version","versionDisplayName":"versionDisplayName"},"userDisplayProperties":{"key":"userDisplayProperties"},"spannerDetails":[{"instanceId":"instanceId","databaseId":"databaseId","projectId":"projectId"},{"instanceId":"instanceId","databaseId":"databaseId","projectId":"projectId"}]},"tempFiles":["tempFiles","tempFiles"],"satisfiesPzs":True,"replacedByJobId":"replacedByJobId","type":"JOB_TYPE_UNKNOWN","createdFromSnapshotId":"createdFromSnapshotId","executionInfo":{"stages":{"key":{"stepName":["stepName","stepName"]}}},"startTime":"startTime","id":"id","stepsLocation":"stepsLocation","requestedState":"JOB_STATE_UNKNOWN","clientRequestId":"clientRequestId","steps":[{"kind":"kind","name":"name","properties":{"key":""}},{"kind":"kind","name":"name","properties":{"key":""}}],"labels":{"key":"labels"},"runtimeUpdatableParams":{"minNumWorkers":9,"maxNumWorkers":7,"workerUtilizationHint":3.616076749251911},"environment":{"workerRegion":"workerRegion","experiments":["experiments","experiments"],"sdkPipelineOptions":{"key":""},"streamingMode":"STREAMING_MODE_UNSPECIFIED","userAgent":{"key":""},"flexResourceSchedulingGoal":"FLEXRS_UNSPECIFIED","serviceOptions":["serviceOptions","serviceOptions"],"version":{"key":""},"serviceKmsKeyName":"serviceKmsKeyName","workerPools":[{"metadata":{"key":"metadata"},"onHostMaintenance":"onHostMaintenance","kind":"kind","poolArgs":{"key":""},"packages":[{"name":"name","location":"location"},{"name":"name","location":"location"}],"diskSourceImage":"diskSourceImage","numThreadsPerWorker":5,"workerHarnessContainerImage":"workerHarnessContainerImage","network":"network","zone":"zone","ipConfiguration":"WORKER_IP_UNSPECIFIED","teardownPolicy":"TEARDOWN_POLICY_UNKNOWN","sdkHarnessContainerImages":[{"useSingleCorePerContainer":True,"capabilities":["capabilities","capabilities"],"environmentId":"environmentId","containerImage":"containerImage"},{"useSingleCorePerContainer":True,"capabilities":["capabilities","capabilities"],"environmentId":"environmentId","containerImage":"containerImage"}],"subnetwork":"subnetwork","numWorkers":5,"autoscalingSettings":{"maxNumWorkers":0,"algorithm":"AUTOSCALING_ALGORITHM_UNKNOWN"},"dataDisks":[{"sizeGb":6,"mountPoint":"mountPoint","diskType":"diskType"},{"sizeGb":6,"mountPoint":"mountPoint","diskType":"diskType"}],"diskType":"diskType","taskrunnerSettings":{"logUploadLocation":"logUploadLocation","alsologtostderr":True,"vmId":"vmId","workflowFileName":"workflowFileName","harnessCommand":"harnessCommand","continueOnException":True,"oauthScopes":["oauthScopes","oauthScopes"],"commandlinesFileName":"commandlinesFileName","taskGroup":"taskGroup","baseUrl":"baseUrl","parallelWorkerSettings":{"reportingEnabled":True,"baseUrl":"baseUrl","shuffleServicePath":"shuffleServicePath","workerId":"workerId","servicePath":"servicePath","tempStoragePrefix":"tempStoragePrefix"},"languageHint":"languageHint","dataflowApiVersion":"dataflowApiVersion","baseTaskDir":"baseTaskDir","streamingWorkerMainClass":"streamingWorkerMainClass","logToSerialconsole":True,"logDir":"logDir","taskUser":"taskUser","tempStoragePrefix":"tempStoragePrefix"},"machineType":"machineType","defaultPackageSet":"DEFAULT_PACKAGE_SET_UNKNOWN","diskSizeGb":1},{"metadata":{"key":"metadata"},"onHostMaintenance":"onHostMaintenance","kind":"kind","poolArgs":{"key":""},"packages":[{"name":"name","location":"location"},{"name":"name","location":"location"}],"diskSourceImage":"diskSourceImage","numThreadsPerWorker":5,"workerHarnessContainerImage":"workerHarnessContainerImage","network":"network","zone":"zone","ipConfiguration":"WORKER_IP_UNSPECIFIED","teardownPolicy":"TEARDOWN_POLICY_UNKNOWN","sdkHarnessContainerImages":[{"useSingleCorePerContainer":True,"capabilities":["capabilities","capabilities"],"environmentId":"environmentId","containerImage":"containerImage"},{"useSingleCorePerContainer":True,"capabilities":["capabilities","capabilities"],"environmentId":"environmentId","containerImage":"containerImage"}],"subnetwork":"subnetwork","numWorkers":5,"autoscalingSettings":{"maxNumWorkers":0,"algorithm":"AUTOSCALING_ALGORITHM_UNKNOWN"},"dataDisks":[{"sizeGb":6,"mountPoint":"mountPoint","diskType":"diskType"},{"sizeGb":6,"mountPoint":"mountPoint","diskType":"diskType"}],"diskType":"diskType","taskrunnerSettings":{"logUploadLocation":"logUploadLocation","alsologtostderr":True,"vmId":"vmId","workflowFileName":"workflowFileName","harnessCommand":"harnessCommand","continueOnException":True,"oauthScopes":["oauthScopes","oauthScopes"],"commandlinesFileName":"commandlinesFileName","taskGroup":"taskGroup","baseUrl":"baseUrl","parallelWorkerSettings":{"reportingEnabled":True,"baseUrl":"baseUrl","shuffleServicePath":"shuffleServicePath","workerId":"workerId","servicePath":"servicePath","tempStoragePrefix":"tempStoragePrefix"},"languageHint":"languageHint","dataflowApiVersion":"dataflowApiVersion","baseTaskDir":"baseTaskDir","streamingWorkerMainClass":"streamingWorkerMainClass","logToSerialconsole":True,"logDir":"logDir","taskUser":"taskUser","tempStoragePrefix":"tempStoragePrefix"},"machineType":"machineType","defaultPackageSet":"DEFAULT_PACKAGE_SET_UNKNOWN","diskSizeGb":1}],"clusterManagerApiService":"clusterManagerApiService","debugOptions":{"enableHotKeyLogging":True,"dataSampling":{"behaviors":["DATA_SAMPLING_BEHAVIOR_UNSPECIFIED","DATA_SAMPLING_BEHAVIOR_UNSPECIFIED"]}},"workerZone":"workerZone","serviceAccountEmail":"serviceAccountEmail","internalExperiments":{"key":""},"shuffleMode":"SHUFFLE_MODE_UNSPECIFIED","dataset":"dataset","useStreamingEngineResourceBasedBilling":True,"tempStoragePrefix":"tempStoragePrefix"},"pipelineDescription":{"stepNamesHash":"stepNamesHash","displayData":[{"int64Value":"int64Value","shortStrValue":"shortStrValue","durationValue":"durationValue","timestampValue":"timestampValue","namespace":"namespace","floatValue":2.302136,"boolValue":True,"javaClassValue":"javaClassValue","label":"label","strValue":"strValue","key":"key","url":"url"},{"int64Value":"int64Value","shortStrValue":"shortStrValue","durationValue":"durationValue","timestampValue":"timestampValue","namespace":"namespace","floatValue":2.302136,"boolValue":True,"javaClassValue":"javaClassValue","label":"label","strValue":"strValue","key":"key","url":"url"}],"originalPipelineTransform":[{"outputCollectionName":["outputCollectionName","outputCollectionName"],"inputCollectionName":["inputCollectionName","inputCollectionName"],"kind":"UNKNOWN_KIND","name":"name","displayData":[{"int64Value":"int64Value","shortStrValue":"shortStrValue","durationValue":"durationValue","timestampValue":"timestampValue","namespace":"namespace","floatValue":2.302136,"boolValue":True,"javaClassValue":"javaClassValue","label":"label","strValue":"strValue","key":"key","url":"url"},{"int64Value":"int64Value","shortStrValue":"shortStrValue","durationValue":"durationValue","timestampValue":"timestampValue","namespace":"namespace","floatValue":2.302136,"boolValue":True,"javaClassValue":"javaClassValue","label":"label","strValue":"strValue","key":"key","url":"url"}],"id":"id"},{"outputCollectionName":["outputCollectionName","outputCollectionName"],"inputCollectionName":["inputCollectionName","inputCollectionName"],"kind":"UNKNOWN_KIND","name":"name","displayData":[{"int64Value":"int64Value","shortStrValue":"shortStrValue","durationValue":"durationValue","timestampValue":"timestampValue","namespace":"namespace","floatValue":2.302136,"boolValue":True,"javaClassValue":"javaClassValue","label":"label","strValue":"strValue","key":"key","url":"url"},{"int64Value":"int64Value","shortStrValue":"shortStrValue","durationValue":"durationValue","timestampValue":"timestampValue","namespace":"namespace","floatValue":2.302136,"boolValue":True,"javaClassValue":"javaClassValue","label":"label","strValue":"strValue","key":"key","url":"url"}],"id":"id"}],"executionPipelineStage":[{"prerequisiteStage":["prerequisiteStage","prerequisiteStage"],"kind":"UNKNOWN_KIND","name":"name","outputSource":[{"originalTransformOrCollection":"originalTransformOrCollection","name":"name","userName":"userName","sizeBytes":"sizeBytes"},{"originalTransformOrCollection":"originalTransformOrCollection","name":"name","userName":"userName","sizeBytes":"sizeBytes"}],"componentTransform":[{"originalTransform":"originalTransform","name":"name","userName":"userName"},{"originalTransform":"originalTransform","name":"name","userName":"userName"}],"id":"id","inputSource":[{"originalTransformOrCollection":"originalTransformOrCollection","name":"name","userName":"userName","sizeBytes":"sizeBytes"},{"originalTransformOrCollection":"originalTransformOrCollection","name":"name","userName":"userName","sizeBytes":"sizeBytes"}],"componentSource":[{"originalTransformOrCollection":"originalTransformOrCollection","name":"name","userName":"userName"},{"originalTransformOrCollection":"originalTransformOrCollection","name":"name","userName":"userName"}]},{"prerequisiteStage":["prerequisiteStage","prerequisiteStage"],"kind":"UNKNOWN_KIND","name":"name","outputSource":[{"originalTransformOrCollection":"originalTransformOrCollection","name":"name","userName":"userName","sizeBytes":"sizeBytes"},{"originalTransformOrCollection":"originalTransformOrCollection","name":"name","userName":"userName","sizeBytes":"sizeBytes"}],"componentTransform":[{"originalTransform":"originalTransform","name":"name","userName":"userName"},{"originalTransform":"originalTransform","name":"name","userName":"userName"}],"id":"id","inputSource":[{"originalTransformOrCollection":"originalTransformOrCollection","name":"name","userName":"userName","sizeBytes":"sizeBytes"},{"originalTransformOrCollection":"originalTransformOrCollection","name":"name","userName":"userName","sizeBytes":"sizeBytes"}],"componentSource":[{"originalTransformOrCollection":"originalTransformOrCollection","name":"name","userName":"userName"},{"originalTransformOrCollection":"originalTransformOrCollection","name":"name","userName":"userName"}]}]},"stageStates":[{"executionStageName":"executionStageName","executionStageState":"JOB_STATE_UNKNOWN","currentStateTime":"currentStateTime"},{"executionStageName":"executionStageName","executionStageState":"JOB_STATE_UNKNOWN","currentStateTime":"currentStateTime"}],"createTime":"createTime","replaceJobId":"replaceJobId","name":"name","location":"location","currentState":"JOB_STATE_UNKNOWN","satisfiesPzi":True,"projectId":"projectId"}
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
        path='/v1b3/projects/{project_id}/locations/{location}/jobs/{job_id}'.format(project_id='project_id_example', location='location_example', job_id='job_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataflow_projects_locations_jobs_work_items_lease(client):
    """Test case for dataflow_projects_locations_jobs_work_items_lease

    
    """
    body = {"currentWorkerTime":"currentWorkerTime","unifiedWorkerRequest":{"key":""},"workerId":"workerId","workItemTypes":["workItemTypes","workItemTypes"],"location":"location","requestedLeaseDuration":"requestedLeaseDuration","workerCapabilities":["workerCapabilities","workerCapabilities"]}
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
        path='/v1b3/projects/{project_id}/locations/{location}/jobs/{job_id}/workItems:lease'.format(project_id='project_id_example', location='location_example', job_id='job_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataflow_projects_locations_jobs_work_items_report_status(client):
    """Test case for dataflow_projects_locations_jobs_work_items_report_status

    
    """
    body = {"currentWorkerTime":"currentWorkerTime","unifiedWorkerRequest":{"key":""},"workerId":"workerId","workItemStatuses":[{"metricUpdates":[{"gauge":"","internal":"","scalar":"","set":"","meanCount":"","kind":"kind","name":{"origin":"origin","context":{"key":"context"},"name":"name"},"updateTime":"updateTime","cumulative":True,"distribution":"","meanSum":""},{"gauge":"","internal":"","scalar":"","set":"","meanCount":"","kind":"kind","name":{"origin":"origin","context":{"key":"context"},"name":"name"},"updateTime":"updateTime","cumulative":True,"distribution":"","meanSum":""}],"sourceFork":{"primarySource":{"derivationMode":"SOURCE_DERIVATION_MODE_UNKNOWN","source":{"codec":{"key":""},"metadata":{"infinite":True,"estimatedSizeBytes":"estimatedSizeBytes","producesSortedKeys":True},"baseSpecs":[{"key":""},{"key":""}],"doesNotNeedSplitting":True,"spec":{"key":""}}},"residual":{"derivationMode":"SOURCE_DERIVATION_MODE_UNKNOWN","source":{"codec":{"key":""},"metadata":{"infinite":True,"estimatedSizeBytes":"estimatedSizeBytes","producesSortedKeys":True},"baseSpecs":[{"key":""},{"key":""}],"doesNotNeedSplitting":True,"spec":{"key":""}}},"primary":{"derivationMode":"SOURCE_DERIVATION_MODE_UNKNOWN","source":{"codec":{"key":""},"metadata":{"infinite":True,"estimatedSizeBytes":"estimatedSizeBytes","producesSortedKeys":True},"baseSpecs":[{"key":""},{"key":""}],"doesNotNeedSplitting":True,"spec":{"key":""}}},"residualSource":{"derivationMode":"SOURCE_DERIVATION_MODE_UNKNOWN","source":{"codec":{"key":""},"metadata":{"infinite":True,"estimatedSizeBytes":"estimatedSizeBytes","producesSortedKeys":True},"baseSpecs":[{"key":""},{"key":""}],"doesNotNeedSplitting":True,"spec":{"key":""}}}},"stopPosition":{"concatPosition":{"index":5},"byteOffset":"byteOffset","end":True,"recordIndex":"recordIndex","key":"key","shufflePosition":"shufflePosition"},"dynamicSourceSplit":{"residual":{"derivationMode":"SOURCE_DERIVATION_MODE_UNKNOWN","source":{"codec":{"key":""},"metadata":{"infinite":True,"estimatedSizeBytes":"estimatedSizeBytes","producesSortedKeys":True},"baseSpecs":[{"key":""},{"key":""}],"doesNotNeedSplitting":True,"spec":{"key":""}}},"primary":{"derivationMode":"SOURCE_DERIVATION_MODE_UNKNOWN","source":{"codec":{"key":""},"metadata":{"infinite":True,"estimatedSizeBytes":"estimatedSizeBytes","producesSortedKeys":True},"baseSpecs":[{"key":""},{"key":""}],"doesNotNeedSplitting":True,"spec":{"key":""}}}},"completed":True,"reportIndex":"reportIndex","workItemId":"workItemId","sourceOperationResponse":{"getMetadata":{"metadata":{"infinite":True,"estimatedSizeBytes":"estimatedSizeBytes","producesSortedKeys":True}},"split":{"shards":[{"derivationMode":"SOURCE_DERIVATION_MODE_UNKNOWN","source":{"codec":{"key":""},"metadata":{"infinite":True,"estimatedSizeBytes":"estimatedSizeBytes","producesSortedKeys":True},"baseSpecs":[{"key":""},{"key":""}],"doesNotNeedSplitting":True,"spec":{"key":""}}},{"derivationMode":"SOURCE_DERIVATION_MODE_UNKNOWN","source":{"codec":{"key":""},"metadata":{"infinite":True,"estimatedSizeBytes":"estimatedSizeBytes","producesSortedKeys":True},"baseSpecs":[{"key":""},{"key":""}],"doesNotNeedSplitting":True,"spec":{"key":""}}}],"bundles":[{"derivationMode":"SOURCE_DERIVATION_MODE_UNKNOWN","source":{"codec":{"key":""},"metadata":{"infinite":True,"estimatedSizeBytes":"estimatedSizeBytes","producesSortedKeys":True},"baseSpecs":[{"key":""},{"key":""}],"doesNotNeedSplitting":True,"spec":{"key":""}}},{"derivationMode":"SOURCE_DERIVATION_MODE_UNKNOWN","source":{"codec":{"key":""},"metadata":{"infinite":True,"estimatedSizeBytes":"estimatedSizeBytes","producesSortedKeys":True},"baseSpecs":[{"key":""},{"key":""}],"doesNotNeedSplitting":True,"spec":{"key":""}}}],"outcome":"SOURCE_SPLIT_OUTCOME_UNKNOWN"}},"counterUpdates":[{"nameAndKind":{"kind":"INVALID","name":"name"},"shortId":"shortId","internal":"","integerList":{"elements":[{"highBits":0,"lowBits":6},{"highBits":0,"lowBits":6}]},"floatingPoint":5.637376656633329,"floatingPointList":{"elements":[2.3021358869347655,2.3021358869347655]},"integer":{"highBits":0,"lowBits":6},"cumulative":True,"distribution":{"histogram":{"bucketCounts":["bucketCounts","bucketCounts"],"firstBucketOffset":1},"sumOfSquares":5.962133916683182,"min":{"highBits":0,"lowBits":6},"max":{"highBits":0,"lowBits":6},"count":{"highBits":0,"lowBits":6},"sum":{"highBits":0,"lowBits":6}},"floatingPointMean":{"count":{"highBits":0,"lowBits":6},"sum":7.061401241503109},"integerGauge":{"value":{"highBits":0,"lowBits":6},"timestamp":"timestamp"},"boolean":True,"stringList":{"elements":["elements","elements"]},"integerMean":{"count":{"highBits":0,"lowBits":6},"sum":{"highBits":0,"lowBits":6}},"structuredNameAndMetadata":{"metadata":{"kind":"INVALID","standardUnits":"BYTES","description":"description","otherUnits":"otherUnits"},"name":{"workerId":"workerId","componentStepName":"componentStepName","inputIndex":9,"origin":"SYSTEM","portion":"ALL","name":"name","originalRequestingStepName":"originalRequestingStepName","executionStepName":"executionStepName","originNamespace":"originNamespace","originalStepName":"originalStepName"}}},{"nameAndKind":{"kind":"INVALID","name":"name"},"shortId":"shortId","internal":"","integerList":{"elements":[{"highBits":0,"lowBits":6},{"highBits":0,"lowBits":6}]},"floatingPoint":5.637376656633329,"floatingPointList":{"elements":[2.3021358869347655,2.3021358869347655]},"integer":{"highBits":0,"lowBits":6},"cumulative":True,"distribution":{"histogram":{"bucketCounts":["bucketCounts","bucketCounts"],"firstBucketOffset":1},"sumOfSquares":5.962133916683182,"min":{"highBits":0,"lowBits":6},"max":{"highBits":0,"lowBits":6},"count":{"highBits":0,"lowBits":6},"sum":{"highBits":0,"lowBits":6}},"floatingPointMean":{"count":{"highBits":0,"lowBits":6},"sum":7.061401241503109},"integerGauge":{"value":{"highBits":0,"lowBits":6},"timestamp":"timestamp"},"boolean":True,"stringList":{"elements":["elements","elements"]},"integerMean":{"count":{"highBits":0,"lowBits":6},"sum":{"highBits":0,"lowBits":6}},"structuredNameAndMetadata":{"metadata":{"kind":"INVALID","standardUnits":"BYTES","description":"description","otherUnits":"otherUnits"},"name":{"workerId":"workerId","componentStepName":"componentStepName","inputIndex":9,"origin":"SYSTEM","portion":"ALL","name":"name","originalRequestingStepName":"originalRequestingStepName","executionStepName":"executionStepName","originNamespace":"originNamespace","originalStepName":"originalStepName"}}}],"progress":{"percentComplete":2.302136,"position":{"concatPosition":{"index":5},"byteOffset":"byteOffset","end":True,"recordIndex":"recordIndex","key":"key","shufflePosition":"shufflePosition"},"remainingTime":"remainingTime"},"totalThrottlerWaitTimeSeconds":4.145608029883936,"requestedLeaseDuration":"requestedLeaseDuration","errors":[{"code":0,"details":[{"key":""},{"key":""}],"message":"message"},{"code":0,"details":[{"key":""},{"key":""}],"message":"message"}],"reportedProgress":{"remainingParallelism":{"isInfinite":True,"value":3.616076749251911},"position":{"concatPosition":{"index":5},"byteOffset":"byteOffset","end":True,"recordIndex":"recordIndex","key":"key","shufflePosition":"shufflePosition"},"fractionConsumed":2.027123023002322,"consumedParallelism":{"isInfinite":True,"value":3.616076749251911}}},{"metricUpdates":[{"gauge":"","internal":"","scalar":"","set":"","meanCount":"","kind":"kind","name":{"origin":"origin","context":{"key":"context"},"name":"name"},"updateTime":"updateTime","cumulative":True,"distribution":"","meanSum":""},{"gauge":"","internal":"","scalar":"","set":"","meanCount":"","kind":"kind","name":{"origin":"origin","context":{"key":"context"},"name":"name"},"updateTime":"updateTime","cumulative":True,"distribution":"","meanSum":""}],"sourceFork":{"primarySource":{"derivationMode":"SOURCE_DERIVATION_MODE_UNKNOWN","source":{"codec":{"key":""},"metadata":{"infinite":True,"estimatedSizeBytes":"estimatedSizeBytes","producesSortedKeys":True},"baseSpecs":[{"key":""},{"key":""}],"doesNotNeedSplitting":True,"spec":{"key":""}}},"residual":{"derivationMode":"SOURCE_DERIVATION_MODE_UNKNOWN","source":{"codec":{"key":""},"metadata":{"infinite":True,"estimatedSizeBytes":"estimatedSizeBytes","producesSortedKeys":True},"baseSpecs":[{"key":""},{"key":""}],"doesNotNeedSplitting":True,"spec":{"key":""}}},"primary":{"derivationMode":"SOURCE_DERIVATION_MODE_UNKNOWN","source":{"codec":{"key":""},"metadata":{"infinite":True,"estimatedSizeBytes":"estimatedSizeBytes","producesSortedKeys":True},"baseSpecs":[{"key":""},{"key":""}],"doesNotNeedSplitting":True,"spec":{"key":""}}},"residualSource":{"derivationMode":"SOURCE_DERIVATION_MODE_UNKNOWN","source":{"codec":{"key":""},"metadata":{"infinite":True,"estimatedSizeBytes":"estimatedSizeBytes","producesSortedKeys":True},"baseSpecs":[{"key":""},{"key":""}],"doesNotNeedSplitting":True,"spec":{"key":""}}}},"stopPosition":{"concatPosition":{"index":5},"byteOffset":"byteOffset","end":True,"recordIndex":"recordIndex","key":"key","shufflePosition":"shufflePosition"},"dynamicSourceSplit":{"residual":{"derivationMode":"SOURCE_DERIVATION_MODE_UNKNOWN","source":{"codec":{"key":""},"metadata":{"infinite":True,"estimatedSizeBytes":"estimatedSizeBytes","producesSortedKeys":True},"baseSpecs":[{"key":""},{"key":""}],"doesNotNeedSplitting":True,"spec":{"key":""}}},"primary":{"derivationMode":"SOURCE_DERIVATION_MODE_UNKNOWN","source":{"codec":{"key":""},"metadata":{"infinite":True,"estimatedSizeBytes":"estimatedSizeBytes","producesSortedKeys":True},"baseSpecs":[{"key":""},{"key":""}],"doesNotNeedSplitting":True,"spec":{"key":""}}}},"completed":True,"reportIndex":"reportIndex","workItemId":"workItemId","sourceOperationResponse":{"getMetadata":{"metadata":{"infinite":True,"estimatedSizeBytes":"estimatedSizeBytes","producesSortedKeys":True}},"split":{"shards":[{"derivationMode":"SOURCE_DERIVATION_MODE_UNKNOWN","source":{"codec":{"key":""},"metadata":{"infinite":True,"estimatedSizeBytes":"estimatedSizeBytes","producesSortedKeys":True},"baseSpecs":[{"key":""},{"key":""}],"doesNotNeedSplitting":True,"spec":{"key":""}}},{"derivationMode":"SOURCE_DERIVATION_MODE_UNKNOWN","source":{"codec":{"key":""},"metadata":{"infinite":True,"estimatedSizeBytes":"estimatedSizeBytes","producesSortedKeys":True},"baseSpecs":[{"key":""},{"key":""}],"doesNotNeedSplitting":True,"spec":{"key":""}}}],"bundles":[{"derivationMode":"SOURCE_DERIVATION_MODE_UNKNOWN","source":{"codec":{"key":""},"metadata":{"infinite":True,"estimatedSizeBytes":"estimatedSizeBytes","producesSortedKeys":True},"baseSpecs":[{"key":""},{"key":""}],"doesNotNeedSplitting":True,"spec":{"key":""}}},{"derivationMode":"SOURCE_DERIVATION_MODE_UNKNOWN","source":{"codec":{"key":""},"metadata":{"infinite":True,"estimatedSizeBytes":"estimatedSizeBytes","producesSortedKeys":True},"baseSpecs":[{"key":""},{"key":""}],"doesNotNeedSplitting":True,"spec":{"key":""}}}],"outcome":"SOURCE_SPLIT_OUTCOME_UNKNOWN"}},"counterUpdates":[{"nameAndKind":{"kind":"INVALID","name":"name"},"shortId":"shortId","internal":"","integerList":{"elements":[{"highBits":0,"lowBits":6},{"highBits":0,"lowBits":6}]},"floatingPoint":5.637376656633329,"floatingPointList":{"elements":[2.3021358869347655,2.3021358869347655]},"integer":{"highBits":0,"lowBits":6},"cumulative":True,"distribution":{"histogram":{"bucketCounts":["bucketCounts","bucketCounts"],"firstBucketOffset":1},"sumOfSquares":5.962133916683182,"min":{"highBits":0,"lowBits":6},"max":{"highBits":0,"lowBits":6},"count":{"highBits":0,"lowBits":6},"sum":{"highBits":0,"lowBits":6}},"floatingPointMean":{"count":{"highBits":0,"lowBits":6},"sum":7.061401241503109},"integerGauge":{"value":{"highBits":0,"lowBits":6},"timestamp":"timestamp"},"boolean":True,"stringList":{"elements":["elements","elements"]},"integerMean":{"count":{"highBits":0,"lowBits":6},"sum":{"highBits":0,"lowBits":6}},"structuredNameAndMetadata":{"metadata":{"kind":"INVALID","standardUnits":"BYTES","description":"description","otherUnits":"otherUnits"},"name":{"workerId":"workerId","componentStepName":"componentStepName","inputIndex":9,"origin":"SYSTEM","portion":"ALL","name":"name","originalRequestingStepName":"originalRequestingStepName","executionStepName":"executionStepName","originNamespace":"originNamespace","originalStepName":"originalStepName"}}},{"nameAndKind":{"kind":"INVALID","name":"name"},"shortId":"shortId","internal":"","integerList":{"elements":[{"highBits":0,"lowBits":6},{"highBits":0,"lowBits":6}]},"floatingPoint":5.637376656633329,"floatingPointList":{"elements":[2.3021358869347655,2.3021358869347655]},"integer":{"highBits":0,"lowBits":6},"cumulative":True,"distribution":{"histogram":{"bucketCounts":["bucketCounts","bucketCounts"],"firstBucketOffset":1},"sumOfSquares":5.962133916683182,"min":{"highBits":0,"lowBits":6},"max":{"highBits":0,"lowBits":6},"count":{"highBits":0,"lowBits":6},"sum":{"highBits":0,"lowBits":6}},"floatingPointMean":{"count":{"highBits":0,"lowBits":6},"sum":7.061401241503109},"integerGauge":{"value":{"highBits":0,"lowBits":6},"timestamp":"timestamp"},"boolean":True,"stringList":{"elements":["elements","elements"]},"integerMean":{"count":{"highBits":0,"lowBits":6},"sum":{"highBits":0,"lowBits":6}},"structuredNameAndMetadata":{"metadata":{"kind":"INVALID","standardUnits":"BYTES","description":"description","otherUnits":"otherUnits"},"name":{"workerId":"workerId","componentStepName":"componentStepName","inputIndex":9,"origin":"SYSTEM","portion":"ALL","name":"name","originalRequestingStepName":"originalRequestingStepName","executionStepName":"executionStepName","originNamespace":"originNamespace","originalStepName":"originalStepName"}}}],"progress":{"percentComplete":2.302136,"position":{"concatPosition":{"index":5},"byteOffset":"byteOffset","end":True,"recordIndex":"recordIndex","key":"key","shufflePosition":"shufflePosition"},"remainingTime":"remainingTime"},"totalThrottlerWaitTimeSeconds":4.145608029883936,"requestedLeaseDuration":"requestedLeaseDuration","errors":[{"code":0,"details":[{"key":""},{"key":""}],"message":"message"},{"code":0,"details":[{"key":""},{"key":""}],"message":"message"}],"reportedProgress":{"remainingParallelism":{"isInfinite":True,"value":3.616076749251911},"position":{"concatPosition":{"index":5},"byteOffset":"byteOffset","end":True,"recordIndex":"recordIndex","key":"key","shufflePosition":"shufflePosition"},"fractionConsumed":2.027123023002322,"consumedParallelism":{"isInfinite":True,"value":3.616076749251911}}}],"location":"location"}
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
        path='/v1b3/projects/{project_id}/locations/{location}/jobs/{job_id}/workItems:reportStatus'.format(project_id='project_id_example', location='location_example', job_id='job_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataflow_projects_locations_snapshots_delete(client):
    """Test case for dataflow_projects_locations_snapshots_delete

    
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
        method='DELETE',
        path='/v1b3/projects/{project_id}/locations/{location}/snapshots/{snapshot_id}'.format(project_id='project_id_example', location='location_example', snapshot_id='snapshot_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataflow_projects_locations_snapshots_get(client):
    """Test case for dataflow_projects_locations_snapshots_get

    
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
        path='/v1b3/projects/{project_id}/locations/{location}/snapshots/{snapshot_id}'.format(project_id='project_id_example', location='location_example', snapshot_id='snapshot_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataflow_projects_locations_snapshots_list(client):
    """Test case for dataflow_projects_locations_snapshots_list

    
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
                    ('jobId', 'job_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1b3/projects/{project_id}/locations/{location}/snapshots'.format(project_id='project_id_example', location='location_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataflow_projects_locations_templates_create(client):
    """Test case for dataflow_projects_locations_templates_create

    
    """
    body = {"gcsPath":"gcsPath","jobName":"jobName","environment":{"additionalUserLabels":{"key":"additionalUserLabels"},"workerRegion":"workerRegion","streamingMode":"STREAMING_MODE_UNSPECIFIED","kmsKeyName":"kmsKeyName","network":"network","additionalExperiments":["additionalExperiments","additionalExperiments"],"enableStreamingEngine":True,"tempLocation":"tempLocation","workerZone":"workerZone","bypassTempDirValidation":True,"maxWorkers":6,"serviceAccountEmail":"serviceAccountEmail","zone":"zone","ipConfiguration":"WORKER_IP_UNSPECIFIED","subnetwork":"subnetwork","numWorkers":1,"machineType":"machineType","diskSizeGb":0},"location":"location","parameters":{"key":"parameters"}}
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
        path='/v1b3/projects/{project_id}/locations/{location}/templates'.format(project_id='project_id_example', location='location_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataflow_projects_locations_templates_get(client):
    """Test case for dataflow_projects_locations_templates_get

    
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
                    ('gcsPath', 'gcs_path_example'),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1b3/projects/{project_id}/locations/{location}/templates:get'.format(project_id='project_id_example', location='location_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataflow_projects_locations_templates_launch(client):
    """Test case for dataflow_projects_locations_templates_launch

    
    """
    body = {"jobName":"jobName","environment":{"additionalUserLabels":{"key":"additionalUserLabels"},"workerRegion":"workerRegion","streamingMode":"STREAMING_MODE_UNSPECIFIED","kmsKeyName":"kmsKeyName","network":"network","additionalExperiments":["additionalExperiments","additionalExperiments"],"enableStreamingEngine":True,"tempLocation":"tempLocation","workerZone":"workerZone","bypassTempDirValidation":True,"maxWorkers":6,"serviceAccountEmail":"serviceAccountEmail","zone":"zone","ipConfiguration":"WORKER_IP_UNSPECIFIED","subnetwork":"subnetwork","numWorkers":1,"machineType":"machineType","diskSizeGb":0},"transformNameMapping":{"key":"transformNameMapping"},"update":True,"parameters":{"key":"parameters"}}
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
                    ('dynamicTemplate.gcsPath', 'dynamic_template_gcs_path_example'),
                    ('dynamicTemplate.stagingLocation', 'dynamic_template_staging_location_example'),
                    ('gcsPath', 'gcs_path_example'),
                    ('validateOnly', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1b3/projects/{project_id}/locations/{location}/templates:launch'.format(project_id='project_id_example', location='location_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataflow_projects_locations_worker_messages(client):
    """Test case for dataflow_projects_locations_worker_messages

    
    """
    body = {"workerMessages":[{"workerLifecycleEvent":{"metadata":{"key":"metadata"},"containerStartTime":"containerStartTime","event":"UNKNOWN_EVENT"},"workerThreadScalingReport":{"currentThreadCount":6},"dataSamplingReport":{"elementsSampledCount":"elementsSampledCount","bytesWrittenDelta":"bytesWrittenDelta","translationErrorsCount":"translationErrorsCount","exceptionsSampledCount":"exceptionsSampledCount","persistenceErrorsCount":"persistenceErrorsCount","elementsSampledBytes":"elementsSampledBytes","pcollectionsSampledCount":"pcollectionsSampledCount"},"workerMessageCode":{"code":"code","parameters":{"key":""}},"workerShutdownNotice":{"reason":"reason"},"workerMetrics":{"memoryInfo":[{"totalGbMs":"totalGbMs","currentOoms":"currentOoms","currentRssBytes":"currentRssBytes","currentLimitBytes":"currentLimitBytes","timestamp":"timestamp"},{"totalGbMs":"totalGbMs","currentOoms":"currentOoms","currentRssBytes":"currentRssBytes","currentLimitBytes":"currentLimitBytes","timestamp":"timestamp"}],"cpuTime":[{"rate":1.4894159098541704,"totalMs":"totalMs","timestamp":"timestamp"},{"rate":1.4894159098541704,"totalMs":"totalMs","timestamp":"timestamp"}],"containers":{}},"time":"time","perWorkerMetrics":{"perStepNamespaceMetrics":[{"originalStep":"originalStep","metricsNamespace":"metricsNamespace","metricValues":[{"valueHistogram":{"outlierStats":{"underflowCount":"underflowCount","overflowCount":"overflowCount","overflowMean":2.3021358869347655,"underflowMean":7.061401241503109},"bucketCounts":["bucketCounts","bucketCounts"],"bucketOptions":{"exponential":{"numberOfBuckets":0,"scale":6},"linear":{"numberOfBuckets":1,"start":5.962133916683182,"width":5.637376656633329}},"count":"count"},"metric":"metric","metricLabels":{"key":"metricLabels"},"valueInt64":"valueInt64"},{"valueHistogram":{"outlierStats":{"underflowCount":"underflowCount","overflowCount":"overflowCount","overflowMean":2.3021358869347655,"underflowMean":7.061401241503109},"bucketCounts":["bucketCounts","bucketCounts"],"bucketOptions":{"exponential":{"numberOfBuckets":0,"scale":6},"linear":{"numberOfBuckets":1,"start":5.962133916683182,"width":5.637376656633329}},"count":"count"},"metric":"metric","metricLabels":{"key":"metricLabels"},"valueInt64":"valueInt64"}]},{"originalStep":"originalStep","metricsNamespace":"metricsNamespace","metricValues":[{"valueHistogram":{"outlierStats":{"underflowCount":"underflowCount","overflowCount":"overflowCount","overflowMean":2.3021358869347655,"underflowMean":7.061401241503109},"bucketCounts":["bucketCounts","bucketCounts"],"bucketOptions":{"exponential":{"numberOfBuckets":0,"scale":6},"linear":{"numberOfBuckets":1,"start":5.962133916683182,"width":5.637376656633329}},"count":"count"},"metric":"metric","metricLabels":{"key":"metricLabels"},"valueInt64":"valueInt64"},{"valueHistogram":{"outlierStats":{"underflowCount":"underflowCount","overflowCount":"overflowCount","overflowMean":2.3021358869347655,"underflowMean":7.061401241503109},"bucketCounts":["bucketCounts","bucketCounts"],"bucketOptions":{"exponential":{"numberOfBuckets":0,"scale":6},"linear":{"numberOfBuckets":1,"start":5.962133916683182,"width":5.637376656633329}},"count":"count"},"metric":"metric","metricLabels":{"key":"metricLabels"},"valueInt64":"valueInt64"}]}]},"streamingScalingReport":{"activeBundleCount":9,"outstandingBytesCount":1,"activeThreadCount":3,"maximumBytes":"maximumBytes","maximumThreadCount":7,"outstandingBytes":"outstandingBytes","maximumBundleCount":2,"outstandingBundleCount":1,"maximumBytesCount":4},"workerHealthReport":{"msg":"msg","reportInterval":"reportInterval","vmIsHealthy":True,"vmBrokenCode":"vmBrokenCode","vmStartupTime":"vmStartupTime","pods":[{"key":""},{"key":""}],"vmIsBroken":True},"labels":{"key":"labels"}},{"workerLifecycleEvent":{"metadata":{"key":"metadata"},"containerStartTime":"containerStartTime","event":"UNKNOWN_EVENT"},"workerThreadScalingReport":{"currentThreadCount":6},"dataSamplingReport":{"elementsSampledCount":"elementsSampledCount","bytesWrittenDelta":"bytesWrittenDelta","translationErrorsCount":"translationErrorsCount","exceptionsSampledCount":"exceptionsSampledCount","persistenceErrorsCount":"persistenceErrorsCount","elementsSampledBytes":"elementsSampledBytes","pcollectionsSampledCount":"pcollectionsSampledCount"},"workerMessageCode":{"code":"code","parameters":{"key":""}},"workerShutdownNotice":{"reason":"reason"},"workerMetrics":{"memoryInfo":[{"totalGbMs":"totalGbMs","currentOoms":"currentOoms","currentRssBytes":"currentRssBytes","currentLimitBytes":"currentLimitBytes","timestamp":"timestamp"},{"totalGbMs":"totalGbMs","currentOoms":"currentOoms","currentRssBytes":"currentRssBytes","currentLimitBytes":"currentLimitBytes","timestamp":"timestamp"}],"cpuTime":[{"rate":1.4894159098541704,"totalMs":"totalMs","timestamp":"timestamp"},{"rate":1.4894159098541704,"totalMs":"totalMs","timestamp":"timestamp"}],"containers":{}},"time":"time","perWorkerMetrics":{"perStepNamespaceMetrics":[{"originalStep":"originalStep","metricsNamespace":"metricsNamespace","metricValues":[{"valueHistogram":{"outlierStats":{"underflowCount":"underflowCount","overflowCount":"overflowCount","overflowMean":2.3021358869347655,"underflowMean":7.061401241503109},"bucketCounts":["bucketCounts","bucketCounts"],"bucketOptions":{"exponential":{"numberOfBuckets":0,"scale":6},"linear":{"numberOfBuckets":1,"start":5.962133916683182,"width":5.637376656633329}},"count":"count"},"metric":"metric","metricLabels":{"key":"metricLabels"},"valueInt64":"valueInt64"},{"valueHistogram":{"outlierStats":{"underflowCount":"underflowCount","overflowCount":"overflowCount","overflowMean":2.3021358869347655,"underflowMean":7.061401241503109},"bucketCounts":["bucketCounts","bucketCounts"],"bucketOptions":{"exponential":{"numberOfBuckets":0,"scale":6},"linear":{"numberOfBuckets":1,"start":5.962133916683182,"width":5.637376656633329}},"count":"count"},"metric":"metric","metricLabels":{"key":"metricLabels"},"valueInt64":"valueInt64"}]},{"originalStep":"originalStep","metricsNamespace":"metricsNamespace","metricValues":[{"valueHistogram":{"outlierStats":{"underflowCount":"underflowCount","overflowCount":"overflowCount","overflowMean":2.3021358869347655,"underflowMean":7.061401241503109},"bucketCounts":["bucketCounts","bucketCounts"],"bucketOptions":{"exponential":{"numberOfBuckets":0,"scale":6},"linear":{"numberOfBuckets":1,"start":5.962133916683182,"width":5.637376656633329}},"count":"count"},"metric":"metric","metricLabels":{"key":"metricLabels"},"valueInt64":"valueInt64"},{"valueHistogram":{"outlierStats":{"underflowCount":"underflowCount","overflowCount":"overflowCount","overflowMean":2.3021358869347655,"underflowMean":7.061401241503109},"bucketCounts":["bucketCounts","bucketCounts"],"bucketOptions":{"exponential":{"numberOfBuckets":0,"scale":6},"linear":{"numberOfBuckets":1,"start":5.962133916683182,"width":5.637376656633329}},"count":"count"},"metric":"metric","metricLabels":{"key":"metricLabels"},"valueInt64":"valueInt64"}]}]},"streamingScalingReport":{"activeBundleCount":9,"outstandingBytesCount":1,"activeThreadCount":3,"maximumBytes":"maximumBytes","maximumThreadCount":7,"outstandingBytes":"outstandingBytes","maximumBundleCount":2,"outstandingBundleCount":1,"maximumBytesCount":4},"workerHealthReport":{"msg":"msg","reportInterval":"reportInterval","vmIsHealthy":True,"vmBrokenCode":"vmBrokenCode","vmStartupTime":"vmStartupTime","pods":[{"key":""},{"key":""}],"vmIsBroken":True},"labels":{"key":"labels"}}],"location":"location"}
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
        path='/v1b3/projects/{project_id}/locations/{location}/WorkerMessages'.format(project_id='project_id_example', location='location_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataflow_projects_snapshots_get(client):
    """Test case for dataflow_projects_snapshots_get

    
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
                    ('location', 'location_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1b3/projects/{project_id}/snapshots/{snapshot_id}'.format(project_id='project_id_example', snapshot_id='snapshot_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataflow_projects_snapshots_list(client):
    """Test case for dataflow_projects_snapshots_list

    
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
                    ('jobId', 'job_id_example'),
                    ('location', 'location_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1b3/projects/{project_id}/snapshots'.format(project_id='project_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataflow_projects_templates_create(client):
    """Test case for dataflow_projects_templates_create

    
    """
    body = {"gcsPath":"gcsPath","jobName":"jobName","environment":{"additionalUserLabels":{"key":"additionalUserLabels"},"workerRegion":"workerRegion","streamingMode":"STREAMING_MODE_UNSPECIFIED","kmsKeyName":"kmsKeyName","network":"network","additionalExperiments":["additionalExperiments","additionalExperiments"],"enableStreamingEngine":True,"tempLocation":"tempLocation","workerZone":"workerZone","bypassTempDirValidation":True,"maxWorkers":6,"serviceAccountEmail":"serviceAccountEmail","zone":"zone","ipConfiguration":"WORKER_IP_UNSPECIFIED","subnetwork":"subnetwork","numWorkers":1,"machineType":"machineType","diskSizeGb":0},"location":"location","parameters":{"key":"parameters"}}
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
        path='/v1b3/projects/{project_id}/templates'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataflow_projects_templates_get(client):
    """Test case for dataflow_projects_templates_get

    
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
                    ('gcsPath', 'gcs_path_example'),
                    ('location', 'location_example'),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1b3/projects/{project_id}/templates:get'.format(project_id='project_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataflow_projects_templates_launch(client):
    """Test case for dataflow_projects_templates_launch

    
    """
    body = {"jobName":"jobName","environment":{"additionalUserLabels":{"key":"additionalUserLabels"},"workerRegion":"workerRegion","streamingMode":"STREAMING_MODE_UNSPECIFIED","kmsKeyName":"kmsKeyName","network":"network","additionalExperiments":["additionalExperiments","additionalExperiments"],"enableStreamingEngine":True,"tempLocation":"tempLocation","workerZone":"workerZone","bypassTempDirValidation":True,"maxWorkers":6,"serviceAccountEmail":"serviceAccountEmail","zone":"zone","ipConfiguration":"WORKER_IP_UNSPECIFIED","subnetwork":"subnetwork","numWorkers":1,"machineType":"machineType","diskSizeGb":0},"transformNameMapping":{"key":"transformNameMapping"},"update":True,"parameters":{"key":"parameters"}}
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
                    ('dynamicTemplate.gcsPath', 'dynamic_template_gcs_path_example'),
                    ('dynamicTemplate.stagingLocation', 'dynamic_template_staging_location_example'),
                    ('gcsPath', 'gcs_path_example'),
                    ('location', 'location_example'),
                    ('validateOnly', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1b3/projects/{project_id}/templates:launch'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataflow_projects_worker_messages(client):
    """Test case for dataflow_projects_worker_messages

    
    """
    body = {"workerMessages":[{"workerLifecycleEvent":{"metadata":{"key":"metadata"},"containerStartTime":"containerStartTime","event":"UNKNOWN_EVENT"},"workerThreadScalingReport":{"currentThreadCount":6},"dataSamplingReport":{"elementsSampledCount":"elementsSampledCount","bytesWrittenDelta":"bytesWrittenDelta","translationErrorsCount":"translationErrorsCount","exceptionsSampledCount":"exceptionsSampledCount","persistenceErrorsCount":"persistenceErrorsCount","elementsSampledBytes":"elementsSampledBytes","pcollectionsSampledCount":"pcollectionsSampledCount"},"workerMessageCode":{"code":"code","parameters":{"key":""}},"workerShutdownNotice":{"reason":"reason"},"workerMetrics":{"memoryInfo":[{"totalGbMs":"totalGbMs","currentOoms":"currentOoms","currentRssBytes":"currentRssBytes","currentLimitBytes":"currentLimitBytes","timestamp":"timestamp"},{"totalGbMs":"totalGbMs","currentOoms":"currentOoms","currentRssBytes":"currentRssBytes","currentLimitBytes":"currentLimitBytes","timestamp":"timestamp"}],"cpuTime":[{"rate":1.4894159098541704,"totalMs":"totalMs","timestamp":"timestamp"},{"rate":1.4894159098541704,"totalMs":"totalMs","timestamp":"timestamp"}],"containers":{}},"time":"time","perWorkerMetrics":{"perStepNamespaceMetrics":[{"originalStep":"originalStep","metricsNamespace":"metricsNamespace","metricValues":[{"valueHistogram":{"outlierStats":{"underflowCount":"underflowCount","overflowCount":"overflowCount","overflowMean":2.3021358869347655,"underflowMean":7.061401241503109},"bucketCounts":["bucketCounts","bucketCounts"],"bucketOptions":{"exponential":{"numberOfBuckets":0,"scale":6},"linear":{"numberOfBuckets":1,"start":5.962133916683182,"width":5.637376656633329}},"count":"count"},"metric":"metric","metricLabels":{"key":"metricLabels"},"valueInt64":"valueInt64"},{"valueHistogram":{"outlierStats":{"underflowCount":"underflowCount","overflowCount":"overflowCount","overflowMean":2.3021358869347655,"underflowMean":7.061401241503109},"bucketCounts":["bucketCounts","bucketCounts"],"bucketOptions":{"exponential":{"numberOfBuckets":0,"scale":6},"linear":{"numberOfBuckets":1,"start":5.962133916683182,"width":5.637376656633329}},"count":"count"},"metric":"metric","metricLabels":{"key":"metricLabels"},"valueInt64":"valueInt64"}]},{"originalStep":"originalStep","metricsNamespace":"metricsNamespace","metricValues":[{"valueHistogram":{"outlierStats":{"underflowCount":"underflowCount","overflowCount":"overflowCount","overflowMean":2.3021358869347655,"underflowMean":7.061401241503109},"bucketCounts":["bucketCounts","bucketCounts"],"bucketOptions":{"exponential":{"numberOfBuckets":0,"scale":6},"linear":{"numberOfBuckets":1,"start":5.962133916683182,"width":5.637376656633329}},"count":"count"},"metric":"metric","metricLabels":{"key":"metricLabels"},"valueInt64":"valueInt64"},{"valueHistogram":{"outlierStats":{"underflowCount":"underflowCount","overflowCount":"overflowCount","overflowMean":2.3021358869347655,"underflowMean":7.061401241503109},"bucketCounts":["bucketCounts","bucketCounts"],"bucketOptions":{"exponential":{"numberOfBuckets":0,"scale":6},"linear":{"numberOfBuckets":1,"start":5.962133916683182,"width":5.637376656633329}},"count":"count"},"metric":"metric","metricLabels":{"key":"metricLabels"},"valueInt64":"valueInt64"}]}]},"streamingScalingReport":{"activeBundleCount":9,"outstandingBytesCount":1,"activeThreadCount":3,"maximumBytes":"maximumBytes","maximumThreadCount":7,"outstandingBytes":"outstandingBytes","maximumBundleCount":2,"outstandingBundleCount":1,"maximumBytesCount":4},"workerHealthReport":{"msg":"msg","reportInterval":"reportInterval","vmIsHealthy":True,"vmBrokenCode":"vmBrokenCode","vmStartupTime":"vmStartupTime","pods":[{"key":""},{"key":""}],"vmIsBroken":True},"labels":{"key":"labels"}},{"workerLifecycleEvent":{"metadata":{"key":"metadata"},"containerStartTime":"containerStartTime","event":"UNKNOWN_EVENT"},"workerThreadScalingReport":{"currentThreadCount":6},"dataSamplingReport":{"elementsSampledCount":"elementsSampledCount","bytesWrittenDelta":"bytesWrittenDelta","translationErrorsCount":"translationErrorsCount","exceptionsSampledCount":"exceptionsSampledCount","persistenceErrorsCount":"persistenceErrorsCount","elementsSampledBytes":"elementsSampledBytes","pcollectionsSampledCount":"pcollectionsSampledCount"},"workerMessageCode":{"code":"code","parameters":{"key":""}},"workerShutdownNotice":{"reason":"reason"},"workerMetrics":{"memoryInfo":[{"totalGbMs":"totalGbMs","currentOoms":"currentOoms","currentRssBytes":"currentRssBytes","currentLimitBytes":"currentLimitBytes","timestamp":"timestamp"},{"totalGbMs":"totalGbMs","currentOoms":"currentOoms","currentRssBytes":"currentRssBytes","currentLimitBytes":"currentLimitBytes","timestamp":"timestamp"}],"cpuTime":[{"rate":1.4894159098541704,"totalMs":"totalMs","timestamp":"timestamp"},{"rate":1.4894159098541704,"totalMs":"totalMs","timestamp":"timestamp"}],"containers":{}},"time":"time","perWorkerMetrics":{"perStepNamespaceMetrics":[{"originalStep":"originalStep","metricsNamespace":"metricsNamespace","metricValues":[{"valueHistogram":{"outlierStats":{"underflowCount":"underflowCount","overflowCount":"overflowCount","overflowMean":2.3021358869347655,"underflowMean":7.061401241503109},"bucketCounts":["bucketCounts","bucketCounts"],"bucketOptions":{"exponential":{"numberOfBuckets":0,"scale":6},"linear":{"numberOfBuckets":1,"start":5.962133916683182,"width":5.637376656633329}},"count":"count"},"metric":"metric","metricLabels":{"key":"metricLabels"},"valueInt64":"valueInt64"},{"valueHistogram":{"outlierStats":{"underflowCount":"underflowCount","overflowCount":"overflowCount","overflowMean":2.3021358869347655,"underflowMean":7.061401241503109},"bucketCounts":["bucketCounts","bucketCounts"],"bucketOptions":{"exponential":{"numberOfBuckets":0,"scale":6},"linear":{"numberOfBuckets":1,"start":5.962133916683182,"width":5.637376656633329}},"count":"count"},"metric":"metric","metricLabels":{"key":"metricLabels"},"valueInt64":"valueInt64"}]},{"originalStep":"originalStep","metricsNamespace":"metricsNamespace","metricValues":[{"valueHistogram":{"outlierStats":{"underflowCount":"underflowCount","overflowCount":"overflowCount","overflowMean":2.3021358869347655,"underflowMean":7.061401241503109},"bucketCounts":["bucketCounts","bucketCounts"],"bucketOptions":{"exponential":{"numberOfBuckets":0,"scale":6},"linear":{"numberOfBuckets":1,"start":5.962133916683182,"width":5.637376656633329}},"count":"count"},"metric":"metric","metricLabels":{"key":"metricLabels"},"valueInt64":"valueInt64"},{"valueHistogram":{"outlierStats":{"underflowCount":"underflowCount","overflowCount":"overflowCount","overflowMean":2.3021358869347655,"underflowMean":7.061401241503109},"bucketCounts":["bucketCounts","bucketCounts"],"bucketOptions":{"exponential":{"numberOfBuckets":0,"scale":6},"linear":{"numberOfBuckets":1,"start":5.962133916683182,"width":5.637376656633329}},"count":"count"},"metric":"metric","metricLabels":{"key":"metricLabels"},"valueInt64":"valueInt64"}]}]},"streamingScalingReport":{"activeBundleCount":9,"outstandingBytesCount":1,"activeThreadCount":3,"maximumBytes":"maximumBytes","maximumThreadCount":7,"outstandingBytes":"outstandingBytes","maximumBundleCount":2,"outstandingBundleCount":1,"maximumBytesCount":4},"workerHealthReport":{"msg":"msg","reportInterval":"reportInterval","vmIsHealthy":True,"vmBrokenCode":"vmBrokenCode","vmStartupTime":"vmStartupTime","pods":[{"key":""},{"key":""}],"vmIsBroken":True},"labels":{"key":"labels"}}],"location":"location"}
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
        path='/v1b3/projects/{project_id}/WorkerMessages'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

