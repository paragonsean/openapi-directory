# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.usage_aggregate_page import UsageAggregatePage


pytestmark = pytest.mark.asyncio

async def test_subscriber_usage_aggregates_list(client):
    """Test case for subscriber_usage_aggregates_list

    
    """
    params = [('api-version', '2015-06-01-preview'),
                    ('reportedStartTime', '2013-10-20T19:20:30+01:00'),
                    ('reportedEndTime', '2013-10-20T19:20:30+01:00'),
                    ('aggregationGranularity', 'aggregation_granularity_example'),
                    ('subscriberId', 'subscriber_id_example'),
                    ('continuationToken', 'continuation_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Commerce/subscriberUsageAggregates'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

