# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_from_json_scale_unit_parameters_list import CreateFromJsonScaleUnitParametersList
from openapi_server.models.scale_out_scale_unit_parameters_list import ScaleOutScaleUnitParametersList
from openapi_server.models.scale_unit import ScaleUnit
from openapi_server.models.scale_unit_list import ScaleUnitList


pytestmark = pytest.mark.asyncio

async def test_scale_units_create_from_json(client):
    """Test case for scale_units_create_from_json

    
    """
    creation_data = {"clusterName":"clusterName","storageNetwork":{"subnet":["subnet","subnet"],"vlanId":["vlanId","vlanId"]},"torSwitchBgpAsn":"torSwitchBgpAsn","torSwitchBgpPeerIp":["torSwitchBgpPeerIp","torSwitchBgpPeerIp"],"physicalNodes":[{"name":"name","bmcIpAddress":"bmcIpAddress"},{"name":"name","bmcIpAddress":"bmcIpAddress"}],"netQosPriority":0,"softwareBgpAsn":"softwareBgpAsn","infrastructureNetwork":{"subnet":["subnet","subnet"],"vlanId":["vlanId","vlanId"]}}
    params = [('api-version', '2016-05-01')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/scaleUnits/{scale_unit}/createFromJson'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', location='location_example', scale_unit='scale_unit_example'),
        headers=headers,
        json=creation_data,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_scale_units_get(client):
    """Test case for scale_units_get

    
    """
    params = [('api-version', '2016-05-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/scaleUnits/{scale_unit}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', location='location_example', scale_unit='scale_unit_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_scale_units_list(client):
    """Test case for scale_units_list

    
    """
    params = [('api-version', '2016-05-01'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/scaleUnits'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', location='location_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_scale_units_scale_out(client):
    """Test case for scale_units_scale_out

    
    """
    scale_unit_node_parameters = {"awaitStorageConvergence":True,"nodeList":[{"bmcIpv4Address":"bmcIpv4Address","computerName":"computerName"},{"bmcIpv4Address":"bmcIpv4Address","computerName":"computerName"}]}
    params = [('api-version', '2016-05-01')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/scaleUnits/{scale_unit}/scaleOut'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', location='location_example', scale_unit='scale_unit_example'),
        headers=headers,
        json=scale_unit_node_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

