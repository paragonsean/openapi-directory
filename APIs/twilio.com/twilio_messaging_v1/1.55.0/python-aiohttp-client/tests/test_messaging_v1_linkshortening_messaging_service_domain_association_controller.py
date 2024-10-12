# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.messaging_v1_linkshortening_messaging_service_domain_association import MessagingV1LinkshorteningMessagingServiceDomainAssociation


pytestmark = pytest.mark.asyncio

async def test_fetch_linkshortening_messaging_service_domain_association(client):
    """Test case for fetch_linkshortening_messaging_service_domain_association

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/LinkShortening/MessagingServices/{messaging_service_sid}/Domain'.format(messaging_service_sid='messaging_service_sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

