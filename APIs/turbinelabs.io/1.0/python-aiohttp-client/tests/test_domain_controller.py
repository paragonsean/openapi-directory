# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.domain_create import DomainCreate
from openapi_server.models.domain_result import DomainResult
from openapi_server.models.error import Error
from openapi_server.models.multi_domain_result import MultiDomainResult


pytestmark = pytest.mark.asyncio

async def test_domain_domain_key_delete(client):
    """Test case for domain_domain_key_delete

    delete domain
    """
    params = [('checksum', '9cd24183-f848-48f8-6f55-0f07240700b9')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1.0/domain/{domain_key}'.format(domain_key='48cf1c9b-f027-4223-b405-d48018ffb900'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_domain_domain_key_get(client):
    """Test case for domain_domain_key_get

    get domain
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.0/domain/{domain_key}'.format(domain_key='48cf1c9b-f027-4223-b405-d48018ffb900'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_domain_get(client):
    """Test case for domain_get

    get domains
    """
    params = [('filters', 'filters_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.0/domain',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_domain_post(client):
    """Test case for domain_post

    create domain
    """
    domain = {"force_https":True,"aliases":["aliases","aliases"],"domain_key":"domain_key","port":0,"redirects":[{"header_constraints":[{"invert":True,"case_sensitive":True,"name":"name","value":"value"},{"invert":True,"case_sensitive":True,"name":"name","value":"value"}],"name":"name","from":"from","to":"to","redirect_type":"permanent"},{"header_constraints":[{"invert":True,"case_sensitive":True,"name":"name","value":"value"},{"invert":True,"case_sensitive":True,"name":"name","value":"value"}],"name":"name","from":"from","to":"to","redirect_type":"permanent"}],"checksum":"checksum","name":"name","zone_key":"zone_key","gzip_enabled":True,"cors_config":{"max_age":0,"allowed_methods":["allowed_methods","allowed_methods"],"allowed_headers":["allowed_headers","allowed_headers"],"allow_credentials":True,"exposed_headers":["exposed_headers","exposed_headers"],"allowed_origins":["allowed_origins","allowed_origins"]},"ssl_config":{"cert_key_pairs":[{"certificate_path":"certificate_path","key_path":"key_path"},{"certificate_path":"certificate_path","key_path":"key_path"}],"cipher_filter":"cipher_filter","protocols":["protocols","protocols"]}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.0/domain',
        headers=headers,
        json=domain,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

