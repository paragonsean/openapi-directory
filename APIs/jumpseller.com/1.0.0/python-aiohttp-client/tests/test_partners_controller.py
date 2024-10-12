# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.partner_error import PartnerError
from openapi_server.models.partner_store_code import PartnerStoreCode
from openapi_server.models.partner_store_create import PartnerStoreCreate
from openapi_server.models.store_check_status_json_get200_response import StoreCheckStatusJsonGet200Response
from openapi_server.models.type import Type


pytestmark = pytest.mark.asyncio

async def test_partners_stores_json_get(client):
    """Test case for partners_stores_json_get

    Retrieve statistics.
    """
    params = [('partner_code', 'partner_code_example'),
                    ('auth_token', 'auth_token_example'),
                    ('page', 1),
                    ('from', '_from_example'),
                    ('to', 'to_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/partners/stores.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_store_check_status_json_get(client):
    """Test case for store_check_status_json_get

    Retrive store creation status.
    """
    params = [('partner_code', 'partner_code_example'),
                    ('auth_token', 'auth_token_example'),
                    ('store_code', 'store_code_example'),
                    ('locale', 'en')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/store/check_status.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_store_create_json_post(client):
    """Test case for store_create_json_post

    Create a Partnered Store
    """
    body = {"aff":"aff","password":"password","reject_duplicates":False,"store_name":"store_name","locale":"en","email":"email","plan_name":"pro"}
    params = [('partner_code', 'partner_code_example'),
                    ('auth_token', 'auth_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/store/create.json',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

