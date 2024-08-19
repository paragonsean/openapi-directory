# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.backup import Backup
from openapi_server.models.cluster import Cluster
from openapi_server.models.connection_info import ConnectionInfo
from openapi_server.models.failover_instance_request import FailoverInstanceRequest
from openapi_server.models.generate_client_certificate_request import GenerateClientCertificateRequest
from openapi_server.models.generate_client_certificate_response import GenerateClientCertificateResponse
from openapi_server.models.google_cloud_location_list_locations_response import GoogleCloudLocationListLocationsResponse
from openapi_server.models.inject_fault_request import InjectFaultRequest
from openapi_server.models.instance import Instance
from openapi_server.models.list_backups_response import ListBackupsResponse
from openapi_server.models.list_clusters_response import ListClustersResponse
from openapi_server.models.list_instances_response import ListInstancesResponse
from openapi_server.models.list_operations_response import ListOperationsResponse
from openapi_server.models.list_supported_database_flags_response import ListSupportedDatabaseFlagsResponse
from openapi_server.models.list_users_response import ListUsersResponse
from openapi_server.models.operation import Operation
from openapi_server.models.promote_cluster_request import PromoteClusterRequest
from openapi_server.models.restart_instance_request import RestartInstanceRequest
from openapi_server.models.restore_cluster_request import RestoreClusterRequest
from openapi_server.models.user import User


pytestmark = pytest.mark.asyncio

