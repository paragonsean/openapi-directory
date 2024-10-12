# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.apply_conversion_workspace_request import ApplyConversionWorkspaceRequest
from openapi_server.models.commit_conversion_workspace_request import CommitConversionWorkspaceRequest
from openapi_server.models.connection_profile import ConnectionProfile
from openapi_server.models.conversion_workspace import ConversionWorkspace
from openapi_server.models.convert_conversion_workspace_request import ConvertConversionWorkspaceRequest
from openapi_server.models.describe_conversion_workspace_revisions_response import DescribeConversionWorkspaceRevisionsResponse
from openapi_server.models.describe_database_entities_response import DescribeDatabaseEntitiesResponse
from openapi_server.models.fetch_static_ips_response import FetchStaticIpsResponse
from openapi_server.models.generate_ssh_script_request import GenerateSshScriptRequest
from openapi_server.models.generate_tcp_proxy_script_request import GenerateTcpProxyScriptRequest
from openapi_server.models.import_mapping_rules_request import ImportMappingRulesRequest
from openapi_server.models.list_connection_profiles_response import ListConnectionProfilesResponse
from openapi_server.models.list_conversion_workspaces_response import ListConversionWorkspacesResponse
from openapi_server.models.list_locations_response import ListLocationsResponse
from openapi_server.models.list_mapping_rules_response import ListMappingRulesResponse
from openapi_server.models.list_migration_jobs_response import ListMigrationJobsResponse
from openapi_server.models.list_operations_response import ListOperationsResponse
from openapi_server.models.list_private_connections_response import ListPrivateConnectionsResponse
from openapi_server.models.mapping_rule import MappingRule
from openapi_server.models.migration_job import MigrationJob
from openapi_server.models.operation import Operation
from openapi_server.models.policy import Policy
from openapi_server.models.private_connection import PrivateConnection
from openapi_server.models.restart_migration_job_request import RestartMigrationJobRequest
from openapi_server.models.search_background_jobs_response import SearchBackgroundJobsResponse
from openapi_server.models.seed_conversion_workspace_request import SeedConversionWorkspaceRequest
from openapi_server.models.set_iam_policy_request import SetIamPolicyRequest
from openapi_server.models.ssh_script import SshScript
from openapi_server.models.start_migration_job_request import StartMigrationJobRequest
from openapi_server.models.tcp_proxy_script import TcpProxyScript
from openapi_server.models.test_iam_permissions_request import TestIamPermissionsRequest
from openapi_server.models.test_iam_permissions_response import TestIamPermissionsResponse
from openapi_server.models.verify_migration_job_request import VerifyMigrationJobRequest


pytestmark = pytest.mark.asyncio

