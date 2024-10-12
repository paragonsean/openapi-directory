# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.default_error_template import DefaultErrorTemplate
from openapi_server.models.default_success_template import DefaultSuccessTemplate


pytestmark = pytest.mark.asyncio

async def test_apps_event_authorizations_list(client):
    """Test case for apps_event_authorizations_list

    
    """
    params = [('event_context', 'event_context_example'),
                    ('cursor', 'cursor_example'),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/apps.event.authorizations.list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

