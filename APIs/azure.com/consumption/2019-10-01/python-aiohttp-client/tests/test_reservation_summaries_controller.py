# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.reservation_summaries_list_result import ReservationSummariesListResult


pytestmark = pytest.mark.asyncio

async def test_reservations_summaries_list(client):
    """Test case for reservations_summaries_list

    
    """
    params = [('grain', 'grain_example'),
                    ('startDate', 'start_date_example'),
                    ('endDate', 'end_date_example'),
                    ('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{scope}/providers/Microsoft.Consumption/reservationSummaries'.format(scope='scope_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reservations_summaries_list_by_reservation_order(client):
    """Test case for reservations_summaries_list_by_reservation_order

    
    """
    params = [('grain', 'grain_example'),
                    ('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Capacity/reservationorders/{reservation_order_id}/providers/Microsoft.Consumption/reservationSummaries'.format(reservation_order_id='reservation_order_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reservations_summaries_list_by_reservation_order_and_reservation(client):
    """Test case for reservations_summaries_list_by_reservation_order_and_reservation

    
    """
    params = [('grain', 'grain_example'),
                    ('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Capacity/reservationorders/{reservation_order_id}/reservations/{reservation_id}/providers/Microsoft.Consumption/reservationSummaries'.format(reservation_order_id='reservation_order_id_example', reservation_id='reservation_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