async def test_datamigration_projects_locations_connection_profiles_create(client):
    """Test case for datamigration_projects_locations_connection_profiles_create

    
    """
    body = {"oracle":{"password":"password","databaseService":"databaseService","port":5,"privateConnectivity":{"privateConnection":"privateConnection"},"host":"host","passwordSet":True,"staticServiceIpConnectivity":"{}","ssl":{"clientCertificate":"clientCertificate","clientKey":"clientKey","type":"SSL_TYPE_UNSPECIFIED","caCertificate":"caCertificate"},"forwardSshConnectivity":{"privateKey":"privateKey","hostname":"hostname","password":"password","port":1,"username":"username"},"username":"username"},"cloudsql":{"settings":{"sourceId":"sourceId","dataDiskSizeGb":"dataDiskSizeGb","storageAutoResizeLimit":"storageAutoResizeLimit","databaseFlags":{"key":"databaseFlags"},"rootPasswordSet":True,"dataDiskType":"SQL_DATA_DISK_TYPE_UNSPECIFIED","activationPolicy":"SQL_ACTIVATION_POLICY_UNSPECIFIED","edition":"EDITION_UNSPECIFIED","userLabels":{"key":"userLabels"},"databaseVersion":"SQL_DATABASE_VERSION_UNSPECIFIED","autoStorageIncrease":True,"ipConfig":{"requireSsl":True,"privateNetwork":"privateNetwork","allocatedIpRange":"allocatedIpRange","authorizedNetworks":[{"expireTime":"expireTime","label":"label","ttl":"ttl","value":"value"},{"expireTime":"expireTime","label":"label","ttl":"ttl","value":"value"}],"enableIpv4":True},"secondaryZone":"secondaryZone","availabilityType":"SQL_AVAILABILITY_TYPE_UNSPECIFIED","cmekKeyName":"cmekKeyName","tier":"tier","zone":"zone","collation":"collation","dataCacheConfig":{"dataCacheEnabled":True},"rootPassword":"rootPassword"},"privateIp":"privateIp","cloudSqlId":"cloudSqlId","publicIp":"publicIp","additionalPublicIp":"additionalPublicIp"},"displayName":"displayName","alloydb":{"settings":{"encryptionConfig":{"kmsKeyName":"kmsKeyName"},"primaryInstanceSettings":{"machineConfig":{"cpuCount":0},"databaseFlags":{"key":"databaseFlags"},"privateIp":"privateIp","id":"id","labels":{"key":"labels"}},"initialUser":{"password":"password","passwordSet":True,"user":"user"},"vpcNetwork":"vpcNetwork","databaseVersion":"DATABASE_VERSION_UNSPECIFIED","labels":{"key":"labels"}},"clusterId":"clusterId"},"updateTime":"updateTime","error":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"},"labels":{"key":"labels"},"postgresql":{"password":"password","privateServiceConnectConnectivity":{"serviceAttachment":"serviceAttachment"},"port":5,"cloudSqlId":"cloudSqlId","host":"host","staticIpConnectivity":"{}","networkArchitecture":"NETWORK_ARCHITECTURE_UNSPECIFIED","passwordSet":True,"alloydbClusterId":"alloydbClusterId","ssl":{"clientCertificate":"clientCertificate","clientKey":"clientKey","type":"SSL_TYPE_UNSPECIFIED","caCertificate":"caCertificate"},"username":"username"},"createTime":"createTime","provider":"DATABASE_PROVIDER_UNSPECIFIED","name":"name","mysql":{"password":"password","port":6,"cloudSqlId":"cloudSqlId","host":"host","passwordSet":True,"ssl":{"clientCertificate":"clientCertificate","clientKey":"clientKey","type":"SSL_TYPE_UNSPECIFIED","caCertificate":"caCertificate"},"username":"username"},"state":"STATE_UNSPECIFIED"}
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
                    ('connectionProfileId', 'connection_profile_id_example'),
                    ('requestId', 'request_id_example'),
                    ('skipValidation', True),
                    ('validateOnly', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/connectionProfiles'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datamigration_projects_locations_connection_profiles_list(client):
    """Test case for datamigration_projects_locations_connection_profiles_list

    
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
        path='/v1/{parent}/connectionProfiles'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datamigration_projects_locations_conversion_workspaces_apply(client):
    """Test case for datamigration_projects_locations_conversion_workspaces_apply

    
    """
    body = {"filter":"filter","dryRun":True,"connectionProfile":"connectionProfile","autoCommit":True}
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
        path='/v1/{nameappl}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datamigration_projects_locations_conversion_workspaces_commit(client):
    """Test case for datamigration_projects_locations_conversion_workspaces_commit

    
    """
    body = {"commitName":"commitName"}
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
        path='/v1/{namecommi}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datamigration_projects_locations_conversion_workspaces_convert(client):
    """Test case for datamigration_projects_locations_conversion_workspaces_convert

    
    """
    body = {"filter":"filter","convertFullPath":True,"autoCommit":True}
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
        path='/v1/{nameconver}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datamigration_projects_locations_conversion_workspaces_create(client):
    """Test case for datamigration_projects_locations_conversion_workspaces_create

    
    """
    body = {"globalSettings":{"key":"globalSettings"},"latestCommitTime":"latestCommitTime","createTime":"createTime","displayName":"displayName","destination":{"engine":"DATABASE_ENGINE_UNSPECIFIED","version":"version"},"name":"name","hasUncommittedChanges":True,"updateTime":"updateTime","source":{"engine":"DATABASE_ENGINE_UNSPECIFIED","version":"version"},"latestCommitId":"latestCommitId"}
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
                    ('conversionWorkspaceId', 'conversion_workspace_id_example'),
                    ('requestId', 'request_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/conversionWorkspaces'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datamigration_projects_locations_conversion_workspaces_describe_conversion_workspace_revisions(client):
    """Test case for datamigration_projects_locations_conversion_workspaces_describe_conversion_workspace_revisions

    
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
                    ('commitId', 'commit_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{conversion_workspacedescribe_conversion_workspace_revision}'.format(conversion_workspace='conversion_workspace_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datamigration_projects_locations_conversion_workspaces_describe_database_entities(client):
    """Test case for datamigration_projects_locations_conversion_workspaces_describe_database_entities

    
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
                    ('commitId', 'commit_id_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('tree', 'tree_example'),
                    ('uncommitted', True),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{conversion_workspacedescribe_database_entitie}'.format(conversion_workspace='conversion_workspace_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datamigration_projects_locations_conversion_workspaces_list(client):
    """Test case for datamigration_projects_locations_conversion_workspaces_list

    
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
        path='/v1/{parent}/conversionWorkspaces'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datamigration_projects_locations_conversion_workspaces_mapping_rules_create(client):
    """Test case for datamigration_projects_locations_conversion_workspaces_mapping_rules_create

    
    """
    body = {"entityMove":{"newSchema":"newSchema"},"ruleScope":"DATABASE_ENTITY_TYPE_UNSPECIFIED","displayName":"displayName","conditionalColumnSetValue":{"sourceTextFilter":{"sourceMinLengthFilter":"sourceMinLengthFilter","sourceMaxLengthFilter":"sourceMaxLengthFilter"},"sourceNumericFilter":{"sourceMinPrecisionFilter":1,"sourceMaxScaleFilter":6,"sourceMinScaleFilter":5,"numericFilterOption":"NUMERIC_FILTER_OPTION_UNSPECIFIED","sourceMaxPrecisionFilter":0},"customFeatures":{"key":""},"valueTransformation":{"roundScale":{"scale":2},"assignSpecificValue":{"value":"value"},"assignMinValue":"{}","assignMaxValue":"{}","doubleComparison":{"valueComparison":"VALUE_COMPARISON_UNSPECIFIED","value":5.637376656633329},"isNull":"{}","valueList":{"valuePresentList":"VALUE_PRESENT_IN_LIST_UNSPECIFIED","ignoreCase":True,"values":["values","values"]},"intComparison":{"valueComparison":"VALUE_COMPARISON_UNSPECIFIED","value":"value"},"assignNull":"{}","applyHash":{"uuidFromBytes":"{}"}}},"convertRowidColumn":{"onlyIfNoPrimaryKey":True},"revisionCreateTime":"revisionCreateTime","singleColumnChange":{"charset":"charset","nullable":True,"udt":True,"dataType":"dataType","fractionalSecondsPrecision":4,"precision":7,"length":"length","scale":1,"arrayLength":2,"array":True,"setValues":["setValues","setValues"],"customFeatures":{"key":""},"comment":"comment","autoGenerated":True,"collation":"collation"},"multiEntityRename":{"sourceNameTransformation":"ENTITY_NAME_TRANSFORMATION_UNSPECIFIED","newNamePattern":"newNamePattern"},"filter":{"entityNameSuffix":"entityNameSuffix","entities":["entities","entities"],"entityNamePrefix":"entityNamePrefix","parentEntity":"parentEntity","entityNameContains":"entityNameContains"},"revisionId":"revisionId","multiColumnDataTypeChange":{"overrideScale":3,"overrideLength":"overrideLength","sourceTextFilter":{"sourceMinLengthFilter":"sourceMinLengthFilter","sourceMaxLengthFilter":"sourceMaxLengthFilter"},"sourceNumericFilter":{"sourceMinPrecisionFilter":1,"sourceMaxScaleFilter":6,"sourceMinScaleFilter":5,"numericFilterOption":"NUMERIC_FILTER_OPTION_UNSPECIFIED","sourceMaxPrecisionFilter":0},"customFeatures":{"key":""},"overridePrecision":9,"sourceDataTypeFilter":"sourceDataTypeFilter","overrideFractionalSecondsPrecision":7,"newDataType":"newDataType"},"singlePackageChange":{"packageDescription":"packageDescription","packageBody":"packageBody"},"filterTableColumns":{"excludeColumns":["excludeColumns","excludeColumns"],"includeColumns":["includeColumns","includeColumns"]},"sourceSqlChange":{"sqlCode":"sqlCode"},"name":"name","ruleOrder":"ruleOrder","state":"STATE_UNSPECIFIED","singleEntityRename":{"newName":"newName"},"setTablePrimaryKey":{"primaryKeyColumns":["primaryKeyColumns","primaryKeyColumns"],"primaryKey":"primaryKey"}}
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
                    ('mappingRuleId', 'mapping_rule_id_example'),
                    ('requestId', 'request_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/mappingRules'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datamigration_projects_locations_conversion_workspaces_mapping_rules_import(client):
    """Test case for datamigration_projects_locations_conversion_workspaces_mapping_rules_import

    
    """
    body = {"rulesFormat":"IMPORT_RULES_FILE_FORMAT_UNSPECIFIED","rulesFiles":[{"rulesContent":"rulesContent","rulesSourceFilename":"rulesSourceFilename"},{"rulesContent":"rulesContent","rulesSourceFilename":"rulesSourceFilename"}],"autoCommit":True}
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
        path='/v1/{parent}/mappingRules:import'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datamigration_projects_locations_conversion_workspaces_mapping_rules_list(client):
    """Test case for datamigration_projects_locations_conversion_workspaces_mapping_rules_list

    
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
        path='/v1/{parent}/mappingRules'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datamigration_projects_locations_conversion_workspaces_rollback(client):
    """Test case for datamigration_projects_locations_conversion_workspaces_rollback

    
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
        path='/v1/{namerollbac}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datamigration_projects_locations_conversion_workspaces_search_background_jobs(client):
    """Test case for datamigration_projects_locations_conversion_workspaces_search_background_jobs

    
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
                    ('completedUntilTime', 'completed_until_time_example'),
                    ('maxSize', 56),
                    ('returnMostRecentPerJobType', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{conversion_workspacesearch_background_job}'.format(conversion_workspace='conversion_workspace_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datamigration_projects_locations_conversion_workspaces_seed(client):
    """Test case for datamigration_projects_locations_conversion_workspaces_seed

    
    """
    body = {"sourceConnectionProfile":"sourceConnectionProfile","destinationConnectionProfile":"destinationConnectionProfile","autoCommit":True}
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
        path='/v1/{namesee}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datamigration_projects_locations_fetch_static_ips(client):
    """Test case for datamigration_projects_locations_fetch_static_ips

    
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
        path='/v1/{namefetch_static_ip}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datamigration_projects_locations_list(client):
    """Test case for datamigration_projects_locations_list

    
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

async def test_datamigration_projects_locations_migration_jobs_create(client):
    """Test case for datamigration_projects_locations_migration_jobs_create

    
    """
    body = {"phase":"PHASE_UNSPECIFIED","dumpFlags":{"dumpFlags":[{"name":"name","value":"value"},{"name":"name","value":"value"}]},"displayName":"displayName","dumpPath":"dumpPath","destination":"destination","destinationDatabase":{"engine":"DATABASE_ENGINE_UNSPECIFIED","provider":"DATABASE_PROVIDER_UNSPECIFIED"},"reverseSshConnectivity":{"vm":"vm","vpc":"vpc","vmIp":"vmIp","vmPort":0},"updateTime":"updateTime","source":"source","error":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"},"type":"TYPE_UNSPECIFIED","labels":{"key":"labels"},"duration":"duration","filter":"filter","conversionWorkspace":{"name":"name","commitId":"commitId"},"vpcPeeringConnectivity":{"vpc":"vpc"},"cmekKeyName":"cmekKeyName","performanceConfig":{"dumpParallelLevel":"DUMP_PARALLEL_LEVEL_UNSPECIFIED"},"createTime":"createTime","sourceDatabase":{"engine":"DATABASE_ENGINE_UNSPECIFIED","provider":"DATABASE_PROVIDER_UNSPECIFIED"},"name":"name","staticIpConnectivity":"{}","endTime":"endTime","state":"STATE_UNSPECIFIED"}
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
                    ('migrationJobId', 'migration_job_id_example'),
                    ('requestId', 'request_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/migrationJobs'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datamigration_projects_locations_migration_jobs_demote_destination(client):
    """Test case for datamigration_projects_locations_migration_jobs_demote_destination

    
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
        path='/v1/{namedemote_destinatio}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datamigration_projects_locations_migration_jobs_generate_ssh_script(client):
    """Test case for datamigration_projects_locations_migration_jobs_generate_ssh_script

    
    """
    body = {"vmCreationConfig":{"subnet":"subnet","vmZone":"vmZone","vmMachineType":"vmMachineType"},"vmSelectionConfig":{"vmZone":"vmZone"},"vm":"vm","vmPort":0}
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
        path='/v1/{migration_jobgenerate_ssh_scrip}'.format(migration_job='migration_job_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datamigration_projects_locations_migration_jobs_generate_tcp_proxy_script(client):
    """Test case for datamigration_projects_locations_migration_jobs_generate_tcp_proxy_script

    
    """
    body = {"vmName":"vmName","vmZone":"vmZone","vmSubnet":"vmSubnet","vmMachineType":"vmMachineType"}
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
        path='/v1/{migration_jobgenerate_tcp_proxy_scrip}'.format(migration_job='migration_job_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datamigration_projects_locations_migration_jobs_list(client):
    """Test case for datamigration_projects_locations_migration_jobs_list

    
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
        path='/v1/{parent}/migrationJobs'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datamigration_projects_locations_migration_jobs_patch(client):
    """Test case for datamigration_projects_locations_migration_jobs_patch

    
    """
    body = {"phase":"PHASE_UNSPECIFIED","dumpFlags":{"dumpFlags":[{"name":"name","value":"value"},{"name":"name","value":"value"}]},"displayName":"displayName","dumpPath":"dumpPath","destination":"destination","destinationDatabase":{"engine":"DATABASE_ENGINE_UNSPECIFIED","provider":"DATABASE_PROVIDER_UNSPECIFIED"},"reverseSshConnectivity":{"vm":"vm","vpc":"vpc","vmIp":"vmIp","vmPort":0},"updateTime":"updateTime","source":"source","error":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"},"type":"TYPE_UNSPECIFIED","labels":{"key":"labels"},"duration":"duration","filter":"filter","conversionWorkspace":{"name":"name","commitId":"commitId"},"vpcPeeringConnectivity":{"vpc":"vpc"},"cmekKeyName":"cmekKeyName","performanceConfig":{"dumpParallelLevel":"DUMP_PARALLEL_LEVEL_UNSPECIFIED"},"createTime":"createTime","sourceDatabase":{"engine":"DATABASE_ENGINE_UNSPECIFIED","provider":"DATABASE_PROVIDER_UNSPECIFIED"},"name":"name","staticIpConnectivity":"{}","endTime":"endTime","state":"STATE_UNSPECIFIED"}
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

async def test_datamigration_projects_locations_migration_jobs_promote(client):
    """Test case for datamigration_projects_locations_migration_jobs_promote

    
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
        path='/v1/{namepromot}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datamigration_projects_locations_migration_jobs_restart(client):
    """Test case for datamigration_projects_locations_migration_jobs_restart

    
    """
    body = {"skipValidation":True}
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
        path='/v1/{namerestar}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datamigration_projects_locations_migration_jobs_resume(client):
    """Test case for datamigration_projects_locations_migration_jobs_resume

    
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

async def test_datamigration_projects_locations_migration_jobs_start(client):
    """Test case for datamigration_projects_locations_migration_jobs_start

    
    """
    body = {"skipValidation":True}
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
        path='/v1/{namestar}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datamigration_projects_locations_migration_jobs_stop(client):
    """Test case for datamigration_projects_locations_migration_jobs_stop

    
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
        path='/v1/{namesto}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datamigration_projects_locations_migration_jobs_verify(client):
    """Test case for datamigration_projects_locations_migration_jobs_verify

    
    """
    body = {"migrationJob":{"phase":"PHASE_UNSPECIFIED","dumpFlags":{"dumpFlags":[{"name":"name","value":"value"},{"name":"name","value":"value"}]},"displayName":"displayName","dumpPath":"dumpPath","destination":"destination","destinationDatabase":{"engine":"DATABASE_ENGINE_UNSPECIFIED","provider":"DATABASE_PROVIDER_UNSPECIFIED"},"reverseSshConnectivity":{"vm":"vm","vpc":"vpc","vmIp":"vmIp","vmPort":0},"updateTime":"updateTime","source":"source","error":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"},"type":"TYPE_UNSPECIFIED","labels":{"key":"labels"},"duration":"duration","filter":"filter","conversionWorkspace":{"name":"name","commitId":"commitId"},"vpcPeeringConnectivity":{"vpc":"vpc"},"cmekKeyName":"cmekKeyName","performanceConfig":{"dumpParallelLevel":"DUMP_PARALLEL_LEVEL_UNSPECIFIED"},"createTime":"createTime","sourceDatabase":{"engine":"DATABASE_ENGINE_UNSPECIFIED","provider":"DATABASE_PROVIDER_UNSPECIFIED"},"name":"name","staticIpConnectivity":"{}","endTime":"endTime","state":"STATE_UNSPECIFIED"},"updateMask":"updateMask"}
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
        path='/v1/{nameverif}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datamigration_projects_locations_operations_cancel(client):
    """Test case for datamigration_projects_locations_operations_cancel

    
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

async def test_datamigration_projects_locations_operations_list(client):
    """Test case for datamigration_projects_locations_operations_list

    
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

async def test_datamigration_projects_locations_private_connections_create(client):
    """Test case for datamigration_projects_locations_private_connections_create

    
    """
    body = {"createTime":"createTime","displayName":"displayName","vpcPeeringConfig":{"subnet":"subnet","vpcName":"vpcName"},"name":"name","updateTime":"updateTime","state":"STATE_UNSPECIFIED","error":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"},"labels":{"key":"labels"}}
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
                    ('privateConnectionId', 'private_connection_id_example'),
                    ('requestId', 'request_id_example'),
                    ('skipValidation', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/privateConnections'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datamigration_projects_locations_private_connections_delete(client):
    """Test case for datamigration_projects_locations_private_connections_delete

    
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
                    ('requestId', 'request_id_example')]
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

async def test_datamigration_projects_locations_private_connections_get(client):
    """Test case for datamigration_projects_locations_private_connections_get

    
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

async def test_datamigration_projects_locations_private_connections_get_iam_policy(client):
    """Test case for datamigration_projects_locations_private_connections_get_iam_policy

    
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

async def test_datamigration_projects_locations_private_connections_list(client):
    """Test case for datamigration_projects_locations_private_connections_list

    
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
        path='/v1/{parent}/privateConnections'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datamigration_projects_locations_private_connections_set_iam_policy(client):
    """Test case for datamigration_projects_locations_private_connections_set_iam_policy

    
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

async def test_datamigration_projects_locations_private_connections_test_iam_permissions(client):
    """Test case for datamigration_projects_locations_private_connections_test_iam_permissions

    
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

