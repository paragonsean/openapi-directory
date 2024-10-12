# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_bucket_response import ListBucketResponse
from openapi_server.models.verify_v2_service_rate_limit_bucket import VerifyV2ServiceRateLimitBucket


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_bucket(client):
    """Test case for create_bucket

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'interval': 56,
        'max': 56
        }
    response = await client.request(
        method='POST',
        path='/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets'.format(service_sid='service_sid_example', rate_limit_sid='rate_limit_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_bucket(client):
    """Test case for delete_bucket

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets/{sid}'.format(service_sid='service_sid_example', rate_limit_sid='rate_limit_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_bucket(client):
    """Test case for fetch_bucket

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets/{sid}'.format(service_sid='service_sid_example', rate_limit_sid='rate_limit_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_bucket(client):
    """Test case for list_bucket

    
    """
    params = [('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets'.format(service_sid='service_sid_example', rate_limit_sid='rate_limit_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_bucket(client):
    """Test case for update_bucket

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'interval': 56,
        'max': 56
        }
    response = await client.request(
        method='POST',
        path='/v2/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets/{sid}'.format(service_sid='service_sid_example', rate_limit_sid='rate_limit_sid_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

