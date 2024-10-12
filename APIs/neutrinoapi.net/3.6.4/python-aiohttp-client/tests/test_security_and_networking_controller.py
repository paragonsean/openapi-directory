# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.domain_lookup_response import DomainLookupResponse
from openapi_server.models.email_verify_response import EmailVerifyResponse
from openapi_server.models.host_reputation_response import HostReputationResponse
from openapi_server.models.ip_blocklist_response import IPBlocklistResponse
from openapi_server.models.ip_probe_response import IPProbeResponse


pytestmark = pytest.mark.asyncio

async def test_domain_lookup(client):
    """Test case for domain_lookup

    Domain Lookup
    """
    params = [('host', 'host_example'),
                    ('live', True)]
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
        'user-id': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/domain-lookup',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_email_verify(client):
    """Test case for email_verify

    Email Verify
    """
    params = [('email', 'email_example'),
                    ('fix-typos', False)]
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
        'user-id': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/email-verify',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_host_reputation(client):
    """Test case for host_reputation

    Host Reputation
    """
    params = [('host', 'host_example'),
                    ('list-rating', 3),
                    ('zones', 'zones_example')]
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
        'user-id': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/host-reputation',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_i_p_blocklist(client):
    """Test case for i_p_blocklist

    IP Blocklist
    """
    params = [('ip', 'ip_example'),
                    ('vpn-lookup', False)]
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
        'user-id': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/ip-blocklist',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_i_p_blocklist_download(client):
    """Test case for i_p_blocklist_download

    IP Blocklist Download
    """
    params = [('format', 'csv'),
                    ('include-vpn', False),
                    ('cidr', False),
                    ('ip6', False)]
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
        'user-id': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/ip-blocklist-download',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_i_p_probe(client):
    """Test case for i_p_probe

    IP Probe
    """
    params = [('ip', 'ip_example')]
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
        'user-id': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/ip-probe',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

