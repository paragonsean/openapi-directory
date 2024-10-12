# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.messaging_v1_linkshortening_messaging_service import MessagingV1LinkshorteningMessagingService


pytestmark = pytest.mark.asyncio

async def test_create_linkshortening_messaging_service(client):
    """Test case for create_linkshortening_messaging_service

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v1/LinkShortening/Domains/{domain_sid}/MessagingServices/{messaging_service_sid}'.format(domain_sid='domain_sid_example', messaging_service_sid='messaging_service_sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_linkshortening_messaging_service(client):
    """Test case for delete_linkshortening_messaging_service

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/LinkShortening/Domains/{domain_sid}/MessagingServices/{messaging_service_sid}'.format(domain_sid='domain_sid_example', messaging_service_sid='messaging_service_sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

