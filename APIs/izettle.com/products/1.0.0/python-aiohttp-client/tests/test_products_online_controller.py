# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_slug_request import CreateSlugRequest
from openapi_server.models.slug_response import SlugResponse


pytestmark = pytest.mark.asyncio

async def test_create_product_slug(client):
    """Test case for create_product_slug

    Create a product identifier
    """
    body = {"productName":"productName"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/organizations/{organization_uuid}/products/online/slug'.format(organization_uuid='organization_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

