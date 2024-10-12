# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_cloud_run_v2_cancel_execution_request import GoogleCloudRunV2CancelExecutionRequest
from openapi_server.models.google_cloud_run_v2_job import GoogleCloudRunV2Job
from openapi_server.models.google_cloud_run_v2_list_executions_response import GoogleCloudRunV2ListExecutionsResponse
from openapi_server.models.google_cloud_run_v2_list_jobs_response import GoogleCloudRunV2ListJobsResponse
from openapi_server.models.google_cloud_run_v2_list_revisions_response import GoogleCloudRunV2ListRevisionsResponse
from openapi_server.models.google_cloud_run_v2_list_services_response import GoogleCloudRunV2ListServicesResponse
from openapi_server.models.google_cloud_run_v2_list_tasks_response import GoogleCloudRunV2ListTasksResponse
from openapi_server.models.google_cloud_run_v2_revision import GoogleCloudRunV2Revision
from openapi_server.models.google_cloud_run_v2_run_job_request import GoogleCloudRunV2RunJobRequest
from openapi_server.models.google_cloud_run_v2_service import GoogleCloudRunV2Service
from openapi_server.models.google_iam_v1_policy import GoogleIamV1Policy
from openapi_server.models.google_iam_v1_set_iam_policy_request import GoogleIamV1SetIamPolicyRequest
from openapi_server.models.google_iam_v1_test_iam_permissions_request import GoogleIamV1TestIamPermissionsRequest
from openapi_server.models.google_iam_v1_test_iam_permissions_response import GoogleIamV1TestIamPermissionsResponse
from openapi_server.models.google_longrunning_list_operations_response import GoogleLongrunningListOperationsResponse
from openapi_server.models.google_longrunning_operation import GoogleLongrunningOperation
from openapi_server.models.google_longrunning_wait_operation_request import GoogleLongrunningWaitOperationRequest


pytestmark = pytest.mark.asyncio

