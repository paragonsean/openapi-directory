# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.extension_config import ExtensionConfig


pytestmark = pytest.mark.asyncio

async def test_extension_configuration(client):
    """Test case for extension_configuration

    Configuration Resource
    """
    headers = { 
        'Accept': 'application/jose',
        'x_applecloudextension_session_id': 'x_applecloudextension_session_id_example',
        'x_applecloudextension_retry_count': 3.4,
        'request_timeout': 3.4,
        'user_agent': 'user_agent_example',
        'accept_language': 'accept_language_example',
        'if_none_match': 'if_none_match_example',
        'cache_control': 'cache_control_example',
    }
    response = await client.request(
        method='GET',
        path='/api/configuration',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

