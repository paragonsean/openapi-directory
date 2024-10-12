# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_ip_access_control_list_response import ListIpAccessControlListResponse
from openapi_server.models.trunking_v1_trunk_ip_access_control_list import TrunkingV1TrunkIpAccessControlList


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_ip_access_control_list(client):
    """Test case for create_ip_access_control_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'ip_access_control_list_sid': 'ip_access_control_list_sid_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Trunks/{trunk_sid}/IpAccessControlLists'.format(trunk_sid='trunk_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_ip_access_control_list(client):
    """Test case for delete_ip_access_control_list

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Trunks/{trunk_sid}/IpAccessControlLists/{sid}'.format(trunk_sid='trunk_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_ip_access_control_list(client):
    """Test case for fetch_ip_access_control_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Trunks/{trunk_sid}/IpAccessControlLists/{sid}'.format(trunk_sid='trunk_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_ip_access_control_list(client):
    """Test case for list_ip_access_control_list

    
    """
    params = [('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Trunks/{trunk_sid}/IpAccessControlLists'.format(trunk_sid='trunk_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

