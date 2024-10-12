# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.generate_service_identity_response import GenerateServiceIdentityResponse
from openapi_server.models.get_guest_attributes_request import GetGuestAttributesRequest
from openapi_server.models.get_guest_attributes_response import GetGuestAttributesResponse
from openapi_server.models.list_accelerator_types_response import ListAcceleratorTypesResponse
from openapi_server.models.list_locations_response import ListLocationsResponse
from openapi_server.models.list_nodes_response import ListNodesResponse
from openapi_server.models.list_operations_response import ListOperationsResponse
from openapi_server.models.list_queued_resources_response import ListQueuedResourcesResponse
from openapi_server.models.list_reservations_response import ListReservationsResponse
from openapi_server.models.list_runtime_versions_response import ListRuntimeVersionsResponse
from openapi_server.models.node import Node
from openapi_server.models.operation import Operation
from openapi_server.models.queued_resource import QueuedResource
from openapi_server.models.runtime_version import RuntimeVersion
from openapi_server.models.simulate_maintenance_event_request import SimulateMaintenanceEventRequest


pytestmark = pytest.mark.asyncio

async def test_tpu_projects_locations_accelerator_types_list(client):
    """Test case for tpu_projects_locations_accelerator_types_list

    
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
        path='/v2alpha1/{parent}/acceleratorTypes'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tpu_projects_locations_generate_service_identity(client):
    """Test case for tpu_projects_locations_generate_service_identity

    
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
        path='/v2alpha1/{parentgenerate_service_identit}'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tpu_projects_locations_list(client):
    """Test case for tpu_projects_locations_list

    
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
        path='/v2alpha1/{name}/locations'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tpu_projects_locations_nodes_create(client):
    """Test case for tpu_projects_locations_nodes_create

    
    """
    body = {"metadata":{"key":"metadata"},"runtimeVersion":"runtimeVersion","description":"description","multisliceNode":True,"acceleratorType":"acceleratorType","apiVersion":"API_VERSION_UNSPECIFIED","id":"id","state":"STATE_UNSPECIFIED","schedulingConfig":{"preemptible":True,"reserved":True,"spot":True},"shieldedInstanceConfig":{"enableSecureBoot":True},"cidrBlock":"cidrBlock","networkConfig":{"queueCount":0,"canIpForward":True,"enableExternalIps":True,"subnetwork":"subnetwork","network":"network"},"bootDiskConfig":{"enableConfidentialCompute":True,"customerEncryptionKey":{"kmsKeyName":"kmsKeyName"}},"health":"HEALTH_UNSPECIFIED","serviceAccount":{"scope":["scope","scope"],"email":"email"},"healthDescription":"healthDescription","autocheckpointEnabled":True,"labels":{"key":"labels"},"tags":["tags","tags"],"symptoms":[{"workerId":"workerId","createTime":"createTime","details":"details","symptomType":"SYMPTOM_TYPE_UNSPECIFIED"},{"workerId":"workerId","createTime":"createTime","details":"details","symptomType":"SYMPTOM_TYPE_UNSPECIFIED"}],"networkEndpoints":[{"port":6,"ipAddress":"ipAddress","accessConfig":{"externalIp":"externalIp"}},{"port":6,"ipAddress":"ipAddress","accessConfig":{"externalIp":"externalIp"}}],"acceleratorConfig":{"topology":"topology","type":"TYPE_UNSPECIFIED"},"createTime":"createTime","name":"name","dataDisks":[{"mode":"DISK_MODE_UNSPECIFIED","sourceDisk":"sourceDisk"},{"mode":"DISK_MODE_UNSPECIFIED","sourceDisk":"sourceDisk"}],"queuedResource":"queuedResource"}
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
                    ('nodeId', 'node_id_example'),
                    ('requestId', 'request_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2alpha1/{parent}/nodes'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tpu_projects_locations_nodes_get_guest_attributes(client):
    """Test case for tpu_projects_locations_nodes_get_guest_attributes

    
    """
    body = {"queryPath":"queryPath","workerIds":["workerIds","workerIds"]}
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
        path='/v2alpha1/{nameget_guest_attribute}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tpu_projects_locations_nodes_list(client):
    """Test case for tpu_projects_locations_nodes_list

    
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
        path='/v2alpha1/{parent}/nodes'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tpu_projects_locations_nodes_patch(client):
    """Test case for tpu_projects_locations_nodes_patch

    
    """
    body = {"metadata":{"key":"metadata"},"runtimeVersion":"runtimeVersion","description":"description","multisliceNode":True,"acceleratorType":"acceleratorType","apiVersion":"API_VERSION_UNSPECIFIED","id":"id","state":"STATE_UNSPECIFIED","schedulingConfig":{"preemptible":True,"reserved":True,"spot":True},"shieldedInstanceConfig":{"enableSecureBoot":True},"cidrBlock":"cidrBlock","networkConfig":{"queueCount":0,"canIpForward":True,"enableExternalIps":True,"subnetwork":"subnetwork","network":"network"},"bootDiskConfig":{"enableConfidentialCompute":True,"customerEncryptionKey":{"kmsKeyName":"kmsKeyName"}},"health":"HEALTH_UNSPECIFIED","serviceAccount":{"scope":["scope","scope"],"email":"email"},"healthDescription":"healthDescription","autocheckpointEnabled":True,"labels":{"key":"labels"},"tags":["tags","tags"],"symptoms":[{"workerId":"workerId","createTime":"createTime","details":"details","symptomType":"SYMPTOM_TYPE_UNSPECIFIED"},{"workerId":"workerId","createTime":"createTime","details":"details","symptomType":"SYMPTOM_TYPE_UNSPECIFIED"}],"networkEndpoints":[{"port":6,"ipAddress":"ipAddress","accessConfig":{"externalIp":"externalIp"}},{"port":6,"ipAddress":"ipAddress","accessConfig":{"externalIp":"externalIp"}}],"acceleratorConfig":{"topology":"topology","type":"TYPE_UNSPECIFIED"},"createTime":"createTime","name":"name","dataDisks":[{"mode":"DISK_MODE_UNSPECIFIED","sourceDisk":"sourceDisk"},{"mode":"DISK_MODE_UNSPECIFIED","sourceDisk":"sourceDisk"}],"queuedResource":"queuedResource"}
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
        path='/v2alpha1/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tpu_projects_locations_nodes_simulate_maintenance_event(client):
    """Test case for tpu_projects_locations_nodes_simulate_maintenance_event

    
    """
    body = {"workerIds":["workerIds","workerIds"]}
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
        path='/v2alpha1/{namesimulate_maintenance_even}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tpu_projects_locations_nodes_start(client):
    """Test case for tpu_projects_locations_nodes_start

    
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
        path='/v2alpha1/{namestar}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tpu_projects_locations_nodes_stop(client):
    """Test case for tpu_projects_locations_nodes_stop

    
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
        path='/v2alpha1/{namesto}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tpu_projects_locations_operations_cancel(client):
    """Test case for tpu_projects_locations_operations_cancel

    
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
        path='/v2alpha1/{namecance}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tpu_projects_locations_operations_list(client):
    """Test case for tpu_projects_locations_operations_list

    
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
        path='/v2alpha1/{name}/operations'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tpu_projects_locations_queued_resources_create(client):
    """Test case for tpu_projects_locations_queued_resources_create

    
    """
    body = {"bestEffort":"{}","createTime":"createTime","queueingPolicy":{"validAfterDuration":"validAfterDuration","validInterval":{"startTime":"startTime","endTime":"endTime"},"validUntilDuration":"validUntilDuration","validUntilTime":"validUntilTime","validAfterTime":"validAfterTime"},"spot":"{}","name":"name","tpu":{"nodeSpec":[{"node":{"metadata":{"key":"metadata"},"runtimeVersion":"runtimeVersion","description":"description","multisliceNode":True,"acceleratorType":"acceleratorType","apiVersion":"API_VERSION_UNSPECIFIED","id":"id","state":"STATE_UNSPECIFIED","schedulingConfig":{"preemptible":True,"reserved":True,"spot":True},"shieldedInstanceConfig":{"enableSecureBoot":True},"cidrBlock":"cidrBlock","networkConfig":{"queueCount":0,"canIpForward":True,"enableExternalIps":True,"subnetwork":"subnetwork","network":"network"},"bootDiskConfig":{"enableConfidentialCompute":True,"customerEncryptionKey":{"kmsKeyName":"kmsKeyName"}},"health":"HEALTH_UNSPECIFIED","serviceAccount":{"scope":["scope","scope"],"email":"email"},"healthDescription":"healthDescription","autocheckpointEnabled":True,"labels":{"key":"labels"},"tags":["tags","tags"],"symptoms":[{"workerId":"workerId","createTime":"createTime","details":"details","symptomType":"SYMPTOM_TYPE_UNSPECIFIED"},{"workerId":"workerId","createTime":"createTime","details":"details","symptomType":"SYMPTOM_TYPE_UNSPECIFIED"}],"networkEndpoints":[{"port":6,"ipAddress":"ipAddress","accessConfig":{"externalIp":"externalIp"}},{"port":6,"ipAddress":"ipAddress","accessConfig":{"externalIp":"externalIp"}}],"acceleratorConfig":{"topology":"topology","type":"TYPE_UNSPECIFIED"},"createTime":"createTime","name":"name","dataDisks":[{"mode":"DISK_MODE_UNSPECIFIED","sourceDisk":"sourceDisk"},{"mode":"DISK_MODE_UNSPECIFIED","sourceDisk":"sourceDisk"}],"queuedResource":"queuedResource"},"parent":"parent","multiNodeParams":{"nodeIdPrefix":"nodeIdPrefix","nodeCount":0},"nodeId":"nodeId"},{"node":{"metadata":{"key":"metadata"},"runtimeVersion":"runtimeVersion","description":"description","multisliceNode":True,"acceleratorType":"acceleratorType","apiVersion":"API_VERSION_UNSPECIFIED","id":"id","state":"STATE_UNSPECIFIED","schedulingConfig":{"preemptible":True,"reserved":True,"spot":True},"shieldedInstanceConfig":{"enableSecureBoot":True},"cidrBlock":"cidrBlock","networkConfig":{"queueCount":0,"canIpForward":True,"enableExternalIps":True,"subnetwork":"subnetwork","network":"network"},"bootDiskConfig":{"enableConfidentialCompute":True,"customerEncryptionKey":{"kmsKeyName":"kmsKeyName"}},"health":"HEALTH_UNSPECIFIED","serviceAccount":{"scope":["scope","scope"],"email":"email"},"healthDescription":"healthDescription","autocheckpointEnabled":True,"labels":{"key":"labels"},"tags":["tags","tags"],"symptoms":[{"workerId":"workerId","createTime":"createTime","details":"details","symptomType":"SYMPTOM_TYPE_UNSPECIFIED"},{"workerId":"workerId","createTime":"createTime","details":"details","symptomType":"SYMPTOM_TYPE_UNSPECIFIED"}],"networkEndpoints":[{"port":6,"ipAddress":"ipAddress","accessConfig":{"externalIp":"externalIp"}},{"port":6,"ipAddress":"ipAddress","accessConfig":{"externalIp":"externalIp"}}],"acceleratorConfig":{"topology":"topology","type":"TYPE_UNSPECIFIED"},"createTime":"createTime","name":"name","dataDisks":[{"mode":"DISK_MODE_UNSPECIFIED","sourceDisk":"sourceDisk"},{"mode":"DISK_MODE_UNSPECIFIED","sourceDisk":"sourceDisk"}],"queuedResource":"queuedResource"},"parent":"parent","multiNodeParams":{"nodeIdPrefix":"nodeIdPrefix","nodeCount":0},"nodeId":"nodeId"}]},"guaranteed":{"minDuration":"minDuration","reserved":True},"state":{"deletingData":"{}","suspendedData":"{}","suspendingData":"{}","acceptedData":"{}","creatingData":"{}","state":"STATE_UNSPECIFIED","stateInitiator":"STATE_INITIATOR_UNSPECIFIED","activeData":"{}","provisioningData":"{}","failedData":{"error":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"}}},"reservationName":"reservationName"}
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
                    ('queuedResourceId', 'queued_resource_id_example'),
                    ('requestId', 'request_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2alpha1/{parent}/queuedResources'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tpu_projects_locations_queued_resources_delete(client):
    """Test case for tpu_projects_locations_queued_resources_delete

    
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
                    ('force', True),
                    ('requestId', 'request_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2alpha1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tpu_projects_locations_queued_resources_list(client):
    """Test case for tpu_projects_locations_queued_resources_list

    
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
        path='/v2alpha1/{parent}/queuedResources'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tpu_projects_locations_queued_resources_reset(client):
    """Test case for tpu_projects_locations_queued_resources_reset

    
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
        path='/v2alpha1/{namerese}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tpu_projects_locations_reservations_list(client):
    """Test case for tpu_projects_locations_reservations_list

    
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
        path='/v2alpha1/{parent}/reservations'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tpu_projects_locations_runtime_versions_get(client):
    """Test case for tpu_projects_locations_runtime_versions_get

    
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
        path='/v2alpha1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tpu_projects_locations_runtime_versions_list(client):
    """Test case for tpu_projects_locations_runtime_versions_list

    
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
        path='/v2alpha1/{parent}/runtimeVersions'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

