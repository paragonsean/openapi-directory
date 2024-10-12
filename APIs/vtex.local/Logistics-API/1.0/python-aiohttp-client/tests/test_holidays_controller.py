# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_update_holiday_request import CreateUpdateHolidayRequest


pytestmark = pytest.mark.asyncio

async def test_all_holidays(client):
    """Test case for all_holidays

    List all holidays
    """
    headers = { 
        'content_type': 'application/json; charset=utf-8',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/logistics/pvt/configuration/holidays',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json; charset&#x3D;utf-8 not supported by Connexion")
async def test_create_update_holiday(client):
    """Test case for create_update_holiday

    Create/update holiday
    """
    body = {"name":"Natal","startDate":"2016-12-25"}
    headers = { 
        'Content-Type': 'application/json; charset=utf-8',
        'accept': 'application/json',
        'content_type': 'application/json; charset=utf-8',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/logistics/pvt/configuration/holidays/{holiday_id}'.format(holiday_id='holiday_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_holiday(client):
    """Test case for holiday

    Delete holiday
    """
    headers = { 
        'content_type': 'application/json; charset=utf-8',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/logistics/pvt/configuration/holidays/{holiday_id}'.format(holiday_id='holiday_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_holiday_by_id(client):
    """Test case for holiday_by_id

    List holiday by ID
    """
    headers = { 
        'content_type': 'application/json; charset=utf-8',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/logistics/pvt/configuration/holidays/{holiday_id}'.format(holiday_id='holiday_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

