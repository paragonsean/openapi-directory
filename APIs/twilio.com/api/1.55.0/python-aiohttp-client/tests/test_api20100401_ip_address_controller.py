# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_v2010_account_sip_sip_ip_access_control_list_sip_ip_address import ApiV2010AccountSipSipIpAccessControlListSipIpAddress
from openapi_server.models.list_sip_ip_address_response import ListSipIpAddressResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_sip_ip_address(client):
    """Test case for create_sip_ip_address

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'cidr_prefix_length': 56,
        'friendly_name': 'friendly_name_example',
        'ip_address': 'ip_address_example'
        }
    response = await client.request(
        method='POST',
        path='/2010-04-01/Accounts/{account_sid}/SIP/IpAccessControlLists/{ip_access_control_list_sid}/IpAddresses.json'.format(account_sid='account_sid_example', ip_access_control_list_sid='ip_access_control_list_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_sip_ip_address(client):
    """Test case for delete_sip_ip_address

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/2010-04-01/Accounts/{account_sid}/SIP/IpAccessControlLists/{ip_access_control_list_sid}/IpAddresses/{sid_jso}'.format(account_sid='account_sid_example', ip_access_control_list_sid='ip_access_control_list_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_sip_ip_address(client):
    """Test case for fetch_sip_ip_address

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/2010-04-01/Accounts/{account_sid}/SIP/IpAccessControlLists/{ip_access_control_list_sid}/IpAddresses/{sid_jso}'.format(account_sid='account_sid_example', ip_access_control_list_sid='ip_access_control_list_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_sip_ip_address(client):
    """Test case for list_sip_ip_address

    
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
        path='/2010-04-01/Accounts/{account_sid}/SIP/IpAccessControlLists/{ip_access_control_list_sid}/IpAddresses.json'.format(account_sid='account_sid_example', ip_access_control_list_sid='ip_access_control_list_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_sip_ip_address(client):
    """Test case for update_sip_ip_address

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'cidr_prefix_length': 56,
        'friendly_name': 'friendly_name_example',
        'ip_address': 'ip_address_example'
        }
    response = await client.request(
        method='POST',
        path='/2010-04-01/Accounts/{account_sid}/SIP/IpAccessControlLists/{ip_access_control_list_sid}/IpAddresses/{sid_jso}'.format(account_sid='account_sid_example', ip_access_control_list_sid='ip_access_control_list_sid_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

