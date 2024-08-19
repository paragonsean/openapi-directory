# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.basic_error import BasicError
from openapi_server.models.code_of_conduct import CodeOfConduct


pytestmark = pytest.mark.asyncio

async def test_codes_of_conduct_get_all_codes_of_conduct(client):
    """Test case for codes_of_conduct_get_all_codes_of_conduct

    Get all codes of conduct
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/codes_of_conduct',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_codes_of_conduct_get_conduct_code(client):
    """Test case for codes_of_conduct_get_conduct_code

    Get a code of conduct
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/codes_of_conduct/{key}'.format(key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

