# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.author import Author
from openapi_server.models.author_complete import AuthorComplete
from openapi_server.models.error_message import ErrorMessage
from openapi_server.models.private_authors_search import PrivateAuthorsSearch


pytestmark = pytest.mark.asyncio

async def test_private_author_details(client):
    """Test case for private_author_details

    Author details
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/account/authors/{author_id}'.format(author_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_authors_search(client):
    """Test case for private_authors_search

    Search Authors
    """
    body = {"is_active":True,"offset":0,"group_id":0,"is_public":True,"limit":10,"orcid":"orcid","order_direction":"desc","page":1,"search_for":"figshare","institution_id":1,"order":"published_date","page_size":10}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/account/authors/search',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

