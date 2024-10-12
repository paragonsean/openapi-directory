# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cancel_test_matrix_response import CancelTestMatrixResponse
from openapi_server.models.device_session import DeviceSession
from openapi_server.models.list_device_sessions_response import ListDeviceSessionsResponse
from openapi_server.models.test_matrix import TestMatrix


pytestmark = pytest.mark.asyncio

async def test_testing_projects_device_sessions_cancel(client):
    """Test case for testing_projects_device_sessions_cancel

    
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

async def test_testing_projects_device_sessions_create(client):
    """Test case for testing_projects_device_sessions_create

    
    """
    body = {"inactivityTimeout":"inactivityTimeout","expireTime":"expireTime","stateHistories":[{"sessionState":"SESSION_STATE_UNSPECIFIED","eventTime":"eventTime","stateMessage":"stateMessage"},{"sessionState":"SESSION_STATE_UNSPECIFIED","eventTime":"eventTime","stateMessage":"stateMessage"}],"createTime":"createTime","activeStartTime":"activeStartTime","displayName":"displayName","name":"name","state":"SESSION_STATE_UNSPECIFIED","ttl":"ttl","androidDevice":{"orientation":"orientation","androidVersionId":"androidVersionId","locale":"locale","androidModelId":"androidModelId"}}
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
        path='/v1/{parent}/deviceSessions'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_testing_projects_device_sessions_get(client):
    """Test case for testing_projects_device_sessions_get

    
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

