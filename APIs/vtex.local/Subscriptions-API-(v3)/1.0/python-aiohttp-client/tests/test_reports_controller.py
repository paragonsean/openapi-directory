# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.report_response import ReportResponse
from openapi_server.models.subscription_report import SubscriptionReport


pytestmark = pytest.mark.asyncio

async def test_api_rns_pvt_reports_get(client):
    """Test case for api_rns_pvt_reports_get

    List report templates
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/rns/pvt/reports',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_rns_pvt_reports_report_name_documents_document_id_get(client):
    """Test case for api_rns_pvt_reports_report_name_documents_document_id_get

    Get report document details
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/rns/pvt/reports/{report_name}/documents/{document_id}'.format(report_name='report_name_example', document_id='document_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_rns_pvt_reports_report_name_documents_post(client):
    """Test case for api_rns_pvt_reports_report_name_documents_post

    Generate report
    """
    params = [('email', 'receiver@email.com'),
                    ('beginDate', '2022-09-01'),
                    ('endDate', '2022-10-01')]
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/rns/pvt/reports/{report_name}/documents'.format(report_name='report_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

