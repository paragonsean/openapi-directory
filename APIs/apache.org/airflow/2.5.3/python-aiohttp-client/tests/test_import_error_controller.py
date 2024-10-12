# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.import_error import ImportError
from openapi_server.models.import_error_collection import ImportErrorCollection


pytestmark = pytest.mark.asyncio

async def test_get_import_error(client):
    """Test case for get_import_error

    Get an import error
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/importErrors/{import_error_id}'.format(import_error_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_import_errors(client):
    """Test case for get_import_errors

    List import errors
    """
    params = [('limit', 100),
                    ('offset', 56),
                    ('order_by', 'order_by_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/importErrors',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

