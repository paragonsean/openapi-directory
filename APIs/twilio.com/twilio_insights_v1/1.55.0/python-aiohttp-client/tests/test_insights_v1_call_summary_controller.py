# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.insights_v1_call_summary import InsightsV1CallSummary
from openapi_server.models.summary_enum_processing_state import SummaryEnumProcessingState


pytestmark = pytest.mark.asyncio

async def test_fetch_summary(client):
    """Test case for fetch_summary

    
    """
    params = [('ProcessingState', openapi_server.SummaryEnumProcessingState())]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Voice/{call_sid}/Summary'.format(call_sid='call_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

