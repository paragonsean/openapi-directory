# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.accounts_list400_response import AccountsList400Response
from openapi_server.models.accounts_list401_response import AccountsList401Response
from openapi_server.models.accounts_list403_response import AccountsList403Response
from openapi_server.models.accounts_read404_response import AccountsRead404Response
from openapi_server.models.ip_address import IpAddress
from openapi_server.models.ip_address_request import IpAddressRequest
from openapi_server.models.ip_address_update import IpAddressUpdate
from openapi_server.models.ip_address_update_partial import IpAddressUpdatePartial


pytestmark = pytest.mark.asyncio

async def test_ips_create(client):
    """Test case for ips_create

    
    """
    body = {"valid_not_before":"2000-01-23T04:56:07.000+00:00","consuming_account":"2381982","managing_account":"238189294","address":"23.142.52.0","fqdn":"fqdn","external_ref":"IX:Service:23042","valid_not_after":"2000-01-23T04:56:07.000+00:00","prefix_length":23,"version":4}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/ips',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ips_list(client):
    """Test case for ips_list

    
    """
    params = [('id', ['id1,id2,id3']),
                    ('managing_account', 'managing_account_example'),
                    ('consuming_account', 'consuming_account_example'),
                    ('external_ref', 'external_ref_example'),
                    ('network_service', 'network_service_example'),
                    ('network_service_config', 'network_service_config_example'),
                    ('network_feature', 'network_feature_example'),
                    ('network_feature_config', 'network_feature_config_example'),
                    ('version', 56),
                    ('fqdn', 'fqdn_example'),
                    ('prefix_length', 56),
                    ('valid_not_before', 'valid_not_before_example'),
                    ('valid_not_after', 'valid_not_after_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/ips',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ips_partial_update(client):
    """Test case for ips_partial_update

    
    """
    body = openapi_server.IpAddressUpdatePartial()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v2/ips/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ips_read(client):
    """Test case for ips_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/ips/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ips_update(client):
    """Test case for ips_update

    
    """
    body = {"valid_not_before":"2000-01-23T04:56:07.000+00:00","consuming_account":"2381982","managing_account":"238189294","address":"23.142.52.0","fqdn":"fqdn","external_ref":"IX:Service:23042","valid_not_after":"2000-01-23T04:56:07.000+00:00","prefix_length":23,"version":4}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/ips/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

