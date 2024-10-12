# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_trunk_response import ListTrunkResponse
from openapi_server.models.trunk_enum_transfer_caller_id import TrunkEnumTransferCallerId
from openapi_server.models.trunk_enum_transfer_setting import TrunkEnumTransferSetting
from openapi_server.models.trunking_v1_trunk import TrunkingV1Trunk


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_trunk(client):
    """Test case for create_trunk

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'cnam_lookup_enabled': True,
        'disaster_recovery_method': 'disaster_recovery_method_example',
        'disaster_recovery_url': 'disaster_recovery_url_example',
        'domain_name': 'domain_name_example',
        'friendly_name': 'friendly_name_example',
        'secure': True,
        'transfer_caller_id': openapi_server.TrunkEnumTransferCallerId(),
        'transfer_mode': openapi_server.TrunkEnumTransferSetting()
        }
    response = await client.request(
        method='POST',
        path='/v1/Trunks',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_trunk(client):
    """Test case for delete_trunk

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Trunks/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_trunk(client):
    """Test case for fetch_trunk

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Trunks/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_trunk(client):
    """Test case for list_trunk

    
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
        path='/v1/Trunks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_trunk(client):
    """Test case for update_trunk

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'cnam_lookup_enabled': True,
        'disaster_recovery_method': 'disaster_recovery_method_example',
        'disaster_recovery_url': 'disaster_recovery_url_example',
        'domain_name': 'domain_name_example',
        'friendly_name': 'friendly_name_example',
        'secure': True,
        'transfer_caller_id': openapi_server.TrunkEnumTransferCallerId(),
        'transfer_mode': openapi_server.TrunkEnumTransferSetting()
        }
    response = await client.request(
        method='POST',
        path='/v1/Trunks/{sid}'.format(sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

