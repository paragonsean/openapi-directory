# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.retrieve_a_page200_response import RetrieveAPage200Response
from openapi_server.models.retrieve_a_page_property_item200_response import RetrieveAPagePropertyItem200Response
from openapi_server.models.update_page_properties200_response import UpdatePageProperties200Response
from openapi_server.models.update_page_properties_request import UpdatePagePropertiesRequest


pytestmark = pytest.mark.asyncio

async def test_retrieve_a_page(client):
    """Test case for retrieve_a_page

    Retrieve a Page
    """
    headers = { 
        'Accept': 'application/json',
        'notion_version': '{{NOTION_VERSION}}',
        '': '',
    }
    response = await client.request(
        method='GET',
        path='/v1/pages/{id}'.format(id='{{PAGE_ID}}'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_a_page_property_item(client):
    """Test case for retrieve_a_page_property_item

    Retrieve a Page Property Item
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/pages/{page_id}/properties/{property_id}'.format(page_id='{{PAGE_ID}}', property_id='property_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_page_properties(client):
    """Test case for update_page_properties

    Update Page properties 
    """
    body = {"properties":{"Status":{"select":{"name":"Reading"}}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'notion_version': '{{NOTION_VERSION}}',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/pages/{id}'.format(id='{{PAGE_ID}}'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

