# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_cash_drawer_shift_events_response import ListCashDrawerShiftEventsResponse
from openapi_server.models.list_cash_drawer_shifts_response import ListCashDrawerShiftsResponse
from openapi_server.models.retrieve_cash_drawer_shift_response import RetrieveCashDrawerShiftResponse


pytestmark = pytest.mark.asyncio

async def test_list_cash_drawer_shift_events(client):
    """Test case for list_cash_drawer_shift_events

    ListCashDrawerShiftEvents
    """
    params = [('location_id', 'location_id_example'),
                    ('limit', 56),
                    ('cursor', 'cursor_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/cash-drawers/shifts/{shift_id}/events'.format(shift_id='shift_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_cash_drawer_shifts(client):
    """Test case for list_cash_drawer_shifts

    ListCashDrawerShifts
    """
    params = [('location_id', 'location_id_example'),
                    ('sort_order', 'sort_order_example'),
                    ('begin_time', 'begin_time_example'),
                    ('end_time', 'end_time_example'),
                    ('limit', 56),
                    ('cursor', 'cursor_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/cash-drawers/shifts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_cash_drawer_shift(client):
    """Test case for retrieve_cash_drawer_shift

    RetrieveCashDrawerShift
    """
    params = [('location_id', 'location_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/cash-drawers/shifts/{shift_id}'.format(shift_id='shift_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

