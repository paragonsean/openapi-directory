# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.detach_lun_request import DetachLunRequest
from openapi_server.models.list_instances_response import ListInstancesResponse
from openapi_server.models.list_locations_response import ListLocationsResponse
from openapi_server.models.list_luns_response import ListLunsResponse
from openapi_server.models.list_network_usage_response import ListNetworkUsageResponse
from openapi_server.models.list_networks_response import ListNetworksResponse
from openapi_server.models.list_nfs_shares_response import ListNfsSharesResponse
from openapi_server.models.list_os_images_response import ListOSImagesResponse
from openapi_server.models.list_provisioning_quotas_response import ListProvisioningQuotasResponse
from openapi_server.models.list_ssh_keys_response import ListSSHKeysResponse
from openapi_server.models.list_volume_snapshots_response import ListVolumeSnapshotsResponse
from openapi_server.models.list_volumes_response import ListVolumesResponse
from openapi_server.models.load_instance_auth_info_response import LoadInstanceAuthInfoResponse
from openapi_server.models.nfs_share import NfsShare
from openapi_server.models.operation import Operation
from openapi_server.models.provisioning_config import ProvisioningConfig
from openapi_server.models.rename_volume_request import RenameVolumeRequest
from openapi_server.models.resize_volume_request import ResizeVolumeRequest
from openapi_server.models.ssh_key import SSHKey
from openapi_server.models.submit_provisioning_config_request import SubmitProvisioningConfigRequest
from openapi_server.models.submit_provisioning_config_response import SubmitProvisioningConfigResponse
from openapi_server.models.volume import Volume
from openapi_server.models.volume_snapshot import VolumeSnapshot


pytestmark = pytest.mark.asyncio

