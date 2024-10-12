# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.jwt_obtain_pair_request import JWTObtainPairRequest
from openapi_server.models.jwt_refresh_request import JWTRefreshRequest
from openapi_server.models.spectacular_jwt_obtain import SpectacularJWTObtain
from openapi_server.models.spectacular_jwt_refresh import SpectacularJWTRefresh


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_j_wt_obtain(client):
    """Test case for j_wt_obtain

    
    """
    body = {"secret_id":"secret_id","secret_key":"secret_key"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/token/new/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_j_wt_refresh(client):
    """Test case for j_wt_refresh

    
    """
    body = {"refresh":"refresh"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/token/refresh/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

