# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.messaging_v1_domain_config import MessagingV1DomainConfig


pytestmark = pytest.mark.asyncio

async def test_fetch_domain_config(client):
    """Test case for fetch_domain_config

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/LinkShortening/Domains/{domain_sid}/Config'.format(domain_sid='domain_sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_domain_config(client):
    """Test case for update_domain_config

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'callback_url': 'callback_url_example',
        'continue_on_failure': True,
        'disable_https': True,
        'fallback_url': 'fallback_url_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/LinkShortening/Domains/{domain_sid}/Config'.format(domain_sid='domain_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

