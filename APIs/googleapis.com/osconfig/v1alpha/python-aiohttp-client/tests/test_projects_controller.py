# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_instance_os_policies_compliances_response import ListInstanceOSPoliciesCompliancesResponse
from openapi_server.models.list_inventories_response import ListInventoriesResponse
from openapi_server.models.list_os_policy_assignment_reports_response import ListOSPolicyAssignmentReportsResponse
from openapi_server.models.list_os_policy_assignment_revisions_response import ListOSPolicyAssignmentRevisionsResponse
from openapi_server.models.list_os_policy_assignments_response import ListOSPolicyAssignmentsResponse
from openapi_server.models.list_vulnerability_reports_response import ListVulnerabilityReportsResponse
from openapi_server.models.os_policy_assignment import OSPolicyAssignment
from openapi_server.models.operation import Operation


pytestmark = pytest.mark.asyncio

async def test_osconfig_projects_locations_instance_os_policies_compliances_list(client):
    """Test case for osconfig_projects_locations_instance_os_policies_compliances_list

    
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
        path='/v1alpha/{parent}/instanceOSPoliciesCompliances'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


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
        path='/v1alpha/{parent}/inventories'.format(parent='parent_example'),
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
        path='/v1alpha/{parent}/reports'.format(parent='parent_example'),
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
        path='/v1alpha/{parent}/vulnerabilityReports'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_osconfig_projects_locations_os_policy_assignments_create(client):
    """Test case for osconfig_projects_locations_os_policy_assignments_create

    
    """
    body = {"rollout":{"disruptionBudget":{"fixed":0,"percent":6},"minWaitDuration":"minWaitDuration"},"instanceFilter":{"all":True,"exclusionLabels":[{"labels":{"key":"labels"}},{"labels":{"key":"labels"}}],"osShortNames":["osShortNames","osShortNames"],"inventories":[{"osVersion":"osVersion","osShortName":"osShortName"},{"osVersion":"osVersion","osShortName":"osShortName"}],"inclusionLabels":[{"labels":{"key":"labels"}},{"labels":{"key":"labels"}}]},"description":"description","reconciling":True,"baseline":True,"revisionCreateTime":"revisionCreateTime","revisionId":"revisionId","uid":"uid","deleted":True,"rolloutState":"ROLLOUT_STATE_UNSPECIFIED","name":"name","etag":"etag","osPolicies":[{"mode":"MODE_UNSPECIFIED","resourceGroups":[{"osFilter":{"osVersion":"osVersion","osShortName":"osShortName"},"inventoryFilters":[{"osVersion":"osVersion","osShortName":"osShortName"},{"osVersion":"osVersion","osShortName":"osShortName"}],"resources":[{"file":{"path":"path","file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"permissions":"permissions","state":"DESIRED_STATE_UNSPECIFIED","content":"content"},"id":"id","repository":{"yum":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"zypper":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"apt":{"archiveType":"ARCHIVE_TYPE_UNSPECIFIED","components":["components","components"],"distribution":"distribution","gpgKey":"gpgKey","uri":"uri"},"goo":{"name":"name","url":"url"}},"pkg":{"deb":{"pullDeps":True,"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True}},"yum":{"name":"name"},"zypper":{"name":"name"},"desiredState":"DESIRED_STATE_UNSPECIFIED","msi":{"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"properties":["properties","properties"]},"apt":{"name":"name"},"googet":{"name":"name"},"rpm":{"pullDeps":True,"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True}}},"exec":{"enforce":{"args":["args","args"],"file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"interpreter":"INTERPRETER_UNSPECIFIED","script":"script","outputFilePath":"outputFilePath"},"validate":{"args":["args","args"],"file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"interpreter":"INTERPRETER_UNSPECIFIED","script":"script","outputFilePath":"outputFilePath"}}},{"file":{"path":"path","file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"permissions":"permissions","state":"DESIRED_STATE_UNSPECIFIED","content":"content"},"id":"id","repository":{"yum":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"zypper":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"apt":{"archiveType":"ARCHIVE_TYPE_UNSPECIFIED","components":["components","components"],"distribution":"distribution","gpgKey":"gpgKey","uri":"uri"},"goo":{"name":"name","url":"url"}},"pkg":{"deb":{"pullDeps":True,"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True}},"yum":{"name":"name"},"zypper":{"name":"name"},"desiredState":"DESIRED_STATE_UNSPECIFIED","msi":{"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"properties":["properties","properties"]},"apt":{"name":"name"},"googet":{"name":"name"},"rpm":{"pullDeps":True,"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True}}},"exec":{"enforce":{"args":["args","args"],"file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"interpreter":"INTERPRETER_UNSPECIFIED","script":"script","outputFilePath":"outputFilePath"},"validate":{"args":["args","args"],"file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"interpreter":"INTERPRETER_UNSPECIFIED","script":"script","outputFilePath":"outputFilePath"}}}]},{"osFilter":{"osVersion":"osVersion","osShortName":"osShortName"},"inventoryFilters":[{"osVersion":"osVersion","osShortName":"osShortName"},{"osVersion":"osVersion","osShortName":"osShortName"}],"resources":[{"file":{"path":"path","file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"permissions":"permissions","state":"DESIRED_STATE_UNSPECIFIED","content":"content"},"id":"id","repository":{"yum":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"zypper":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"apt":{"archiveType":"ARCHIVE_TYPE_UNSPECIFIED","components":["components","components"],"distribution":"distribution","gpgKey":"gpgKey","uri":"uri"},"goo":{"name":"name","url":"url"}},"pkg":{"deb":{"pullDeps":True,"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True}},"yum":{"name":"name"},"zypper":{"name":"name"},"desiredState":"DESIRED_STATE_UNSPECIFIED","msi":{"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"properties":["properties","properties"]},"apt":{"name":"name"},"googet":{"name":"name"},"rpm":{"pullDeps":True,"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True}}},"exec":{"enforce":{"args":["args","args"],"file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"interpreter":"INTERPRETER_UNSPECIFIED","script":"script","outputFilePath":"outputFilePath"},"validate":{"args":["args","args"],"file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"interpreter":"INTERPRETER_UNSPECIFIED","script":"script","outputFilePath":"outputFilePath"}}},{"file":{"path":"path","file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"permissions":"permissions","state":"DESIRED_STATE_UNSPECIFIED","content":"content"},"id":"id","repository":{"yum":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"zypper":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"apt":{"archiveType":"ARCHIVE_TYPE_UNSPECIFIED","components":["components","components"],"distribution":"distribution","gpgKey":"gpgKey","uri":"uri"},"goo":{"name":"name","url":"url"}},"pkg":{"deb":{"pullDeps":True,"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True}},"yum":{"name":"name"},"zypper":{"name":"name"},"desiredState":"DESIRED_STATE_UNSPECIFIED","msi":{"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"properties":["properties","properties"]},"apt":{"name":"name"},"googet":{"name":"name"},"rpm":{"pullDeps":True,"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True}}},"exec":{"enforce":{"args":["args","args"],"file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"interpreter":"INTERPRETER_UNSPECIFIED","script":"script","outputFilePath":"outputFilePath"},"validate":{"args":["args","args"],"file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"interpreter":"INTERPRETER_UNSPECIFIED","script":"script","outputFilePath":"outputFilePath"}}}]}],"description":"description","id":"id","allowNoResourceGroupMatch":True},{"mode":"MODE_UNSPECIFIED","resourceGroups":[{"osFilter":{"osVersion":"osVersion","osShortName":"osShortName"},"inventoryFilters":[{"osVersion":"osVersion","osShortName":"osShortName"},{"osVersion":"osVersion","osShortName":"osShortName"}],"resources":[{"file":{"path":"path","file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"permissions":"permissions","state":"DESIRED_STATE_UNSPECIFIED","content":"content"},"id":"id","repository":{"yum":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"zypper":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"apt":{"archiveType":"ARCHIVE_TYPE_UNSPECIFIED","components":["components","components"],"distribution":"distribution","gpgKey":"gpgKey","uri":"uri"},"goo":{"name":"name","url":"url"}},"pkg":{"deb":{"pullDeps":True,"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True}},"yum":{"name":"name"},"zypper":{"name":"name"},"desiredState":"DESIRED_STATE_UNSPECIFIED","msi":{"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"properties":["properties","properties"]},"apt":{"name":"name"},"googet":{"name":"name"},"rpm":{"pullDeps":True,"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True}}},"exec":{"enforce":{"args":["args","args"],"file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"interpreter":"INTERPRETER_UNSPECIFIED","script":"script","outputFilePath":"outputFilePath"},"validate":{"args":["args","args"],"file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"interpreter":"INTERPRETER_UNSPECIFIED","script":"script","outputFilePath":"outputFilePath"}}},{"file":{"path":"path","file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"permissions":"permissions","state":"DESIRED_STATE_UNSPECIFIED","content":"content"},"id":"id","repository":{"yum":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"zypper":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"apt":{"archiveType":"ARCHIVE_TYPE_UNSPECIFIED","components":["components","components"],"distribution":"distribution","gpgKey":"gpgKey","uri":"uri"},"goo":{"name":"name","url":"url"}},"pkg":{"deb":{"pullDeps":True,"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True}},"yum":{"name":"name"},"zypper":{"name":"name"},"desiredState":"DESIRED_STATE_UNSPECIFIED","msi":{"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"properties":["properties","properties"]},"apt":{"name":"name"},"googet":{"name":"name"},"rpm":{"pullDeps":True,"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True}}},"exec":{"enforce":{"args":["args","args"],"file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"interpreter":"INTERPRETER_UNSPECIFIED","script":"script","outputFilePath":"outputFilePath"},"validate":{"args":["args","args"],"file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"interpreter":"INTERPRETER_UNSPECIFIED","script":"script","outputFilePath":"outputFilePath"}}}]},{"osFilter":{"osVersion":"osVersion","osShortName":"osShortName"},"inventoryFilters":[{"osVersion":"osVersion","osShortName":"osShortName"},{"osVersion":"osVersion","osShortName":"osShortName"}],"resources":[{"file":{"path":"path","file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"permissions":"permissions","state":"DESIRED_STATE_UNSPECIFIED","content":"content"},"id":"id","repository":{"yum":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"zypper":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"apt":{"archiveType":"ARCHIVE_TYPE_UNSPECIFIED","components":["components","components"],"distribution":"distribution","gpgKey":"gpgKey","uri":"uri"},"goo":{"name":"name","url":"url"}},"pkg":{"deb":{"pullDeps":True,"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True}},"yum":{"name":"name"},"zypper":{"name":"name"},"desiredState":"DESIRED_STATE_UNSPECIFIED","msi":{"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"properties":["properties","properties"]},"apt":{"name":"name"},"googet":{"name":"name"},"rpm":{"pullDeps":True,"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True}}},"exec":{"enforce":{"args":["args","args"],"file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"interpreter":"INTERPRETER_UNSPECIFIED","script":"script","outputFilePath":"outputFilePath"},"validate":{"args":["args","args"],"file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"interpreter":"INTERPRETER_UNSPECIFIED","script":"script","outputFilePath":"outputFilePath"}}},{"file":{"path":"path","file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"permissions":"permissions","state":"DESIRED_STATE_UNSPECIFIED","content":"content"},"id":"id","repository":{"yum":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"zypper":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"apt":{"archiveType":"ARCHIVE_TYPE_UNSPECIFIED","components":["components","components"],"distribution":"distribution","gpgKey":"gpgKey","uri":"uri"},"goo":{"name":"name","url":"url"}},"pkg":{"deb":{"pullDeps":True,"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True}},"yum":{"name":"name"},"zypper":{"name":"name"},"desiredState":"DESIRED_STATE_UNSPECIFIED","msi":{"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"properties":["properties","properties"]},"apt":{"name":"name"},"googet":{"name":"name"},"rpm":{"pullDeps":True,"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True}}},"exec":{"enforce":{"args":["args","args"],"file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"interpreter":"INTERPRETER_UNSPECIFIED","script":"script","outputFilePath":"outputFilePath"},"validate":{"args":["args","args"],"file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"interpreter":"INTERPRETER_UNSPECIFIED","script":"script","outputFilePath":"outputFilePath"}}}]}],"description":"description","id":"id","allowNoResourceGroupMatch":True}]}
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
        path='/v1alpha/{parent}/osPolicyAssignments'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_osconfig_projects_locations_os_policy_assignments_delete(client):
    """Test case for osconfig_projects_locations_os_policy_assignments_delete

    
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
        path='/v1alpha/{name}'.format(name='name_example'),
        headers=headers,
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
        path='/v1alpha/{parent}/osPolicyAssignments'.format(parent='parent_example'),
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
        path='/v1alpha/{namelist_revision}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_osconfig_projects_locations_os_policy_assignments_operations_cancel(client):
    """Test case for osconfig_projects_locations_os_policy_assignments_operations_cancel

    
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
        path='/v1alpha/{namecance}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_osconfig_projects_locations_os_policy_assignments_operations_get(client):
    """Test case for osconfig_projects_locations_os_policy_assignments_operations_get

    
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
        path='/v1alpha/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_osconfig_projects_locations_os_policy_assignments_patch(client):
    """Test case for osconfig_projects_locations_os_policy_assignments_patch

    
    """
    body = {"rollout":{"disruptionBudget":{"fixed":0,"percent":6},"minWaitDuration":"minWaitDuration"},"instanceFilter":{"all":True,"exclusionLabels":[{"labels":{"key":"labels"}},{"labels":{"key":"labels"}}],"osShortNames":["osShortNames","osShortNames"],"inventories":[{"osVersion":"osVersion","osShortName":"osShortName"},{"osVersion":"osVersion","osShortName":"osShortName"}],"inclusionLabels":[{"labels":{"key":"labels"}},{"labels":{"key":"labels"}}]},"description":"description","reconciling":True,"baseline":True,"revisionCreateTime":"revisionCreateTime","revisionId":"revisionId","uid":"uid","deleted":True,"rolloutState":"ROLLOUT_STATE_UNSPECIFIED","name":"name","etag":"etag","osPolicies":[{"mode":"MODE_UNSPECIFIED","resourceGroups":[{"osFilter":{"osVersion":"osVersion","osShortName":"osShortName"},"inventoryFilters":[{"osVersion":"osVersion","osShortName":"osShortName"},{"osVersion":"osVersion","osShortName":"osShortName"}],"resources":[{"file":{"path":"path","file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"permissions":"permissions","state":"DESIRED_STATE_UNSPECIFIED","content":"content"},"id":"id","repository":{"yum":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"zypper":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"apt":{"archiveType":"ARCHIVE_TYPE_UNSPECIFIED","components":["components","components"],"distribution":"distribution","gpgKey":"gpgKey","uri":"uri"},"goo":{"name":"name","url":"url"}},"pkg":{"deb":{"pullDeps":True,"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True}},"yum":{"name":"name"},"zypper":{"name":"name"},"desiredState":"DESIRED_STATE_UNSPECIFIED","msi":{"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"properties":["properties","properties"]},"apt":{"name":"name"},"googet":{"name":"name"},"rpm":{"pullDeps":True,"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True}}},"exec":{"enforce":{"args":["args","args"],"file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"interpreter":"INTERPRETER_UNSPECIFIED","script":"script","outputFilePath":"outputFilePath"},"validate":{"args":["args","args"],"file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"interpreter":"INTERPRETER_UNSPECIFIED","script":"script","outputFilePath":"outputFilePath"}}},{"file":{"path":"path","file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"permissions":"permissions","state":"DESIRED_STATE_UNSPECIFIED","content":"content"},"id":"id","repository":{"yum":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"zypper":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"apt":{"archiveType":"ARCHIVE_TYPE_UNSPECIFIED","components":["components","components"],"distribution":"distribution","gpgKey":"gpgKey","uri":"uri"},"goo":{"name":"name","url":"url"}},"pkg":{"deb":{"pullDeps":True,"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True}},"yum":{"name":"name"},"zypper":{"name":"name"},"desiredState":"DESIRED_STATE_UNSPECIFIED","msi":{"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"properties":["properties","properties"]},"apt":{"name":"name"},"googet":{"name":"name"},"rpm":{"pullDeps":True,"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True}}},"exec":{"enforce":{"args":["args","args"],"file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"interpreter":"INTERPRETER_UNSPECIFIED","script":"script","outputFilePath":"outputFilePath"},"validate":{"args":["args","args"],"file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"interpreter":"INTERPRETER_UNSPECIFIED","script":"script","outputFilePath":"outputFilePath"}}}]},{"osFilter":{"osVersion":"osVersion","osShortName":"osShortName"},"inventoryFilters":[{"osVersion":"osVersion","osShortName":"osShortName"},{"osVersion":"osVersion","osShortName":"osShortName"}],"resources":[{"file":{"path":"path","file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"permissions":"permissions","state":"DESIRED_STATE_UNSPECIFIED","content":"content"},"id":"id","repository":{"yum":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"zypper":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"apt":{"archiveType":"ARCHIVE_TYPE_UNSPECIFIED","components":["components","components"],"distribution":"distribution","gpgKey":"gpgKey","uri":"uri"},"goo":{"name":"name","url":"url"}},"pkg":{"deb":{"pullDeps":True,"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True}},"yum":{"name":"name"},"zypper":{"name":"name"},"desiredState":"DESIRED_STATE_UNSPECIFIED","msi":{"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"properties":["properties","properties"]},"apt":{"name":"name"},"googet":{"name":"name"},"rpm":{"pullDeps":True,"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True}}},"exec":{"enforce":{"args":["args","args"],"file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"interpreter":"INTERPRETER_UNSPECIFIED","script":"script","outputFilePath":"outputFilePath"},"validate":{"args":["args","args"],"file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"interpreter":"INTERPRETER_UNSPECIFIED","script":"script","outputFilePath":"outputFilePath"}}},{"file":{"path":"path","file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"permissions":"permissions","state":"DESIRED_STATE_UNSPECIFIED","content":"content"},"id":"id","repository":{"yum":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"zypper":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"apt":{"archiveType":"ARCHIVE_TYPE_UNSPECIFIED","components":["components","components"],"distribution":"distribution","gpgKey":"gpgKey","uri":"uri"},"goo":{"name":"name","url":"url"}},"pkg":{"deb":{"pullDeps":True,"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True}},"yum":{"name":"name"},"zypper":{"name":"name"},"desiredState":"DESIRED_STATE_UNSPECIFIED","msi":{"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"properties":["properties","properties"]},"apt":{"name":"name"},"googet":{"name":"name"},"rpm":{"pullDeps":True,"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True}}},"exec":{"enforce":{"args":["args","args"],"file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"interpreter":"INTERPRETER_UNSPECIFIED","script":"script","outputFilePath":"outputFilePath"},"validate":{"args":["args","args"],"file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"interpreter":"INTERPRETER_UNSPECIFIED","script":"script","outputFilePath":"outputFilePath"}}}]}],"description":"description","id":"id","allowNoResourceGroupMatch":True},{"mode":"MODE_UNSPECIFIED","resourceGroups":[{"osFilter":{"osVersion":"osVersion","osShortName":"osShortName"},"inventoryFilters":[{"osVersion":"osVersion","osShortName":"osShortName"},{"osVersion":"osVersion","osShortName":"osShortName"}],"resources":[{"file":{"path":"path","file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"permissions":"permissions","state":"DESIRED_STATE_UNSPECIFIED","content":"content"},"id":"id","repository":{"yum":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"zypper":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"apt":{"archiveType":"ARCHIVE_TYPE_UNSPECIFIED","components":["components","components"],"distribution":"distribution","gpgKey":"gpgKey","uri":"uri"},"goo":{"name":"name","url":"url"}},"pkg":{"deb":{"pullDeps":True,"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True}},"yum":{"name":"name"},"zypper":{"name":"name"},"desiredState":"DESIRED_STATE_UNSPECIFIED","msi":{"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"properties":["properties","properties"]},"apt":{"name":"name"},"googet":{"name":"name"},"rpm":{"pullDeps":True,"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True}}},"exec":{"enforce":{"args":["args","args"],"file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"interpreter":"INTERPRETER_UNSPECIFIED","script":"script","outputFilePath":"outputFilePath"},"validate":{"args":["args","args"],"file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"interpreter":"INTERPRETER_UNSPECIFIED","script":"script","outputFilePath":"outputFilePath"}}},{"file":{"path":"path","file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"permissions":"permissions","state":"DESIRED_STATE_UNSPECIFIED","content":"content"},"id":"id","repository":{"yum":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"zypper":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"apt":{"archiveType":"ARCHIVE_TYPE_UNSPECIFIED","components":["components","components"],"distribution":"distribution","gpgKey":"gpgKey","uri":"uri"},"goo":{"name":"name","url":"url"}},"pkg":{"deb":{"pullDeps":True,"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True}},"yum":{"name":"name"},"zypper":{"name":"name"},"desiredState":"DESIRED_STATE_UNSPECIFIED","msi":{"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"properties":["properties","properties"]},"apt":{"name":"name"},"googet":{"name":"name"},"rpm":{"pullDeps":True,"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True}}},"exec":{"enforce":{"args":["args","args"],"file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"interpreter":"INTERPRETER_UNSPECIFIED","script":"script","outputFilePath":"outputFilePath"},"validate":{"args":["args","args"],"file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"interpreter":"INTERPRETER_UNSPECIFIED","script":"script","outputFilePath":"outputFilePath"}}}]},{"osFilter":{"osVersion":"osVersion","osShortName":"osShortName"},"inventoryFilters":[{"osVersion":"osVersion","osShortName":"osShortName"},{"osVersion":"osVersion","osShortName":"osShortName"}],"resources":[{"file":{"path":"path","file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"permissions":"permissions","state":"DESIRED_STATE_UNSPECIFIED","content":"content"},"id":"id","repository":{"yum":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"zypper":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"apt":{"archiveType":"ARCHIVE_TYPE_UNSPECIFIED","components":["components","components"],"distribution":"distribution","gpgKey":"gpgKey","uri":"uri"},"goo":{"name":"name","url":"url"}},"pkg":{"deb":{"pullDeps":True,"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True}},"yum":{"name":"name"},"zypper":{"name":"name"},"desiredState":"DESIRED_STATE_UNSPECIFIED","msi":{"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"properties":["properties","properties"]},"apt":{"name":"name"},"googet":{"name":"name"},"rpm":{"pullDeps":True,"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True}}},"exec":{"enforce":{"args":["args","args"],"file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"interpreter":"INTERPRETER_UNSPECIFIED","script":"script","outputFilePath":"outputFilePath"},"validate":{"args":["args","args"],"file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"interpreter":"INTERPRETER_UNSPECIFIED","script":"script","outputFilePath":"outputFilePath"}}},{"file":{"path":"path","file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"permissions":"permissions","state":"DESIRED_STATE_UNSPECIFIED","content":"content"},"id":"id","repository":{"yum":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"zypper":{"baseUrl":"baseUrl","displayName":"displayName","id":"id","gpgKeys":["gpgKeys","gpgKeys"]},"apt":{"archiveType":"ARCHIVE_TYPE_UNSPECIFIED","components":["components","components"],"distribution":"distribution","gpgKey":"gpgKey","uri":"uri"},"goo":{"name":"name","url":"url"}},"pkg":{"deb":{"pullDeps":True,"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True}},"yum":{"name":"name"},"zypper":{"name":"name"},"desiredState":"DESIRED_STATE_UNSPECIFIED","msi":{"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"properties":["properties","properties"]},"apt":{"name":"name"},"googet":{"name":"name"},"rpm":{"pullDeps":True,"source":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True}}},"exec":{"enforce":{"args":["args","args"],"file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"interpreter":"INTERPRETER_UNSPECIFIED","script":"script","outputFilePath":"outputFilePath"},"validate":{"args":["args","args"],"file":{"gcs":{"bucket":"bucket","generation":"generation","object":"object"},"localPath":"localPath","remote":{"sha256Checksum":"sha256Checksum","uri":"uri"},"allowInsecure":True},"interpreter":"INTERPRETER_UNSPECIFIED","script":"script","outputFilePath":"outputFilePath"}}}]}],"description":"description","id":"id","allowNoResourceGroupMatch":True}]}
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
        path='/v1alpha/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

