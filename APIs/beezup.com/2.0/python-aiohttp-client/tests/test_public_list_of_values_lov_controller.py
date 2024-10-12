# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.public_list_of_values_response import PublicListOfValuesResponse
from openapi_server.models.public_lov_index import PublicLovIndex


pytestmark = pytest.mark.asyncio

async def test_get_public_list_of_values(client):
    """Test case for get_public_list_of_values

    Get the list of values related to this list name
    """
    headers = { 
        'Accept': 'application/json',
        'accept_language': ['accept_language_example'],
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/public/lov/{list_name}'.format(list_name='list_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_public_lov_index(client):
    """Test case for get_public_lov_index

    Get all list names
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/public/lov/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

