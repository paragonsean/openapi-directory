# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.page_result_vat_type_dto import PageResultVatTypeDto


pytestmark = pytest.mark.asyncio

async def test_vat_types_get(client):
    """Test case for vat_types_get

    Returns a list of global Vat Types. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \"id\" field.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vatTypes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

