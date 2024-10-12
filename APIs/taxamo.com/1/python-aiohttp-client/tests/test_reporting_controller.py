# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_domestic_summary_report_out import GetDomesticSummaryReportOut
from openapi_server.models.get_eu_vies_report_out import GetEuViesReportOut


pytestmark = pytest.mark.asyncio

async def test_get_domestic_summary_report(client):
    """Test case for get_domestic_summary_report

    Calculate domestic summary
    """
    params = [('format', 'format_example'),
                    ('country_code', 'country_code_example'),
                    ('currency_code', 'currency_code_example'),
                    ('start_month', 'start_month_example'),
                    ('end_month', 'end_month_example'),
                    ('fx_date_type', 'fx_date_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/reports/domestic/summary',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_eu_vies_report(client):
    """Test case for get_eu_vies_report

    Calculate EU VIES report
    """
    params = [('period_length', 'period_length_example'),
                    ('lff_sequence_number', 'lff_sequence_number_example'),
                    ('transformation', 'transformation_example'),
                    ('currency_code', 'currency_code_example'),
                    ('end_month', 'end_month_example'),
                    ('tax_id', 'tax_id_example'),
                    ('start_month', 'start_month_example'),
                    ('eu_country_code', 'eu_country_code_example'),
                    ('fx_date_type', 'fx_date_type_example'),
                    ('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/reports/eu/vies',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

