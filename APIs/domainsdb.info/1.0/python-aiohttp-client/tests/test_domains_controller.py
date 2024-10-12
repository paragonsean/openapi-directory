# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.search_results import SearchResults
from openapi_server.models.update_model import UpdateModel


pytestmark = pytest.mark.asyncio

async def test_domains_tld_zone_id_download_get(client):
    """Test case for domains_tld_zone_id_download_get

    Download Whole Dataset for TLD
    """
    params = [('api_key', 'api_key_example'),
                    ('date', '_date_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v1/domains/tld/{zone_id}/download'.format(zone_id='zone_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_domains_tld_zone_id_search_get(client):
    """Test case for domains_tld_zone_id_search_get

    Domains Search for TLD
    """
    params = [('api_key', 'api_key_example'),
                    ('date', '_date_example'),
                    ('page', 'page_example'),
                    ('limit', 50),
                    ('domain', 'domain_example'),
                    ('country', 'country_example'),
                    ('isDead', True),
                    ('A', 'a_example'),
                    ('NS', 'ns_example'),
                    ('CNAME', 'cname_example'),
                    ('MX', 'mx_example'),
                    ('TXT', 'txt_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/domains/tld/{zone_id}/search'.format(zone_id='zone_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_domains_updates_added_download_get(client):
    """Test case for domains_updates_added_download_get

    Download added domains, latest if date not specified
    """
    params = [('api_key', 'api_key_example'),
                    ('date', '_date_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v1/domains/updates/added/download',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_domains_updates_added_get(client):
    """Test case for domains_updates_added_get

    Get added domains, latest if date not specified
    """
    params = [('api_key', 'api_key_example'),
                    ('date', '_date_example'),
                    ('page', 'page_example'),
                    ('limit', 50)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/domains/updates/added',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_domains_updates_deleted_download_get(client):
    """Test case for domains_updates_deleted_download_get

    Download deleted domains, latest if date not specified
    """
    params = [('api_key', 'api_key_example'),
                    ('date', '_date_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v1/domains/updates/deleted/download',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_domains_updates_deleted_get(client):
    """Test case for domains_updates_deleted_get

    Get deleted domains, latest if date not specified
    """
    params = [('api_key', 'api_key_example'),
                    ('date', '_date_example'),
                    ('page', 'page_example'),
                    ('limit', 50)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/domains/updates/deleted',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_domains_updates_list_get(client):
    """Test case for domains_updates_list_get

    List of updates
    """
    params = [('api_key', 'api_key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/domains/updates/list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_search_domain_item(client):
    """Test case for get_search_domain_item

    Domains Database Search
    """
    params = [('api_key', 'api_key_example'),
                    ('date', '_date_example'),
                    ('page', 'page_example'),
                    ('limit', 50),
                    ('domain', 'domain_example'),
                    ('zone', 'zone_example'),
                    ('country', 'country_example'),
                    ('isDead', True),
                    ('A', 'a_example'),
                    ('NS', 'ns_example'),
                    ('CNAME', 'cname_example'),
                    ('MX', 'mx_example'),
                    ('TXT', 'txt_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/domains/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tld_domain_item(client):
    """Test case for get_tld_domain_item

    Get TLD records
    """
    params = [('api_key', 'api_key_example'),
                    ('date', '_date_example'),
                    ('page', 'page_example'),
                    ('limit', 50),
                    ('domain', 'domain_example'),
                    ('country', 'country_example'),
                    ('isDead', True),
                    ('A', 'a_example'),
                    ('NS', 'ns_example'),
                    ('CNAME', 'cname_example'),
                    ('MX', 'mx_example'),
                    ('TXT', 'txt_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/domains/tld/{zone_id}'.format(zone_id='zone_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

