# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_content_and_approvals_response import ListContentAndApprovalsResponse


pytestmark = pytest.mark.asyncio

async def test_list_content_and_approvals(client):
    """Test case for list_content_and_approvals

    
    """
    params = [('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/ContentAndApprovals',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

