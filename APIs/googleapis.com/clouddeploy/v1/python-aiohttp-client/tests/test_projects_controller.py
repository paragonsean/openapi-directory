# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.advance_rollout_request import AdvanceRolloutRequest
from openapi_server.models.approve_rollout_request import ApproveRolloutRequest
from openapi_server.models.automation import Automation
from openapi_server.models.custom_target_type import CustomTargetType
from openapi_server.models.delivery_pipeline import DeliveryPipeline
from openapi_server.models.ignore_job_request import IgnoreJobRequest
from openapi_server.models.list_automation_runs_response import ListAutomationRunsResponse
from openapi_server.models.list_automations_response import ListAutomationsResponse
from openapi_server.models.list_custom_target_types_response import ListCustomTargetTypesResponse
from openapi_server.models.list_delivery_pipelines_response import ListDeliveryPipelinesResponse
from openapi_server.models.list_job_runs_response import ListJobRunsResponse
from openapi_server.models.list_locations_response import ListLocationsResponse
from openapi_server.models.list_operations_response import ListOperationsResponse
from openapi_server.models.list_releases_response import ListReleasesResponse
from openapi_server.models.list_rollouts_response import ListRolloutsResponse
from openapi_server.models.list_targets_response import ListTargetsResponse
from openapi_server.models.operation import Operation
from openapi_server.models.policy import Policy
from openapi_server.models.release import Release
from openapi_server.models.retry_job_request import RetryJobRequest
from openapi_server.models.rollback_target_request import RollbackTargetRequest
from openapi_server.models.rollback_target_response import RollbackTargetResponse
from openapi_server.models.rollout import Rollout
from openapi_server.models.set_iam_policy_request import SetIamPolicyRequest
from openapi_server.models.target import Target
from openapi_server.models.test_iam_permissions_request import TestIamPermissionsRequest
from openapi_server.models.test_iam_permissions_response import TestIamPermissionsResponse


pytestmark = pytest.mark.asyncio

