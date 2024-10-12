# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.agent_secondary_certificate_info import AgentSecondaryCertificateInfo
from openapi_server.models.agent_secondary_certificate_info_list_response import AgentSecondaryCertificateInfoListResponse


pytestmark = pytest.mark.asyncio

async def test_mark_agent_secondary_certificate(client):
    """Test case for mark_agent_secondary_certificate

    Mark a certificate to be added to agents
    """
    body = 'body_example'
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/certificate/agent',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_agent_secondary_certificate(client):
    """Test case for query_agent_secondary_certificate

    Get all potential agent secondary cluster certificates
    """
    params = [('is_agent_enabled', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/certificate/agent',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unmark_agent_secondary_certificate(client):
    """Test case for unmark_agent_secondary_certificate

    Unmark a certificate that was previously marked
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/certificate/agent/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

