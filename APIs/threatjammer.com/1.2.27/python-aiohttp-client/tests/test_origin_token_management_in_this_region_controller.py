# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.body_delete_token_v1_origin_token_delete import BodyDeleteTokenV1OriginTokenDelete
from openapi_server.models.body_disable_origin_token_v1_origin_token_disable_put import BodyDisableOriginTokenV1OriginTokenDisablePut
from openapi_server.models.body_enable_origin_token_v1_origin_token_enable_put import BodyEnableOriginTokenV1OriginTokenEnablePut
from openapi_server.models.body_query_origin_token_info_v1_origin_token_post import BodyQueryOriginTokenInfoV1OriginTokenPost
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.origin_token_collection_output import OriginTokenCollectionOutput
from openapi_server.models.origin_token_input import OriginTokenInput
from openapi_server.models.origin_token_output import OriginTokenOutput


pytestmark = pytest.mark.asyncio

async def test_create_a_new_origin_token_v1_origin_token_new_post(client):
    """Test case for create_a_new_origin_token_v1_origin_token_new_post

    Create an origin token of the user in the region.
    """
    body = {"origin":"origin"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/origin_token/new',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_token_v1_origin_token_delete(client):
    """Test case for delete_token_v1_origin_token_delete

    Delete an origin token of the user in the region.
    """
    body = openapi_server.BodyDeleteTokenV1OriginTokenDelete()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/origin_token',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disable_origin_token_v1_origin_token_disable_put(client):
    """Test case for disable_origin_token_v1_origin_token_disable_put

    Disable a enabled origin token of the user in the region.
    """
    body = openapi_server.BodyDisableOriginTokenV1OriginTokenDisablePut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/origin_token/disable',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enable_origin_token_v1_origin_token_enable_put(client):
    """Test case for enable_origin_token_v1_origin_token_enable_put

    Enable a disabled origin token of the user in the region.
    """
    body = openapi_server.BodyEnableOriginTokenV1OriginTokenEnablePut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/origin_token/enable',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_all_origin_tokens_in_the_region_v1_origin_token_all_get(client):
    """Test case for query_all_origin_tokens_in_the_region_v1_origin_token_all_get

    Get the information of the origin tokens of the user in the region.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/origin_token/all',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_origin_token_info_v1_origin_token_post(client):
    """Test case for query_origin_token_info_v1_origin_token_post

    Get the information of an origin token of the user in the region.
    """
    body = openapi_server.BodyQueryOriginTokenInfoV1OriginTokenPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/origin_token',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

