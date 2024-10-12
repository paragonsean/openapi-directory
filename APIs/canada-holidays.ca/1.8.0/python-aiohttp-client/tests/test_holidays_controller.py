# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.holiday200_response import Holiday200Response
from openapi_server.models.holiday400_response import Holiday400Response
from openapi_server.models.holidays200_response import Holidays200Response


pytestmark = pytest.mark.asyncio

async def test_holiday(client):
    """Test case for holiday

    Get a holiday by id
    """
    params = [('year', 2023),
                    ('optional', false)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/holidays/{holiday_id}'.format(holiday_id=2),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_holidays(client):
    """Test case for holidays

    Get all holidays
    """
    params = [('year', 2023),
                    ('federal', 'federal_example'),
                    ('optional', false)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/holidays',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

