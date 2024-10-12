# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.id_provider_auth_domain_info import IdProviderAuthDomainInfo
from openapi_server.models.id_provider_auth_domain_info_update import IdProviderAuthDomainInfoUpdate
from openapi_server.models.id_provider_auth_domain_summary import IdProviderAuthDomainSummary
from openapi_server.models.id_provider_auth_domain_summary_list_response import IdProviderAuthDomainSummaryListResponse


pytestmark = pytest.mark.asyncio

async def test_create_id_provider_auth_domain(client):
    """Test case for create_id_provider_auth_domain

    Add a new IdP authentication domain
    """
    body = {"skewnessInSec":0,"name":"name","metadataXmlBase64":"metadataXmlBase64"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/idp_auth_domain',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_id_provider_auth_domain(client):
    """Test case for delete_id_provider_auth_domain

    Delete an IdP authentication domain for the given ID
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/idp_auth_domain/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_id_provider_auth_domain(client):
    """Test case for get_id_provider_auth_domain

    Get an IdP authentication domain for the given id
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/idp_auth_domain/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_id_provider_auth_domain(client):
    """Test case for query_id_provider_auth_domain

    Get a list of IdP authentication domains
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/idp_auth_domain',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_id_provider_auth_domain(client):
    """Test case for update_id_provider_auth_domain

    Update an existing IdP authentication domain
    """
    body = {"skewnessInSec":0,"name":"name","metadataXmlBase64":"metadataXmlBase64"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/idp_auth_domain/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

