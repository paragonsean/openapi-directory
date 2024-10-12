# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_financials_event_costs0_get(client):
    """Test case for financials_event_costs0_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
        'filter_by_event_id': 3.4,
        'filter_by_event_start_date_greater_than_or_equal_to': '2013-10-20',
        'filter_by_event_start_date_smaller_than_or_equal_to': '2013-10-20',
        'filter_by_event_end_date_greater_than_or_equal_to': '2013-10-20',
        'filter_by_event_end_date_smaller_than_or_equal_to': '2013-10-20',
    }
    response = await client.request(
        method='GET',
        path='/v1/financials/event_costs',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_financials_misc_annual_expense_costs0_get(client):
    """Test case for financials_misc_annual_expense_costs0_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
        'budget_year': 3.4,
    }
    response = await client.request(
        method='GET',
        path='/v1/financials/misc_annual_expense_costs',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

