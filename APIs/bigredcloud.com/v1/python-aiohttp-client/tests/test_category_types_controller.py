# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.page_result_category_type_dto import PageResultCategoryTypeDto


pytestmark = pytest.mark.asyncio

async def test_category_types_get(client):
    """Test case for category_types_get

    Returns a list of company's Category Types. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \"id\" field.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/categoryTypes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

