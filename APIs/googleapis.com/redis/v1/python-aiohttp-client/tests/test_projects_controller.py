# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cluster import Cluster
from openapi_server.models.export_instance_request import ExportInstanceRequest
from openapi_server.models.failover_instance_request import FailoverInstanceRequest
from openapi_server.models.import_instance_request import ImportInstanceRequest
from openapi_server.models.instance import Instance
from openapi_server.models.instance_auth_string import InstanceAuthString
from openapi_server.models.list_clusters_response import ListClustersResponse
from openapi_server.models.list_instances_response import ListInstancesResponse
from openapi_server.models.list_locations_response import ListLocationsResponse
from openapi_server.models.list_operations_response import ListOperationsResponse
from openapi_server.models.operation import Operation
from openapi_server.models.reschedule_maintenance_request import RescheduleMaintenanceRequest
from openapi_server.models.upgrade_instance_request import UpgradeInstanceRequest


pytestmark = pytest.mark.asyncio

async def test_redis_projects_locations_clusters_create(client):
    """Test case for redis_projects_locations_clusters_create

    
    """
    body = {"sizeGb":5,"discoveryEndpoints":[{"address":"address","port":0,"pscConfig":{"network":"network"}},{"address":"address","port":0,"pscConfig":{"network":"network"}}],"pscConfigs":[{"network":"network"},{"network":"network"}],"uid":"uid","replicaCount":6,"createTime":"createTime","name":"name","pscConnections":[{"address":"address","forwardingRule":"forwardingRule","projectId":"projectId","pscConnectionId":"pscConnectionId","network":"network"},{"address":"address","forwardingRule":"forwardingRule","projectId":"projectId","pscConnectionId":"pscConnectionId","network":"network"}],"stateInfo":{"updateInfo":{"targetReplicaCount":5,"targetShardCount":2}},"authorizationMode":"AUTH_MODE_UNSPECIFIED","state":"STATE_UNSPECIFIED","shardCount":1,"transitEncryptionMode":"TRANSIT_ENCRYPTION_MODE_UNSPECIFIED"}
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
                    ('requestId', 'request_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/clusters'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_redis_projects_locations_clusters_list(client):
    """Test case for redis_projects_locations_clusters_list

    
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
        path='/v1/{parent}/clusters'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_redis_projects_locations_instances_create(client):
    """Test case for redis_projects_locations_instances_create

    
    """
    body = {"authEnabled":True,"authorizedNetwork":"authorizedNetwork","displayName":"displayName","maintenanceVersion":"maintenanceVersion","reservedIpRange":"reservedIpRange","satisfiesPzs":True,"secondaryIpRange":"secondaryIpRange","readEndpoint":"readEndpoint","persistenceConfig":{"rdbNextSnapshotTime":"rdbNextSnapshotTime","persistenceMode":"PERSISTENCE_MODE_UNSPECIFIED","rdbSnapshotStartTime":"rdbSnapshotStartTime","rdbSnapshotPeriod":"SNAPSHOT_PERIOD_UNSPECIFIED"},"replicaCount":9,"connectMode":"CONNECT_MODE_UNSPECIFIED","tier":"TIER_UNSPECIFIED","suspensionReasons":["SUSPENSION_REASON_UNSPECIFIED","SUSPENSION_REASON_UNSPECIFIED"],"locationId":"locationId","memorySizeGb":5,"persistenceIamIdentity":"persistenceIamIdentity","host":"host","availableMaintenanceVersions":["availableMaintenanceVersions","availableMaintenanceVersions"],"customerManagedKey":"customerManagedKey","state":"STATE_UNSPECIFIED","redisConfigs":{"key":"redisConfigs"},"serverCaCerts":[{"expireTime":"expireTime","serialNumber":"serialNumber","createTime":"createTime","sha1Fingerprint":"sha1Fingerprint","cert":"cert"},{"expireTime":"expireTime","serialNumber":"serialNumber","createTime":"createTime","sha1Fingerprint":"sha1Fingerprint","cert":"cert"}],"maintenanceSchedule":{"canReschedule":True,"startTime":"startTime","endTime":"endTime","scheduleDeadlineTime":"scheduleDeadlineTime"},"statusMessage":"statusMessage","labels":{"key":"labels"},"maintenancePolicy":{"createTime":"createTime","description":"description","weeklyMaintenanceWindow":[{"duration":"duration","startTime":{"hours":0,"seconds":5,"nanos":1,"minutes":6},"day":"DAY_OF_WEEK_UNSPECIFIED"},{"duration":"duration","startTime":{"hours":0,"seconds":5,"nanos":1,"minutes":6},"day":"DAY_OF_WEEK_UNSPECIFIED"}],"updateTime":"updateTime"},"redisVersion":"redisVersion","nodes":[{"zone":"zone","id":"id"},{"zone":"zone","id":"id"}],"createTime":"createTime","port":2,"readReplicasMode":"READ_REPLICAS_MODE_UNSPECIFIED","alternativeLocationId":"alternativeLocationId","name":"name","satisfiesPzi":True,"currentLocationId":"currentLocationId","readEndpointPort":7,"transitEncryptionMode":"TRANSIT_ENCRYPTION_MODE_UNSPECIFIED"}
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
                    ('instanceId', 'instance_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/instances'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_redis_projects_locations_instances_export(client):
    """Test case for redis_projects_locations_instances_export

    
    """
    body = {"outputConfig":{"gcsDestination":{"uri":"uri"}}}
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
        path='/v1/{nameexpor}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_redis_projects_locations_instances_failover(client):
    """Test case for redis_projects_locations_instances_failover

    
    """
    body = {"dataProtectionMode":"DATA_PROTECTION_MODE_UNSPECIFIED"}
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
        path='/v1/{namefailove}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_redis_projects_locations_instances_get_auth_string(client):
    """Test case for redis_projects_locations_instances_get_auth_string

    
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
        path='/v1/{name}/authString'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_redis_projects_locations_instances_import(client):
    """Test case for redis_projects_locations_instances_import

    
    """
    body = {"inputConfig":{"gcsSource":{"uri":"uri"}}}
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
        path='/v1/{nameimpor}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_redis_projects_locations_instances_list(client):
    """Test case for redis_projects_locations_instances_list

    
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
        path='/v1/{parent}/instances'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_redis_projects_locations_instances_patch(client):
    """Test case for redis_projects_locations_instances_patch

    
    """
    body = {"authEnabled":True,"authorizedNetwork":"authorizedNetwork","displayName":"displayName","maintenanceVersion":"maintenanceVersion","reservedIpRange":"reservedIpRange","satisfiesPzs":True,"secondaryIpRange":"secondaryIpRange","readEndpoint":"readEndpoint","persistenceConfig":{"rdbNextSnapshotTime":"rdbNextSnapshotTime","persistenceMode":"PERSISTENCE_MODE_UNSPECIFIED","rdbSnapshotStartTime":"rdbSnapshotStartTime","rdbSnapshotPeriod":"SNAPSHOT_PERIOD_UNSPECIFIED"},"replicaCount":9,"connectMode":"CONNECT_MODE_UNSPECIFIED","tier":"TIER_UNSPECIFIED","suspensionReasons":["SUSPENSION_REASON_UNSPECIFIED","SUSPENSION_REASON_UNSPECIFIED"],"locationId":"locationId","memorySizeGb":5,"persistenceIamIdentity":"persistenceIamIdentity","host":"host","availableMaintenanceVersions":["availableMaintenanceVersions","availableMaintenanceVersions"],"customerManagedKey":"customerManagedKey","state":"STATE_UNSPECIFIED","redisConfigs":{"key":"redisConfigs"},"serverCaCerts":[{"expireTime":"expireTime","serialNumber":"serialNumber","createTime":"createTime","sha1Fingerprint":"sha1Fingerprint","cert":"cert"},{"expireTime":"expireTime","serialNumber":"serialNumber","createTime":"createTime","sha1Fingerprint":"sha1Fingerprint","cert":"cert"}],"maintenanceSchedule":{"canReschedule":True,"startTime":"startTime","endTime":"endTime","scheduleDeadlineTime":"scheduleDeadlineTime"},"statusMessage":"statusMessage","labels":{"key":"labels"},"maintenancePolicy":{"createTime":"createTime","description":"description","weeklyMaintenanceWindow":[{"duration":"duration","startTime":{"hours":0,"seconds":5,"nanos":1,"minutes":6},"day":"DAY_OF_WEEK_UNSPECIFIED"},{"duration":"duration","startTime":{"hours":0,"seconds":5,"nanos":1,"minutes":6},"day":"DAY_OF_WEEK_UNSPECIFIED"}],"updateTime":"updateTime"},"redisVersion":"redisVersion","nodes":[{"zone":"zone","id":"id"},{"zone":"zone","id":"id"}],"createTime":"createTime","port":2,"readReplicasMode":"READ_REPLICAS_MODE_UNSPECIFIED","alternativeLocationId":"alternativeLocationId","name":"name","satisfiesPzi":True,"currentLocationId":"currentLocationId","readEndpointPort":7,"transitEncryptionMode":"TRANSIT_ENCRYPTION_MODE_UNSPECIFIED"}
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

async def test_redis_projects_locations_instances_reschedule_maintenance(client):
    """Test case for redis_projects_locations_instances_reschedule_maintenance

    
    """
    body = {"scheduleTime":"scheduleTime","rescheduleType":"RESCHEDULE_TYPE_UNSPECIFIED"}
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
        path='/v1/{namereschedule_maintenanc}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_redis_projects_locations_instances_upgrade(client):
    """Test case for redis_projects_locations_instances_upgrade

    
    """
    body = {"redisVersion":"redisVersion"}
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
        path='/v1/{nameupgrad}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_redis_projects_locations_list(client):
    """Test case for redis_projects_locations_list

    
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

async def test_redis_projects_locations_operations_cancel(client):
    """Test case for redis_projects_locations_operations_cancel

    
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
        path='/v1/{namecance}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_redis_projects_locations_operations_delete(client):
    """Test case for redis_projects_locations_operations_delete

    
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

async def test_redis_projects_locations_operations_get(client):
    """Test case for redis_projects_locations_operations_get

    
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

async def test_redis_projects_locations_operations_list(client):
    """Test case for redis_projects_locations_operations_list

    
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

