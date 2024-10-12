# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.query_a_database200_response import QueryADatabase200Response
from openapi_server.models.query_a_database_request import QueryADatabaseRequest
from openapi_server.models.retrieve_a_database200_response import RetrieveADatabase200Response
from openapi_server.models.update_a_database200_response import UpdateADatabase200Response
from openapi_server.models.update_a_database_request import UpdateADatabaseRequest


pytestmark = pytest.mark.asyncio

async def test_query_a_database(client):
    """Test case for query_a_database

    Query a database
    """
    body = {"filter":{"property":"Status","select":{"equals":"Reading"}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'notion_version': '{{NOTION_VERSION}}',
    }
    response = await client.request(
        method='POST',
        path='/v1/databases/{id}/query'.format(id='{{DATABASE_ID}}'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_a_database(client):
    """Test case for retrieve_a_database

    Retrieve a database
    """
    headers = { 
        'Accept': 'application/json',
        'notion_version': '{{NOTION_VERSION}}',
    }
    response = await client.request(
        method='GET',
        path='/v1/databases/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_a_database(client):
    """Test case for update_a_database

    Update a database
    """
    body = {"properties":{"Wine Pairing":{"rich_text":{}}},"title":[{"text":{"content":"Ever Better Reading List Title"}}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'notion_version': '{{NOTION_VERSION}}',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/databases/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

