# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.collect_request import CollectRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.rank_collect_response import RankCollectResponse
from openapi_server.models.rank_submit_request import RankSubmitRequest
from openapi_server.models.rank_submit_response import RankSubmitResponse
from openapi_server.models.serp_collect_response import SerpCollectResponse
from openapi_server.models.serp_submit_request import SerpSubmitRequest
from openapi_server.models.serp_submit_response import SerpSubmitResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json; charset&#x3D;utf-8 not supported by Connexion")
async def test_rank_collect(client):
    """Test case for rank_collect

    
    """
    body = openapi_server.CollectRequest()
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json; charset=utf-8',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/seo/api/rank-collect',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json; charset&#x3D;utf-8 not supported by Connexion")
async def test_rank_submit(client):
    """Test case for rank_submit

    
    """
    body = openapi_server.RankSubmitRequest()
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json; charset=utf-8',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/seo/api/rank-submit',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json; charset&#x3D;utf-8 not supported by Connexion")
async def test_serp_collect(client):
    """Test case for serp_collect

    
    """
    body = openapi_server.CollectRequest()
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json; charset=utf-8',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/seo/api/serp-collect',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json; charset&#x3D;utf-8 not supported by Connexion")
async def test_serp_submit(client):
    """Test case for serp_submit

    
    """
    body = openapi_server.SerpSubmitRequest()
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json; charset=utf-8',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/seo/api/serp-submit',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

