# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.extended_error_model import ExtendedErrorModel
from openapi_server.models.test_response import TestResponse


pytestmark = pytest.mark.asyncio

async def test_utils_errors_errorcode_get(client):
    """Test case for utils_errors_errorcode_get

    
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/utils/errors/{errorcode}'.format(errorcode='errorcode_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_utils_test_get(client):
    """Test case for utils_test_get

    
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/utils/test',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

