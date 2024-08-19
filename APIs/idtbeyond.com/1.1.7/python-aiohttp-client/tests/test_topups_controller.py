# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.topups import Topups
from openapi_server.models.topups_reports import TopupsReports
from openapi_server.models.topups_reversal import TopupsReversal


pytestmark = pytest.mark.asyncio

async def test_iatu_topups_post(client):
    """Test case for iatu_topups_post

    Topup a mobile phone
    """
    body = {"country_code":"GT","amount":0,"client_transaction_id":"","mobile_number":"50231234567","product_code":"","plan":"Sandbox","terminal_id":"Kiosk 5","carrier_code":"Claro"}
    headers = { 
        'Content-Type': 'application/json',
        'x_idt_beyond_app_id': 'APP_ID',
        'x_idt_beyond_app_key': 'APP_KEY',
    }
    response = await client.request(
        method='POST',
        path='/v1/iatu/topups',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_iatu_topups_reports_all_csv_get(client):
    """Test case for iatu_topups_reports_all_csv_get

    List of account topups in CSV
    """
    params = [('date_from', '2016-01-28'),
                    ('date_to', '2016-01-28')]
    headers = { 
        'x_idt_beyond_app_id': 'APP_ID',
        'x_idt_beyond_app_key': 'APP_KEY',
    }
    response = await client.request(
        method='GET',
        path='/v1/iatu/topups/reports/all.csv',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_iatu_topups_reports_all_get(client):
    """Test case for iatu_topups_reports_all_get

    List of account topups in JSON
    """
    params = [('date_from', '2016-01-28'),
                    ('date_to', '2016-01-28')]
    headers = { 
        'x_idt_beyond_app_id': 'APP_ID',
        'x_idt_beyond_app_key': 'APP_KEY',
    }
    response = await client.request(
        method='GET',
        path='/v1/iatu/topups/reports/all',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_iatu_topups_reports_post(client):
    """Test case for iatu_topups_reports_post

    Search topups transactions
    """
    body = {"to_service_number":"123456789","type_of_report":"client_transaction_id or to_service_number","date_to":"2016-01-28","client_transaction_id":"trans0123456789","date_from":"2016-01-28"}
    headers = { 
        'Content-Type': 'application/json',
        'x_idt_beyond_app_id': 'APP_ID',
        'x_idt_beyond_app_key': 'APP_KEY',
    }
    response = await client.request(
        method='POST',
        path='/v1/iatu/topups/reports',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_iatu_topups_reports_totals_get(client):
    """Test case for iatu_topups_reports_totals_get

    Summary of account topups in JSON
    """
    params = [('date_from', '2016-01-28'),
                    ('date_to', '2016-01-28')]
    headers = { 
        'x_idt_beyond_app_id': 'APP_ID',
        'x_idt_beyond_app_key': 'APP_KEY',
    }
    response = await client.request(
        method='GET',
        path='/v1/iatu/topups/reports/totals',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_iatu_topups_reverse_post(client):
    """Test case for iatu_topups_reverse_post

    Reversal of a Topup
    """
    body = {"to_service_number":"123456789","client_transaction_id":"trans0123456789"}
    headers = { 
        'Content-Type': 'application/json',
        'x_idt_beyond_app_id': 'APP_ID',
        'x_idt_beyond_app_key': 'APP_KEY',
    }
    response = await client.request(
        method='POST',
        path='/v1/iatu/topups/reverse',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