async def test_testing_projects_device_sessions_list(client):
    """Test case for testing_projects_device_sessions_list

    
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
        path='/v1/{parent}/deviceSessions'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_testing_projects_device_sessions_patch(client):
    """Test case for testing_projects_device_sessions_patch

    
    """
    body = {"inactivityTimeout":"inactivityTimeout","expireTime":"expireTime","stateHistories":[{"sessionState":"SESSION_STATE_UNSPECIFIED","eventTime":"eventTime","stateMessage":"stateMessage"},{"sessionState":"SESSION_STATE_UNSPECIFIED","eventTime":"eventTime","stateMessage":"stateMessage"}],"createTime":"createTime","activeStartTime":"activeStartTime","displayName":"displayName","name":"name","state":"SESSION_STATE_UNSPECIFIED","ttl":"ttl","androidDevice":{"orientation":"orientation","androidVersionId":"androidVersionId","locale":"locale","androidModelId":"androidModelId"}}
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
        method='PATCH',
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_testing_projects_test_matrices_cancel(client):
    """Test case for testing_projects_test_matrices_cancel

    
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
        path='/v1/projects/{project_id}/testMatrices/{test_matrix_idcance}'.format(project_id='project_id_example', test_matrix_id='test_matrix_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_testing_projects_test_matrices_create(client):
    """Test case for testing_projects_test_matrices_create

    
    """
    body = {"environmentMatrix":{"androidDeviceList":{"androidDevices":[{"orientation":"orientation","androidVersionId":"androidVersionId","locale":"locale","androidModelId":"androidModelId"},{"orientation":"orientation","androidVersionId":"androidVersionId","locale":"locale","androidModelId":"androidModelId"}]},"androidMatrix":{"locales":["locales","locales"],"orientations":["orientations","orientations"],"androidModelIds":["androidModelIds","androidModelIds"],"androidVersionIds":["androidVersionIds","androidVersionIds"]},"iosDeviceList":{"iosDevices":[{"iosVersionId":"iosVersionId","orientation":"orientation","iosModelId":"iosModelId","locale":"locale"},{"iosVersionId":"iosVersionId","orientation":"orientation","iosModelId":"iosModelId","locale":"locale"}]}},"clientInfo":{"name":"name","clientInfoDetails":[{"value":"value","key":"key"},{"value":"value","key":"key"}]},"extendedInvalidMatrixDetails":[{"reason":"reason","message":"message"},{"reason":"reason","message":"message"}],"failFast":True,"testSpecification":{"disablePerformanceMetrics":True,"iosTestSetup":{"pushFiles":[{"devicePath":"devicePath","bundleId":"bundleId","content":{"gcsPath":"gcsPath"}},{"devicePath":"devicePath","bundleId":"bundleId","content":{"gcsPath":"gcsPath"}}],"networkProfile":"networkProfile","pullDirectories":[{"devicePath":"devicePath","bundleId":"bundleId","content":{"gcsPath":"gcsPath"}},{"devicePath":"devicePath","bundleId":"bundleId","content":{"gcsPath":"gcsPath"}}],"additionalIpas":[{"gcsPath":"gcsPath"},{"gcsPath":"gcsPath"}]},"testSetup":{"directoriesToPull":["directoriesToPull","directoriesToPull"],"environmentVariables":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"filesToPush":[{"regularFile":{"devicePath":"devicePath","content":{"gcsPath":"gcsPath"}},"obbFile":{"obb":{"gcsPath":"gcsPath"},"obbFileName":"obbFileName"}},{"regularFile":{"devicePath":"devicePath","content":{"gcsPath":"gcsPath"}},"obbFile":{"obb":{"gcsPath":"gcsPath"},"obbFileName":"obbFileName"}}],"systrace":{"durationSeconds":3},"additionalApks":[{"location":{"gcsPath":"gcsPath"},"packageName":"packageName"},{"location":{"gcsPath":"gcsPath"},"packageName":"packageName"}],"dontAutograntPermissions":True,"networkProfile":"networkProfile","initialSetupApks":[{"location":{"gcsPath":"gcsPath"},"packageName":"packageName"},{"location":{"gcsPath":"gcsPath"},"packageName":"packageName"}],"account":{"googleAuto":"{}"}},"testTimeout":"testTimeout","androidInstrumentationTest":{"testRunnerClass":"testRunnerClass","testTargets":["testTargets","testTargets"],"appPackageId":"appPackageId","testPackageId":"testPackageId","appBundle":{"bundleLocation":{"gcsPath":"gcsPath"}},"orchestratorOption":"ORCHESTRATOR_OPTION_UNSPECIFIED","testApk":{"gcsPath":"gcsPath"},"shardingOption":{"uniformSharding":{"numShards":5},"manualSharding":{"testTargetsForShard":[{"testTargets":["testTargets","testTargets"]},{"testTargets":["testTargets","testTargets"]}]},"smartSharding":{"targetedShardDuration":"targetedShardDuration"}},"appApk":{"gcsPath":"gcsPath"}},"androidRoboTest":{"maxDepth":5,"roboScript":{"gcsPath":"gcsPath"},"startingIntents":[{"noActivity":"{}","launcherActivity":"{}","startActivity":{"action":"action","categories":["categories","categories"],"uri":"uri"},"timeout":"timeout"},{"noActivity":"{}","launcherActivity":"{}","startActivity":{"action":"action","categories":["categories","categories"],"uri":"uri"},"timeout":"timeout"}],"roboMode":"ROBO_MODE_UNSPECIFIED","appPackageId":"appPackageId","maxSteps":2,"appInitialActivity":"appInitialActivity","appBundle":{"bundleLocation":{"gcsPath":"gcsPath"}},"appApk":{"gcsPath":"gcsPath"},"roboDirectives":[{"actionType":"ACTION_TYPE_UNSPECIFIED","inputText":"inputText","resourceName":"resourceName"},{"actionType":"ACTION_TYPE_UNSPECIFIED","inputText":"inputText","resourceName":"resourceName"}]},"disableVideoRecording":True,"iosTestLoop":{"appBundleId":"appBundleId","scenarios":[9,9],"appIpa":{"gcsPath":"gcsPath"}},"androidTestLoop":{"scenarioLabels":["scenarioLabels","scenarioLabels"],"appPackageId":"appPackageId","scenarios":[7,7],"appBundle":{"bundleLocation":{"gcsPath":"gcsPath"}},"appApk":{"gcsPath":"gcsPath"}},"iosRoboTest":{"appBundleId":"appBundleId","roboScript":{"gcsPath":"gcsPath"},"appIpa":{"gcsPath":"gcsPath"}},"iosXcTest":{"xctestrun":{"gcsPath":"gcsPath"},"testsZip":{"gcsPath":"gcsPath"},"appBundleId":"appBundleId","testSpecialEntitlements":True,"xcodeVersion":"xcodeVersion"}},"invalidMatrixDetails":"INVALID_MATRIX_DETAILS_UNSPECIFIED","resultStorage":{"resultsUrl":"resultsUrl","toolResultsExecution":{"executionId":"executionId","historyId":"historyId","projectId":"projectId"},"googleCloudStorage":{"gcsPath":"gcsPath"},"toolResultsHistory":{"historyId":"historyId","projectId":"projectId"}},"flakyTestAttempts":0,"testExecutions":[{"environment":{"iosDevice":{"iosVersionId":"iosVersionId","orientation":"orientation","iosModelId":"iosModelId","locale":"locale"},"androidDevice":{"orientation":"orientation","androidVersionId":"androidVersionId","locale":"locale","androidModelId":"androidModelId"}},"testDetails":{"progressMessages":["progressMessages","progressMessages"],"errorMessage":"errorMessage"},"toolResultsStep":{"executionId":"executionId","historyId":"historyId","stepId":"stepId","projectId":"projectId"},"matrixId":"matrixId","id":"id","shard":{"testTargetsForShard":{"testTargets":["testTargets","testTargets"]},"shardIndex":1,"estimatedShardDuration":"estimatedShardDuration","numShards":6},"state":"TEST_STATE_UNSPECIFIED","projectId":"projectId","testSpecification":{"disablePerformanceMetrics":True,"iosTestSetup":{"pushFiles":[{"devicePath":"devicePath","bundleId":"bundleId","content":{"gcsPath":"gcsPath"}},{"devicePath":"devicePath","bundleId":"bundleId","content":{"gcsPath":"gcsPath"}}],"networkProfile":"networkProfile","pullDirectories":[{"devicePath":"devicePath","bundleId":"bundleId","content":{"gcsPath":"gcsPath"}},{"devicePath":"devicePath","bundleId":"bundleId","content":{"gcsPath":"gcsPath"}}],"additionalIpas":[{"gcsPath":"gcsPath"},{"gcsPath":"gcsPath"}]},"testSetup":{"directoriesToPull":["directoriesToPull","directoriesToPull"],"environmentVariables":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"filesToPush":[{"regularFile":{"devicePath":"devicePath","content":{"gcsPath":"gcsPath"}},"obbFile":{"obb":{"gcsPath":"gcsPath"},"obbFileName":"obbFileName"}},{"regularFile":{"devicePath":"devicePath","content":{"gcsPath":"gcsPath"}},"obbFile":{"obb":{"gcsPath":"gcsPath"},"obbFileName":"obbFileName"}}],"systrace":{"durationSeconds":3},"additionalApks":[{"location":{"gcsPath":"gcsPath"},"packageName":"packageName"},{"location":{"gcsPath":"gcsPath"},"packageName":"packageName"}],"dontAutograntPermissions":True,"networkProfile":"networkProfile","initialSetupApks":[{"location":{"gcsPath":"gcsPath"},"packageName":"packageName"},{"location":{"gcsPath":"gcsPath"},"packageName":"packageName"}],"account":{"googleAuto":"{}"}},"testTimeout":"testTimeout","androidInstrumentationTest":{"testRunnerClass":"testRunnerClass","testTargets":["testTargets","testTargets"],"appPackageId":"appPackageId","testPackageId":"testPackageId","appBundle":{"bundleLocation":{"gcsPath":"gcsPath"}},"orchestratorOption":"ORCHESTRATOR_OPTION_UNSPECIFIED","testApk":{"gcsPath":"gcsPath"},"shardingOption":{"uniformSharding":{"numShards":5},"manualSharding":{"testTargetsForShard":[{"testTargets":["testTargets","testTargets"]},{"testTargets":["testTargets","testTargets"]}]},"smartSharding":{"targetedShardDuration":"targetedShardDuration"}},"appApk":{"gcsPath":"gcsPath"}},"androidRoboTest":{"maxDepth":5,"roboScript":{"gcsPath":"gcsPath"},"startingIntents":[{"noActivity":"{}","launcherActivity":"{}","startActivity":{"action":"action","categories":["categories","categories"],"uri":"uri"},"timeout":"timeout"},{"noActivity":"{}","launcherActivity":"{}","startActivity":{"action":"action","categories":["categories","categories"],"uri":"uri"},"timeout":"timeout"}],"roboMode":"ROBO_MODE_UNSPECIFIED","appPackageId":"appPackageId","maxSteps":2,"appInitialActivity":"appInitialActivity","appBundle":{"bundleLocation":{"gcsPath":"gcsPath"}},"appApk":{"gcsPath":"gcsPath"},"roboDirectives":[{"actionType":"ACTION_TYPE_UNSPECIFIED","inputText":"inputText","resourceName":"resourceName"},{"actionType":"ACTION_TYPE_UNSPECIFIED","inputText":"inputText","resourceName":"resourceName"}]},"disableVideoRecording":True,"iosTestLoop":{"appBundleId":"appBundleId","scenarios":[9,9],"appIpa":{"gcsPath":"gcsPath"}},"androidTestLoop":{"scenarioLabels":["scenarioLabels","scenarioLabels"],"appPackageId":"appPackageId","scenarios":[7,7],"appBundle":{"bundleLocation":{"gcsPath":"gcsPath"}},"appApk":{"gcsPath":"gcsPath"}},"iosRoboTest":{"appBundleId":"appBundleId","roboScript":{"gcsPath":"gcsPath"},"appIpa":{"gcsPath":"gcsPath"}},"iosXcTest":{"xctestrun":{"gcsPath":"gcsPath"},"testsZip":{"gcsPath":"gcsPath"},"appBundleId":"appBundleId","testSpecialEntitlements":True,"xcodeVersion":"xcodeVersion"}},"timestamp":"timestamp"},{"environment":{"iosDevice":{"iosVersionId":"iosVersionId","orientation":"orientation","iosModelId":"iosModelId","locale":"locale"},"androidDevice":{"orientation":"orientation","androidVersionId":"androidVersionId","locale":"locale","androidModelId":"androidModelId"}},"testDetails":{"progressMessages":["progressMessages","progressMessages"],"errorMessage":"errorMessage"},"toolResultsStep":{"executionId":"executionId","historyId":"historyId","stepId":"stepId","projectId":"projectId"},"matrixId":"matrixId","id":"id","shard":{"testTargetsForShard":{"testTargets":["testTargets","testTargets"]},"shardIndex":1,"estimatedShardDuration":"estimatedShardDuration","numShards":6},"state":"TEST_STATE_UNSPECIFIED","projectId":"projectId","testSpecification":{"disablePerformanceMetrics":True,"iosTestSetup":{"pushFiles":[{"devicePath":"devicePath","bundleId":"bundleId","content":{"gcsPath":"gcsPath"}},{"devicePath":"devicePath","bundleId":"bundleId","content":{"gcsPath":"gcsPath"}}],"networkProfile":"networkProfile","pullDirectories":[{"devicePath":"devicePath","bundleId":"bundleId","content":{"gcsPath":"gcsPath"}},{"devicePath":"devicePath","bundleId":"bundleId","content":{"gcsPath":"gcsPath"}}],"additionalIpas":[{"gcsPath":"gcsPath"},{"gcsPath":"gcsPath"}]},"testSetup":{"directoriesToPull":["directoriesToPull","directoriesToPull"],"environmentVariables":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"filesToPush":[{"regularFile":{"devicePath":"devicePath","content":{"gcsPath":"gcsPath"}},"obbFile":{"obb":{"gcsPath":"gcsPath"},"obbFileName":"obbFileName"}},{"regularFile":{"devicePath":"devicePath","content":{"gcsPath":"gcsPath"}},"obbFile":{"obb":{"gcsPath":"gcsPath"},"obbFileName":"obbFileName"}}],"systrace":{"durationSeconds":3},"additionalApks":[{"location":{"gcsPath":"gcsPath"},"packageName":"packageName"},{"location":{"gcsPath":"gcsPath"},"packageName":"packageName"}],"dontAutograntPermissions":True,"networkProfile":"networkProfile","initialSetupApks":[{"location":{"gcsPath":"gcsPath"},"packageName":"packageName"},{"location":{"gcsPath":"gcsPath"},"packageName":"packageName"}],"account":{"googleAuto":"{}"}},"testTimeout":"testTimeout","androidInstrumentationTest":{"testRunnerClass":"testRunnerClass","testTargets":["testTargets","testTargets"],"appPackageId":"appPackageId","testPackageId":"testPackageId","appBundle":{"bundleLocation":{"gcsPath":"gcsPath"}},"orchestratorOption":"ORCHESTRATOR_OPTION_UNSPECIFIED","testApk":{"gcsPath":"gcsPath"},"shardingOption":{"uniformSharding":{"numShards":5},"manualSharding":{"testTargetsForShard":[{"testTargets":["testTargets","testTargets"]},{"testTargets":["testTargets","testTargets"]}]},"smartSharding":{"targetedShardDuration":"targetedShardDuration"}},"appApk":{"gcsPath":"gcsPath"}},"androidRoboTest":{"maxDepth":5,"roboScript":{"gcsPath":"gcsPath"},"startingIntents":[{"noActivity":"{}","launcherActivity":"{}","startActivity":{"action":"action","categories":["categories","categories"],"uri":"uri"},"timeout":"timeout"},{"noActivity":"{}","launcherActivity":"{}","startActivity":{"action":"action","categories":["categories","categories"],"uri":"uri"},"timeout":"timeout"}],"roboMode":"ROBO_MODE_UNSPECIFIED","appPackageId":"appPackageId","maxSteps":2,"appInitialActivity":"appInitialActivity","appBundle":{"bundleLocation":{"gcsPath":"gcsPath"}},"appApk":{"gcsPath":"gcsPath"},"roboDirectives":[{"actionType":"ACTION_TYPE_UNSPECIFIED","inputText":"inputText","resourceName":"resourceName"},{"actionType":"ACTION_TYPE_UNSPECIFIED","inputText":"inputText","resourceName":"resourceName"}]},"disableVideoRecording":True,"iosTestLoop":{"appBundleId":"appBundleId","scenarios":[9,9],"appIpa":{"gcsPath":"gcsPath"}},"androidTestLoop":{"scenarioLabels":["scenarioLabels","scenarioLabels"],"appPackageId":"appPackageId","scenarios":[7,7],"appBundle":{"bundleLocation":{"gcsPath":"gcsPath"}},"appApk":{"gcsPath":"gcsPath"}},"iosRoboTest":{"appBundleId":"appBundleId","roboScript":{"gcsPath":"gcsPath"},"appIpa":{"gcsPath":"gcsPath"}},"iosXcTest":{"xctestrun":{"gcsPath":"gcsPath"},"testsZip":{"gcsPath":"gcsPath"},"appBundleId":"appBundleId","testSpecialEntitlements":True,"xcodeVersion":"xcodeVersion"}},"timestamp":"timestamp"}],"testMatrixId":"testMatrixId","outcomeSummary":"OUTCOME_SUMMARY_UNSPECIFIED","state":"TEST_STATE_UNSPECIFIED","projectId":"projectId","timestamp":"timestamp"}
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
        path='/v1/projects/{project_id}/testMatrices'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_testing_projects_test_matrices_get(client):
    """Test case for testing_projects_test_matrices_get

    
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
        path='/v1/projects/{project_id}/testMatrices/{test_matrix_id}'.format(project_id='project_id_example', test_matrix_id='test_matrix_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

