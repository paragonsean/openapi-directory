# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.ergo_pay_response import ErgoPayResponse
from openapi_server.models.fetch_action_response import FetchActionResponse
from openapi_server.models.mosaik_app import MosaikApp


pytestmark = pytest.mark.asyncio

async def test_do_create_babel_box(client):
    """Test case for do_create_babel_box

    
    """
    body = None
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/mosaik/babelfee/newoffer/doit',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ergo_pay_create_babel_box(client):
    """Test case for ergo_pay_create_babel_box

    
    """
    params = [('tokenId', 'token_id_example'),
                    ('ergAmount', 56),
                    ('tokenAmount', 56)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/createbabel/{address}'.format(address='address_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_babel_fee_new_offer(client):
    """Test case for get_babel_fee_new_offer

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/mosaik/babelfee/newoffer',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replace_token_amount_input_fields(client):
    """Test case for replace_token_amount_input_fields

    
    """
    body = None
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/mosaik/babelfee/newoffer/new-input',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

