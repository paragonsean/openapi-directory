# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_customer_segments_response import ListCustomerSegmentsResponse
from openapi_server.models.retrieve_customer_segment_response import RetrieveCustomerSegmentResponse


pytestmark = pytest.mark.asyncio

async def test_list_customer_segments(client):
    """Test case for list_customer_segments

    ListCustomerSegments
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/customers/segments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_customer_segment(client):
    """Test case for retrieve_customer_segment

    RetrieveCustomerSegment
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/customers/segments/{segment_id}'.format(segment_id='segment_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

