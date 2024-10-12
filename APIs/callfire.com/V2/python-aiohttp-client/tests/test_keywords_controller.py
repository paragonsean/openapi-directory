# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.keyword_config import KeywordConfig
from openapi_server.models.keyword_lease import KeywordLease
from openapi_server.models.keyword_lease_page import KeywordLeasePage
from openapi_server.models.keyword_list import KeywordList
from openapi_server.models.page import Page


pytestmark = pytest.mark.asyncio

async def test_find_keyword_lease_configs(client):
    """Test case for find_keyword_lease_configs

    Find keyword lease configs
    """
    params = [('limit', 20),
                    ('offset', 0),
                    ('filter', 'filter_example'),
                    ('labelName', 'label_name_example'),
                    ('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/keywords/leases/configs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_keyword_leases(client):
    """Test case for find_keyword_leases

    Find keyword leases
    """
    params = [('limit', 100),
                    ('offset', 0),
                    ('filter', 'filter_example'),
                    ('labelName', 'label_name_example'),
                    ('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/keywords/leases',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_keywords(client):
    """Test case for find_keywords

    Find keywords
    """
    params = [('keywords', ['keywords_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/keywords',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_keyword_lease(client):
    """Test case for get_keyword_lease

    Find a specific lease
    """
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/keywords/leases/{keyword}'.format(keyword='keyword_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_keyword_lease_by_id(client):
    """Test case for get_keyword_lease_by_id

    Find a keyword by id
    """
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/keywords/leases/id/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_keyword_lease_config(client):
    """Test case for get_keyword_lease_config

    Find a specific keyword lease config
    """
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/keywords/leases/configs/{keyword}'.format(keyword='keyword_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_is_keyword_available(client):
    """Test case for is_keyword_available

    Check for a specific keyword
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/keywords/{keyword}/available'.format(keyword='keyword_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_keyword_lease(client):
    """Test case for update_keyword_lease

    Update a lease
    """
    body = {"number":"number","contactListId":5,"optInConfirmationMessage":"optInConfirmationMessage","autoRenew":True,"doubleOptInEnabled":True,"leaseBegin":5,"keyword":"keyword","leaseEnd":2,"type":"PLAN","shortCode":"shortCode","labels":["labels","labels"],"status":"PENDING"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/v2/keywords/leases/{keyword}'.format(keyword='keyword_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_keyword_lease_config(client):
    """Test case for update_keyword_lease_config

    Update a keyword lease config
    """
    body = {"keyword":"keyword","textInboundConfig":{"forwardNumber":"forwardNumber","forwardEnabled":True}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/v2/keywords/leases/configs/{keyword}'.format(keyword='keyword_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

