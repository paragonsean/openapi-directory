# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_appliance import CloudAppliance
from openapi_server.models.cloud_appliance_configuration_list import CloudApplianceConfigurationList


pytestmark = pytest.mark.asyncio

async def test_cloud_appliances_list_supported_configurations(client):
    """Test case for cloud_appliances_list_supported_configurations

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorSimple/managers/{manager_name}/cloudApplianceConfigurations'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', manager_name='manager_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloud_appliances_provision(client):
    """Test case for cloud_appliances_provision

    
    """
    parameters = {"vmType":"vmType","vnetRegion":"vnetRegion","name":"name","vmImageName":"vmImageName","storageAccountName":"storageAccountName","modelNumber":"modelNumber","storageAccountType":"storageAccountType","vnetName":"vnetName","isVnetExpressConfigured":True,"isVnetDnsConfigured":True,"subnetName":"subnetName"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorSimple/managers/{manager_name}/provisionCloudAppliance'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', manager_name='manager_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

