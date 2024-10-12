# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.express_route_port import ExpressRoutePort
from openapi_server.models.express_route_port_list_result import ExpressRoutePortListResult
from openapi_server.models.express_route_ports_update_tags_request import ExpressRoutePortsUpdateTagsRequest


pytestmark = pytest.mark.asyncio

async def test_express_route_ports_create_or_update(client):
    """Test case for express_route_ports_create_or_update

    
    """
    parameters = {"identity":"{}","etag":"etag","properties":{"allocationDate":"allocationDate","bandwidthInGbps":0,"encapsulation":"Dot1Q","resourceGuid":"resourceGuid","provisionedBandwidthInGbps":6.027456183070403,"etherType":"etherType","links":[{"name":"name","etag":"etag","properties":{"macSecConfig":{"cipher":"gcm-aes-128","cakSecretIdentifier":"cakSecretIdentifier","cknSecretIdentifier":"cknSecretIdentifier"},"connectorType":"LC","routerName":"routerName","adminState":"Enabled","patchPanelId":"patchPanelId","interfaceName":"interfaceName","provisioningState":"Succeeded","rackId":"rackId"}},{"name":"name","etag":"etag","properties":{"macSecConfig":{"cipher":"gcm-aes-128","cakSecretIdentifier":"cakSecretIdentifier","cknSecretIdentifier":"cknSecretIdentifier"},"connectorType":"LC","routerName":"routerName","adminState":"Enabled","patchPanelId":"patchPanelId","interfaceName":"interfaceName","provisioningState":"Succeeded","rackId":"rackId"}}],"provisioningState":"Succeeded","circuits":[{"id":"id"},{"id":"id"}],"mtu":"mtu","peeringLocation":"peeringLocation"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/ExpressRoutePorts/{express_route_port_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', express_route_port_name='express_route_port_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_express_route_ports_delete(client):
    """Test case for express_route_ports_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/ExpressRoutePorts/{express_route_port_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', express_route_port_name='express_route_port_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_express_route_ports_get(client):
    """Test case for express_route_ports_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/ExpressRoutePorts/{express_route_port_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', express_route_port_name='express_route_port_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_express_route_ports_list(client):
    """Test case for express_route_ports_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network/ExpressRoutePorts'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_express_route_ports_list_by_resource_group(client):
    """Test case for express_route_ports_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/ExpressRoutePorts'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_express_route_ports_update_tags(client):
    """Test case for express_route_ports_update_tags

    
    """
    parameters = openapi_server.ExpressRoutePortsUpdateTagsRequest()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/ExpressRoutePorts/{express_route_port_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', express_route_port_name='express_route_port_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

