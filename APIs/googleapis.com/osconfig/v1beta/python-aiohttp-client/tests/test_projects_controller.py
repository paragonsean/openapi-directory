# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.effective_guest_policy import EffectiveGuestPolicy
from openapi_server.models.execute_patch_job_request import ExecutePatchJobRequest
from openapi_server.models.guest_policy import GuestPolicy
from openapi_server.models.list_guest_policies_response import ListGuestPoliciesResponse
from openapi_server.models.list_patch_deployments_response import ListPatchDeploymentsResponse
from openapi_server.models.list_patch_job_instance_details_response import ListPatchJobInstanceDetailsResponse
from openapi_server.models.list_patch_jobs_response import ListPatchJobsResponse
from openapi_server.models.lookup_effective_guest_policy_request import LookupEffectiveGuestPolicyRequest
from openapi_server.models.patch_deployment import PatchDeployment
from openapi_server.models.patch_job import PatchJob


pytestmark = pytest.mark.asyncio

async def test_osconfig_projects_guest_policies_create(client):
    """Test case for osconfig_projects_guest_policies_create

    
    """
    body = {"recipes":[{"desiredState":"DESIRED_STATE_UNSPECIFIED","installSteps":[{"fileCopy":{"permissions":"permissions","destination":"destination","artifactId":"artifactId","overwrite":True},"scriptRun":{"allowedExitCodes":[1,1],"interpreter":"INTERPRETER_UNSPECIFIED","script":"script"},"rpmInstallation":{"artifactId":"artifactId"},"archiveExtraction":{"destination":"destination","artifactId":"artifactId","type":"ARCHIVE_TYPE_UNSPECIFIED"},"msiInstallation":{"allowedExitCodes":[6,6],"flags":["flags","flags"],"artifactId":"artifactId"},"dpkgInstallation":{"artifactId":"artifactId"},"fileExec":{"args":["args","args"],"allowedExitCodes":[0,0],"localPath":"localPath","artifactId":"artifactId"}},{"fileCopy":{"permissions":"permissions","destination":"destination","artifactId":"artifactId","overwrite":True},"scriptRun":{"allowedExitCodes":[1,1],"interpreter":"INTERPRETER_UNSPECIFIED","script":"script"},"rpmInstallation":{"artifactId":"artifactId"},"archiveExtraction":{"destination":"destination","artifactId":"artifactId","type":"ARCHIVE_TYPE_UNSPECIFIED"},"msiInstallation":{"allowedExitCodes":[6,6],"flags":["flags","flags"],"artifactId":"artifactId"},"dpkgInstallation":{"artifactId":"artifactId"},"fileExec":{"args":["args","args"],"allowedExitCodes":[0,0],"localPath":"localPath","artifactId":"artifactId"}}],"updateSteps":[{"fileCopy":{"permissions":"permissions","destination":"destination","artifactId":"artifactId","overwrite":True},"scriptRun":{"allowedExitCodes":[1,1],"interpreter":"INTERPRETER_UNSPECIFIED","script":"script"},"rpmInstallation":{"artifactId":"artifactId"},"archiveExtraction":{"destination":"destination","artifactId":"artifactId","type":"ARCHIVE_TYPE_UNSPECIFIED"},"msiInstallation":{"allowedExitCodes":[6,6],"flags":["flags","flags"],"artifactId":"artifactId"},"dpkgInstallation":{"artifactId":"artifactId"},"fileExec":{"args":["args","args"],"allowedExitCodes":[0,0],"localPath":"localPath","artifactId":"artifactId"}},{"fileCopy":{"permissions":"permissions","destination":"destination","artifactId":"artifactId","overwrite":True},"scriptRun":{"allowedExitCodes":[1,1],"interpreter":"INTERPRETER_UNSPECIFIED","script":"script"},"rpmInstallation":{"artifactId":"artifactId"},"archiveExtraction":{"destination":"destination","artifactId":"artifactId","type":"ARCHIVE_TYPE_UNSPECIFIED"},"msiInstallation":{"allowedExitCodes":[6,6],"flags":["flags","flags"],"artifactId":"artifactId"},"dpkgInstallation":{"artifactId":"artifactId"},"fileExec":{"args":["args","args"],"allowedExitCodes":[0,0],"localPath":"localPath","artifactId":"artifactId"}}],"name":"name","version":"version","artifacts":[{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"id":"id","remote":{"checksum":"checksum","uri":"uri"},"allowInsecure":True},{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"id":"id","remote":{"checksum":"checksum","uri":"uri"},"allowInsecure":True}]},{"desiredState":"DESIRED_STATE_UNSPECIFIED","installSteps":[{"fileCopy":{"permissions":"permissions","destination":"destination","artifactId":"artifactId","overwrite":True},"scriptRun":{"allowedExitCodes":[1,1],"interpreter":"INTERPRETER_UNSPECIFIED","script":"script"},"rpmInstallation":{"artifactId":"artifactId"},"archiveExtraction":{"destination":"destination","artifactId":"artifactId","type":"ARCHIVE_TYPE_UNSPECIFIED"},"msiInstallation":{"allowedExitCodes":[6,6],"flags":["flags","flags"],"artifactId":"artifactId"},"dpkgInstallation":{"artifactId":"artifactId"},"fileExec":{"args":["args","args"],"allowedExitCodes":[0,0],"localPath":"localPath","artifactId":"artifactId"}},{"fileCopy":{"permissions":"permissions","destination":"destination","artifactId":"artifactId","overwrite":True},"scriptRun":{"allowedExitCodes":[1,1],"interpreter":"INTERPRETER_UNSPECIFIED","script":"script"},"rpmInstallation":{"artifactId":"artifactId"},"archiveExtraction":{"destination":"destination","artifactId":"artifactId","type":"ARCHIVE_TYPE_UNSPECIFIED"},"msiInstallation":{"allowedExitCodes":[6,6],"flags":["flags","flags"],"artifactId":"artifactId"},"dpkgInstallation":{"artifactId":"artifactId"},"fileExec":{"args":["args","args"],"allowedExitCodes":[0,0],"localPath":"localPath","artifactId":"artifactId"}}],"updateSteps":[{"fileCopy":{"permissions":"permissions","destination":"destination","artifactId":"artifactId","overwrite":True},"scriptRun":{"allowedExitCodes":[1,1],"interpreter":"INTERPRETER_UNSPECIFIED","script":"script"},"rpmInstallation":{"artifactId":"artifactId"},"archiveExtraction":{"destination":"destination","artifactId":"artifactId","type":"ARCHIVE_TYPE_UNSPECIFIED"},"msiInstallation":{"allowedExitCodes":[6,6],"flags":["flags","flags"],"artifactId":"artifactId"},"dpkgInstallation":{"artifactId":"artifactId"},"fileExec":{"args":["args","args"],"allowedExitCodes":[0,0],"localPath":"localPath","artifactId":"artifactId"}},{"fileCopy":{"permissions":"permissions","destination":"destination","artifactId":"artifactId","overwrite":True},"scriptRun":{"allowedExitCodes":[1,1],"interpreter":"INTERPRETER_UNSPECIFIED","script":"script"},"rpmInstallation":{"artifactId":"artifactId"},"archiveExtraction":{"destination":"destination","artifactId":"artifactId","type":"ARCHIVE_TYPE_UNSPECIFIED"},"msiInstallation":{"allowedExitCodes":[6,6],"flags":["flags","flags"],"artifactId":"artifactId"},"dpkgInstallation":{"artifactId":"artifactId"},"fileExec":{"args":["args","args"],"allowedExitCodes":[0,0],"localPath":"localPath","artifactId":"artifactId"}}],"name":"name","version":"version","artifacts":[{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"id":"id","remote":{"checksum":"checksum","uri":"uri"},"allowInsecure":True},{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"id":"id","remote":{"checksum":"checksum","uri":"uri"},"allowInsecure":True}]}],"createTime":"createTime","assignment":{"groupLabels":[{"labels":{"key":"labels"}},{"labels":{"key":"labels"}}],"instanceNamePrefixes":["instanceNamePrefixes","instanceNamePrefixes"],"instances":["instances","instances"],"osTypes":[{"osVersion":"osVersion","osShortName":"osShortName","osArchitecture":"osArchitecture"},{"osVersion":"osVersion","osShortName":"osShortName","osArchitecture":"osArchitecture"}],"zones":["zones","zones"]},"name":"name","description":"description","etag":"etag","updateTime":"updateTime","packages":[{"desiredState":"DESIRED_STATE_UNSPECIFIED","manager":"MANAGER_UNSPECIFIED","name":"name"},{"desiredState":"DESIRED_STATE_UNSPECIFIED","manager":"MANAGER_UNSPECIFIED","name":"name"}],"packageRepositories":[{"yum":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"zypper":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"apt":{"archiveType":"ARCHIVE_TYPE_UNSPECIFIED","components":["components","components"],"distribution":"distribution","gpgKey":"gpgKey","uri":"uri"},"goo":{"name":"name","url":"url"}},{"yum":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"zypper":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"apt":{"archiveType":"ARCHIVE_TYPE_UNSPECIFIED","components":["components","components"],"distribution":"distribution","gpgKey":"gpgKey","uri":"uri"},"goo":{"name":"name","url":"url"}}]}
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
                    ('guestPolicyId', 'guest_policy_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta/{parent}/guestPolicies'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_osconfig_projects_guest_policies_list(client):
    """Test case for osconfig_projects_guest_policies_list

    
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
        path='/v1beta/{parent}/guestPolicies'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_osconfig_projects_patch_deployments_create(client):
    """Test case for osconfig_projects_patch_deployments_create

    
    """
    body = {"duration":"duration","lastExecuteTime":"lastExecuteTime","oneTimeSchedule":{"executeTime":"executeTime"},"rollout":{"mode":"MODE_UNSPECIFIED","disruptionBudget":{"fixed":1,"percent":5}},"createTime":"createTime","recurringSchedule":{"lastExecuteTime":"lastExecuteTime","nextExecuteTime":"nextExecuteTime","monthly":{"weekDayOfMonth":{"weekOrdinal":1,"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","dayOffset":6},"monthDay":0},"timeZone":{"id":"id","version":"version"},"startTime":"startTime","endTime":"endTime","weekly":{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED"},"frequency":"FREQUENCY_UNSPECIFIED","timeOfDay":{"hours":5,"seconds":7,"nanos":2,"minutes":5}},"instanceFilter":{"all":True,"groupLabels":[{"labels":{"key":"labels"}},{"labels":{"key":"labels"}}],"instanceNamePrefixes":["instanceNamePrefixes","instanceNamePrefixes"],"instances":["instances","instances"],"zones":["zones","zones"]},"name":"name","description":"description","updateTime":"updateTime","state":"STATE_UNSPECIFIED","patchConfig":{"yum":{"minimal":True,"security":True,"excludes":["excludes","excludes"],"exclusivePackages":["exclusivePackages","exclusivePackages"]},"zypper":{"exclusivePatches":["exclusivePatches","exclusivePatches"],"excludes":["excludes","excludes"],"withUpdate":True,"categories":["categories","categories"],"withOptional":True,"severities":["severities","severities"]},"postStep":{"windowsExecStepConfig":{"localPath":"localPath","gcsObject":{"bucket":"bucket","generationNumber":"generationNumber","object":"object"},"allowedSuccessCodes":[0,0],"interpreter":"INTERPRETER_UNSPECIFIED"},"linuxExecStepConfig":{"localPath":"localPath","gcsObject":{"bucket":"bucket","generationNumber":"generationNumber","object":"object"},"allowedSuccessCodes":[0,0],"interpreter":"INTERPRETER_UNSPECIFIED"}},"apt":{"excludes":["excludes","excludes"],"exclusivePackages":["exclusivePackages","exclusivePackages"],"type":"TYPE_UNSPECIFIED"},"goo":"{}","preStep":{"windowsExecStepConfig":{"localPath":"localPath","gcsObject":{"bucket":"bucket","generationNumber":"generationNumber","object":"object"},"allowedSuccessCodes":[0,0],"interpreter":"INTERPRETER_UNSPECIFIED"},"linuxExecStepConfig":{"localPath":"localPath","gcsObject":{"bucket":"bucket","generationNumber":"generationNumber","object":"object"},"allowedSuccessCodes":[0,0],"interpreter":"INTERPRETER_UNSPECIFIED"}},"migInstancesAllowed":True,"rebootConfig":"REBOOT_CONFIG_UNSPECIFIED","windowsUpdate":{"classifications":["CLASSIFICATION_UNSPECIFIED","CLASSIFICATION_UNSPECIFIED"],"exclusivePatches":["exclusivePatches","exclusivePatches"],"excludes":["excludes","excludes"]}}}
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
                    ('patchDeploymentId', 'patch_deployment_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta/{parent}/patchDeployments'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_osconfig_projects_patch_deployments_delete(client):
    """Test case for osconfig_projects_patch_deployments_delete

    
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
        path='/v1beta/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_osconfig_projects_patch_deployments_list(client):
    """Test case for osconfig_projects_patch_deployments_list

    
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
        path='/v1beta/{parent}/patchDeployments'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_osconfig_projects_patch_deployments_patch(client):
    """Test case for osconfig_projects_patch_deployments_patch

    
    """
    body = {"duration":"duration","lastExecuteTime":"lastExecuteTime","oneTimeSchedule":{"executeTime":"executeTime"},"rollout":{"mode":"MODE_UNSPECIFIED","disruptionBudget":{"fixed":1,"percent":5}},"createTime":"createTime","recurringSchedule":{"lastExecuteTime":"lastExecuteTime","nextExecuteTime":"nextExecuteTime","monthly":{"weekDayOfMonth":{"weekOrdinal":1,"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","dayOffset":6},"monthDay":0},"timeZone":{"id":"id","version":"version"},"startTime":"startTime","endTime":"endTime","weekly":{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED"},"frequency":"FREQUENCY_UNSPECIFIED","timeOfDay":{"hours":5,"seconds":7,"nanos":2,"minutes":5}},"instanceFilter":{"all":True,"groupLabels":[{"labels":{"key":"labels"}},{"labels":{"key":"labels"}}],"instanceNamePrefixes":["instanceNamePrefixes","instanceNamePrefixes"],"instances":["instances","instances"],"zones":["zones","zones"]},"name":"name","description":"description","updateTime":"updateTime","state":"STATE_UNSPECIFIED","patchConfig":{"yum":{"minimal":True,"security":True,"excludes":["excludes","excludes"],"exclusivePackages":["exclusivePackages","exclusivePackages"]},"zypper":{"exclusivePatches":["exclusivePatches","exclusivePatches"],"excludes":["excludes","excludes"],"withUpdate":True,"categories":["categories","categories"],"withOptional":True,"severities":["severities","severities"]},"postStep":{"windowsExecStepConfig":{"localPath":"localPath","gcsObject":{"bucket":"bucket","generationNumber":"generationNumber","object":"object"},"allowedSuccessCodes":[0,0],"interpreter":"INTERPRETER_UNSPECIFIED"},"linuxExecStepConfig":{"localPath":"localPath","gcsObject":{"bucket":"bucket","generationNumber":"generationNumber","object":"object"},"allowedSuccessCodes":[0,0],"interpreter":"INTERPRETER_UNSPECIFIED"}},"apt":{"excludes":["excludes","excludes"],"exclusivePackages":["exclusivePackages","exclusivePackages"],"type":"TYPE_UNSPECIFIED"},"goo":"{}","preStep":{"windowsExecStepConfig":{"localPath":"localPath","gcsObject":{"bucket":"bucket","generationNumber":"generationNumber","object":"object"},"allowedSuccessCodes":[0,0],"interpreter":"INTERPRETER_UNSPECIFIED"},"linuxExecStepConfig":{"localPath":"localPath","gcsObject":{"bucket":"bucket","generationNumber":"generationNumber","object":"object"},"allowedSuccessCodes":[0,0],"interpreter":"INTERPRETER_UNSPECIFIED"}},"migInstancesAllowed":True,"rebootConfig":"REBOOT_CONFIG_UNSPECIFIED","windowsUpdate":{"classifications":["CLASSIFICATION_UNSPECIFIED","CLASSIFICATION_UNSPECIFIED"],"exclusivePatches":["exclusivePatches","exclusivePatches"],"excludes":["excludes","excludes"]}}}
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
        path='/v1beta/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_osconfig_projects_patch_deployments_pause(client):
    """Test case for osconfig_projects_patch_deployments_pause

    
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
        path='/v1beta/{namepaus}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_osconfig_projects_patch_deployments_resume(client):
    """Test case for osconfig_projects_patch_deployments_resume

    
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
        path='/v1beta/{nameresum}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_osconfig_projects_patch_jobs_cancel(client):
    """Test case for osconfig_projects_patch_jobs_cancel

    
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
        path='/v1beta/{namecance}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_osconfig_projects_patch_jobs_execute(client):
    """Test case for osconfig_projects_patch_jobs_execute

    
    """
    body = {"duration":"duration","dryRun":True,"rollout":{"mode":"MODE_UNSPECIFIED","disruptionBudget":{"fixed":1,"percent":5}},"displayName":"displayName","instanceFilter":{"all":True,"groupLabels":[{"labels":{"key":"labels"}},{"labels":{"key":"labels"}}],"instanceNamePrefixes":["instanceNamePrefixes","instanceNamePrefixes"],"instances":["instances","instances"],"zones":["zones","zones"]},"description":"description","patchConfig":{"yum":{"minimal":True,"security":True,"excludes":["excludes","excludes"],"exclusivePackages":["exclusivePackages","exclusivePackages"]},"zypper":{"exclusivePatches":["exclusivePatches","exclusivePatches"],"excludes":["excludes","excludes"],"withUpdate":True,"categories":["categories","categories"],"withOptional":True,"severities":["severities","severities"]},"postStep":{"windowsExecStepConfig":{"localPath":"localPath","gcsObject":{"bucket":"bucket","generationNumber":"generationNumber","object":"object"},"allowedSuccessCodes":[0,0],"interpreter":"INTERPRETER_UNSPECIFIED"},"linuxExecStepConfig":{"localPath":"localPath","gcsObject":{"bucket":"bucket","generationNumber":"generationNumber","object":"object"},"allowedSuccessCodes":[0,0],"interpreter":"INTERPRETER_UNSPECIFIED"}},"apt":{"excludes":["excludes","excludes"],"exclusivePackages":["exclusivePackages","exclusivePackages"],"type":"TYPE_UNSPECIFIED"},"goo":"{}","preStep":{"windowsExecStepConfig":{"localPath":"localPath","gcsObject":{"bucket":"bucket","generationNumber":"generationNumber","object":"object"},"allowedSuccessCodes":[0,0],"interpreter":"INTERPRETER_UNSPECIFIED"},"linuxExecStepConfig":{"localPath":"localPath","gcsObject":{"bucket":"bucket","generationNumber":"generationNumber","object":"object"},"allowedSuccessCodes":[0,0],"interpreter":"INTERPRETER_UNSPECIFIED"}},"migInstancesAllowed":True,"rebootConfig":"REBOOT_CONFIG_UNSPECIFIED","windowsUpdate":{"classifications":["CLASSIFICATION_UNSPECIFIED","CLASSIFICATION_UNSPECIFIED"],"exclusivePatches":["exclusivePatches","exclusivePatches"],"excludes":["excludes","excludes"]}}}
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
        path='/v1beta/{parent}/patchJobs:execute'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_osconfig_projects_patch_jobs_get(client):
    """Test case for osconfig_projects_patch_jobs_get

    
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
        path='/v1beta/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_osconfig_projects_patch_jobs_instance_details_list(client):
    """Test case for osconfig_projects_patch_jobs_instance_details_list

    
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
        path='/v1beta/{parent}/instanceDetails'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_osconfig_projects_patch_jobs_list(client):
    """Test case for osconfig_projects_patch_jobs_list

    
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
        path='/v1beta/{parent}/patchJobs'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_osconfig_projects_zones_instances_lookup_effective_guest_policy(client):
    """Test case for osconfig_projects_zones_instances_lookup_effective_guest_policy

    
    """
    body = {"osVersion":"osVersion","osShortName":"osShortName","osArchitecture":"osArchitecture"}
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
        path='/v1beta/{instancelookup_effective_guest_polic}'.format(instance='instance_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

