# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.dialog_open_error_schema import DialogOpenErrorSchema
from openapi_server.models.dialog_open_schema import DialogOpenSchema


pytestmark = pytest.mark.asyncio

async def test_dialog_open(client):
    """Test case for dialog_open

    
    """
    params = [('dialog', 'dialog_example'),
                    ('trigger_id', 'trigger_id_example')]
    headers = { 
        'Accept': 'application/json',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dialog.open',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

