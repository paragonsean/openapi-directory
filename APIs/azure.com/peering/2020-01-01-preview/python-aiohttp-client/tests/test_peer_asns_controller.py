# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.peer_asn import PeerAsn
from openapi_server.models.peer_asn_list_result import PeerAsnListResult


pytestmark = pytest.mark.asyncio

async def test_peer_asns_create_or_update(client):
    """Test case for peer_asns_create_or_update

    
    """
    peer_asn = {"properties":{"peerName":"peerName","errorMessage":"errorMessage","peerContactDetail":[{"role":"Noc","phone":"phone","email":"email"},{"role":"Noc","phone":"phone","email":"email"}],"peerAsn":0,"validationState":"None"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Peering/peerAsns/{peer_asn_name}'.format(peer_asn_name='peer_asn_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=peer_asn,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_peer_asns_delete(client):
    """Test case for peer_asns_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Peering/peerAsns/{peer_asn_name}'.format(peer_asn_name='peer_asn_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_peer_asns_get(client):
    """Test case for peer_asns_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Peering/peerAsns/{peer_asn_name}'.format(peer_asn_name='peer_asn_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_peer_asns_list_by_subscription(client):
    """Test case for peer_asns_list_by_subscription

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Peering/peerAsns'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

