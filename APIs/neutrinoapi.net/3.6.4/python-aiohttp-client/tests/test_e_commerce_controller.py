# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.bin_lookup_response import BINLookupResponse
from openapi_server.models.convert_response import ConvertResponse


pytestmark = pytest.mark.asyncio

async def test_b_in_list_download(client):
    """Test case for b_in_list_download

    BIN List Download
    """
    params = [('include-iso3', False),
                    ('include-8digit', False)]
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
        'user-id': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/bin-list-download',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_b_in_lookup(client):
    """Test case for b_in_lookup

    BIN Lookup
    """
    params = [('bin-number', 'bin_number_example'),
                    ('customer-ip', 'customer_ip_example')]
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
        'user-id': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/bin-lookup',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_convert(client):
    """Test case for convert

    Convert
    """
    params = [('from-value', 'from_value_example'),
                    ('from-type', 'from_type_example'),
                    ('to-type', 'to_type_example')]
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
        'user-id': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/convert',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

