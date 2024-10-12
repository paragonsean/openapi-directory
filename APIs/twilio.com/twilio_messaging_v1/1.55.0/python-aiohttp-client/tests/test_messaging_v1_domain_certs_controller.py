# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.messaging_v1_domain_cert_v4 import MessagingV1DomainCertV4


pytestmark = pytest.mark.asyncio

async def test_delete_domain_cert_v4(client):
    """Test case for delete_domain_cert_v4

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/LinkShortening/Domains/{domain_sid}/Certificate'.format(domain_sid='domain_sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_domain_cert_v4(client):
    """Test case for fetch_domain_cert_v4

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/LinkShortening/Domains/{domain_sid}/Certificate'.format(domain_sid='domain_sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_domain_cert_v4(client):
    """Test case for update_domain_cert_v4

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'tls_cert': 'tls_cert_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/LinkShortening/Domains/{domain_sid}/Certificate'.format(domain_sid='domain_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

