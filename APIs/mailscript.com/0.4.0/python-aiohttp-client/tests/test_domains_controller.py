# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_domain_request import AddDomainRequest
from openapi_server.models.check_domain_verify import CheckDomainVerify
from openapi_server.models.domain_response import DomainResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.get_all_domains_response import GetAllDomainsResponse


pytestmark = pytest.mark.asyncio

async def test_add_domain(client):
    """Test case for add_domain

    Claim a new Domain
    """
    body = {"domain":"domain"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/domains',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_check_domain_verify(client):
    """Test case for check_domain_verify

    Check a new Domain
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/domains/verify/{domain}'.format(domain='domain_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_domains(client):
    """Test case for get_all_domains

    Get all domains you have access to
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/domains',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_domain_verify(client):
    """Test case for get_domain_verify

    Get domain verification
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/domains/verify/{domain}'.format(domain='domain_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_domain_verify(client):
    """Test case for remove_domain_verify

    Remove a domain
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/domains/{domain}'.format(domain='domain_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