async def test_alloydb_projects_locations_backups_create(client):
    """Test case for alloydb_projects_locations_backups_create

    
    """
    body = {"encryptionConfig":{"kmsKeyName":"kmsKeyName"},"encryptionInfo":{"encryptionType":"TYPE_UNSPECIFIED","kmsKeyVersions":["kmsKeyVersions","kmsKeyVersions"]},"clusterUid":"clusterUid","displayName":"displayName","annotations":{"key":"annotations"},"description":"description","reconciling":True,"satisfiesPzs":True,"updateTime":"updateTime","type":"TYPE_UNSPECIFIED","databaseVersion":"DATABASE_VERSION_UNSPECIFIED","labels":{"key":"labels"},"sizeBytes":"sizeBytes","uid":"uid","createTime":"createTime","deleteTime":"deleteTime","clusterName":"clusterName","expiryTime":"expiryTime","name":"name","etag":"etag","state":"STATE_UNSPECIFIED","satisfiesPzi":True,"expiryQuantity":{"totalRetentionCount":6,"retentionCount":0}}
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
                    ('backupId', 'backup_id_example'),
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
        path='/v1alpha/{parent}/backups'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alloydb_projects_locations_backups_list(client):
    """Test case for alloydb_projects_locations_backups_list

    
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
        path='/v1alpha/{parent}/backups'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alloydb_projects_locations_clusters_create(client):
    """Test case for alloydb_projects_locations_clusters_create

    
    """
    body = {"encryptionInfo":{"encryptionType":"TYPE_UNSPECIFIED","kmsKeyVersions":["kmsKeyVersions","kmsKeyVersions"]},"sslConfig":{"caSource":"CA_SOURCE_UNSPECIFIED","sslMode":"SSL_MODE_UNSPECIFIED"},"displayName":"displayName","annotations":{"key":"annotations"},"reconciling":True,"satisfiesPzs":True,"continuousBackupInfo":{"encryptionInfo":{"encryptionType":"TYPE_UNSPECIFIED","kmsKeyVersions":["kmsKeyVersions","kmsKeyVersions"]},"schedule":["DAY_OF_WEEK_UNSPECIFIED","DAY_OF_WEEK_UNSPECIFIED"],"enabledTime":"enabledTime","earliestRestorableTime":"earliestRestorableTime"},"continuousBackupConfig":{"encryptionConfig":{"kmsKeyName":"kmsKeyName"},"recoveryWindowDays":2,"enabled":True},"databaseVersion":"DATABASE_VERSION_UNSPECIFIED","network":"network","primaryConfig":{"secondaryClusterNames":["secondaryClusterNames","secondaryClusterNames"]},"uid":"uid","state":"STATE_UNSPECIFIED","clusterType":"CLUSTER_TYPE_UNSPECIFIED","encryptionConfig":{"kmsKeyName":"kmsKeyName"},"automatedBackupPolicy":{"encryptionConfig":{"kmsKeyName":"kmsKeyName"},"weeklySchedule":{"daysOfWeek":["DAY_OF_WEEK_UNSPECIFIED","DAY_OF_WEEK_UNSPECIFIED"],"startTimes":[{"hours":6,"seconds":5,"nanos":5,"minutes":1},{"hours":6,"seconds":5,"nanos":5,"minutes":1}]},"timeBasedRetention":{"retentionPeriod":"retentionPeriod"},"location":"location","backupWindow":"backupWindow","quantityBasedRetention":{"count":0},"enabled":True,"labels":{"key":"labels"}},"pscConfig":{"pscEnabled":True},"networkConfig":{"allocatedIpRange":"allocatedIpRange","network":"network"},"updateTime":"updateTime","initialUser":{"password":"password","user":"user"},"labels":{"key":"labels"},"secondaryConfig":{"primaryClusterName":"primaryClusterName"},"createTime":"createTime","deleteTime":"deleteTime","migrationSource":{"sourceType":"MIGRATION_SOURCE_TYPE_UNSPECIFIED","hostPort":"hostPort","referenceId":"referenceId"},"name":"name","etag":"etag","satisfiesPzi":True,"backupSource":{"backupUid":"backupUid","backupName":"backupName"}}
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
                    ('clusterId', 'cluster_id_example'),
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
        path='/v1alpha/{parent}/clusters'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alloydb_projects_locations_clusters_createsecondary(client):
    """Test case for alloydb_projects_locations_clusters_createsecondary

    
    """
    body = {"encryptionInfo":{"encryptionType":"TYPE_UNSPECIFIED","kmsKeyVersions":["kmsKeyVersions","kmsKeyVersions"]},"sslConfig":{"caSource":"CA_SOURCE_UNSPECIFIED","sslMode":"SSL_MODE_UNSPECIFIED"},"displayName":"displayName","annotations":{"key":"annotations"},"reconciling":True,"satisfiesPzs":True,"continuousBackupInfo":{"encryptionInfo":{"encryptionType":"TYPE_UNSPECIFIED","kmsKeyVersions":["kmsKeyVersions","kmsKeyVersions"]},"schedule":["DAY_OF_WEEK_UNSPECIFIED","DAY_OF_WEEK_UNSPECIFIED"],"enabledTime":"enabledTime","earliestRestorableTime":"earliestRestorableTime"},"continuousBackupConfig":{"encryptionConfig":{"kmsKeyName":"kmsKeyName"},"recoveryWindowDays":2,"enabled":True},"databaseVersion":"DATABASE_VERSION_UNSPECIFIED","network":"network","primaryConfig":{"secondaryClusterNames":["secondaryClusterNames","secondaryClusterNames"]},"uid":"uid","state":"STATE_UNSPECIFIED","clusterType":"CLUSTER_TYPE_UNSPECIFIED","encryptionConfig":{"kmsKeyName":"kmsKeyName"},"automatedBackupPolicy":{"encryptionConfig":{"kmsKeyName":"kmsKeyName"},"weeklySchedule":{"daysOfWeek":["DAY_OF_WEEK_UNSPECIFIED","DAY_OF_WEEK_UNSPECIFIED"],"startTimes":[{"hours":6,"seconds":5,"nanos":5,"minutes":1},{"hours":6,"seconds":5,"nanos":5,"minutes":1}]},"timeBasedRetention":{"retentionPeriod":"retentionPeriod"},"location":"location","backupWindow":"backupWindow","quantityBasedRetention":{"count":0},"enabled":True,"labels":{"key":"labels"}},"pscConfig":{"pscEnabled":True},"networkConfig":{"allocatedIpRange":"allocatedIpRange","network":"network"},"updateTime":"updateTime","initialUser":{"password":"password","user":"user"},"labels":{"key":"labels"},"secondaryConfig":{"primaryClusterName":"primaryClusterName"},"createTime":"createTime","deleteTime":"deleteTime","migrationSource":{"sourceType":"MIGRATION_SOURCE_TYPE_UNSPECIFIED","hostPort":"hostPort","referenceId":"referenceId"},"name":"name","etag":"etag","satisfiesPzi":True,"backupSource":{"backupUid":"backupUid","backupName":"backupName"}}
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
                    ('clusterId', 'cluster_id_example'),
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
        path='/v1alpha/{parent}/clusters:createsecondary'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alloydb_projects_locations_clusters_generate_client_certificate(client):
    """Test case for alloydb_projects_locations_clusters_generate_client_certificate

    
    """
    body = {"requestId":"requestId","certDuration":"certDuration","pemCsr":"pemCsr","publicKey":"publicKey","useMetadataExchange":True}
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
        path='/v1alpha/{parentgenerate_client_certificat}'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alloydb_projects_locations_clusters_instances_create(client):
    """Test case for alloydb_projects_locations_clusters_instances_create

    
    """
    body = {"writableNode":{"ip":"ip","zoneId":"zoneId","id":"id","state":"state"},"machineConfig":{"cpuCount":0},"databaseFlags":{"key":"databaseFlags"},"displayName":"displayName","annotations":{"key":"annotations"},"reconciling":True,"satisfiesPzs":True,"queryInsightsConfig":{"recordClientAddress":True,"queryStringLength":1,"queryPlansPerMinute":6,"recordApplicationTags":True},"uid":"uid","availabilityType":"AVAILABILITY_TYPE_UNSPECIFIED","clientConnectionConfig":{"sslConfig":{"caSource":"CA_SOURCE_UNSPECIFIED","sslMode":"SSL_MODE_UNSPECIFIED"},"requireConnectors":True},"readPoolConfig":{"nodeCount":5},"updatePolicy":{"mode":"MODE_UNSPECIFIED"},"state":"STATE_UNSPECIFIED","gceZone":"gceZone","pscInstanceConfig":{"pscInterfaceConfigs":[{"consumerEndpointIps":["consumerEndpointIps","consumerEndpointIps"],"networkAttachment":"networkAttachment"},{"consumerEndpointIps":["consumerEndpointIps","consumerEndpointIps"],"networkAttachment":"networkAttachment"}],"allowedConsumerNetworks":["allowedConsumerNetworks","allowedConsumerNetworks"],"outgoingServiceAttachmentLinks":["outgoingServiceAttachmentLinks","outgoingServiceAttachmentLinks"],"pscEnabled":True,"serviceAttachmentLink":"serviceAttachmentLink","allowedConsumerProjects":["allowedConsumerProjects","allowedConsumerProjects"]},"publicIpAddress":"publicIpAddress","instanceType":"INSTANCE_TYPE_UNSPECIFIED","ipAddress":"ipAddress","networkConfig":{"authorizedExternalNetworks":[{"cidrRange":"cidrRange"},{"cidrRange":"cidrRange"}],"enablePublicIp":True},"updateTime":"updateTime","labels":{"key":"labels"},"nodes":[{"ip":"ip","zoneId":"zoneId","id":"id","state":"state"},{"ip":"ip","zoneId":"zoneId","id":"id","state":"state"}],"createTime":"createTime","deleteTime":"deleteTime","name":"name","etag":"etag","satisfiesPzi":True}
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
                    ('instanceId', 'instance_id_example'),
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
        path='/v1alpha/{parent}/instances'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alloydb_projects_locations_clusters_instances_createsecondary(client):
    """Test case for alloydb_projects_locations_clusters_instances_createsecondary

    
    """
    body = {"writableNode":{"ip":"ip","zoneId":"zoneId","id":"id","state":"state"},"machineConfig":{"cpuCount":0},"databaseFlags":{"key":"databaseFlags"},"displayName":"displayName","annotations":{"key":"annotations"},"reconciling":True,"satisfiesPzs":True,"queryInsightsConfig":{"recordClientAddress":True,"queryStringLength":1,"queryPlansPerMinute":6,"recordApplicationTags":True},"uid":"uid","availabilityType":"AVAILABILITY_TYPE_UNSPECIFIED","clientConnectionConfig":{"sslConfig":{"caSource":"CA_SOURCE_UNSPECIFIED","sslMode":"SSL_MODE_UNSPECIFIED"},"requireConnectors":True},"readPoolConfig":{"nodeCount":5},"updatePolicy":{"mode":"MODE_UNSPECIFIED"},"state":"STATE_UNSPECIFIED","gceZone":"gceZone","pscInstanceConfig":{"pscInterfaceConfigs":[{"consumerEndpointIps":["consumerEndpointIps","consumerEndpointIps"],"networkAttachment":"networkAttachment"},{"consumerEndpointIps":["consumerEndpointIps","consumerEndpointIps"],"networkAttachment":"networkAttachment"}],"allowedConsumerNetworks":["allowedConsumerNetworks","allowedConsumerNetworks"],"outgoingServiceAttachmentLinks":["outgoingServiceAttachmentLinks","outgoingServiceAttachmentLinks"],"pscEnabled":True,"serviceAttachmentLink":"serviceAttachmentLink","allowedConsumerProjects":["allowedConsumerProjects","allowedConsumerProjects"]},"publicIpAddress":"publicIpAddress","instanceType":"INSTANCE_TYPE_UNSPECIFIED","ipAddress":"ipAddress","networkConfig":{"authorizedExternalNetworks":[{"cidrRange":"cidrRange"},{"cidrRange":"cidrRange"}],"enablePublicIp":True},"updateTime":"updateTime","labels":{"key":"labels"},"nodes":[{"ip":"ip","zoneId":"zoneId","id":"id","state":"state"},{"ip":"ip","zoneId":"zoneId","id":"id","state":"state"}],"createTime":"createTime","deleteTime":"deleteTime","name":"name","etag":"etag","satisfiesPzi":True}
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
                    ('instanceId', 'instance_id_example'),
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
        path='/v1alpha/{parent}/instances:createsecondary'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alloydb_projects_locations_clusters_instances_failover(client):
    """Test case for alloydb_projects_locations_clusters_instances_failover

    
    """
    body = {"validateOnly":True,"requestId":"requestId"}
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
        path='/v1alpha/{namefailove}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alloydb_projects_locations_clusters_instances_get_connection_info(client):
    """Test case for alloydb_projects_locations_clusters_instances_get_connection_info

    
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
        method='GET',
        path='/v1alpha/{parent}/connectionInfo'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alloydb_projects_locations_clusters_instances_inject_fault(client):
    """Test case for alloydb_projects_locations_clusters_instances_inject_fault

    
    """
    body = {"validateOnly":True,"requestId":"requestId","faultType":"FAULT_TYPE_UNSPECIFIED"}
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
        path='/v1alpha/{nameinject_faul}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alloydb_projects_locations_clusters_instances_list(client):
    """Test case for alloydb_projects_locations_clusters_instances_list

    
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
        path='/v1alpha/{parent}/instances'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alloydb_projects_locations_clusters_instances_restart(client):
    """Test case for alloydb_projects_locations_clusters_instances_restart

    
    """
    body = {"validateOnly":True,"requestId":"requestId"}
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
        path='/v1alpha/{namerestar}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alloydb_projects_locations_clusters_list(client):
    """Test case for alloydb_projects_locations_clusters_list

    
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
        path='/v1alpha/{parent}/clusters'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alloydb_projects_locations_clusters_promote(client):
    """Test case for alloydb_projects_locations_clusters_promote

    
    """
    body = {"validateOnly":True,"requestId":"requestId","etag":"etag"}
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
        path='/v1alpha/{namepromot}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alloydb_projects_locations_clusters_restore(client):
    """Test case for alloydb_projects_locations_clusters_restore

    
    """
    body = {"cluster":{"encryptionInfo":{"encryptionType":"TYPE_UNSPECIFIED","kmsKeyVersions":["kmsKeyVersions","kmsKeyVersions"]},"sslConfig":{"caSource":"CA_SOURCE_UNSPECIFIED","sslMode":"SSL_MODE_UNSPECIFIED"},"displayName":"displayName","annotations":{"key":"annotations"},"reconciling":True,"satisfiesPzs":True,"continuousBackupInfo":{"encryptionInfo":{"encryptionType":"TYPE_UNSPECIFIED","kmsKeyVersions":["kmsKeyVersions","kmsKeyVersions"]},"schedule":["DAY_OF_WEEK_UNSPECIFIED","DAY_OF_WEEK_UNSPECIFIED"],"enabledTime":"enabledTime","earliestRestorableTime":"earliestRestorableTime"},"continuousBackupConfig":{"encryptionConfig":{"kmsKeyName":"kmsKeyName"},"recoveryWindowDays":2,"enabled":True},"databaseVersion":"DATABASE_VERSION_UNSPECIFIED","network":"network","primaryConfig":{"secondaryClusterNames":["secondaryClusterNames","secondaryClusterNames"]},"uid":"uid","state":"STATE_UNSPECIFIED","clusterType":"CLUSTER_TYPE_UNSPECIFIED","encryptionConfig":{"kmsKeyName":"kmsKeyName"},"automatedBackupPolicy":{"encryptionConfig":{"kmsKeyName":"kmsKeyName"},"weeklySchedule":{"daysOfWeek":["DAY_OF_WEEK_UNSPECIFIED","DAY_OF_WEEK_UNSPECIFIED"],"startTimes":[{"hours":6,"seconds":5,"nanos":5,"minutes":1},{"hours":6,"seconds":5,"nanos":5,"minutes":1}]},"timeBasedRetention":{"retentionPeriod":"retentionPeriod"},"location":"location","backupWindow":"backupWindow","quantityBasedRetention":{"count":0},"enabled":True,"labels":{"key":"labels"}},"pscConfig":{"pscEnabled":True},"networkConfig":{"allocatedIpRange":"allocatedIpRange","network":"network"},"updateTime":"updateTime","initialUser":{"password":"password","user":"user"},"labels":{"key":"labels"},"secondaryConfig":{"primaryClusterName":"primaryClusterName"},"createTime":"createTime","deleteTime":"deleteTime","migrationSource":{"sourceType":"MIGRATION_SOURCE_TYPE_UNSPECIFIED","hostPort":"hostPort","referenceId":"referenceId"},"name":"name","etag":"etag","satisfiesPzi":True,"backupSource":{"backupUid":"backupUid","backupName":"backupName"}},"validateOnly":True,"continuousBackupSource":{"cluster":"cluster","pointInTime":"pointInTime"},"requestId":"requestId","clusterId":"clusterId","backupSource":{"backupUid":"backupUid","backupName":"backupName"}}
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
        path='/v1alpha/{parent}/clusters:restore'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alloydb_projects_locations_clusters_users_create(client):
    """Test case for alloydb_projects_locations_clusters_users_create

    
    """
    body = {"password":"password","databaseRoles":["databaseRoles","databaseRoles"],"name":"name","userType":"USER_TYPE_UNSPECIFIED"}
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
                    ('userId', 'user_id_example'),
                    ('validateOnly', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1alpha/{parent}/users'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alloydb_projects_locations_clusters_users_list(client):
    """Test case for alloydb_projects_locations_clusters_users_list

    
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
        path='/v1alpha/{parent}/users'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alloydb_projects_locations_clusters_users_patch(client):
    """Test case for alloydb_projects_locations_clusters_users_patch

    
    """
    body = {"password":"password","databaseRoles":["databaseRoles","databaseRoles"],"name":"name","userType":"USER_TYPE_UNSPECIFIED"}
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
        path='/v1alpha/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alloydb_projects_locations_list(client):
    """Test case for alloydb_projects_locations_list

    
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
        path='/v1alpha/{name}/locations'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alloydb_projects_locations_operations_cancel(client):
    """Test case for alloydb_projects_locations_operations_cancel

    
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

async def test_alloydb_projects_locations_operations_delete(client):
    """Test case for alloydb_projects_locations_operations_delete

    
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
                    ('requestId', 'request_id_example'),
                    ('validateOnly', True)]
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

async def test_alloydb_projects_locations_operations_get(client):
    """Test case for alloydb_projects_locations_operations_get

    
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

async def test_alloydb_projects_locations_operations_list(client):
    """Test case for alloydb_projects_locations_operations_list

    
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
        path='/v1alpha/{name}/operations'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alloydb_projects_locations_supported_database_flags_list(client):
    """Test case for alloydb_projects_locations_supported_database_flags_list

    
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
        path='/v1alpha/{parent}/supportedDatabaseFlags'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

