# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.dns_record import DnsRecord
from openapi_server.models.dns_record_create import DnsRecordCreate
from openapi_server.models.dns_zone import DnsZone
from openapi_server.models.dns_zone_setup import DnsZoneSetup
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_configure_dns_for_site(client):
    """Test case for configure_dns_for_site

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/sites/{site_id}/dns'.format(site_id='site_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_dns_record(client):
    """Test case for create_dns_record

    
    """
    dns_record = openapi_server.DnsRecordCreate()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/dns_zones/{zone_id}/dns_records'.format(zone_id='zone_id_example'),
        headers=headers,
        json=dns_record,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_dns_zone(client):
    """Test case for create_dns_zone

    
    """
    dns_zone_params = openapi_server.DnsZoneSetup()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/dns_zones',
        headers=headers,
        json=dns_zone_params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_dns_record(client):
    """Test case for delete_dns_record

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/dns_zones/{zone_id}/dns_records/{dns_record_id}'.format(zone_id='zone_id_example', dns_record_id='dns_record_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_dns_zone(client):
    """Test case for delete_dns_zone

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/dns_zones/{zone_id}'.format(zone_id='zone_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dns_for_site(client):
    """Test case for get_dns_for_site

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/sites/{site_id}/dns'.format(site_id='site_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dns_records(client):
    """Test case for get_dns_records

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/dns_zones/{zone_id}/dns_records'.format(zone_id='zone_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dns_zone(client):
    """Test case for get_dns_zone

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/dns_zones/{zone_id}'.format(zone_id='zone_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dns_zones(client):
    """Test case for get_dns_zones

    
    """
    params = [('account_slug', 'account_slug_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/dns_zones',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_individual_dns_record(client):
    """Test case for get_individual_dns_record

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/dns_zones/{zone_id}/dns_records/{dns_record_id}'.format(zone_id='zone_id_example', dns_record_id='dns_record_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transfer_dns_zone(client):
    """Test case for transfer_dns_zone

    
    """
    params = [('account_id', 'account_id_example'),
                    ('transfer_account_id', 'transfer_account_id_example'),
                    ('transfer_user_id', 'transfer_user_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/dns_zones/{zone_id}/transfer'.format(zone_id='zone_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

