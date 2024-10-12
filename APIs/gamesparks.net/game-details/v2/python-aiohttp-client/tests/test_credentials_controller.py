# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.message_model import MessageModel


pytestmark = pytest.mark.asyncio

async def test_update_credential_secret_using_post(client):
    """Test case for update_credential_secret_using_post

    Resets the secret of a credential
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='POST',
        path='/restv2/game/{api_key}/config/~credentials/{credential_name}/resetSecret'.format(api_key='api_key_example', credential_name='credential_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

