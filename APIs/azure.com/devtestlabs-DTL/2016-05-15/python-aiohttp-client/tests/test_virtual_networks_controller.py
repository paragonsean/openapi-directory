# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.response_with_continuation_virtual_network import ResponseWithContinuationVirtualNetwork
from openapi_server.models.virtual_network import VirtualNetwork
from openapi_server.models.virtual_network_fragment import VirtualNetworkFragment


pytestmark = pytest.mark.asyncio

async def test_virtual_networks_create_or_update(client):
    """Test case for virtual_networks_create_or_update

    
    """
    virtual_network = {"properties":{"subnetOverrides":[{"useInVmCreationPermission":"Default","resourceId":"resourceId","usePublicIpAddressPermission":"Default","virtualNetworkPoolName":"virtualNetworkPoolName","labSubnetName":"labSubnetName","sharedPublicIpAddressConfiguration":{"allowedPorts":[{"backendPort":0,"transportProtocol":"Tcp"},{"backendPort":0,"transportProtocol":"Tcp"}]}},{"useInVmCreationPermission":"Default","resourceId":"resourceId","usePublicIpAddressPermission":"Default","virtualNetworkPoolName":"virtualNetworkPoolName","labSubnetName":"labSubnetName","sharedPublicIpAddressConfiguration":{"allowedPorts":[{"backendPort":0,"transportProtocol":"Tcp"},{"backendPort":0,"transportProtocol":"Tcp"}]}}],"createdDate":"2000-01-23T04:56:07.000+00:00","externalProviderResourceId":"externalProviderResourceId","allowedSubnets":[{"resourceId":"resourceId","allowPublicIp":"Default","labSubnetName":"labSubnetName"},{"resourceId":"resourceId","allowPublicIp":"Default","labSubnetName":"labSubnetName"}],"description":"description","provisioningState":"provisioningState","externalSubnets":[{"name":"name","id":"id"},{"name":"name","id":"id"}],"uniqueIdentifier":"uniqueIdentifier"}}
    params = [('api-version', '2016-05-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/virtualnetworks/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', name='name_example'),
        headers=headers,
        json=virtual_network,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_networks_delete(client):
    """Test case for virtual_networks_delete

    
    """
    params = [('api-version', '2016-05-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/virtualnetworks/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_networks_get(client):
    """Test case for virtual_networks_get

    
    """
    params = [('$expand', 'expand_example'),
                    ('api-version', '2016-05-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/virtualnetworks/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_networks_list(client):
    """Test case for virtual_networks_list

    
    """
    params = [('$expand', 'expand_example'),
                    ('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$orderby', 'orderby_example'),
                    ('api-version', '2016-05-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/virtualnetworks'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_networks_update(client):
    """Test case for virtual_networks_update

    
    """
    virtual_network = {"properties":{"subnetOverrides":[{"useInVmCreationPermission":"Default","resourceId":"resourceId","usePublicIpAddressPermission":"Default","virtualNetworkPoolName":"virtualNetworkPoolName","labSubnetName":"labSubnetName","sharedPublicIpAddressConfiguration":{"allowedPorts":[{"backendPort":0,"transportProtocol":"Tcp"},{"backendPort":0,"transportProtocol":"Tcp"}]}},{"useInVmCreationPermission":"Default","resourceId":"resourceId","usePublicIpAddressPermission":"Default","virtualNetworkPoolName":"virtualNetworkPoolName","labSubnetName":"labSubnetName","sharedPublicIpAddressConfiguration":{"allowedPorts":[{"backendPort":0,"transportProtocol":"Tcp"},{"backendPort":0,"transportProtocol":"Tcp"}]}}],"externalProviderResourceId":"externalProviderResourceId","allowedSubnets":[{"resourceId":"resourceId","allowPublicIp":"Default","labSubnetName":"labSubnetName"},{"resourceId":"resourceId","allowPublicIp":"Default","labSubnetName":"labSubnetName"}],"description":"description","provisioningState":"provisioningState","externalSubnets":[{"name":"name","id":"id"},{"name":"name","id":"id"}],"uniqueIdentifier":"uniqueIdentifier"}}
    params = [('api-version', '2016-05-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/virtualnetworks/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', name='name_example'),
        headers=headers,
        json=virtual_network,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

