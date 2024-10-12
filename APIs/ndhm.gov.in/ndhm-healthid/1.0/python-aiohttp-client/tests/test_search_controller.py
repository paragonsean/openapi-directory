# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.search_by_health_id_request import SearchByHealthIdRequest
from openapi_server.models.search_by_mobile_request import SearchByMobileRequest
from openapi_server.models.search_response_single import SearchResponseSingle


pytestmark = pytest.mark.asyncio

async def test_search_user_by_account_using_post(client):
    """Test case for search_user_by_account_using_post

    Search a user by Health ID Number.
    """
    search_request = {"healthId":"healthId"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/search/searchByHealthId',
        headers=headers,
        json=search_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_user_by_mobile_using_post(client):
    """Test case for search_user_by_mobile_using_post

    Search users with a mobile number.
    """
    search_request = {"gender":"gender","mobile":"mobile","name":"name","yearOfBirth":"yearOfBirth"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/search/searchByMobile',
        headers=headers,
        json=search_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_user_by_userid_using_post(client):
    """Test case for search_user_by_userid_using_post

    Search a user by Health IDs.
    """
    search_dto = {"healthId":"healthId"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/search/existsByHealthId',
        headers=headers,
        json=search_dto,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

