# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_line_item_entity import AccountLineItemEntity


pytestmark = pytest.mark.asyncio

async def test_get_invoices(client):
    """Test case for get_invoices

    List Invoices
    """
    params = [('cursor', 'cursor_example'),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/invoices',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_invoices_id(client):
    """Test case for get_invoices_id

    Show Invoice
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/invoices/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

