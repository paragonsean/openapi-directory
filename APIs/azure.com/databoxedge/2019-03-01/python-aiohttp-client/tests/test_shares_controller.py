# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.share import Share
from openapi_server.models.share_list import ShareList


pytestmark = pytest.mark.asyncio

async def test_shares_create_or_update(client):
    """Test case for shares_create_or_update

    Creates a new share or updates an existing share on the device.
    """
    share = {"properties":{"shareMappings":[{"mountPoint":"mountPoint","roleId":"roleId","shareId":"shareId","roleType":"IOT"},{"mountPoint":"mountPoint","roleId":"roleId","shareId":"shareId","roleType":"IOT"}],"azureContainerInfo":{"containerName":"containerName","dataFormat":"BlockBlob","storageAccountCredentialId":"storageAccountCredentialId"},"clientAccessRights":[{"accessPermission":"NoAccess","client":"client"},{"accessPermission":"NoAccess","client":"client"}],"userAccessRights":[{"accessType":"Change","userId":"userId"},{"accessType":"Change","userId":"userId"}],"monitoringStatus":"Enabled","dataPolicy":"Cloud","description":"description","accessProtocol":"SMB","refreshDetails":{"errorManifestFile":"errorManifestFile","lastJob":"lastJob","inProgressRefreshJobId":"inProgressRefreshJobId","lastCompletedRefreshJobTimeInUTC":"2000-01-23T04:56:07.000+00:00"},"shareStatus":"Online"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{device_name}/shares/{name}'.format(device_name='device_name_example', name='name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        json=share,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shares_delete(client):
    """Test case for shares_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{device_name}/shares/{name}'.format(device_name='device_name_example', name='name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shares_get(client):
    """Test case for shares_get

    Gets a share by name.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{device_name}/shares/{name}'.format(device_name='device_name_example', name='name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shares_list_by_data_box_edge_device(client):
    """Test case for shares_list_by_data_box_edge_device

    Lists all the shares in a data box edge/gateway device.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{device_name}/shares'.format(device_name='device_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shares_refresh(client):
    """Test case for shares_refresh

    Refreshes the share metadata with the data from the cloud.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{device_name}/shares/{name}/refresh'.format(device_name='device_name_example', name='name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