async def test_clouddeploy_projects_locations_custom_target_types_create(client):
    """Test case for clouddeploy_projects_locations_custom_target_types_create

    
    """
    body = {"uid":"uid","createTime":"createTime","customTargetTypeId":"customTargetTypeId","customActions":{"deployAction":"deployAction","renderAction":"renderAction","includeSkaffoldModules":[{"configs":["configs","configs"],"git":{"path":"path","ref":"ref","repo":"repo"},"googleCloudStorage":{"path":"path","source":"source"}},{"configs":["configs","configs"],"git":{"path":"path","ref":"ref","repo":"repo"},"googleCloudStorage":{"path":"path","source":"source"}}]},"name":"name","annotations":{"key":"annotations"},"description":"description","etag":"etag","updateTime":"updateTime","labels":{"key":"labels"}}
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
                    ('customTargetTypeId', 'custom_target_type_id_example'),
                    ('requestId', 'request_id_example'),
                    ('validateOnly', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/customTargetTypes'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clouddeploy_projects_locations_custom_target_types_list(client):
    """Test case for clouddeploy_projects_locations_custom_target_types_list

    
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
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/customTargetTypes'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clouddeploy_projects_locations_delivery_pipelines_automation_runs_list(client):
    """Test case for clouddeploy_projects_locations_delivery_pipelines_automation_runs_list

    
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
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/automationRuns'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clouddeploy_projects_locations_delivery_pipelines_automations_create(client):
    """Test case for clouddeploy_projects_locations_delivery_pipelines_automations_create

    
    """
    body = {"uid":"uid","createTime":"createTime","name":"name","annotations":{"key":"annotations"},"description":"description","etag":"etag","rules":[{"promoteReleaseRule":{"condition":{"targetsPresentCondition":{"missingTargets":["missingTargets","missingTargets"],"updateTime":"updateTime","status":True}},"wait":"wait","destinationTargetId":"destinationTargetId","id":"id","destinationPhase":"destinationPhase"},"advanceRolloutRule":{"condition":{"targetsPresentCondition":{"missingTargets":["missingTargets","missingTargets"],"updateTime":"updateTime","status":True}},"wait":"wait","sourcePhases":["sourcePhases","sourcePhases"],"id":"id"},"repairRolloutRule":{"condition":{"targetsPresentCondition":{"missingTargets":["missingTargets","missingTargets"],"updateTime":"updateTime","status":True}},"sourcePhases":["sourcePhases","sourcePhases"],"jobs":["jobs","jobs"],"repairModes":[{"rollback":{"destinationPhase":"destinationPhase"},"retry":{"backoffMode":"BACKOFF_MODE_UNSPECIFIED","wait":"wait","attempts":"attempts"}},{"rollback":{"destinationPhase":"destinationPhase"},"retry":{"backoffMode":"BACKOFF_MODE_UNSPECIFIED","wait":"wait","attempts":"attempts"}}],"id":"id"}},{"promoteReleaseRule":{"condition":{"targetsPresentCondition":{"missingTargets":["missingTargets","missingTargets"],"updateTime":"updateTime","status":True}},"wait":"wait","destinationTargetId":"destinationTargetId","id":"id","destinationPhase":"destinationPhase"},"advanceRolloutRule":{"condition":{"targetsPresentCondition":{"missingTargets":["missingTargets","missingTargets"],"updateTime":"updateTime","status":True}},"wait":"wait","sourcePhases":["sourcePhases","sourcePhases"],"id":"id"},"repairRolloutRule":{"condition":{"targetsPresentCondition":{"missingTargets":["missingTargets","missingTargets"],"updateTime":"updateTime","status":True}},"sourcePhases":["sourcePhases","sourcePhases"],"jobs":["jobs","jobs"],"repairModes":[{"rollback":{"destinationPhase":"destinationPhase"},"retry":{"backoffMode":"BACKOFF_MODE_UNSPECIFIED","wait":"wait","attempts":"attempts"}},{"rollback":{"destinationPhase":"destinationPhase"},"retry":{"backoffMode":"BACKOFF_MODE_UNSPECIFIED","wait":"wait","attempts":"attempts"}}],"id":"id"}}],"selector":{"targets":[{"id":"id","labels":{"key":"labels"}},{"id":"id","labels":{"key":"labels"}}]},"serviceAccount":"serviceAccount","updateTime":"updateTime","suspended":True,"labels":{"key":"labels"}}
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
                    ('automationId', 'automation_id_example'),
                    ('requestId', 'request_id_example'),
                    ('validateOnly', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/automations'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clouddeploy_projects_locations_delivery_pipelines_automations_list(client):
    """Test case for clouddeploy_projects_locations_delivery_pipelines_automations_list

    
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
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/automations'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clouddeploy_projects_locations_delivery_pipelines_create(client):
    """Test case for clouddeploy_projects_locations_delivery_pipelines_create

    
    """
    body = {"uid":"uid","condition":{"pipelineReadyCondition":{"updateTime":"updateTime","status":True},"targetsPresentCondition":{"missingTargets":["missingTargets","missingTargets"],"updateTime":"updateTime","status":True},"targetsTypeCondition":{"errorDetails":"errorDetails","status":True}},"createTime":"createTime","name":"name","annotations":{"key":"annotations"},"description":"description","etag":"etag","updateTime":"updateTime","serialPipeline":{"stages":[{"deployParameters":[{"matchTargetLabels":{"key":"matchTargetLabels"},"values":{"key":"values"}},{"matchTargetLabels":{"key":"matchTargetLabels"},"values":{"key":"values"}}],"targetId":"targetId","profiles":["profiles","profiles"],"strategy":{"standard":{"postdeploy":{"actions":["actions","actions"]},"verify":True,"predeploy":{"actions":["actions","actions"]}},"canary":{"customCanaryDeployment":{"phaseConfigs":[{"percentage":6,"postdeploy":{"actions":["actions","actions"]},"phaseId":"phaseId","profiles":["profiles","profiles"],"verify":True,"predeploy":{"actions":["actions","actions"]}},{"percentage":6,"postdeploy":{"actions":["actions","actions"]},"phaseId":"phaseId","profiles":["profiles","profiles"],"verify":True,"predeploy":{"actions":["actions","actions"]}}]},"canaryDeployment":{"postdeploy":{"actions":["actions","actions"]},"percentages":[0,0],"verify":True,"predeploy":{"actions":["actions","actions"]}},"runtimeConfig":{"kubernetes":{"gatewayServiceMesh":{"routeUpdateWaitTime":"routeUpdateWaitTime","service":"service","stableCutbackDuration":"stableCutbackDuration","deployment":"deployment","httpRoute":"httpRoute"},"serviceNetworking":{"service":"service","disablePodOverprovisioning":True,"deployment":"deployment"}},"cloudRun":{"canaryRevisionTags":["canaryRevisionTags","canaryRevisionTags"],"priorRevisionTags":["priorRevisionTags","priorRevisionTags"],"stableRevisionTags":["stableRevisionTags","stableRevisionTags"],"automaticTrafficControl":True}}}}},{"deployParameters":[{"matchTargetLabels":{"key":"matchTargetLabels"},"values":{"key":"values"}},{"matchTargetLabels":{"key":"matchTargetLabels"},"values":{"key":"values"}}],"targetId":"targetId","profiles":["profiles","profiles"],"strategy":{"standard":{"postdeploy":{"actions":["actions","actions"]},"verify":True,"predeploy":{"actions":["actions","actions"]}},"canary":{"customCanaryDeployment":{"phaseConfigs":[{"percentage":6,"postdeploy":{"actions":["actions","actions"]},"phaseId":"phaseId","profiles":["profiles","profiles"],"verify":True,"predeploy":{"actions":["actions","actions"]}},{"percentage":6,"postdeploy":{"actions":["actions","actions"]},"phaseId":"phaseId","profiles":["profiles","profiles"],"verify":True,"predeploy":{"actions":["actions","actions"]}}]},"canaryDeployment":{"postdeploy":{"actions":["actions","actions"]},"percentages":[0,0],"verify":True,"predeploy":{"actions":["actions","actions"]}},"runtimeConfig":{"kubernetes":{"gatewayServiceMesh":{"routeUpdateWaitTime":"routeUpdateWaitTime","service":"service","stableCutbackDuration":"stableCutbackDuration","deployment":"deployment","httpRoute":"httpRoute"},"serviceNetworking":{"service":"service","disablePodOverprovisioning":True,"deployment":"deployment"}},"cloudRun":{"canaryRevisionTags":["canaryRevisionTags","canaryRevisionTags"],"priorRevisionTags":["priorRevisionTags","priorRevisionTags"],"stableRevisionTags":["stableRevisionTags","stableRevisionTags"],"automaticTrafficControl":True}}}}}]},"suspended":True,"labels":{"key":"labels"}}
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
                    ('deliveryPipelineId', 'delivery_pipeline_id_example'),
                    ('requestId', 'request_id_example'),
                    ('validateOnly', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/deliveryPipelines'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clouddeploy_projects_locations_delivery_pipelines_list(client):
    """Test case for clouddeploy_projects_locations_delivery_pipelines_list

    
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
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/deliveryPipelines'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clouddeploy_projects_locations_delivery_pipelines_releases_abandon(client):
    """Test case for clouddeploy_projects_locations_delivery_pipelines_releases_abandon

    
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
        path='/v1/{nameabando}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clouddeploy_projects_locations_delivery_pipelines_releases_create(client):
    """Test case for clouddeploy_projects_locations_delivery_pipelines_releases_create

    
    """
    body = {"skaffoldConfigUri":"skaffoldConfigUri","renderStartTime":"renderStartTime","targetSnapshots":[{"gke":{"cluster":"cluster","internalIp":True},"executionConfigs":[{"executionTimeout":"executionTimeout","artifactStorage":"artifactStorage","serviceAccount":"serviceAccount","usages":["EXECUTION_ENVIRONMENT_USAGE_UNSPECIFIED","EXECUTION_ENVIRONMENT_USAGE_UNSPECIFIED"],"workerPool":"workerPool","privatePool":{"artifactStorage":"artifactStorage","serviceAccount":"serviceAccount","workerPool":"workerPool"},"defaultPool":{"artifactStorage":"artifactStorage","serviceAccount":"serviceAccount"}},{"executionTimeout":"executionTimeout","artifactStorage":"artifactStorage","serviceAccount":"serviceAccount","usages":["EXECUTION_ENVIRONMENT_USAGE_UNSPECIFIED","EXECUTION_ENVIRONMENT_USAGE_UNSPECIFIED"],"workerPool":"workerPool","privatePool":{"artifactStorage":"artifactStorage","serviceAccount":"serviceAccount","workerPool":"workerPool"},"defaultPool":{"artifactStorage":"artifactStorage","serviceAccount":"serviceAccount"}}],"multiTarget":{"targetIds":["targetIds","targetIds"]},"targetId":"targetId","customTarget":{"customTargetType":"customTargetType"},"annotations":{"key":"annotations"},"description":"description","run":{"location":"location"},"updateTime":"updateTime","anthosCluster":{"membership":"membership"},"labels":{"key":"labels"},"uid":"uid","deployParameters":{"key":"deployParameters"},"createTime":"createTime","requireApproval":True,"name":"name","etag":"etag"},{"gke":{"cluster":"cluster","internalIp":True},"executionConfigs":[{"executionTimeout":"executionTimeout","artifactStorage":"artifactStorage","serviceAccount":"serviceAccount","usages":["EXECUTION_ENVIRONMENT_USAGE_UNSPECIFIED","EXECUTION_ENVIRONMENT_USAGE_UNSPECIFIED"],"workerPool":"workerPool","privatePool":{"artifactStorage":"artifactStorage","serviceAccount":"serviceAccount","workerPool":"workerPool"},"defaultPool":{"artifactStorage":"artifactStorage","serviceAccount":"serviceAccount"}},{"executionTimeout":"executionTimeout","artifactStorage":"artifactStorage","serviceAccount":"serviceAccount","usages":["EXECUTION_ENVIRONMENT_USAGE_UNSPECIFIED","EXECUTION_ENVIRONMENT_USAGE_UNSPECIFIED"],"workerPool":"workerPool","privatePool":{"artifactStorage":"artifactStorage","serviceAccount":"serviceAccount","workerPool":"workerPool"},"defaultPool":{"artifactStorage":"artifactStorage","serviceAccount":"serviceAccount"}}],"multiTarget":{"targetIds":["targetIds","targetIds"]},"targetId":"targetId","customTarget":{"customTargetType":"customTargetType"},"annotations":{"key":"annotations"},"description":"description","run":{"location":"location"},"updateTime":"updateTime","anthosCluster":{"membership":"membership"},"labels":{"key":"labels"},"uid":"uid","deployParameters":{"key":"deployParameters"},"createTime":"createTime","requireApproval":True,"name":"name","etag":"etag"}],"renderEndTime":"renderEndTime","annotations":{"key":"annotations"},"description":"description","skaffoldConfigPath":"skaffoldConfigPath","targetArtifacts":{"key":{"manifestPath":"manifestPath","skaffoldConfigPath":"skaffoldConfigPath","artifactUri":"artifactUri","phaseArtifacts":{"key":{"manifestPath":"manifestPath","skaffoldConfigPath":"skaffoldConfigPath","jobManifestsPath":"jobManifestsPath"}}}},"deliveryPipelineSnapshot":{"uid":"uid","condition":{"pipelineReadyCondition":{"updateTime":"updateTime","status":True},"targetsPresentCondition":{"missingTargets":["missingTargets","missingTargets"],"updateTime":"updateTime","status":True},"targetsTypeCondition":{"errorDetails":"errorDetails","status":True}},"createTime":"createTime","name":"name","annotations":{"key":"annotations"},"description":"description","etag":"etag","updateTime":"updateTime","serialPipeline":{"stages":[{"deployParameters":[{"matchTargetLabels":{"key":"matchTargetLabels"},"values":{"key":"values"}},{"matchTargetLabels":{"key":"matchTargetLabels"},"values":{"key":"values"}}],"targetId":"targetId","profiles":["profiles","profiles"],"strategy":{"standard":{"postdeploy":{"actions":["actions","actions"]},"verify":True,"predeploy":{"actions":["actions","actions"]}},"canary":{"customCanaryDeployment":{"phaseConfigs":[{"percentage":6,"postdeploy":{"actions":["actions","actions"]},"phaseId":"phaseId","profiles":["profiles","profiles"],"verify":True,"predeploy":{"actions":["actions","actions"]}},{"percentage":6,"postdeploy":{"actions":["actions","actions"]},"phaseId":"phaseId","profiles":["profiles","profiles"],"verify":True,"predeploy":{"actions":["actions","actions"]}}]},"canaryDeployment":{"postdeploy":{"actions":["actions","actions"]},"percentages":[0,0],"verify":True,"predeploy":{"actions":["actions","actions"]}},"runtimeConfig":{"kubernetes":{"gatewayServiceMesh":{"routeUpdateWaitTime":"routeUpdateWaitTime","service":"service","stableCutbackDuration":"stableCutbackDuration","deployment":"deployment","httpRoute":"httpRoute"},"serviceNetworking":{"service":"service","disablePodOverprovisioning":True,"deployment":"deployment"}},"cloudRun":{"canaryRevisionTags":["canaryRevisionTags","canaryRevisionTags"],"priorRevisionTags":["priorRevisionTags","priorRevisionTags"],"stableRevisionTags":["stableRevisionTags","stableRevisionTags"],"automaticTrafficControl":True}}}}},{"deployParameters":[{"matchTargetLabels":{"key":"matchTargetLabels"},"values":{"key":"values"}},{"matchTargetLabels":{"key":"matchTargetLabels"},"values":{"key":"values"}}],"targetId":"targetId","profiles":["profiles","profiles"],"strategy":{"standard":{"postdeploy":{"actions":["actions","actions"]},"verify":True,"predeploy":{"actions":["actions","actions"]}},"canary":{"customCanaryDeployment":{"phaseConfigs":[{"percentage":6,"postdeploy":{"actions":["actions","actions"]},"phaseId":"phaseId","profiles":["profiles","profiles"],"verify":True,"predeploy":{"actions":["actions","actions"]}},{"percentage":6,"postdeploy":{"actions":["actions","actions"]},"phaseId":"phaseId","profiles":["profiles","profiles"],"verify":True,"predeploy":{"actions":["actions","actions"]}}]},"canaryDeployment":{"postdeploy":{"actions":["actions","actions"]},"percentages":[0,0],"verify":True,"predeploy":{"actions":["actions","actions"]}},"runtimeConfig":{"kubernetes":{"gatewayServiceMesh":{"routeUpdateWaitTime":"routeUpdateWaitTime","service":"service","stableCutbackDuration":"stableCutbackDuration","deployment":"deployment","httpRoute":"httpRoute"},"serviceNetworking":{"service":"service","disablePodOverprovisioning":True,"deployment":"deployment"}},"cloudRun":{"canaryRevisionTags":["canaryRevisionTags","canaryRevisionTags"],"priorRevisionTags":["priorRevisionTags","priorRevisionTags"],"stableRevisionTags":["stableRevisionTags","stableRevisionTags"],"automaticTrafficControl":True}}}}}]},"suspended":True,"labels":{"key":"labels"}},"labels":{"key":"labels"},"renderState":"RENDER_STATE_UNSPECIFIED","skaffoldVersion":"skaffoldVersion","buildArtifacts":[{"image":"image","tag":"tag"},{"image":"image","tag":"tag"}],"customTargetTypeSnapshots":[{"uid":"uid","createTime":"createTime","customTargetTypeId":"customTargetTypeId","customActions":{"deployAction":"deployAction","renderAction":"renderAction","includeSkaffoldModules":[{"configs":["configs","configs"],"git":{"path":"path","ref":"ref","repo":"repo"},"googleCloudStorage":{"path":"path","source":"source"}},{"configs":["configs","configs"],"git":{"path":"path","ref":"ref","repo":"repo"},"googleCloudStorage":{"path":"path","source":"source"}}]},"name":"name","annotations":{"key":"annotations"},"description":"description","etag":"etag","updateTime":"updateTime","labels":{"key":"labels"}},{"uid":"uid","createTime":"createTime","customTargetTypeId":"customTargetTypeId","customActions":{"deployAction":"deployAction","renderAction":"renderAction","includeSkaffoldModules":[{"configs":["configs","configs"],"git":{"path":"path","ref":"ref","repo":"repo"},"googleCloudStorage":{"path":"path","source":"source"}},{"configs":["configs","configs"],"git":{"path":"path","ref":"ref","repo":"repo"},"googleCloudStorage":{"path":"path","source":"source"}}]},"name":"name","annotations":{"key":"annotations"},"description":"description","etag":"etag","updateTime":"updateTime","labels":{"key":"labels"}}],"uid":"uid","condition":{"releaseReadyCondition":{"status":True},"skaffoldSupportedCondition":{"skaffoldSupportState":"SKAFFOLD_SUPPORT_STATE_UNSPECIFIED","maintenanceModeTime":"maintenanceModeTime","status":True,"supportExpirationTime":"supportExpirationTime"}},"deployParameters":{"key":"deployParameters"},"createTime":"createTime","name":"name","etag":"etag","abandoned":True,"targetRenders":{"key":{"metadata":{"custom":{"values":{"key":"values"}},"cloudRun":{"service":"service"}},"renderingState":"TARGET_RENDER_STATE_UNSPECIFIED","failureCause":"FAILURE_CAUSE_UNSPECIFIED","renderingBuild":"renderingBuild","failureMessage":"failureMessage"}}}
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
                    ('releaseId', 'release_id_example'),
                    ('requestId', 'request_id_example'),
                    ('validateOnly', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/releases'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clouddeploy_projects_locations_delivery_pipelines_releases_list(client):
    """Test case for clouddeploy_projects_locations_delivery_pipelines_releases_list

    
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
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/releases'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clouddeploy_projects_locations_delivery_pipelines_releases_rollouts_advance(client):
    """Test case for clouddeploy_projects_locations_delivery_pipelines_releases_rollouts_advance

    
    """
    body = {"phaseId":"phaseId"}
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
        path='/v1/{nameadvanc}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clouddeploy_projects_locations_delivery_pipelines_releases_rollouts_approve(client):
    """Test case for clouddeploy_projects_locations_delivery_pipelines_releases_rollouts_approve

    
    """
    body = {"approved":True}
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
        path='/v1/{nameapprov}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clouddeploy_projects_locations_delivery_pipelines_releases_rollouts_create(client):
    """Test case for clouddeploy_projects_locations_delivery_pipelines_releases_rollouts_create

    
    """
    body = {"metadata":{"automation":{"promoteAutomationRun":"promoteAutomationRun","advanceAutomationRuns":["advanceAutomationRuns","advanceAutomationRuns"],"currentRepairAutomationRun":"currentRepairAutomationRun","repairAutomationRuns":["repairAutomationRuns","repairAutomationRuns"]},"custom":{"values":{"key":"values"}},"cloudRun":{"service":"service","serviceUrls":["serviceUrls","serviceUrls"],"job":"job","revision":"revision"}},"targetId":"targetId","approvalState":"APPROVAL_STATE_UNSPECIFIED","annotations":{"key":"annotations"},"description":"description","deployStartTime":"deployStartTime","deployingBuild":"deployingBuild","enqueueTime":"enqueueTime","labels":{"key":"labels"},"rolledBackByRollouts":["rolledBackByRollouts","rolledBackByRollouts"],"uid":"uid","rollbackOfRollout":"rollbackOfRollout","controllerRollout":"controllerRollout","deployEndTime":"deployEndTime","createTime":"createTime","failureReason":"failureReason","name":"name","etag":"etag","state":"STATE_UNSPECIFIED","approveTime":"approveTime","deployFailureCause":"FAILURE_CAUSE_UNSPECIFIED","phases":[{"deploymentJobs":{"predeployJob":{"jobRun":"jobRun","predeployJob":{"actions":["actions","actions"]},"createChildRolloutJob":"{}","advanceChildRolloutJob":"{}","id":"id","state":"STATE_UNSPECIFIED","deployJob":"{}","postdeployJob":{"actions":["actions","actions"]},"verifyJob":"{}","skipMessage":"skipMessage"},"deployJob":{"jobRun":"jobRun","predeployJob":{"actions":["actions","actions"]},"createChildRolloutJob":"{}","advanceChildRolloutJob":"{}","id":"id","state":"STATE_UNSPECIFIED","deployJob":"{}","postdeployJob":{"actions":["actions","actions"]},"verifyJob":"{}","skipMessage":"skipMessage"},"postdeployJob":{"jobRun":"jobRun","predeployJob":{"actions":["actions","actions"]},"createChildRolloutJob":"{}","advanceChildRolloutJob":"{}","id":"id","state":"STATE_UNSPECIFIED","deployJob":"{}","postdeployJob":{"actions":["actions","actions"]},"verifyJob":"{}","skipMessage":"skipMessage"},"verifyJob":{"jobRun":"jobRun","predeployJob":{"actions":["actions","actions"]},"createChildRolloutJob":"{}","advanceChildRolloutJob":"{}","id":"id","state":"STATE_UNSPECIFIED","deployJob":"{}","postdeployJob":{"actions":["actions","actions"]},"verifyJob":"{}","skipMessage":"skipMessage"}},"id":"id","state":"STATE_UNSPECIFIED","childRolloutJobs":{"advanceRolloutJobs":[{"jobRun":"jobRun","predeployJob":{"actions":["actions","actions"]},"createChildRolloutJob":"{}","advanceChildRolloutJob":"{}","id":"id","state":"STATE_UNSPECIFIED","deployJob":"{}","postdeployJob":{"actions":["actions","actions"]},"verifyJob":"{}","skipMessage":"skipMessage"},{"jobRun":"jobRun","predeployJob":{"actions":["actions","actions"]},"createChildRolloutJob":"{}","advanceChildRolloutJob":"{}","id":"id","state":"STATE_UNSPECIFIED","deployJob":"{}","postdeployJob":{"actions":["actions","actions"]},"verifyJob":"{}","skipMessage":"skipMessage"}],"createRolloutJobs":[{"jobRun":"jobRun","predeployJob":{"actions":["actions","actions"]},"createChildRolloutJob":"{}","advanceChildRolloutJob":"{}","id":"id","state":"STATE_UNSPECIFIED","deployJob":"{}","postdeployJob":{"actions":["actions","actions"]},"verifyJob":"{}","skipMessage":"skipMessage"},{"jobRun":"jobRun","predeployJob":{"actions":["actions","actions"]},"createChildRolloutJob":"{}","advanceChildRolloutJob":"{}","id":"id","state":"STATE_UNSPECIFIED","deployJob":"{}","postdeployJob":{"actions":["actions","actions"]},"verifyJob":"{}","skipMessage":"skipMessage"}]},"skipMessage":"skipMessage"},{"deploymentJobs":{"predeployJob":{"jobRun":"jobRun","predeployJob":{"actions":["actions","actions"]},"createChildRolloutJob":"{}","advanceChildRolloutJob":"{}","id":"id","state":"STATE_UNSPECIFIED","deployJob":"{}","postdeployJob":{"actions":["actions","actions"]},"verifyJob":"{}","skipMessage":"skipMessage"},"deployJob":{"jobRun":"jobRun","predeployJob":{"actions":["actions","actions"]},"createChildRolloutJob":"{}","advanceChildRolloutJob":"{}","id":"id","state":"STATE_UNSPECIFIED","deployJob":"{}","postdeployJob":{"actions":["actions","actions"]},"verifyJob":"{}","skipMessage":"skipMessage"},"postdeployJob":{"jobRun":"jobRun","predeployJob":{"actions":["actions","actions"]},"createChildRolloutJob":"{}","advanceChildRolloutJob":"{}","id":"id","state":"STATE_UNSPECIFIED","deployJob":"{}","postdeployJob":{"actions":["actions","actions"]},"verifyJob":"{}","skipMessage":"skipMessage"},"verifyJob":{"jobRun":"jobRun","predeployJob":{"actions":["actions","actions"]},"createChildRolloutJob":"{}","advanceChildRolloutJob":"{}","id":"id","state":"STATE_UNSPECIFIED","deployJob":"{}","postdeployJob":{"actions":["actions","actions"]},"verifyJob":"{}","skipMessage":"skipMessage"}},"id":"id","state":"STATE_UNSPECIFIED","childRolloutJobs":{"advanceRolloutJobs":[{"jobRun":"jobRun","predeployJob":{"actions":["actions","actions"]},"createChildRolloutJob":"{}","advanceChildRolloutJob":"{}","id":"id","state":"STATE_UNSPECIFIED","deployJob":"{}","postdeployJob":{"actions":["actions","actions"]},"verifyJob":"{}","skipMessage":"skipMessage"},{"jobRun":"jobRun","predeployJob":{"actions":["actions","actions"]},"createChildRolloutJob":"{}","advanceChildRolloutJob":"{}","id":"id","state":"STATE_UNSPECIFIED","deployJob":"{}","postdeployJob":{"actions":["actions","actions"]},"verifyJob":"{}","skipMessage":"skipMessage"}],"createRolloutJobs":[{"jobRun":"jobRun","predeployJob":{"actions":["actions","actions"]},"createChildRolloutJob":"{}","advanceChildRolloutJob":"{}","id":"id","state":"STATE_UNSPECIFIED","deployJob":"{}","postdeployJob":{"actions":["actions","actions"]},"verifyJob":"{}","skipMessage":"skipMessage"},{"jobRun":"jobRun","predeployJob":{"actions":["actions","actions"]},"createChildRolloutJob":"{}","advanceChildRolloutJob":"{}","id":"id","state":"STATE_UNSPECIFIED","deployJob":"{}","postdeployJob":{"actions":["actions","actions"]},"verifyJob":"{}","skipMessage":"skipMessage"}]},"skipMessage":"skipMessage"}]}
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
                    ('requestId', 'request_id_example'),
                    ('rolloutId', 'rollout_id_example'),
                    ('startingPhaseId', 'starting_phase_id_example'),
                    ('validateOnly', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/rollouts'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clouddeploy_projects_locations_delivery_pipelines_releases_rollouts_ignore_job(client):
    """Test case for clouddeploy_projects_locations_delivery_pipelines_releases_rollouts_ignore_job

    
    """
    body = {"jobId":"jobId","phaseId":"phaseId"}
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
        path='/v1/{rolloutignore_jo}'.format(rollout='rollout_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clouddeploy_projects_locations_delivery_pipelines_releases_rollouts_job_runs_list(client):
    """Test case for clouddeploy_projects_locations_delivery_pipelines_releases_rollouts_job_runs_list

    
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
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/jobRuns'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clouddeploy_projects_locations_delivery_pipelines_releases_rollouts_job_runs_terminate(client):
    """Test case for clouddeploy_projects_locations_delivery_pipelines_releases_rollouts_job_runs_terminate

    
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
        path='/v1/{nameterminat}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clouddeploy_projects_locations_delivery_pipelines_releases_rollouts_list(client):
    """Test case for clouddeploy_projects_locations_delivery_pipelines_releases_rollouts_list

    
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
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/rollouts'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clouddeploy_projects_locations_delivery_pipelines_releases_rollouts_retry_job(client):
    """Test case for clouddeploy_projects_locations_delivery_pipelines_releases_rollouts_retry_job

    
    """
    body = {"jobId":"jobId","phaseId":"phaseId"}
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
        path='/v1/{rolloutretry_jo}'.format(rollout='rollout_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clouddeploy_projects_locations_delivery_pipelines_rollback_target(client):
    """Test case for clouddeploy_projects_locations_delivery_pipelines_rollback_target

    
    """
    body = {"validateOnly":True,"targetId":"targetId","releaseId":"releaseId","rolloutId":"rolloutId","rollbackConfig":{"rollout":{"metadata":{"automation":{"promoteAutomationRun":"promoteAutomationRun","advanceAutomationRuns":["advanceAutomationRuns","advanceAutomationRuns"],"currentRepairAutomationRun":"currentRepairAutomationRun","repairAutomationRuns":["repairAutomationRuns","repairAutomationRuns"]},"custom":{"values":{"key":"values"}},"cloudRun":{"service":"service","serviceUrls":["serviceUrls","serviceUrls"],"job":"job","revision":"revision"}},"targetId":"targetId","approvalState":"APPROVAL_STATE_UNSPECIFIED","annotations":{"key":"annotations"},"description":"description","deployStartTime":"deployStartTime","deployingBuild":"deployingBuild","enqueueTime":"enqueueTime","labels":{"key":"labels"},"rolledBackByRollouts":["rolledBackByRollouts","rolledBackByRollouts"],"uid":"uid","rollbackOfRollout":"rollbackOfRollout","controllerRollout":"controllerRollout","deployEndTime":"deployEndTime","createTime":"createTime","failureReason":"failureReason","name":"name","etag":"etag","state":"STATE_UNSPECIFIED","approveTime":"approveTime","deployFailureCause":"FAILURE_CAUSE_UNSPECIFIED","phases":[{"deploymentJobs":{"predeployJob":{"jobRun":"jobRun","predeployJob":{"actions":["actions","actions"]},"createChildRolloutJob":"{}","advanceChildRolloutJob":"{}","id":"id","state":"STATE_UNSPECIFIED","deployJob":"{}","postdeployJob":{"actions":["actions","actions"]},"verifyJob":"{}","skipMessage":"skipMessage"},"deployJob":{"jobRun":"jobRun","predeployJob":{"actions":["actions","actions"]},"createChildRolloutJob":"{}","advanceChildRolloutJob":"{}","id":"id","state":"STATE_UNSPECIFIED","deployJob":"{}","postdeployJob":{"actions":["actions","actions"]},"verifyJob":"{}","skipMessage":"skipMessage"},"postdeployJob":{"jobRun":"jobRun","predeployJob":{"actions":["actions","actions"]},"createChildRolloutJob":"{}","advanceChildRolloutJob":"{}","id":"id","state":"STATE_UNSPECIFIED","deployJob":"{}","postdeployJob":{"actions":["actions","actions"]},"verifyJob":"{}","skipMessage":"skipMessage"},"verifyJob":{"jobRun":"jobRun","predeployJob":{"actions":["actions","actions"]},"createChildRolloutJob":"{}","advanceChildRolloutJob":"{}","id":"id","state":"STATE_UNSPECIFIED","deployJob":"{}","postdeployJob":{"actions":["actions","actions"]},"verifyJob":"{}","skipMessage":"skipMessage"}},"id":"id","state":"STATE_UNSPECIFIED","childRolloutJobs":{"advanceRolloutJobs":[{"jobRun":"jobRun","predeployJob":{"actions":["actions","actions"]},"createChildRolloutJob":"{}","advanceChildRolloutJob":"{}","id":"id","state":"STATE_UNSPECIFIED","deployJob":"{}","postdeployJob":{"actions":["actions","actions"]},"verifyJob":"{}","skipMessage":"skipMessage"},{"jobRun":"jobRun","predeployJob":{"actions":["actions","actions"]},"createChildRolloutJob":"{}","advanceChildRolloutJob":"{}","id":"id","state":"STATE_UNSPECIFIED","deployJob":"{}","postdeployJob":{"actions":["actions","actions"]},"verifyJob":"{}","skipMessage":"skipMessage"}],"createRolloutJobs":[{"jobRun":"jobRun","predeployJob":{"actions":["actions","actions"]},"createChildRolloutJob":"{}","advanceChildRolloutJob":"{}","id":"id","state":"STATE_UNSPECIFIED","deployJob":"{}","postdeployJob":{"actions":["actions","actions"]},"verifyJob":"{}","skipMessage":"skipMessage"},{"jobRun":"jobRun","predeployJob":{"actions":["actions","actions"]},"createChildRolloutJob":"{}","advanceChildRolloutJob":"{}","id":"id","state":"STATE_UNSPECIFIED","deployJob":"{}","postdeployJob":{"actions":["actions","actions"]},"verifyJob":"{}","skipMessage":"skipMessage"}]},"skipMessage":"skipMessage"},{"deploymentJobs":{"predeployJob":{"jobRun":"jobRun","predeployJob":{"actions":["actions","actions"]},"createChildRolloutJob":"{}","advanceChildRolloutJob":"{}","id":"id","state":"STATE_UNSPECIFIED","deployJob":"{}","postdeployJob":{"actions":["actions","actions"]},"verifyJob":"{}","skipMessage":"skipMessage"},"deployJob":{"jobRun":"jobRun","predeployJob":{"actions":["actions","actions"]},"createChildRolloutJob":"{}","advanceChildRolloutJob":"{}","id":"id","state":"STATE_UNSPECIFIED","deployJob":"{}","postdeployJob":{"actions":["actions","actions"]},"verifyJob":"{}","skipMessage":"skipMessage"},"postdeployJob":{"jobRun":"jobRun","predeployJob":{"actions":["actions","actions"]},"createChildRolloutJob":"{}","advanceChildRolloutJob":"{}","id":"id","state":"STATE_UNSPECIFIED","deployJob":"{}","postdeployJob":{"actions":["actions","actions"]},"verifyJob":"{}","skipMessage":"skipMessage"},"verifyJob":{"jobRun":"jobRun","predeployJob":{"actions":["actions","actions"]},"createChildRolloutJob":"{}","advanceChildRolloutJob":"{}","id":"id","state":"STATE_UNSPECIFIED","deployJob":"{}","postdeployJob":{"actions":["actions","actions"]},"verifyJob":"{}","skipMessage":"skipMessage"}},"id":"id","state":"STATE_UNSPECIFIED","childRolloutJobs":{"advanceRolloutJobs":[{"jobRun":"jobRun","predeployJob":{"actions":["actions","actions"]},"createChildRolloutJob":"{}","advanceChildRolloutJob":"{}","id":"id","state":"STATE_UNSPECIFIED","deployJob":"{}","postdeployJob":{"actions":["actions","actions"]},"verifyJob":"{}","skipMessage":"skipMessage"},{"jobRun":"jobRun","predeployJob":{"actions":["actions","actions"]},"createChildRolloutJob":"{}","advanceChildRolloutJob":"{}","id":"id","state":"STATE_UNSPECIFIED","deployJob":"{}","postdeployJob":{"actions":["actions","actions"]},"verifyJob":"{}","skipMessage":"skipMessage"}],"createRolloutJobs":[{"jobRun":"jobRun","predeployJob":{"actions":["actions","actions"]},"createChildRolloutJob":"{}","advanceChildRolloutJob":"{}","id":"id","state":"STATE_UNSPECIFIED","deployJob":"{}","postdeployJob":{"actions":["actions","actions"]},"verifyJob":"{}","skipMessage":"skipMessage"},{"jobRun":"jobRun","predeployJob":{"actions":["actions","actions"]},"createChildRolloutJob":"{}","advanceChildRolloutJob":"{}","id":"id","state":"STATE_UNSPECIFIED","deployJob":"{}","postdeployJob":{"actions":["actions","actions"]},"verifyJob":"{}","skipMessage":"skipMessage"}]},"skipMessage":"skipMessage"}]},"startingPhaseId":"startingPhaseId"},"rolloutToRollBack":"rolloutToRollBack"}
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
        path='/v1/{namerollback_targe}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clouddeploy_projects_locations_list(client):
    """Test case for clouddeploy_projects_locations_list

    
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
        path='/v1/{name}/locations'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clouddeploy_projects_locations_operations_cancel(client):
    """Test case for clouddeploy_projects_locations_operations_cancel

    
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
        path='/v1/{namecance}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clouddeploy_projects_locations_operations_list(client):
    """Test case for clouddeploy_projects_locations_operations_list

    
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
        path='/v1/{name}/operations'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clouddeploy_projects_locations_targets_create(client):
    """Test case for clouddeploy_projects_locations_targets_create

    
    """
    body = {"gke":{"cluster":"cluster","internalIp":True},"executionConfigs":[{"executionTimeout":"executionTimeout","artifactStorage":"artifactStorage","serviceAccount":"serviceAccount","usages":["EXECUTION_ENVIRONMENT_USAGE_UNSPECIFIED","EXECUTION_ENVIRONMENT_USAGE_UNSPECIFIED"],"workerPool":"workerPool","privatePool":{"artifactStorage":"artifactStorage","serviceAccount":"serviceAccount","workerPool":"workerPool"},"defaultPool":{"artifactStorage":"artifactStorage","serviceAccount":"serviceAccount"}},{"executionTimeout":"executionTimeout","artifactStorage":"artifactStorage","serviceAccount":"serviceAccount","usages":["EXECUTION_ENVIRONMENT_USAGE_UNSPECIFIED","EXECUTION_ENVIRONMENT_USAGE_UNSPECIFIED"],"workerPool":"workerPool","privatePool":{"artifactStorage":"artifactStorage","serviceAccount":"serviceAccount","workerPool":"workerPool"},"defaultPool":{"artifactStorage":"artifactStorage","serviceAccount":"serviceAccount"}}],"multiTarget":{"targetIds":["targetIds","targetIds"]},"targetId":"targetId","customTarget":{"customTargetType":"customTargetType"},"annotations":{"key":"annotations"},"description":"description","run":{"location":"location"},"updateTime":"updateTime","anthosCluster":{"membership":"membership"},"labels":{"key":"labels"},"uid":"uid","deployParameters":{"key":"deployParameters"},"createTime":"createTime","requireApproval":True,"name":"name","etag":"etag"}
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
                    ('requestId', 'request_id_example'),
                    ('targetId', 'target_id_example'),
                    ('validateOnly', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/targets'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clouddeploy_projects_locations_targets_delete(client):
    """Test case for clouddeploy_projects_locations_targets_delete

    
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
                    ('allowMissing', True),
                    ('etag', 'etag_example'),
                    ('requestId', 'request_id_example'),
                    ('validateOnly', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clouddeploy_projects_locations_targets_get(client):
    """Test case for clouddeploy_projects_locations_targets_get

    
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
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clouddeploy_projects_locations_targets_get_iam_policy(client):
    """Test case for clouddeploy_projects_locations_targets_get_iam_policy

    
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
        path='/v1/{resourceget_iam_polic}'.format(resource='resource_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clouddeploy_projects_locations_targets_list(client):
    """Test case for clouddeploy_projects_locations_targets_list

    
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
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/targets'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clouddeploy_projects_locations_targets_patch(client):
    """Test case for clouddeploy_projects_locations_targets_patch

    
    """
    body = {"gke":{"cluster":"cluster","internalIp":True},"executionConfigs":[{"executionTimeout":"executionTimeout","artifactStorage":"artifactStorage","serviceAccount":"serviceAccount","usages":["EXECUTION_ENVIRONMENT_USAGE_UNSPECIFIED","EXECUTION_ENVIRONMENT_USAGE_UNSPECIFIED"],"workerPool":"workerPool","privatePool":{"artifactStorage":"artifactStorage","serviceAccount":"serviceAccount","workerPool":"workerPool"},"defaultPool":{"artifactStorage":"artifactStorage","serviceAccount":"serviceAccount"}},{"executionTimeout":"executionTimeout","artifactStorage":"artifactStorage","serviceAccount":"serviceAccount","usages":["EXECUTION_ENVIRONMENT_USAGE_UNSPECIFIED","EXECUTION_ENVIRONMENT_USAGE_UNSPECIFIED"],"workerPool":"workerPool","privatePool":{"artifactStorage":"artifactStorage","serviceAccount":"serviceAccount","workerPool":"workerPool"},"defaultPool":{"artifactStorage":"artifactStorage","serviceAccount":"serviceAccount"}}],"multiTarget":{"targetIds":["targetIds","targetIds"]},"targetId":"targetId","customTarget":{"customTargetType":"customTargetType"},"annotations":{"key":"annotations"},"description":"description","run":{"location":"location"},"updateTime":"updateTime","anthosCluster":{"membership":"membership"},"labels":{"key":"labels"},"uid":"uid","deployParameters":{"key":"deployParameters"},"createTime":"createTime","requireApproval":True,"name":"name","etag":"etag"}
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
                    ('requestId', 'request_id_example'),
                    ('updateMask', 'update_mask_example'),
                    ('validateOnly', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clouddeploy_projects_locations_targets_set_iam_policy(client):
    """Test case for clouddeploy_projects_locations_targets_set_iam_policy

    
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
        path='/v1/{resourceset_iam_polic}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clouddeploy_projects_locations_targets_test_iam_permissions(client):
    """Test case for clouddeploy_projects_locations_targets_test_iam_permissions

    
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
        path='/v1/{resourcetest_iam_permission}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

