# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.platform_entity import PlatformEntity


pytestmark = pytest.mark.asyncio

async def test_get_platform_collection(client):
    """Test case for get_platform_collection

    GET for platform
    """
    params = [('page_size', 56),
                    ('page', 56),
                    ('fields', 'fields_example'),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'x_api2_crm_user_key': 'e2a6379ab878ae7e58119d4ec842bf9c',
    }
    response = await client.request(
        method='GET',
        path='/v1/platform/list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_platform_entity(client):
    """Test case for get_platform_entity

    GET for platform
    """
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'x_api2_crm_user_key': 'e2a6379ab878ae7e58119d4ec842bf9c',
    }
    response = await client.request(
        method='GET',
        path='/v1/platform/{type}'.format(type='type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

