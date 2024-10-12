# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.input_date_time_conversion import InputDateTimeConversion
from openapi_server.models.input_date_time_difference import InputDateTimeDifference
from openapi_server.models.input_date_time_format import InputDateTimeFormat
from openapi_server.models.input_date_time_info import InputDateTimeInfo
from openapi_server.models.output_date_difference import OutputDateDifference
from openapi_server.models.output_date_info import OutputDateInfo
from openapi_server.models.output_string import OutputString


pytestmark = pytest.mark.asyncio

async def test_date_time_difference(client):
    """Test case for date_time_difference

    DateTime - DateTime difference
    """
    date_time_difference = openapi_server.InputDateTimeDifference()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/DateTimeDifference',
        headers=headers,
        json=date_time_difference,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_date_time_info(client):
    """Test case for date_time_info

    DateTime - Get date and time information
    """
    date_time_info = openapi_server.InputDateTimeInfo()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/DateTimeInfo',
        headers=headers,
        json=date_time_info,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_format_date_time(client):
    """Test case for format_date_time

    DateTime - Format date and time
    """
    date_time_format = openapi_server.InputDateTimeFormat()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/FormatDateTime',
        headers=headers,
        json=date_time_format,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_world_time(client):
    """Test case for world_time

    DateTime - Get world time
    """
    date_time_conversion = openapi_server.InputDateTimeConversion()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/WorldTime',
        headers=headers,
        json=date_time_conversion,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

