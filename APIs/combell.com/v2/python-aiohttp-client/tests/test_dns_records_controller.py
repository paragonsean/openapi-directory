# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.dns_record import DnsRecord


pytestmark = pytest.mark.asyncio

async def test_dns_domain_name_records_get(client):
    """Test case for dns_domain_name_records_get

    Get records
    """
    params = [('domain_name', 'domain_name_example'),
                    ('skip', 56),
                    ('take', 56),
                    ('type', 'type_example'),
                    ('record_name', 'record_name_example'),
                    ('service', 'service_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/dns/{domain_name}/records'.format(domain_name2='domain_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dns_domain_name_records_post(client):
    """Test case for dns_domain_name_records_post

    Create a record
    """
    body = {"protocol":"TCP","port":0,"service":"service","weight":5,"record_name":"record_name","id":"id","priority":6,"type":"type","ttl":1,"content":"content","target":"target"}
    params = [('domain_name', 'domain_name_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/dns/{domain_name}/records'.format(domain_name2='domain_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dns_domain_name_records_record_id_delete(client):
    """Test case for dns_domain_name_records_record_id_delete

    Delete a record
    """
    params = [('domain_name', 'domain_name_example'),
                    ('record_id', 'record_id_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/dns/{domain_name}/records/{record_id}'.format(domain_name2='domain_name_example', record_id2='record_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dns_domain_name_records_record_id_get(client):
    """Test case for dns_domain_name_records_record_id_get

    Get specific record
    """
    params = [('domain_name', 'domain_name_example'),
                    ('record_id', 'record_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/dns/{domain_name}/records/{record_id}'.format(domain_name2='domain_name_example', record_id2='record_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dns_domain_name_records_record_id_put(client):
    """Test case for dns_domain_name_records_record_id_put

    Edit a record
    """
    body = {"protocol":"TCP","port":0,"service":"service","weight":5,"record_name":"record_name","id":"id","priority":6,"type":"type","ttl":1,"content":"content","target":"target"}
    params = [('domain_name', 'domain_name_example'),
                    ('record_id', 'record_id_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/dns/{domain_name}/records/{record_id}'.format(domain_name2='domain_name_example', record_id2='record_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

