# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_create_pdf(client):
    """Test case for create_pdf

    Create PDF
    """
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/checks/{check_id}/pdf'.format(check_id='check_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pdf(client):
    """Test case for get_pdf

    Get PDF
    """
    params = [('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/checks/{check_id}/pdf'.format(check_id='check_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

