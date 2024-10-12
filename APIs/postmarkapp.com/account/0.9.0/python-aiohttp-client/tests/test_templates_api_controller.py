# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.standard_postmark_response import StandardPostmarkResponse
from openapi_server.models.templates_push_model import TemplatesPushModel
from openapi_server.models.templates_push_response import TemplatesPushResponse


pytestmark = pytest.mark.asyncio

async def test_push_templates(client):
    """Test case for push_templates

    Push templates from one server to another
    """
    body = {"PerformChanges":True,"DestinationServerId":0,"SourceServerId":6}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_postmark_account_token': 'x_postmark_account_token_example',
    }
    response = await client.request(
        method='PUT',
        path='/templates/push',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

