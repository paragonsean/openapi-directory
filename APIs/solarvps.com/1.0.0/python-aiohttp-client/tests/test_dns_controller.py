# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_dns_domain_add_post(client):
    """Test case for dns_domain_add_post

    Add dns record for given domain
    """
    params = [('name', 'name_example'),
                    ('type', 'type_example'),
                    ('content', 'content_example'),
                    ('ttl', 'ttl_example'),
                    ('prio', 'prio_example')]
    headers = { 
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/dns/{domain}/add'.format(domain='domain_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dns_domain_delete_post(client):
    """Test case for dns_domain_delete_post

    Delete dns record for a given domain
    """
    params = [('id', 'id_example')]
    headers = { 
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/dns/{domain}/delete'.format(domain='domain_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dns_domain_get(client):
    """Test case for dns_domain_get

    View all your records for a given domain
    """
    headers = { 
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/dns/{domain}'.format(domain='domain_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dns_domain_update_post(client):
    """Test case for dns_domain_update_post

    Update dns record for a given domain
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('type', 'type_example'),
                    ('content', 'content_example'),
                    ('ttl', 'ttl_example'),
                    ('prio', 'prio_example')]
    headers = { 
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/dns/{domain}/update'.format(domain='domain_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

