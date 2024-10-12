# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.directory_data_currency_information_interface import DirectoryDataCurrencyInformationInterface
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_directory_currency_information_acquirer_v1_get_currency_info_get(client):
    """Test case for directory_currency_information_acquirer_v1_get_currency_info_get

    directory/currency
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/directory/currency',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

