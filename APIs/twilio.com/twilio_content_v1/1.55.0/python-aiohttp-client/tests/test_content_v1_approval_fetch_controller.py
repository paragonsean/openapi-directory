# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.content_v1_content_approval_fetch import ContentV1ContentApprovalFetch


pytestmark = pytest.mark.asyncio

async def test_fetch_approval_fetch(client):
    """Test case for fetch_approval_fetch

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Content/{sid}/ApprovalRequests'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

