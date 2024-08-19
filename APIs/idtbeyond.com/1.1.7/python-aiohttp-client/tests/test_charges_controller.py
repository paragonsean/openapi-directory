# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_iatu_charges_reports_all_csv_get(client):
    """Test case for iatu_charges_reports_all_csv_get

    List of account charges in CSV
    """
    params = [('date_from', '2016-01-28'),
                    ('date_to', '2016-01-28')]
    headers = { 
        'x_idt_beyond_app_id': 'APP_ID',
        'x_idt_beyond_app_key': 'APP_KEY',
    }
    response = await client.request(
        method='GET',
        path='/v1/iatu/charges/reports/all.csv',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_iatu_charges_reports_all_get(client):
    """Test case for iatu_charges_reports_all_get

    List of account charges in JSON
    """
    params = [('date_from', '2016-01-28'),
                    ('date_to', '2016-01-28')]
    headers = { 
        'x_idt_beyond_app_id': 'APP_ID',
        'x_idt_beyond_app_key': 'APP_KEY',
    }
    response = await client.request(
        method='GET',
        path='/v1/iatu/charges/reports/all',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

