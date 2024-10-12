# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.containers_quota_info import ContainersQuotaInfo
from openapi_server.models.containers_quota_list import ContainersQuotaList
from openapi_server.models.containers_usage_info import ContainersUsageInfo


pytestmark = pytest.mark.asyncio

async def test_containers_quota_get(client):
    """Test case for containers_quota_get

    Retrieve organization and space specific quota
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'x_auth_token_example',
        'x_auth_project_id': 'x_auth_project_id_example',
    }
    response = await client.request(
        method='GET',
        path='/v3/containers/quota',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containers_quota_put(client):
    """Test case for containers_quota_put

    Update space quota
    """
    body = {"floating_ips":0,"ram":6}
    headers = { 
        'Content-Type': 'application/json',
        'x_auth_token': 'x_auth_token_example',
        'x_auth_project_id': 'x_auth_project_id_example',
    }
    response = await client.request(
        method='PUT',
        path='/v3/containers/quota',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containers_usage_get(client):
    """Test case for containers_usage_get

    List container sizes and quota limits
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'x_auth_token_example',
        'x_auth_project_id': 'x_auth_project_id_example',
    }
    response = await client.request(
        method='GET',
        path='/v3/containers/usage',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