async def test_baremetalsolution_projects_locations_instances_detach_lun(client):
    """Test case for baremetalsolution_projects_locations_instances_detach_lun

    
    """
    body = {"lun":"lun","skipReboot":True}
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
        path='/v2/{instancedetach_lu}'.format(instance='instance_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_baremetalsolution_projects_locations_instances_disable_interactive_serial_console(client):
    """Test case for baremetalsolution_projects_locations_instances_disable_interactive_serial_console

    
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
        path='/v2/{namedisable_interactive_serial_consol}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_baremetalsolution_projects_locations_instances_enable_interactive_serial_console(client):
    """Test case for baremetalsolution_projects_locations_instances_enable_interactive_serial_console

    
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
        path='/v2/{nameenable_interactive_serial_consol}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_baremetalsolution_projects_locations_instances_list(client):
    """Test case for baremetalsolution_projects_locations_instances_list

    
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
        path='/v2/{parent}/instances'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_baremetalsolution_projects_locations_instances_load_auth_info(client):
    """Test case for baremetalsolution_projects_locations_instances_load_auth_info

    
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
        path='/v2/{nameload_auth_inf}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_baremetalsolution_projects_locations_instances_reset(client):
    """Test case for baremetalsolution_projects_locations_instances_reset

    
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
        path='/v2/{namerese}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_baremetalsolution_projects_locations_instances_start(client):
    """Test case for baremetalsolution_projects_locations_instances_start

    
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
        path='/v2/{namestar}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_baremetalsolution_projects_locations_instances_stop(client):
    """Test case for baremetalsolution_projects_locations_instances_stop

    
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
        path='/v2/{namesto}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_baremetalsolution_projects_locations_list(client):
    """Test case for baremetalsolution_projects_locations_list

    
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
        path='/v2/{name}/locations'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_baremetalsolution_projects_locations_networks_list(client):
    """Test case for baremetalsolution_projects_locations_networks_list

    
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
        path='/v2/{parent}/networks'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_baremetalsolution_projects_locations_networks_list_network_usage(client):
    """Test case for baremetalsolution_projects_locations_networks_list_network_usage

    
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
        path='/v2/{location}/networks:listNetworkUsage'.format(location='location_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_baremetalsolution_projects_locations_nfs_shares_create(client):
    """Test case for baremetalsolution_projects_locations_nfs_shares_create

    
    """
    body = {"volume":"volume","pod":"pod","requestedSizeGib":"requestedSizeGib","allowedClients":[{"noRootSquash":True,"nfsPath":"nfsPath","shareIp":"shareIp","allowSuid":True,"allowedClientsCidr":"allowedClientsCidr","allowDev":True,"mountPermissions":"MOUNT_PERMISSIONS_UNSPECIFIED","network":"network"},{"noRootSquash":True,"nfsPath":"nfsPath","shareIp":"shareIp","allowSuid":True,"allowedClientsCidr":"allowedClientsCidr","allowDev":True,"mountPermissions":"MOUNT_PERMISSIONS_UNSPECIFIED","network":"network"}],"name":"name","storageType":"STORAGE_TYPE_UNSPECIFIED","id":"id","state":"STATE_UNSPECIFIED","nfsShareId":"nfsShareId","labels":{"key":"labels"}}
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
        path='/v2/{parent}/nfsShares'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_baremetalsolution_projects_locations_nfs_shares_list(client):
    """Test case for baremetalsolution_projects_locations_nfs_shares_list

    
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
        path='/v2/{parent}/nfsShares'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_baremetalsolution_projects_locations_os_images_list(client):
    """Test case for baremetalsolution_projects_locations_os_images_list

    
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
        path='/v2/{parent}/osImages'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_baremetalsolution_projects_locations_provisioning_configs_create(client):
    """Test case for baremetalsolution_projects_locations_provisioning_configs_create

    
    """
    body = {"pod":"pod","instances":[{"networkTemplate":"networkTemplate","privateNetwork":{"address":"address","existingNetworkId":"existingNetworkId","networkId":"networkId"},"userNote":"userNote","instanceType":"instanceType","networkConfig":"NETWORKCONFIG_UNSPECIFIED","kmsKeyVersion":"kmsKeyVersion","logicalInterfaces":[{"name":"name","interfaceIndex":0,"logicalNetworkInterfaces":[{"ipAddress":"ipAddress","id":"id","networkType":"TYPE_UNSPECIFIED","defaultGateway":True,"network":"network"},{"ipAddress":"ipAddress","id":"id","networkType":"TYPE_UNSPECIFIED","defaultGateway":True,"network":"network"}]},{"name":"name","interfaceIndex":0,"logicalNetworkInterfaces":[{"ipAddress":"ipAddress","id":"id","networkType":"TYPE_UNSPECIFIED","defaultGateway":True,"network":"network"},{"ipAddress":"ipAddress","id":"id","networkType":"TYPE_UNSPECIFIED","defaultGateway":True,"network":"network"}]}],"clientNetwork":{"address":"address","existingNetworkId":"existingNetworkId","networkId":"networkId"},"accountNetworksEnabled":True,"name":"name","sshKeyNames":["sshKeyNames","sshKeyNames"],"id":"id","hyperthreading":True,"osImage":"osImage"},{"networkTemplate":"networkTemplate","privateNetwork":{"address":"address","existingNetworkId":"existingNetworkId","networkId":"networkId"},"userNote":"userNote","instanceType":"instanceType","networkConfig":"NETWORKCONFIG_UNSPECIFIED","kmsKeyVersion":"kmsKeyVersion","logicalInterfaces":[{"name":"name","interfaceIndex":0,"logicalNetworkInterfaces":[{"ipAddress":"ipAddress","id":"id","networkType":"TYPE_UNSPECIFIED","defaultGateway":True,"network":"network"},{"ipAddress":"ipAddress","id":"id","networkType":"TYPE_UNSPECIFIED","defaultGateway":True,"network":"network"}]},{"name":"name","interfaceIndex":0,"logicalNetworkInterfaces":[{"ipAddress":"ipAddress","id":"id","networkType":"TYPE_UNSPECIFIED","defaultGateway":True,"network":"network"},{"ipAddress":"ipAddress","id":"id","networkType":"TYPE_UNSPECIFIED","defaultGateway":True,"network":"network"}]}],"clientNetwork":{"address":"address","existingNetworkId":"existingNetworkId","networkId":"networkId"},"accountNetworksEnabled":True,"name":"name","sshKeyNames":["sshKeyNames","sshKeyNames"],"id":"id","hyperthreading":True,"osImage":"osImage"}],"volumes":[{"sizeGb":1,"gcpService":"gcpService","protocol":"PROTOCOL_UNSPECIFIED","performanceTier":"VOLUME_PERFORMANCE_TIER_UNSPECIFIED","lunRanges":[{"sizeGb":6,"quantity":0},{"sizeGb":6,"quantity":0}],"userNote":"userNote","machineIds":["machineIds","machineIds"],"name":"name","snapshotsEnabled":True,"id":"id","type":"TYPE_UNSPECIFIED","nfsExports":[{"machineId":"machineId","noRootSquash":True,"permissions":"PERMISSIONS_UNSPECIFIED","allowSuid":True,"cidr":"cidr","networkId":"networkId","allowDev":True},{"machineId":"machineId","noRootSquash":True,"permissions":"PERMISSIONS_UNSPECIFIED","allowSuid":True,"cidr":"cidr","networkId":"networkId","allowDev":True}]},{"sizeGb":1,"gcpService":"gcpService","protocol":"PROTOCOL_UNSPECIFIED","performanceTier":"VOLUME_PERFORMANCE_TIER_UNSPECIFIED","lunRanges":[{"sizeGb":6,"quantity":0},{"sizeGb":6,"quantity":0}],"userNote":"userNote","machineIds":["machineIds","machineIds"],"name":"name","snapshotsEnabled":True,"id":"id","type":"TYPE_UNSPECIFIED","nfsExports":[{"machineId":"machineId","noRootSquash":True,"permissions":"PERMISSIONS_UNSPECIFIED","allowSuid":True,"cidr":"cidr","networkId":"networkId","allowDev":True},{"machineId":"machineId","noRootSquash":True,"permissions":"PERMISSIONS_UNSPECIFIED","allowSuid":True,"cidr":"cidr","networkId":"networkId","allowDev":True}]}],"updateTime":"updateTime","vpcScEnabled":True,"networks":[{"vlanAttachments":[{"id":"id","pairingKey":"pairingKey"},{"id":"id","pairingKey":"pairingKey"}],"gcpService":"gcpService","bandwidth":"BANDWIDTH_UNSPECIFIED","jumboFramesEnabled":True,"userNote":"userNote","name":"name","cidr":"cidr","id":"id","vlanSameProject":True,"type":"TYPE_UNSPECIFIED","serviceCidr":"SERVICE_CIDR_UNSPECIFIED"},{"vlanAttachments":[{"id":"id","pairingKey":"pairingKey"},{"id":"id","pairingKey":"pairingKey"}],"gcpService":"gcpService","bandwidth":"BANDWIDTH_UNSPECIFIED","jumboFramesEnabled":True,"userNote":"userNote","name":"name","cidr":"cidr","id":"id","vlanSameProject":True,"type":"TYPE_UNSPECIFIED","serviceCidr":"SERVICE_CIDR_UNSPECIFIED"}],"customId":"customId","statusMessage":"statusMessage","handoverServiceAccount":"handoverServiceAccount","cloudConsoleUri":"cloudConsoleUri","name":"name","location":"location","state":"STATE_UNSPECIFIED","email":"email","ticketId":"ticketId"}
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
                    ('email', 'email_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/{parent}/provisioningConfigs'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_baremetalsolution_projects_locations_provisioning_configs_submit(client):
    """Test case for baremetalsolution_projects_locations_provisioning_configs_submit

    
    """
    body = {"provisioningConfig":{"pod":"pod","instances":[{"networkTemplate":"networkTemplate","privateNetwork":{"address":"address","existingNetworkId":"existingNetworkId","networkId":"networkId"},"userNote":"userNote","instanceType":"instanceType","networkConfig":"NETWORKCONFIG_UNSPECIFIED","kmsKeyVersion":"kmsKeyVersion","logicalInterfaces":[{"name":"name","interfaceIndex":0,"logicalNetworkInterfaces":[{"ipAddress":"ipAddress","id":"id","networkType":"TYPE_UNSPECIFIED","defaultGateway":True,"network":"network"},{"ipAddress":"ipAddress","id":"id","networkType":"TYPE_UNSPECIFIED","defaultGateway":True,"network":"network"}]},{"name":"name","interfaceIndex":0,"logicalNetworkInterfaces":[{"ipAddress":"ipAddress","id":"id","networkType":"TYPE_UNSPECIFIED","defaultGateway":True,"network":"network"},{"ipAddress":"ipAddress","id":"id","networkType":"TYPE_UNSPECIFIED","defaultGateway":True,"network":"network"}]}],"clientNetwork":{"address":"address","existingNetworkId":"existingNetworkId","networkId":"networkId"},"accountNetworksEnabled":True,"name":"name","sshKeyNames":["sshKeyNames","sshKeyNames"],"id":"id","hyperthreading":True,"osImage":"osImage"},{"networkTemplate":"networkTemplate","privateNetwork":{"address":"address","existingNetworkId":"existingNetworkId","networkId":"networkId"},"userNote":"userNote","instanceType":"instanceType","networkConfig":"NETWORKCONFIG_UNSPECIFIED","kmsKeyVersion":"kmsKeyVersion","logicalInterfaces":[{"name":"name","interfaceIndex":0,"logicalNetworkInterfaces":[{"ipAddress":"ipAddress","id":"id","networkType":"TYPE_UNSPECIFIED","defaultGateway":True,"network":"network"},{"ipAddress":"ipAddress","id":"id","networkType":"TYPE_UNSPECIFIED","defaultGateway":True,"network":"network"}]},{"name":"name","interfaceIndex":0,"logicalNetworkInterfaces":[{"ipAddress":"ipAddress","id":"id","networkType":"TYPE_UNSPECIFIED","defaultGateway":True,"network":"network"},{"ipAddress":"ipAddress","id":"id","networkType":"TYPE_UNSPECIFIED","defaultGateway":True,"network":"network"}]}],"clientNetwork":{"address":"address","existingNetworkId":"existingNetworkId","networkId":"networkId"},"accountNetworksEnabled":True,"name":"name","sshKeyNames":["sshKeyNames","sshKeyNames"],"id":"id","hyperthreading":True,"osImage":"osImage"}],"volumes":[{"sizeGb":1,"gcpService":"gcpService","protocol":"PROTOCOL_UNSPECIFIED","performanceTier":"VOLUME_PERFORMANCE_TIER_UNSPECIFIED","lunRanges":[{"sizeGb":6,"quantity":0},{"sizeGb":6,"quantity":0}],"userNote":"userNote","machineIds":["machineIds","machineIds"],"name":"name","snapshotsEnabled":True,"id":"id","type":"TYPE_UNSPECIFIED","nfsExports":[{"machineId":"machineId","noRootSquash":True,"permissions":"PERMISSIONS_UNSPECIFIED","allowSuid":True,"cidr":"cidr","networkId":"networkId","allowDev":True},{"machineId":"machineId","noRootSquash":True,"permissions":"PERMISSIONS_UNSPECIFIED","allowSuid":True,"cidr":"cidr","networkId":"networkId","allowDev":True}]},{"sizeGb":1,"gcpService":"gcpService","protocol":"PROTOCOL_UNSPECIFIED","performanceTier":"VOLUME_PERFORMANCE_TIER_UNSPECIFIED","lunRanges":[{"sizeGb":6,"quantity":0},{"sizeGb":6,"quantity":0}],"userNote":"userNote","machineIds":["machineIds","machineIds"],"name":"name","snapshotsEnabled":True,"id":"id","type":"TYPE_UNSPECIFIED","nfsExports":[{"machineId":"machineId","noRootSquash":True,"permissions":"PERMISSIONS_UNSPECIFIED","allowSuid":True,"cidr":"cidr","networkId":"networkId","allowDev":True},{"machineId":"machineId","noRootSquash":True,"permissions":"PERMISSIONS_UNSPECIFIED","allowSuid":True,"cidr":"cidr","networkId":"networkId","allowDev":True}]}],"updateTime":"updateTime","vpcScEnabled":True,"networks":[{"vlanAttachments":[{"id":"id","pairingKey":"pairingKey"},{"id":"id","pairingKey":"pairingKey"}],"gcpService":"gcpService","bandwidth":"BANDWIDTH_UNSPECIFIED","jumboFramesEnabled":True,"userNote":"userNote","name":"name","cidr":"cidr","id":"id","vlanSameProject":True,"type":"TYPE_UNSPECIFIED","serviceCidr":"SERVICE_CIDR_UNSPECIFIED"},{"vlanAttachments":[{"id":"id","pairingKey":"pairingKey"},{"id":"id","pairingKey":"pairingKey"}],"gcpService":"gcpService","bandwidth":"BANDWIDTH_UNSPECIFIED","jumboFramesEnabled":True,"userNote":"userNote","name":"name","cidr":"cidr","id":"id","vlanSameProject":True,"type":"TYPE_UNSPECIFIED","serviceCidr":"SERVICE_CIDR_UNSPECIFIED"}],"customId":"customId","statusMessage":"statusMessage","handoverServiceAccount":"handoverServiceAccount","cloudConsoleUri":"cloudConsoleUri","name":"name","location":"location","state":"STATE_UNSPECIFIED","email":"email","ticketId":"ticketId"},"email":"email"}
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
        path='/v2/{parent}/provisioningConfigs:submit'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_baremetalsolution_projects_locations_provisioning_quotas_list(client):
    """Test case for baremetalsolution_projects_locations_provisioning_quotas_list

    
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
        path='/v2/{parent}/provisioningQuotas'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_baremetalsolution_projects_locations_ssh_keys_create(client):
    """Test case for baremetalsolution_projects_locations_ssh_keys_create

    
    """
    body = {"name":"name","publicKey":"publicKey"}
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
                    ('sshKeyId', 'ssh_key_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/{parent}/sshKeys'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_baremetalsolution_projects_locations_ssh_keys_list(client):
    """Test case for baremetalsolution_projects_locations_ssh_keys_list

    
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
        path='/v2/{parent}/sshKeys'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_baremetalsolution_projects_locations_volumes_list(client):
    """Test case for baremetalsolution_projects_locations_volumes_list

    
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
        path='/v2/{parent}/volumes'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_baremetalsolution_projects_locations_volumes_luns_evict(client):
    """Test case for baremetalsolution_projects_locations_volumes_luns_evict

    
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
        path='/v2/{nameevic}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_baremetalsolution_projects_locations_volumes_luns_list(client):
    """Test case for baremetalsolution_projects_locations_volumes_luns_list

    
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
        path='/v2/{parent}/luns'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_baremetalsolution_projects_locations_volumes_patch(client):
    """Test case for baremetalsolution_projects_locations_volumes_patch

    
    """
    body = {"bootVolume":True,"maxSizeGib":"maxSizeGib","notes":"notes","pod":"pod","requestedSizeGib":"requestedSizeGib","instances":["instances","instances"],"originallyRequestedSizeGib":"originallyRequestedSizeGib","snapshotReservationDetail":{"reservedSpacePercent":0,"reservedSpaceUsedPercent":6,"reservedSpaceRemainingGib":"reservedSpaceRemainingGib","reservedSpaceGib":"reservedSpaceGib"},"autoGrownSizeGib":"autoGrownSizeGib","labels":{"key":"labels"},"remainingSpaceGib":"remainingSpaceGib","protocol":"PROTOCOL_UNSPECIFIED","snapshotAutoDeleteBehavior":"SNAPSHOT_AUTO_DELETE_BEHAVIOR_UNSPECIFIED","workloadProfile":"WORKLOAD_PROFILE_UNSPECIFIED","expireTime":"expireTime","performanceTier":"VOLUME_PERFORMANCE_TIER_UNSPECIFIED","snapshotEnabled":True,"attached":True,"name":"name","storageType":"STORAGE_TYPE_UNSPECIFIED","currentSizeGib":"currentSizeGib","id":"id","state":"STATE_UNSPECIFIED","emergencySizeGib":"emergencySizeGib"}
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
        path='/v2/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_baremetalsolution_projects_locations_volumes_rename(client):
    """Test case for baremetalsolution_projects_locations_volumes_rename

    
    """
    body = {"newVolumeId":"newVolumeId"}
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
        path='/v2/{namerenam}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_baremetalsolution_projects_locations_volumes_resize(client):
    """Test case for baremetalsolution_projects_locations_volumes_resize

    
    """
    body = {"sizeGib":"sizeGib"}
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
        path='/v2/{volumeresiz}'.format(volume='volume_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_baremetalsolution_projects_locations_volumes_snapshots_create(client):
    """Test case for baremetalsolution_projects_locations_volumes_snapshots_create

    
    """
    body = {"storageVolume":"storageVolume","createTime":"createTime","name":"name","description":"description","id":"id","type":"SNAPSHOT_TYPE_UNSPECIFIED"}
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
        path='/v2/{parent}/snapshots'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_baremetalsolution_projects_locations_volumes_snapshots_delete(client):
    """Test case for baremetalsolution_projects_locations_volumes_snapshots_delete

    
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
        path='/v2/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_baremetalsolution_projects_locations_volumes_snapshots_get(client):
    """Test case for baremetalsolution_projects_locations_volumes_snapshots_get

    
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
        path='/v2/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_baremetalsolution_projects_locations_volumes_snapshots_list(client):
    """Test case for baremetalsolution_projects_locations_volumes_snapshots_list

    
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
        path='/v2/{parent}/snapshots'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_baremetalsolution_projects_locations_volumes_snapshots_restore_volume_snapshot(client):
    """Test case for baremetalsolution_projects_locations_volumes_snapshots_restore_volume_snapshot

    
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
        path='/v2/{volume_snapshotrestore_volume_snapsho}'.format(volume_snapshot='volume_snapshot_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

