# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.check_upgrade_request import CheckUpgradeRequest
from openapi_server.models.environment import Environment
from openapi_server.models.execute_airflow_command_request import ExecuteAirflowCommandRequest
from openapi_server.models.execute_airflow_command_response import ExecuteAirflowCommandResponse
from openapi_server.models.fetch_database_properties_response import FetchDatabasePropertiesResponse
from openapi_server.models.list_environments_response import ListEnvironmentsResponse
from openapi_server.models.list_image_versions_response import ListImageVersionsResponse
from openapi_server.models.list_operations_response import ListOperationsResponse
from openapi_server.models.list_user_workloads_config_maps_response import ListUserWorkloadsConfigMapsResponse
from openapi_server.models.list_user_workloads_secrets_response import ListUserWorkloadsSecretsResponse
from openapi_server.models.list_workloads_response import ListWorkloadsResponse
from openapi_server.models.load_snapshot_request import LoadSnapshotRequest
from openapi_server.models.operation import Operation
from openapi_server.models.poll_airflow_command_request import PollAirflowCommandRequest
from openapi_server.models.poll_airflow_command_response import PollAirflowCommandResponse
from openapi_server.models.save_snapshot_request import SaveSnapshotRequest
from openapi_server.models.stop_airflow_command_request import StopAirflowCommandRequest
from openapi_server.models.stop_airflow_command_response import StopAirflowCommandResponse
from openapi_server.models.user_workloads_config_map import UserWorkloadsConfigMap
from openapi_server.models.user_workloads_secret import UserWorkloadsSecret


pytestmark = pytest.mark.asyncio

