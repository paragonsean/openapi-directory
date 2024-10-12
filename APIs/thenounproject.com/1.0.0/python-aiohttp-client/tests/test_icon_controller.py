# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_icon_by_id(client):
    """Test case for get_icon_by_id

    Get icon by id
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/icon/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_icon_by_term(client):
    """Test case for get_icon_by_term

    Get icon by term
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/icon/{term}'.format(term='term_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

