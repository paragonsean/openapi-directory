# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.compliance_summary_slav1 import ComplianceSummarySLAV1
from openapi_server.models.compliance_summary_v1 import ComplianceSummaryV1
from openapi_server.models.report_config_patch import ReportConfigPatch
from openapi_server.models.report_config_response import ReportConfigResponse


pytestmark = pytest.mark.asyncio

async def test_get_compliance_summary_slav1(client):
    """Test case for get_compliance_summary_slav1

    Get compliance summary information
    """
    params = [('snapshot_range', 'snapshot_range_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/report/compliance_summary_sla',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_compliance_summary_v1(client):
    """Test case for get_compliance_summary_v1

    Get compliance summary information
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/report/compliance_summary',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_report_config(client):
    """Test case for set_report_config

    Modify the report config
    """
    body = {"cleanupReportJobInstanceForLogJobs":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/report/config',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