async def test_composer_projects_locations_environments_check_upgrade(client):
    """Test case for composer_projects_locations_environments_check_upgrade

    
    """
    body = {"imageVersion":"imageVersion"}
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
        path='/v1beta1/{environmentcheck_upgrad}'.format(environment='environment_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_composer_projects_locations_environments_create(client):
    """Test case for composer_projects_locations_environments_create

    
    """
    body = {"storageConfig":{"bucket":"bucket"},"createTime":"createTime","name":"name","satisfiesPzs":True,"updateTime":"updateTime","state":"STATE_UNSPECIFIED","config":{"encryptionConfig":{"kmsKeyName":"kmsKeyName"},"softwareConfig":{"imageVersion":"imageVersion","pypiPackages":{"key":"pypiPackages"},"pythonVersion":"pythonVersion","webServerPluginsMode":"WEB_SERVER_PLUGINS_MODE_UNSPECIFIED","envVariables":{"key":"envVariables"},"airflowConfigOverrides":{"key":"airflowConfigOverrides"},"cloudDataLineageIntegration":{"enabled":True},"schedulerCount":5},"webServerConfig":{"machineType":"machineType"},"databaseConfig":{"zone":"zone","machineType":"machineType"},"masterAuthorizedNetworksConfig":{"cidrBlocks":[{"displayName":"displayName","cidrBlock":"cidrBlock"},{"displayName":"displayName","cidrBlock":"cidrBlock"}],"enabled":True},"gkeCluster":"gkeCluster","nodeConfig":{"serviceAccount":"serviceAccount","oauthScopes":["oauthScopes","oauthScopes"],"ipAllocationPolicy":{"clusterIpv4CidrBlock":"clusterIpv4CidrBlock","useIpAliases":True,"servicesIpv4CidrBlock":"servicesIpv4CidrBlock","clusterSecondaryRangeName":"clusterSecondaryRangeName","servicesSecondaryRangeName":"servicesSecondaryRangeName"},"maxPodsPerNode":6,"network":"network","tags":["tags","tags"],"enableIpMasqAgent":True,"subnetwork":"subnetwork","composerInternalIpv4CidrBlock":"composerInternalIpv4CidrBlock","location":"location","machineType":"machineType","composerNetworkAttachment":"composerNetworkAttachment","diskSizeGb":0},"airflowByoidUri":"airflowByoidUri","webServerNetworkAccessControl":{"allowedIpRanges":[{"description":"description","value":"value"},{"description":"description","value":"value"}]},"maintenanceWindow":{"recurrence":"recurrence","startTime":"startTime","endTime":"endTime"},"airflowUri":"airflowUri","dagGcsPrefix":"dagGcsPrefix","resilienceMode":"RESILIENCE_MODE_UNSPECIFIED","dataRetentionConfig":{"taskLogsRetentionConfig":{"storageMode":"TASK_LOGS_STORAGE_MODE_UNSPECIFIED"}},"privateEnvironmentConfig":{"enablePrivatelyUsedPublicIps":True,"cloudComposerConnectionSubnetwork":"cloudComposerConnectionSubnetwork","enablePrivateBuildsOnly":True,"enablePrivateEnvironment":True,"cloudComposerNetworkIpv4ReservedRange":"cloudComposerNetworkIpv4ReservedRange","cloudComposerNetworkIpv4CidrBlock":"cloudComposerNetworkIpv4CidrBlock","webServerIpv4ReservedRange":"webServerIpv4ReservedRange","networkingConfig":{"connectionType":"CONNECTION_TYPE_UNSPECIFIED"},"cloudSqlIpv4CidrBlock":"cloudSqlIpv4CidrBlock","privateClusterConfig":{"enablePrivateEndpoint":True,"masterIpv4ReservedRange":"masterIpv4ReservedRange","masterIpv4CidrBlock":"masterIpv4CidrBlock"},"webServerIpv4CidrBlock":"webServerIpv4CidrBlock"},"workloadsConfig":{"scheduler":{"count":3,"cpu":2.027123,"memoryGb":4.145608,"storageGb":7.386282},"triggerer":{"count":1,"cpu":1.0246457,"memoryGb":1.4894159},"dagProcessor":{"count":5,"cpu":2.302136,"memoryGb":7.0614014,"storageGb":9.301444},"webServer":{"cpu":6.846853,"memoryGb":7.4577446,"storageGb":1.1730742},"worker":{"cpu":4.9652185,"minCount":9,"memoryGb":9.965781,"maxCount":5,"storageGb":6.6835623}},"nodeCount":1,"environmentSize":"ENVIRONMENT_SIZE_UNSPECIFIED","recoveryConfig":{"scheduledSnapshotsConfig":{"timeZone":"timeZone","snapshotLocation":"snapshotLocation","enabled":True,"snapshotCreationSchedule":"snapshotCreationSchedule"}}},"uuid":"uuid","labels":{"key":"labels"}}
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
        path='/v1beta1/{parent}/environments'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_composer_projects_locations_environments_database_failover(client):
    """Test case for composer_projects_locations_environments_database_failover

    
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
        path='/v1beta1/{environmentdatabase_failove}'.format(environment='environment_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_composer_projects_locations_environments_execute_airflow_command(client):
    """Test case for composer_projects_locations_environments_execute_airflow_command

    
    """
    body = {"subcommand":"subcommand","parameters":["parameters","parameters"],"command":"command"}
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
        path='/v1beta1/{environmentexecute_airflow_comman}'.format(environment='environment_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_composer_projects_locations_environments_fetch_database_properties(client):
    """Test case for composer_projects_locations_environments_fetch_database_properties

    
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
        path='/v1beta1/{environmentfetch_database_propertie}'.format(environment='environment_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_composer_projects_locations_environments_list(client):
    """Test case for composer_projects_locations_environments_list

    
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
        path='/v1beta1/{parent}/environments'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_composer_projects_locations_environments_load_snapshot(client):
    """Test case for composer_projects_locations_environments_load_snapshot

    
    """
    body = {"snapshotPath":"snapshotPath","skipGcsDataCopying":True,"skipAirflowOverridesSetting":True,"skipEnvironmentVariablesSetting":True,"skipPypiPackagesInstallation":True}
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
        path='/v1beta1/{environmentload_snapsho}'.format(environment='environment_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_composer_projects_locations_environments_patch(client):
    """Test case for composer_projects_locations_environments_patch

    
    """
    body = {"storageConfig":{"bucket":"bucket"},"createTime":"createTime","name":"name","satisfiesPzs":True,"updateTime":"updateTime","state":"STATE_UNSPECIFIED","config":{"encryptionConfig":{"kmsKeyName":"kmsKeyName"},"softwareConfig":{"imageVersion":"imageVersion","pypiPackages":{"key":"pypiPackages"},"pythonVersion":"pythonVersion","webServerPluginsMode":"WEB_SERVER_PLUGINS_MODE_UNSPECIFIED","envVariables":{"key":"envVariables"},"airflowConfigOverrides":{"key":"airflowConfigOverrides"},"cloudDataLineageIntegration":{"enabled":True},"schedulerCount":5},"webServerConfig":{"machineType":"machineType"},"databaseConfig":{"zone":"zone","machineType":"machineType"},"masterAuthorizedNetworksConfig":{"cidrBlocks":[{"displayName":"displayName","cidrBlock":"cidrBlock"},{"displayName":"displayName","cidrBlock":"cidrBlock"}],"enabled":True},"gkeCluster":"gkeCluster","nodeConfig":{"serviceAccount":"serviceAccount","oauthScopes":["oauthScopes","oauthScopes"],"ipAllocationPolicy":{"clusterIpv4CidrBlock":"clusterIpv4CidrBlock","useIpAliases":True,"servicesIpv4CidrBlock":"servicesIpv4CidrBlock","clusterSecondaryRangeName":"clusterSecondaryRangeName","servicesSecondaryRangeName":"servicesSecondaryRangeName"},"maxPodsPerNode":6,"network":"network","tags":["tags","tags"],"enableIpMasqAgent":True,"subnetwork":"subnetwork","composerInternalIpv4CidrBlock":"composerInternalIpv4CidrBlock","location":"location","machineType":"machineType","composerNetworkAttachment":"composerNetworkAttachment","diskSizeGb":0},"airflowByoidUri":"airflowByoidUri","webServerNetworkAccessControl":{"allowedIpRanges":[{"description":"description","value":"value"},{"description":"description","value":"value"}]},"maintenanceWindow":{"recurrence":"recurrence","startTime":"startTime","endTime":"endTime"},"airflowUri":"airflowUri","dagGcsPrefix":"dagGcsPrefix","resilienceMode":"RESILIENCE_MODE_UNSPECIFIED","dataRetentionConfig":{"taskLogsRetentionConfig":{"storageMode":"TASK_LOGS_STORAGE_MODE_UNSPECIFIED"}},"privateEnvironmentConfig":{"enablePrivatelyUsedPublicIps":True,"cloudComposerConnectionSubnetwork":"cloudComposerConnectionSubnetwork","enablePrivateBuildsOnly":True,"enablePrivateEnvironment":True,"cloudComposerNetworkIpv4ReservedRange":"cloudComposerNetworkIpv4ReservedRange","cloudComposerNetworkIpv4CidrBlock":"cloudComposerNetworkIpv4CidrBlock","webServerIpv4ReservedRange":"webServerIpv4ReservedRange","networkingConfig":{"connectionType":"CONNECTION_TYPE_UNSPECIFIED"},"cloudSqlIpv4CidrBlock":"cloudSqlIpv4CidrBlock","privateClusterConfig":{"enablePrivateEndpoint":True,"masterIpv4ReservedRange":"masterIpv4ReservedRange","masterIpv4CidrBlock":"masterIpv4CidrBlock"},"webServerIpv4CidrBlock":"webServerIpv4CidrBlock"},"workloadsConfig":{"scheduler":{"count":3,"cpu":2.027123,"memoryGb":4.145608,"storageGb":7.386282},"triggerer":{"count":1,"cpu":1.0246457,"memoryGb":1.4894159},"dagProcessor":{"count":5,"cpu":2.302136,"memoryGb":7.0614014,"storageGb":9.301444},"webServer":{"cpu":6.846853,"memoryGb":7.4577446,"storageGb":1.1730742},"worker":{"cpu":4.9652185,"minCount":9,"memoryGb":9.965781,"maxCount":5,"storageGb":6.6835623}},"nodeCount":1,"environmentSize":"ENVIRONMENT_SIZE_UNSPECIFIED","recoveryConfig":{"scheduledSnapshotsConfig":{"timeZone":"timeZone","snapshotLocation":"snapshotLocation","enabled":True,"snapshotCreationSchedule":"snapshotCreationSchedule"}}},"uuid":"uuid","labels":{"key":"labels"}}
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
        path='/v1beta1/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_composer_projects_locations_environments_poll_airflow_command(client):
    """Test case for composer_projects_locations_environments_poll_airflow_command

    
    """
    body = {"executionId":"executionId","podNamespace":"podNamespace","pod":"pod","nextLineNumber":0}
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
        path='/v1beta1/{environmentpoll_airflow_comman}'.format(environment='environment_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_composer_projects_locations_environments_restart_web_server(client):
    """Test case for composer_projects_locations_environments_restart_web_server

    
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
        path='/v1beta1/{namerestart_web_serve}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_composer_projects_locations_environments_save_snapshot(client):
    """Test case for composer_projects_locations_environments_save_snapshot

    
    """
    body = {"snapshotLocation":"snapshotLocation"}
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
        path='/v1beta1/{environmentsave_snapsho}'.format(environment='environment_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_composer_projects_locations_environments_stop_airflow_command(client):
    """Test case for composer_projects_locations_environments_stop_airflow_command

    
    """
    body = {"executionId":"executionId","podNamespace":"podNamespace","pod":"pod","force":True}
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
        path='/v1beta1/{environmentstop_airflow_comman}'.format(environment='environment_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_composer_projects_locations_environments_user_workloads_config_maps_create(client):
    """Test case for composer_projects_locations_environments_user_workloads_config_maps_create

    
    """
    body = {"data":{"key":"data"},"name":"name"}
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
        path='/v1beta1/{parent}/userWorkloadsConfigMaps'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_composer_projects_locations_environments_user_workloads_config_maps_list(client):
    """Test case for composer_projects_locations_environments_user_workloads_config_maps_list

    
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
        path='/v1beta1/{parent}/userWorkloadsConfigMaps'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_composer_projects_locations_environments_user_workloads_secrets_create(client):
    """Test case for composer_projects_locations_environments_user_workloads_secrets_create

    
    """
    body = {"data":{"key":"data"},"name":"name"}
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
        path='/v1beta1/{parent}/userWorkloadsSecrets'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_composer_projects_locations_environments_user_workloads_secrets_list(client):
    """Test case for composer_projects_locations_environments_user_workloads_secrets_list

    
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
        path='/v1beta1/{parent}/userWorkloadsSecrets'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_composer_projects_locations_environments_user_workloads_secrets_update(client):
    """Test case for composer_projects_locations_environments_user_workloads_secrets_update

    
    """
    body = {"data":{"key":"data"},"name":"name"}
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
        method='PUT',
        path='/v1beta1/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_composer_projects_locations_environments_workloads_list(client):
    """Test case for composer_projects_locations_environments_workloads_list

    
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
        path='/v1beta1/{parent}/workloads'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_composer_projects_locations_image_versions_list(client):
    """Test case for composer_projects_locations_image_versions_list

    
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
                    ('includePastReleases', True),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/imageVersions'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_composer_projects_locations_operations_delete(client):
    """Test case for composer_projects_locations_operations_delete

    
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
        path='/v1beta1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_composer_projects_locations_operations_get(client):
    """Test case for composer_projects_locations_operations_get

    
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
        path='/v1beta1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_composer_projects_locations_operations_list(client):
    """Test case for composer_projects_locations_operations_list

    
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
        path='/v1beta1/{name}/operations'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

