# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_verification_template_response import ListVerificationTemplateResponse


pytestmark = pytest.mark.asyncio

async def test_list_verification_template(client):
    """Test case for list_verification_template

    
    """
    params = [('FriendlyName', 'friendly_name_example'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/Templates',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

