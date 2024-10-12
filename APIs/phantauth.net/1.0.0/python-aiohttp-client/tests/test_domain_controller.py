# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.domain_domainname_get200_response import DomainDomainnameGet200Response


pytestmark = pytest.mark.asyncio

async def test_domain_domainname_get(client):
    """Test case for domain_domainname_get

    Get a Domain
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/domain/{domainname}'.format(domainname='domainname_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

