# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.peering import Peering
from openapi_server.models.peering_list_result import PeeringListResult
from openapi_server.models.resource_tags import ResourceTags


pytestmark = pytest.mark.asyncio

async def test_peerings_create_or_update(client):
    """Test case for peerings_create_or_update

    
    """
    peering = {"kind":"Direct","location":"location","sku":{"size":"Free","tier":"Basic","name":"Basic_Exchange_Free","family":"Direct"},"properties":{"direct":{"useForPeeringService":True,"peerAsn":{"id":"id"},"connections":[{"provisionedBandwidthInMbps":5,"bandwidthInMbps":0,"connectionState":"None","peeringDBFacilityId":5,"bgpSession":{"peerSessionIPv4Address":"peerSessionIPv4Address","md5AuthenticationKey":"md5AuthenticationKey","microsoftSessionIPv6Address":"microsoftSessionIPv6Address","sessionPrefixV4":"sessionPrefixV4","microsoftSessionIPv4Address":"microsoftSessionIPv4Address","peerSessionIPv6Address":"peerSessionIPv6Address","maxPrefixesAdvertisedV4":6,"sessionStateV6":"None","sessionStateV4":"None","maxPrefixesAdvertisedV6":1,"sessionPrefixV6":"sessionPrefixV6"}},{"provisionedBandwidthInMbps":5,"bandwidthInMbps":0,"connectionState":"None","peeringDBFacilityId":5,"bgpSession":{"peerSessionIPv4Address":"peerSessionIPv4Address","md5AuthenticationKey":"md5AuthenticationKey","microsoftSessionIPv6Address":"microsoftSessionIPv6Address","sessionPrefixV4":"sessionPrefixV4","microsoftSessionIPv4Address":"microsoftSessionIPv4Address","peerSessionIPv6Address":"peerSessionIPv6Address","maxPrefixesAdvertisedV4":6,"sessionStateV6":"None","sessionStateV4":"None","maxPrefixesAdvertisedV6":1,"sessionPrefixV6":"sessionPrefixV6"}}]},"exchange":{"peerAsn":{"id":"id"},"connections":[{"connectionState":"None","peeringDBFacilityId":2,"bgpSession":{"peerSessionIPv4Address":"peerSessionIPv4Address","md5AuthenticationKey":"md5AuthenticationKey","microsoftSessionIPv6Address":"microsoftSessionIPv6Address","sessionPrefixV4":"sessionPrefixV4","microsoftSessionIPv4Address":"microsoftSessionIPv4Address","peerSessionIPv6Address":"peerSessionIPv6Address","maxPrefixesAdvertisedV4":6,"sessionStateV6":"None","sessionStateV4":"None","maxPrefixesAdvertisedV6":1,"sessionPrefixV6":"sessionPrefixV6"}},{"connectionState":"None","peeringDBFacilityId":2,"bgpSession":{"peerSessionIPv4Address":"peerSessionIPv4Address","md5AuthenticationKey":"md5AuthenticationKey","microsoftSessionIPv6Address":"microsoftSessionIPv6Address","sessionPrefixV4":"sessionPrefixV4","microsoftSessionIPv4Address":"microsoftSessionIPv4Address","peerSessionIPv6Address":"peerSessionIPv6Address","maxPrefixesAdvertisedV4":6,"sessionStateV6":"None","sessionStateV4":"None","maxPrefixesAdvertisedV6":1,"sessionPrefixV6":"sessionPrefixV6"}}]},"provisioningState":"Succeeded","peeringLocation":"peeringLocation"},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Peering/peerings/{peering_name}'.format(resource_group_name='resource_group_name_example', peering_name='peering_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=peering,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_peerings_delete(client):
    """Test case for peerings_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Peering/peerings/{peering_name}'.format(resource_group_name='resource_group_name_example', peering_name='peering_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_peerings_get(client):
    """Test case for peerings_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Peering/peerings/{peering_name}'.format(resource_group_name='resource_group_name_example', peering_name='peering_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_peerings_list_by_resource_group(client):
    """Test case for peerings_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Peering/peerings'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_peerings_list_by_subscription(client):
    """Test case for peerings_list_by_subscription

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Peering/peerings'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_peerings_update(client):
    """Test case for peerings_update

    
    """
    tags = {"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Peering/peerings/{peering_name}'.format(resource_group_name='resource_group_name_example', peering_name='peering_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=tags,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

