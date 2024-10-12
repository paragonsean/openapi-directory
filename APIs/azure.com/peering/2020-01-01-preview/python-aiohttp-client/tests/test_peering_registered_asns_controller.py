# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.peering_registered_asn import PeeringRegisteredAsn
from openapi_server.models.peering_registered_asn_list_result import PeeringRegisteredAsnListResult


pytestmark = pytest.mark.asyncio

async def test_registered_asns_create_or_update(client):
    """Test case for registered_asns_create_or_update

    
    """
    registered_asn = {"properties":{"peeringServicePrefixKey":"peeringServicePrefixKey","provisioningState":"Succeeded","asn":0}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Peering/peerings/{peering_name}/registeredAsns/{registered_asn_name}'.format(resource_group_name='resource_group_name_example', peering_name='peering_name_example', registered_asn_name='registered_asn_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=registered_asn,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registered_asns_delete(client):
    """Test case for registered_asns_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Peering/peerings/{peering_name}/registeredAsns/{registered_asn_name}'.format(resource_group_name='resource_group_name_example', peering_name='peering_name_example', registered_asn_name='registered_asn_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registered_asns_get(client):
    """Test case for registered_asns_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Peering/peerings/{peering_name}/registeredAsns/{registered_asn_name}'.format(resource_group_name='resource_group_name_example', peering_name='peering_name_example', registered_asn_name='registered_asn_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registered_asns_list_by_peering(client):
    """Test case for registered_asns_list_by_peering

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Peering/peerings/{peering_name}/registeredAsns'.format(resource_group_name='resource_group_name_example', peering_name='peering_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

