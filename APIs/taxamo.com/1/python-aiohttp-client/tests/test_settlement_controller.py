# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_detailed_refunds_out import GetDetailedRefundsOut
from openapi_server.models.get_refunds_out import GetRefundsOut
from openapi_server.models.get_settlement_out import GetSettlementOut
from openapi_server.models.get_settlement_summary_out import GetSettlementSummaryOut


pytestmark = pytest.mark.asyncio

async def test_get_detailed_refunds(client):
    """Test case for get_detailed_refunds

    Detailed refunds
    """
    params = [('format', 'format_example'),
                    ('country_codes', 'country_codes_example'),
                    ('date_from', 'date_from_example'),
                    ('date_to', 'date_to_example'),
                    ('limit', 3.4),
                    ('offset', 3.4)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/settlement/detailed_refunds',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_refunds(client):
    """Test case for get_refunds

    Fetch refunds
    """
    params = [('format', 'format_example'),
                    ('moss_country_code', 'moss_country_code_example'),
                    ('tax_region', 'tax_region_example'),
                    ('date_from', 'date_from_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/settlement/refunds',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_settlement(client):
    """Test case for get_settlement

    Fetch settlement
    """
    params = [('moss_tax_id', 'moss_tax_id_example'),
                    ('currency_code', 'currency_code_example'),
                    ('end_month', 'end_month_example'),
                    ('tax_id', 'tax_id_example'),
                    ('refund_date_kind_override', 'refund_date_kind_override_example'),
                    ('start_month', 'start_month_example'),
                    ('moss_country_code', 'moss_country_code_example'),
                    ('format', 'format_example'),
                    ('tax_country_code', 'tax_country_code_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/settlement/{quarter}'.format(quarter='quarter_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_settlement_summary(client):
    """Test case for get_settlement_summary

    Fetch summary
    """
    params = [('moss_country_code', 'moss_country_code_example'),
                    ('tax_region', 'tax_region_example'),
                    ('start_month', 'start_month_example'),
                    ('end_month', 'end_month_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/settlement/summary/{quarter}'.format(quarter='quarter_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

