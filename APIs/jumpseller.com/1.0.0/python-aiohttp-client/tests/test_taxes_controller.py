# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.not_found import NotFound
from openapi_server.models.tax import Tax
from openapi_server.models.tax_edit import TaxEdit


pytestmark = pytest.mark.asyncio

async def test_taxes_id_json_get(client):
    """Test case for taxes_id_json_get

    Retrieve a single Tax information.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/taxes/{id_jso}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_taxes_json_get(client):
    """Test case for taxes_json_get

    Retrieve all Taxes.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/taxes.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_taxes_json_post(client):
    """Test case for taxes_json_post

    Create a new Tax.
    """
    body = {"tax":{"country":"country","category_id":0,"shipping":False,"name":"name","fixed":False,"tax":6.0274563,"region":"region"}}
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/taxes.json',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

