# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.page_result_book_tran_type_dto import PageResultBookTranTypeDto


pytestmark = pytest.mark.asyncio

async def test_book_tran_types_get(client):
    """Test case for book_tran_types_get

    Returns a list of global Book Transactions' Types. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \"id\" field.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/bookTranTypes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

