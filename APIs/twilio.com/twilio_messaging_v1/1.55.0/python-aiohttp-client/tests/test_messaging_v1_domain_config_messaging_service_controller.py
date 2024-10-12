# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.messaging_v1_domain_config_messaging_service import MessagingV1DomainConfigMessagingService


pytestmark = pytest.mark.asyncio

async def test_fetch_domain_config_messaging_service(client):
    """Test case for fetch_domain_config_messaging_service

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/LinkShortening/MessagingService/{messaging_service_sid}/DomainConfig'.format(messaging_service_sid='messaging_service_sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

