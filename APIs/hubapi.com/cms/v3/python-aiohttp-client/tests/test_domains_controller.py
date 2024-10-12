# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.collection_response_with_total_domain_forward_paging import CollectionResponseWithTotalDomainForwardPaging
from openapi_server.models.domain import Domain
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_get_cms_v3_domains_domain_id_get_by_id(client):
    """Test case for get_cms_v3_domains_domain_id_get_by_id

    Get a single domain
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'private_apps_legacy': 'special-key',
        'Authorization': 'Bearer special-key',
        'private_apps': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/cms/v3/domains/{domain_id}'.format(domain_id='domain_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cms_v3_domains_get_page(client):
    """Test case for get_cms_v3_domains_get_page

    Get current domains
    """
    params = [('createdAt', '2013-10-20T19:20:30+01:00'),
                    ('createdAfter', '2013-10-20T19:20:30+01:00'),
                    ('createdBefore', '2013-10-20T19:20:30+01:00'),
                    ('updatedAt', '2013-10-20T19:20:30+01:00'),
                    ('updatedAfter', '2013-10-20T19:20:30+01:00'),
                    ('updatedBefore', '2013-10-20T19:20:30+01:00'),
                    ('sort', ['sort_example']),
                    ('after', 'after_example'),
                    ('limit', 56),
                    ('archived', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'private_apps_legacy': 'special-key',
        'Authorization': 'Bearer special-key',
        'private_apps': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/cms/v3/domains/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

