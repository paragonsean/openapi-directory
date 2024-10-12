# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.flux_response import FluxResponse


pytestmark = pytest.mark.asyncio

async def test_get_notification_rules_id_query(client):
    """Test case for get_notification_rules_id_query

    Retrieve a notification rule query
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/notificationRules/{rule_id}/query'.format(rule_id='rule_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