async def test_run_projects_locations_jobs_create(client):
    """Test case for run_projects_locations_jobs_create

    
    """
    body = {"generation":"generation","template":{"template":{"maxRetries":9,"volumes":[{"cloudSqlInstance":{"instances":["instances","instances"]},"gcs":{"bucket":"bucket","readOnly":True},"emptyDir":{"sizeLimit":"sizeLimit","medium":"MEDIUM_UNSPECIFIED"},"name":"name","nfs":{"path":"path","server":"server","readOnly":True},"secret":{"defaultMode":1,"secret":"secret","items":[{"mode":1,"path":"path","version":"version"},{"mode":1,"path":"path","version":"version"}]}},{"cloudSqlInstance":{"instances":["instances","instances"]},"gcs":{"bucket":"bucket","readOnly":True},"emptyDir":{"sizeLimit":"sizeLimit","medium":"MEDIUM_UNSPECIFIED"},"name":"name","nfs":{"path":"path","server":"server","readOnly":True},"secret":{"defaultMode":1,"secret":"secret","items":[{"mode":1,"path":"path","version":"version"},{"mode":1,"path":"path","version":"version"}]}}],"vpcAccess":{"networkInterfaces":[{"subnetwork":"subnetwork","network":"network","tags":["tags","tags"]},{"subnetwork":"subnetwork","network":"network","tags":["tags","tags"]}],"connector":"connector","egress":"VPC_EGRESS_UNSPECIFIED"},"containers":[{"args":["args","args"],"image":"image","livenessProbe":{"failureThreshold":0,"periodSeconds":5,"tcpSocket":{"port":2},"timeoutSeconds":7,"initialDelaySeconds":5,"grpc":{"port":6,"service":"service"},"httpGet":{"path":"path","port":1,"httpHeaders":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}},"dependsOn":["dependsOn","dependsOn"],"workingDir":"workingDir","name":"name","resources":{"startupCpuBoost":True,"cpuIdle":True,"limits":{"key":"limits"}},"startupProbe":{"failureThreshold":0,"periodSeconds":5,"tcpSocket":{"port":2},"timeoutSeconds":7,"initialDelaySeconds":5,"grpc":{"port":6,"service":"service"},"httpGet":{"path":"path","port":1,"httpHeaders":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}},"env":[{"name":"name","value":"value","valueSource":{"secretKeyRef":{"secret":"secret","version":"version"}}},{"name":"name","value":"value","valueSource":{"secretKeyRef":{"secret":"secret","version":"version"}}}],"ports":[{"name":"name","containerPort":9},{"name":"name","containerPort":9}],"command":["command","command"],"volumeMounts":[{"mountPath":"mountPath","name":"name"},{"mountPath":"mountPath","name":"name"}]},{"args":["args","args"],"image":"image","livenessProbe":{"failureThreshold":0,"periodSeconds":5,"tcpSocket":{"port":2},"timeoutSeconds":7,"initialDelaySeconds":5,"grpc":{"port":6,"service":"service"},"httpGet":{"path":"path","port":1,"httpHeaders":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}},"dependsOn":["dependsOn","dependsOn"],"workingDir":"workingDir","name":"name","resources":{"startupCpuBoost":True,"cpuIdle":True,"limits":{"key":"limits"}},"startupProbe":{"failureThreshold":0,"periodSeconds":5,"tcpSocket":{"port":2},"timeoutSeconds":7,"initialDelaySeconds":5,"grpc":{"port":6,"service":"service"},"httpGet":{"path":"path","port":1,"httpHeaders":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}},"env":[{"name":"name","value":"value","valueSource":{"secretKeyRef":{"secret":"secret","version":"version"}}},{"name":"name","value":"value","valueSource":{"secretKeyRef":{"secret":"secret","version":"version"}}}],"ports":[{"name":"name","containerPort":9},{"name":"name","containerPort":9}],"command":["command","command"],"volumeMounts":[{"mountPath":"mountPath","name":"name"},{"mountPath":"mountPath","name":"name"}]}],"serviceAccount":"serviceAccount","encryptionKey":"encryptionKey","timeout":"timeout","executionEnvironment":"EXECUTION_ENVIRONMENT_UNSPECIFIED"},"taskCount":1,"parallelism":6,"annotations":{"key":"annotations"},"labels":{"key":"labels"}},"creator":"creator","terminalCondition":{"severity":"SEVERITY_UNSPECIFIED","reason":"COMMON_REASON_UNDEFINED","revisionReason":"REVISION_REASON_UNDEFINED","executionReason":"EXECUTION_REASON_UNDEFINED","state":"STATE_UNSPECIFIED","lastTransitionTime":"lastTransitionTime","message":"message","type":"type"},"annotations":{"key":"annotations"},"lastModifier":"lastModifier","reconciling":True,"satisfiesPzs":True,"updateTime":"updateTime","launchStage":"LAUNCH_STAGE_UNSPECIFIED","clientVersion":"clientVersion","labels":{"key":"labels"},"uid":"uid","expireTime":"expireTime","createTime":"createTime","deleteTime":"deleteTime","name":"name","client":"client","executionCount":0,"etag":"etag","binaryAuthorization":{"breakglassJustification":"breakglassJustification","useDefault":True},"conditions":[{"severity":"SEVERITY_UNSPECIFIED","reason":"COMMON_REASON_UNDEFINED","revisionReason":"REVISION_REASON_UNDEFINED","executionReason":"EXECUTION_REASON_UNDEFINED","state":"STATE_UNSPECIFIED","lastTransitionTime":"lastTransitionTime","message":"message","type":"type"},{"severity":"SEVERITY_UNSPECIFIED","reason":"COMMON_REASON_UNDEFINED","revisionReason":"REVISION_REASON_UNDEFINED","executionReason":"EXECUTION_REASON_UNDEFINED","state":"STATE_UNSPECIFIED","lastTransitionTime":"lastTransitionTime","message":"message","type":"type"}],"latestCreatedExecution":{"completionTime":"completionTime","createTime":"createTime","name":"name"},"observedGeneration":"observedGeneration"}
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
                    ('validateOnly', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/{parent}/jobs'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_projects_locations_jobs_executions_cancel(client):
    """Test case for run_projects_locations_jobs_executions_cancel

    
    """
    body = {"validateOnly":True,"etag":"etag"}
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
        path='/v2/{namecance}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_projects_locations_jobs_executions_list(client):
    """Test case for run_projects_locations_jobs_executions_list

    
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
                    ('pageToken', 'page_token_example'),
                    ('showDeleted', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/{parent}/executions'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_projects_locations_jobs_executions_tasks_list(client):
    """Test case for run_projects_locations_jobs_executions_tasks_list

    
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
                    ('pageToken', 'page_token_example'),
                    ('showDeleted', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/{parent}/tasks'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_projects_locations_jobs_list(client):
    """Test case for run_projects_locations_jobs_list

    
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
                    ('pageToken', 'page_token_example'),
                    ('showDeleted', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/{parent}/jobs'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_projects_locations_jobs_run(client):
    """Test case for run_projects_locations_jobs_run

    
    """
    body = {"validateOnly":True,"etag":"etag","overrides":{"taskCount":0,"containerOverrides":[{"args":["args","args"],"name":"name","env":[{"name":"name","value":"value","valueSource":{"secretKeyRef":{"secret":"secret","version":"version"}}},{"name":"name","value":"value","valueSource":{"secretKeyRef":{"secret":"secret","version":"version"}}}],"clearArgs":True},{"args":["args","args"],"name":"name","env":[{"name":"name","value":"value","valueSource":{"secretKeyRef":{"secret":"secret","version":"version"}}},{"name":"name","value":"value","valueSource":{"secretKeyRef":{"secret":"secret","version":"version"}}}],"clearArgs":True}],"timeout":"timeout"}}
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
        path='/v2/{nameru}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_projects_locations_operations_list(client):
    """Test case for run_projects_locations_operations_list

    
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
        path='/v2/{name}/operations'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_projects_locations_operations_wait(client):
    """Test case for run_projects_locations_operations_wait

    
    """
    body = {"timeout":"timeout"}
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
        path='/v2/{namewai}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_projects_locations_services_create(client):
    """Test case for run_projects_locations_services_create

    
    """
    body = {"template":{"maxInstanceRequestConcurrency":6,"scaling":{"maxInstanceCount":2,"minInstanceCount":4},"sessionAffinity":True,"volumes":[{"cloudSqlInstance":{"instances":["instances","instances"]},"gcs":{"bucket":"bucket","readOnly":True},"emptyDir":{"sizeLimit":"sizeLimit","medium":"MEDIUM_UNSPECIFIED"},"name":"name","nfs":{"path":"path","server":"server","readOnly":True},"secret":{"defaultMode":1,"secret":"secret","items":[{"mode":1,"path":"path","version":"version"},{"mode":1,"path":"path","version":"version"}]}},{"cloudSqlInstance":{"instances":["instances","instances"]},"gcs":{"bucket":"bucket","readOnly":True},"emptyDir":{"sizeLimit":"sizeLimit","medium":"MEDIUM_UNSPECIFIED"},"name":"name","nfs":{"path":"path","server":"server","readOnly":True},"secret":{"defaultMode":1,"secret":"secret","items":[{"mode":1,"path":"path","version":"version"},{"mode":1,"path":"path","version":"version"}]}}],"annotations":{"key":"annotations"},"vpcAccess":{"networkInterfaces":[{"subnetwork":"subnetwork","network":"network","tags":["tags","tags"]},{"subnetwork":"subnetwork","network":"network","tags":["tags","tags"]}],"connector":"connector","egress":"VPC_EGRESS_UNSPECIFIED"},"serviceAccount":"serviceAccount","encryptionKey":"encryptionKey","healthCheckDisabled":True,"timeout":"timeout","executionEnvironment":"EXECUTION_ENVIRONMENT_UNSPECIFIED","labels":{"key":"labels"},"revision":"revision","containers":[{"args":["args","args"],"image":"image","livenessProbe":{"failureThreshold":0,"periodSeconds":5,"tcpSocket":{"port":2},"timeoutSeconds":7,"initialDelaySeconds":5,"grpc":{"port":6,"service":"service"},"httpGet":{"path":"path","port":1,"httpHeaders":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}},"dependsOn":["dependsOn","dependsOn"],"workingDir":"workingDir","name":"name","resources":{"startupCpuBoost":True,"cpuIdle":True,"limits":{"key":"limits"}},"startupProbe":{"failureThreshold":0,"periodSeconds":5,"tcpSocket":{"port":2},"timeoutSeconds":7,"initialDelaySeconds":5,"grpc":{"port":6,"service":"service"},"httpGet":{"path":"path","port":1,"httpHeaders":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}},"env":[{"name":"name","value":"value","valueSource":{"secretKeyRef":{"secret":"secret","version":"version"}}},{"name":"name","value":"value","valueSource":{"secretKeyRef":{"secret":"secret","version":"version"}}}],"ports":[{"name":"name","containerPort":9},{"name":"name","containerPort":9}],"command":["command","command"],"volumeMounts":[{"mountPath":"mountPath","name":"name"},{"mountPath":"mountPath","name":"name"}]},{"args":["args","args"],"image":"image","livenessProbe":{"failureThreshold":0,"periodSeconds":5,"tcpSocket":{"port":2},"timeoutSeconds":7,"initialDelaySeconds":5,"grpc":{"port":6,"service":"service"},"httpGet":{"path":"path","port":1,"httpHeaders":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}},"dependsOn":["dependsOn","dependsOn"],"workingDir":"workingDir","name":"name","resources":{"startupCpuBoost":True,"cpuIdle":True,"limits":{"key":"limits"}},"startupProbe":{"failureThreshold":0,"periodSeconds":5,"tcpSocket":{"port":2},"timeoutSeconds":7,"initialDelaySeconds":5,"grpc":{"port":6,"service":"service"},"httpGet":{"path":"path","port":1,"httpHeaders":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}},"env":[{"name":"name","value":"value","valueSource":{"secretKeyRef":{"secret":"secret","version":"version"}}},{"name":"name","value":"value","valueSource":{"secretKeyRef":{"secret":"secret","version":"version"}}}],"ports":[{"name":"name","containerPort":9},{"name":"name","containerPort":9}],"command":["command","command"],"volumeMounts":[{"mountPath":"mountPath","name":"name"},{"mountPath":"mountPath","name":"name"}]}]},"terminalCondition":{"severity":"SEVERITY_UNSPECIFIED","reason":"COMMON_REASON_UNDEFINED","revisionReason":"REVISION_REASON_UNDEFINED","executionReason":"EXECUTION_REASON_UNDEFINED","state":"STATE_UNSPECIFIED","lastTransitionTime":"lastTransitionTime","message":"message","type":"type"},"latestCreatedRevision":"latestCreatedRevision","annotations":{"key":"annotations"},"description":"description","lastModifier":"lastModifier","reconciling":True,"satisfiesPzs":True,"clientVersion":"clientVersion","uid":"uid","customAudiences":["customAudiences","customAudiences"],"client":"client","binaryAuthorization":{"breakglassJustification":"breakglassJustification","useDefault":True},"defaultUriDisabled":True,"latestReadyRevision":"latestReadyRevision","traffic":[{"tag":"tag","type":"TRAFFIC_TARGET_ALLOCATION_TYPE_UNSPECIFIED","percent":1,"revision":"revision"},{"tag":"tag","type":"TRAFFIC_TARGET_ALLOCATION_TYPE_UNSPECIFIED","percent":1,"revision":"revision"}],"generation":"generation","creator":"creator","scaling":{"minInstanceCount":0},"updateTime":"updateTime","launchStage":"LAUNCH_STAGE_UNSPECIFIED","uri":"uri","labels":{"key":"labels"},"ingress":"INGRESS_TRAFFIC_UNSPECIFIED","expireTime":"expireTime","createTime":"createTime","deleteTime":"deleteTime","name":"name","etag":"etag","trafficStatuses":[{"tag":"tag","type":"TRAFFIC_TARGET_ALLOCATION_TYPE_UNSPECIFIED","percent":5,"uri":"uri","revision":"revision"},{"tag":"tag","type":"TRAFFIC_TARGET_ALLOCATION_TYPE_UNSPECIFIED","percent":5,"uri":"uri","revision":"revision"}],"conditions":[{"severity":"SEVERITY_UNSPECIFIED","reason":"COMMON_REASON_UNDEFINED","revisionReason":"REVISION_REASON_UNDEFINED","executionReason":"EXECUTION_REASON_UNDEFINED","state":"STATE_UNSPECIFIED","lastTransitionTime":"lastTransitionTime","message":"message","type":"type"},{"severity":"SEVERITY_UNSPECIFIED","reason":"COMMON_REASON_UNDEFINED","revisionReason":"REVISION_REASON_UNDEFINED","executionReason":"EXECUTION_REASON_UNDEFINED","state":"STATE_UNSPECIFIED","lastTransitionTime":"lastTransitionTime","message":"message","type":"type"}],"observedGeneration":"observedGeneration"}
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
                    ('serviceId', 'service_id_example'),
                    ('validateOnly', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/{parent}/services'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_projects_locations_services_get_iam_policy(client):
    """Test case for run_projects_locations_services_get_iam_policy

    
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
                    ('options.requestedPolicyVersion', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/{resourceget_iam_polic}'.format(resource='resource_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_projects_locations_services_list(client):
    """Test case for run_projects_locations_services_list

    
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
                    ('pageToken', 'page_token_example'),
                    ('showDeleted', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/{parent}/services'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_projects_locations_services_patch(client):
    """Test case for run_projects_locations_services_patch

    
    """
    body = {"template":{"maxInstanceRequestConcurrency":6,"scaling":{"maxInstanceCount":2,"minInstanceCount":4},"sessionAffinity":True,"volumes":[{"cloudSqlInstance":{"instances":["instances","instances"]},"gcs":{"bucket":"bucket","readOnly":True},"emptyDir":{"sizeLimit":"sizeLimit","medium":"MEDIUM_UNSPECIFIED"},"name":"name","nfs":{"path":"path","server":"server","readOnly":True},"secret":{"defaultMode":1,"secret":"secret","items":[{"mode":1,"path":"path","version":"version"},{"mode":1,"path":"path","version":"version"}]}},{"cloudSqlInstance":{"instances":["instances","instances"]},"gcs":{"bucket":"bucket","readOnly":True},"emptyDir":{"sizeLimit":"sizeLimit","medium":"MEDIUM_UNSPECIFIED"},"name":"name","nfs":{"path":"path","server":"server","readOnly":True},"secret":{"defaultMode":1,"secret":"secret","items":[{"mode":1,"path":"path","version":"version"},{"mode":1,"path":"path","version":"version"}]}}],"annotations":{"key":"annotations"},"vpcAccess":{"networkInterfaces":[{"subnetwork":"subnetwork","network":"network","tags":["tags","tags"]},{"subnetwork":"subnetwork","network":"network","tags":["tags","tags"]}],"connector":"connector","egress":"VPC_EGRESS_UNSPECIFIED"},"serviceAccount":"serviceAccount","encryptionKey":"encryptionKey","healthCheckDisabled":True,"timeout":"timeout","executionEnvironment":"EXECUTION_ENVIRONMENT_UNSPECIFIED","labels":{"key":"labels"},"revision":"revision","containers":[{"args":["args","args"],"image":"image","livenessProbe":{"failureThreshold":0,"periodSeconds":5,"tcpSocket":{"port":2},"timeoutSeconds":7,"initialDelaySeconds":5,"grpc":{"port":6,"service":"service"},"httpGet":{"path":"path","port":1,"httpHeaders":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}},"dependsOn":["dependsOn","dependsOn"],"workingDir":"workingDir","name":"name","resources":{"startupCpuBoost":True,"cpuIdle":True,"limits":{"key":"limits"}},"startupProbe":{"failureThreshold":0,"periodSeconds":5,"tcpSocket":{"port":2},"timeoutSeconds":7,"initialDelaySeconds":5,"grpc":{"port":6,"service":"service"},"httpGet":{"path":"path","port":1,"httpHeaders":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}},"env":[{"name":"name","value":"value","valueSource":{"secretKeyRef":{"secret":"secret","version":"version"}}},{"name":"name","value":"value","valueSource":{"secretKeyRef":{"secret":"secret","version":"version"}}}],"ports":[{"name":"name","containerPort":9},{"name":"name","containerPort":9}],"command":["command","command"],"volumeMounts":[{"mountPath":"mountPath","name":"name"},{"mountPath":"mountPath","name":"name"}]},{"args":["args","args"],"image":"image","livenessProbe":{"failureThreshold":0,"periodSeconds":5,"tcpSocket":{"port":2},"timeoutSeconds":7,"initialDelaySeconds":5,"grpc":{"port":6,"service":"service"},"httpGet":{"path":"path","port":1,"httpHeaders":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}},"dependsOn":["dependsOn","dependsOn"],"workingDir":"workingDir","name":"name","resources":{"startupCpuBoost":True,"cpuIdle":True,"limits":{"key":"limits"}},"startupProbe":{"failureThreshold":0,"periodSeconds":5,"tcpSocket":{"port":2},"timeoutSeconds":7,"initialDelaySeconds":5,"grpc":{"port":6,"service":"service"},"httpGet":{"path":"path","port":1,"httpHeaders":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}},"env":[{"name":"name","value":"value","valueSource":{"secretKeyRef":{"secret":"secret","version":"version"}}},{"name":"name","value":"value","valueSource":{"secretKeyRef":{"secret":"secret","version":"version"}}}],"ports":[{"name":"name","containerPort":9},{"name":"name","containerPort":9}],"command":["command","command"],"volumeMounts":[{"mountPath":"mountPath","name":"name"},{"mountPath":"mountPath","name":"name"}]}]},"terminalCondition":{"severity":"SEVERITY_UNSPECIFIED","reason":"COMMON_REASON_UNDEFINED","revisionReason":"REVISION_REASON_UNDEFINED","executionReason":"EXECUTION_REASON_UNDEFINED","state":"STATE_UNSPECIFIED","lastTransitionTime":"lastTransitionTime","message":"message","type":"type"},"latestCreatedRevision":"latestCreatedRevision","annotations":{"key":"annotations"},"description":"description","lastModifier":"lastModifier","reconciling":True,"satisfiesPzs":True,"clientVersion":"clientVersion","uid":"uid","customAudiences":["customAudiences","customAudiences"],"client":"client","binaryAuthorization":{"breakglassJustification":"breakglassJustification","useDefault":True},"defaultUriDisabled":True,"latestReadyRevision":"latestReadyRevision","traffic":[{"tag":"tag","type":"TRAFFIC_TARGET_ALLOCATION_TYPE_UNSPECIFIED","percent":1,"revision":"revision"},{"tag":"tag","type":"TRAFFIC_TARGET_ALLOCATION_TYPE_UNSPECIFIED","percent":1,"revision":"revision"}],"generation":"generation","creator":"creator","scaling":{"minInstanceCount":0},"updateTime":"updateTime","launchStage":"LAUNCH_STAGE_UNSPECIFIED","uri":"uri","labels":{"key":"labels"},"ingress":"INGRESS_TRAFFIC_UNSPECIFIED","expireTime":"expireTime","createTime":"createTime","deleteTime":"deleteTime","name":"name","etag":"etag","trafficStatuses":[{"tag":"tag","type":"TRAFFIC_TARGET_ALLOCATION_TYPE_UNSPECIFIED","percent":5,"uri":"uri","revision":"revision"},{"tag":"tag","type":"TRAFFIC_TARGET_ALLOCATION_TYPE_UNSPECIFIED","percent":5,"uri":"uri","revision":"revision"}],"conditions":[{"severity":"SEVERITY_UNSPECIFIED","reason":"COMMON_REASON_UNDEFINED","revisionReason":"REVISION_REASON_UNDEFINED","executionReason":"EXECUTION_REASON_UNDEFINED","state":"STATE_UNSPECIFIED","lastTransitionTime":"lastTransitionTime","message":"message","type":"type"},{"severity":"SEVERITY_UNSPECIFIED","reason":"COMMON_REASON_UNDEFINED","revisionReason":"REVISION_REASON_UNDEFINED","executionReason":"EXECUTION_REASON_UNDEFINED","state":"STATE_UNSPECIFIED","lastTransitionTime":"lastTransitionTime","message":"message","type":"type"}],"observedGeneration":"observedGeneration"}
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
                    ('allowMissing', True),
                    ('validateOnly', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v2/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_projects_locations_services_revisions_delete(client):
    """Test case for run_projects_locations_services_revisions_delete

    
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
                    ('etag', 'etag_example'),
                    ('validateOnly', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_projects_locations_services_revisions_get(client):
    """Test case for run_projects_locations_services_revisions_get

    
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
        path='/v2/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_projects_locations_services_revisions_list(client):
    """Test case for run_projects_locations_services_revisions_list

    
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
                    ('pageToken', 'page_token_example'),
                    ('showDeleted', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/{parent}/revisions'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_projects_locations_services_set_iam_policy(client):
    """Test case for run_projects_locations_services_set_iam_policy

    
    """
    body = {"updateMask":"updateMask","policy":{"bindings":[{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"role":"role","members":["members","members"]},{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"role":"role","members":["members","members"]}],"etag":"etag","version":0,"auditConfigs":[{"auditLogConfigs":[{"logType":"LOG_TYPE_UNSPECIFIED","exemptedMembers":["exemptedMembers","exemptedMembers"]},{"logType":"LOG_TYPE_UNSPECIFIED","exemptedMembers":["exemptedMembers","exemptedMembers"]}],"service":"service"},{"auditLogConfigs":[{"logType":"LOG_TYPE_UNSPECIFIED","exemptedMembers":["exemptedMembers","exemptedMembers"]},{"logType":"LOG_TYPE_UNSPECIFIED","exemptedMembers":["exemptedMembers","exemptedMembers"]}],"service":"service"}]}}
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
        path='/v2/{resourceset_iam_polic}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_projects_locations_services_test_iam_permissions(client):
    """Test case for run_projects_locations_services_test_iam_permissions

    
    """
    body = {"permissions":["permissions","permissions"]}
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
        path='/v2/{resourcetest_iam_permission}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

