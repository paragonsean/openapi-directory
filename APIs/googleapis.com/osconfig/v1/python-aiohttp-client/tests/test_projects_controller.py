# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.execute_patch_job_request import ExecutePatchJobRequest
from openapi_server.models.list_inventories_response import ListInventoriesResponse
from openapi_server.models.list_os_policy_assignment_reports_response import ListOSPolicyAssignmentReportsResponse
from openapi_server.models.list_os_policy_assignment_revisions_response import ListOSPolicyAssignmentRevisionsResponse
from openapi_server.models.list_os_policy_assignments_response import ListOSPolicyAssignmentsResponse
from openapi_server.models.list_patch_deployments_response import ListPatchDeploymentsResponse
from openapi_server.models.list_patch_job_instance_details_response import ListPatchJobInstanceDetailsResponse
from openapi_server.models.list_patch_jobs_response import ListPatchJobsResponse
from openapi_server.models.list_vulnerability_reports_response import ListVulnerabilityReportsResponse
from openapi_server.models.os_policy_assignment import OSPolicyAssignment
from openapi_server.models.operation import Operation
from openapi_server.models.patch_deployment import PatchDeployment
from openapi_server.models.patch_job import PatchJob


pytestmark = pytest.mark.asyncio

async def test_osconfig_projects_locations_instances_inventories_list(client):
    """Test case for osconfig_projects_locations_instances_inventories_list

    
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
                    ('pageToken', 'page_token_example'),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/inventories'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_osconfig_projects_locations_instances_os_policy_assignments_reports_list(client):
    """Test case for osconfig_projects_locations_instances_os_policy_assignments_reports_list

    
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
        path='/v1/{parent}/reports'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_osconfig_projects_locations_instances_vulnerability_reports_list(client):
    """Test case for osconfig_projects_locations_instances_vulnerability_reports_list

    
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
        path='/v1/{parent}/vulnerabilityReports'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_osconfig_projects_locations_os_policy_assignments_create(client):
    """Test case for osconfig_projects_locations_os_policy_assignments_create

    
    """
    body = {"rollout":{"disruptionBudget":{"fixed":1,"percent":5},"minWaitDuration":"minWaitDuration"},"instanceFilter":{"all":True,"exclusionLabels":[{"labels":{"key":"labels"}},{"labels":{"key":"labels"}}],"inventories":[{"osVersion":"osVersion","osShortName":"osShortName"},{"osVersion":"osVersion","osShortName":"osShortName"}],"inclusionLabels":[{"labels":{"key":"labels"}},{"labels":{"key":"labels"}}]},"description":"description","reconciling":True,"baseline":True,"revisionCreateTime":"revisionCreateTime","revisionId":"revisionId","uid":"uid","deleted":True,"rolloutState":"ROLLOUT_STATE_UNSPECIFIED","name":"name","etag":"etag","osPolicies":[{"mode":"MODE_UNSPECIFIED","resourceGroups":[{"inventoryFilters":[{"osVersion":"osVersion","osShortName":"osShortName"},{"osVersion":"osVersion","osShortName":"osShortName"}],"resources":[{"file":{"path":"path","file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"permissions":"permissions","state":"DESIRED_STATE_UNSPECIFIED","content":"content"},"id":"id","repository":{"yum":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"zypper":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"apt":{"archiveType":"ARCHIVE_TYPE_UNSPECIFIED","components":["components","components"],"distribution":"distribution","gpgKey":"gpgKey","uri":"uri"},"goo":{"name":"name","url":"url"}},"pkg":{"deb":{"pullDeps":True,"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True}},"yum":{"name":"name"},"zypper":{"name":"name"},"desiredState":"DESIRED_STATE_UNSPECIFIED","msi":{"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"properties":["properties","properties"]},"apt":{"name":"name"},"googet":{"name":"name"},"rpm":{"pullDeps":True,"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True}}},"exec":{"enforce":{"args":["args","args"],"file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"interpreter":"INTERPRETER_UNSPECIFIED","script":"script","outputFilePath":"outputFilePath"},"validate":{"args":["args","args"],"file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"interpreter":"INTERPRETER_UNSPECIFIED","script":"script","outputFilePath":"outputFilePath"}}},{"file":{"path":"path","file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"permissions":"permissions","state":"DESIRED_STATE_UNSPECIFIED","content":"content"},"id":"id","repository":{"yum":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"zypper":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"apt":{"archiveType":"ARCHIVE_TYPE_UNSPECIFIED","components":["components","components"],"distribution":"distribution","gpgKey":"gpgKey","uri":"uri"},"goo":{"name":"name","url":"url"}},"pkg":{"deb":{"pullDeps":True,"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True}},"yum":{"name":"name"},"zypper":{"name":"name"},"desiredState":"DESIRED_STATE_UNSPECIFIED","msi":{"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"properties":["properties","properties"]},"apt":{"name":"name"},"googet":{"name":"name"},"rpm":{"pullDeps":True,"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True}}},"exec":{"enforce":{"args":["args","args"],"file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"interpreter":"INTERPRETER_UNSPECIFIED","script":"script","outputFilePath":"outputFilePath"},"validate":{"args":["args","args"],"file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"interpreter":"INTERPRETER_UNSPECIFIED","script":"script","outputFilePath":"outputFilePath"}}}]},{"inventoryFilters":[{"osVersion":"osVersion","osShortName":"osShortName"},{"osVersion":"osVersion","osShortName":"osShortName"}],"resources":[{"file":{"path":"path","file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"permissions":"permissions","state":"DESIRED_STATE_UNSPECIFIED","content":"content"},"id":"id","repository":{"yum":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"zypper":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"apt":{"archiveType":"ARCHIVE_TYPE_UNSPECIFIED","components":["components","components"],"distribution":"distribution","gpgKey":"gpgKey","uri":"uri"},"goo":{"name":"name","url":"url"}},"pkg":{"deb":{"pullDeps":True,"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True}},"yum":{"name":"name"},"zypper":{"name":"name"},"desiredState":"DESIRED_STATE_UNSPECIFIED","msi":{"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"properties":["properties","properties"]},"apt":{"name":"name"},"googet":{"name":"name"},"rpm":{"pullDeps":True,"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True}}},"exec":{"enforce":{"args":["args","args"],"file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"interpreter":"INTERPRETER_UNSPECIFIED","script":"script","outputFilePath":"outputFilePath"},"validate":{"args":["args","args"],"file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"interpreter":"INTERPRETER_UNSPECIFIED","script":"script","outputFilePath":"outputFilePath"}}},{"file":{"path":"path","file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"permissions":"permissions","state":"DESIRED_STATE_UNSPECIFIED","content":"content"},"id":"id","repository":{"yum":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"zypper":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"apt":{"archiveType":"ARCHIVE_TYPE_UNSPECIFIED","components":["components","components"],"distribution":"distribution","gpgKey":"gpgKey","uri":"uri"},"goo":{"name":"name","url":"url"}},"pkg":{"deb":{"pullDeps":True,"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True}},"yum":{"name":"name"},"zypper":{"name":"name"},"desiredState":"DESIRED_STATE_UNSPECIFIED","msi":{"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"properties":["properties","properties"]},"apt":{"name":"name"},"googet":{"name":"name"},"rpm":{"pullDeps":True,"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True}}},"exec":{"enforce":{"args":["args","args"],"file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"interpreter":"INTERPRETER_UNSPECIFIED","script":"script","outputFilePath":"outputFilePath"},"validate":{"args":["args","args"],"file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"interpreter":"INTERPRETER_UNSPECIFIED","script":"script","outputFilePath":"outputFilePath"}}}]}],"description":"description","id":"id","allowNoResourceGroupMatch":True},{"mode":"MODE_UNSPECIFIED","resourceGroups":[{"inventoryFilters":[{"osVersion":"osVersion","osShortName":"osShortName"},{"osVersion":"osVersion","osShortName":"osShortName"}],"resources":[{"file":{"path":"path","file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"permissions":"permissions","state":"DESIRED_STATE_UNSPECIFIED","content":"content"},"id":"id","repository":{"yum":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"zypper":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"apt":{"archiveType":"ARCHIVE_TYPE_UNSPECIFIED","components":["components","components"],"distribution":"distribution","gpgKey":"gpgKey","uri":"uri"},"goo":{"name":"name","url":"url"}},"pkg":{"deb":{"pullDeps":True,"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True}},"yum":{"name":"name"},"zypper":{"name":"name"},"desiredState":"DESIRED_STATE_UNSPECIFIED","msi":{"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"properties":["properties","properties"]},"apt":{"name":"name"},"googet":{"name":"name"},"rpm":{"pullDeps":True,"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True}}},"exec":{"enforce":{"args":["args","args"],"file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"interpreter":"INTERPRETER_UNSPECIFIED","script":"script","outputFilePath":"outputFilePath"},"validate":{"args":["args","args"],"file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"interpreter":"INTERPRETER_UNSPECIFIED","script":"script","outputFilePath":"outputFilePath"}}},{"file":{"path":"path","file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"permissions":"permissions","state":"DESIRED_STATE_UNSPECIFIED","content":"content"},"id":"id","repository":{"yum":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"zypper":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"apt":{"archiveType":"ARCHIVE_TYPE_UNSPECIFIED","components":["components","components"],"distribution":"distribution","gpgKey":"gpgKey","uri":"uri"},"goo":{"name":"name","url":"url"}},"pkg":{"deb":{"pullDeps":True,"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True}},"yum":{"name":"name"},"zypper":{"name":"name"},"desiredState":"DESIRED_STATE_UNSPECIFIED","msi":{"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"properties":["properties","properties"]},"apt":{"name":"name"},"googet":{"name":"name"},"rpm":{"pullDeps":True,"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True}}},"exec":{"enforce":{"args":["args","args"],"file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"interpreter":"INTERPRETER_UNSPECIFIED","script":"script","outputFilePath":"outputFilePath"},"validate":{"args":["args","args"],"file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"interpreter":"INTERPRETER_UNSPECIFIED","script":"script","outputFilePath":"outputFilePath"}}}]},{"inventoryFilters":[{"osVersion":"osVersion","osShortName":"osShortName"},{"osVersion":"osVersion","osShortName":"osShortName"}],"resources":[{"file":{"path":"path","file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"permissions":"permissions","state":"DESIRED_STATE_UNSPECIFIED","content":"content"},"id":"id","repository":{"yum":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"zypper":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"apt":{"archiveType":"ARCHIVE_TYPE_UNSPECIFIED","components":["components","components"],"distribution":"distribution","gpgKey":"gpgKey","uri":"uri"},"goo":{"name":"name","url":"url"}},"pkg":{"deb":{"pullDeps":True,"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True}},"yum":{"name":"name"},"zypper":{"name":"name"},"desiredState":"DESIRED_STATE_UNSPECIFIED","msi":{"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"properties":["properties","properties"]},"apt":{"name":"name"},"googet":{"name":"name"},"rpm":{"pullDeps":True,"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True}}},"exec":{"enforce":{"args":["args","args"],"file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"interpreter":"INTERPRETER_UNSPECIFIED","script":"script","outputFilePath":"outputFilePath"},"validate":{"args":["args","args"],"file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"interpreter":"INTERPRETER_UNSPECIFIED","script":"script","outputFilePath":"outputFilePath"}}},{"file":{"path":"path","file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"permissions":"permissions","state":"DESIRED_STATE_UNSPECIFIED","content":"content"},"id":"id","repository":{"yum":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"zypper":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"apt":{"archiveType":"ARCHIVE_TYPE_UNSPECIFIED","components":["components","components"],"distribution":"distribution","gpgKey":"gpgKey","uri":"uri"},"goo":{"name":"name","url":"url"}},"pkg":{"deb":{"pullDeps":True,"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True}},"yum":{"name":"name"},"zypper":{"name":"name"},"desiredState":"DESIRED_STATE_UNSPECIFIED","msi":{"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"properties":["properties","properties"]},"apt":{"name":"name"},"googet":{"name":"name"},"rpm":{"pullDeps":True,"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True}}},"exec":{"enforce":{"args":["args","args"],"file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"interpreter":"INTERPRETER_UNSPECIFIED","script":"script","outputFilePath":"outputFilePath"},"validate":{"args":["args","args"],"file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"interpreter":"INTERPRETER_UNSPECIFIED","script":"script","outputFilePath":"outputFilePath"}}}]}],"description":"description","id":"id","allowNoResourceGroupMatch":True}]}
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
                    ('osPolicyAssignmentId', 'os_policy_assignment_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/osPolicyAssignments'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_osconfig_projects_locations_os_policy_assignments_list(client):
    """Test case for osconfig_projects_locations_os_policy_assignments_list

    
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
        path='/v1/{parent}/osPolicyAssignments'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_osconfig_projects_locations_os_policy_assignments_list_revisions(client):
    """Test case for osconfig_projects_locations_os_policy_assignments_list_revisions

    
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
        path='/v1/{namelist_revision}'.format(name='name_example'),
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
        path='/v1/{parent}/patchDeployments'.format(parent='parent_example'),
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
        path='/v1/{name}'.format(name='name_example'),
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
        path='/v1/{parent}/patchDeployments'.format(parent='parent_example'),
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
        path='/v1/{name}'.format(name='name_example'),
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
        path='/v1/{namepaus}'.format(name='name_example'),
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
        path='/v1/{nameresum}'.format(name='name_example'),
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
        path='/v1/{namecance}'.format(name='name_example'),
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
        path='/v1/{parent}/patchJobs:execute'.format(parent='parent_example'),
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
                    ('uploadType', 'upload_type_example'),
                    ('view', 'view_example')]
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
        path='/v1/{parent}/instanceDetails'.format(parent='parent_example'),
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
        path='/v1/{parent}/patchJobs'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

