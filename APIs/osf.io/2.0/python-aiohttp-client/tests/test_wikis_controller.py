# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.wiki import Wiki


pytestmark = pytest.mark.asyncio

async def test_wiki_content(client):
    """Test case for wiki_content

    Retrieve the Content of a Wiki
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/wikis/{wiki_id}/content'.format(wiki_id='wiki_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wiki_read(client):
    """Test case for wiki_read

    Retrieve a Wiki
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/wikis/{wiki_id}'.format(wiki_id='wiki_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

