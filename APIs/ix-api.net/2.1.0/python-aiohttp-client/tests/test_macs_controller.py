# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.accounts_list400_response import AccountsList400Response
from openapi_server.models.accounts_list401_response import AccountsList401Response
from openapi_server.models.accounts_list403_response import AccountsList403Response
from openapi_server.models.accounts_read404_response import AccountsRead404Response
from openapi_server.models.contacts_destroy400_response import ContactsDestroy400Response
from openapi_server.models.mac_address import MacAddress
from openapi_server.models.mac_address_request import MacAddressRequest


pytestmark = pytest.mark.asyncio

async def test_macs_create(client):
    """Test case for macs_create

    
    """
    body = {"valid_not_before":"2000-01-23T04:56:07.000+00:00","consuming_account":"2381982","managing_account":"238189294","address":"42:23:bc:8e:b8:b0","external_ref":"IX:Service:23042","valid_not_after":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/macs',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_macs_destroy(client):
    """Test case for macs_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/macs/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_macs_list(client):
    """Test case for macs_list

    
    """
    params = [('id', ['id1,id2,id3']),
                    ('managing_account', 'managing_account_example'),
                    ('consuming_account', 'consuming_account_example'),
                    ('external_ref', 'external_ref_example'),
                    ('network_service_config', 'network_service_config_example'),
                    ('address', 'address_example'),
                    ('assigned_at', 'assigned_at_example'),
                    ('valid_not_before', 'valid_not_before_example'),
                    ('valid_not_after', 'valid_not_after_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/macs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_macs_read(client):
    """Test case for macs_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/macs/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

