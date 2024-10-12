# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.citation_style import CitationStyle


pytestmark = pytest.mark.asyncio

async def test_citations_styles_list(client):
    """Test case for citations_styles_list

    List all citation styles
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/citations/styles/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_citations_styles_read(client):
    """Test case for citations_styles_read

    Retrieve a citation style
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/citations/styles/{style_id}'.format(style_id='style_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

