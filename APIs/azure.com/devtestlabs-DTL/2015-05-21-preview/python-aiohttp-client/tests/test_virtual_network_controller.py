# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.response_with_continuation_virtual_network import ResponseWithContinuationVirtualNetwork
from openapi_server.models.virtual_network import VirtualNetwork


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_virtual_network_create_or_update_resource(client):
    """Test case for virtual_network_create_or_update_resource

    
    """
    virtual_network = {"name":"name","location":"location","id":"id","type":"type","properties":{"subnetOverrides":[{"useInVmCreationPermission":"Default","resourceId":"resourceId","usePublicIpAddressPermission":"Default","labSubnetName":"labSubnetName"},{"useInVmCreationPermission":"Default","resourceId":"resourceId","usePublicIpAddressPermission":"Default","labSubnetName":"labSubnetName"}],"externalProviderResourceId":"externalProviderResourceId","allowedSubnets":[{"resourceId":"resourceId","allowPublicIp":"Default","labSubnetName":"labSubnetName"},{"resourceId":"resourceId","allowPublicIp":"Default","labSubnetName":"labSubnetName"}],"description":"description","provisioningState":"provisioningState"},"tags":{"key":"tags"}}
    params = [('api-version', '2015-05-21-preview')]
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

async def test_virtual_network_delete_resource(client):
    """Test case for virtual_network_delete_resource

    
    """
    params = [('api-version', '2015-05-21-preview')]
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

async def test_virtual_network_get_resource(client):
    """Test case for virtual_network_get_resource

    
    """
    params = [('api-version', '2015-05-21-preview')]
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

async def test_virtual_network_list(client):
    """Test case for virtual_network_list

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$orderBy', 'order_by_example'),
                    ('api-version', '2015-05-21-preview')]
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

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_virtual_network_patch_resource(client):
    """Test case for virtual_network_patch_resource

    
    """
    virtual_network = {"name":"name","location":"location","id":"id","type":"type","properties":{"subnetOverrides":[{"useInVmCreationPermission":"Default","resourceId":"resourceId","usePublicIpAddressPermission":"Default","labSubnetName":"labSubnetName"},{"useInVmCreationPermission":"Default","resourceId":"resourceId","usePublicIpAddressPermission":"Default","labSubnetName":"labSubnetName"}],"externalProviderResourceId":"externalProviderResourceId","allowedSubnets":[{"resourceId":"resourceId","allowPublicIp":"Default","labSubnetName":"labSubnetName"},{"resourceId":"resourceId","allowPublicIp":"Default","labSubnetName":"labSubnetName"}],"description":"description","provisioningState":"provisioningState"},"tags":{"key":"tags"}}
    params = [('api-version', '2015-05-21-preview')]
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

