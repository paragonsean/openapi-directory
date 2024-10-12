# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.exec_api import ExecAPI
from openapi_server.models.type import Type


pytestmark = pytest.mark.asyncio

async def test_marketstat_get(client):
    """Test case for marketstat_get

    XML Marketstat
    """
    params = [('typeid', [56]),
                    ('regionlimit', 56),
                    ('usesystem', 56)]
    headers = { 
        'Accept': 'application/xml',
    }
    response = await client.request(
        method='GET',
        path='/ec/marketstat',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_marketstat_json_get(client):
    """Test case for marketstat_json_get

    JSON Marketstat
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('typeid', [56])
    data.add_field('regionlimit', 56)
    data.add_field('usesystem', 56)
    response = await client.request(
        method='GET',
        path='/ec/marketstat/json',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_marketstat_json_post(client):
    """Test case for marketstat_json_post

    JSON Marketstat
    """
    params = [('typeid', [56]),
                    ('regionlimit', 56),
                    ('usesystem', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/ec/marketstat/json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_marketstat_post(client):
    """Test case for marketstat_post

    XML Marketstat
    """
    headers = { 
        'Accept': 'application/xml',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('typeid', [56])
    data.add_field('regionlimit', 56)
    data.add_field('usesystem', 56)
    response = await client.request(
        method='POST',
        path='/ec/marketstat',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

