# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.page_result_account_dto import PageResultAccountDto


pytestmark = pytest.mark.asyncio

async def test_accounts_get(client):
    """Test case for accounts_get

    Returns a list of company's Accounts. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \"id\" and \"code\" fields.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/accounts',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

