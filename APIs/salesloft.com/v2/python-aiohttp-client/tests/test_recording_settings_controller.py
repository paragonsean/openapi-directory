# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.recording_setting import RecordingSetting


pytestmark = pytest.mark.asyncio

async def test_v2_phone_numbers_recording_settings_id_json_get(client):
    """Test case for v2_phone_numbers_recording_settings_id_json_get

    Fetch recording setting
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/phone_numbers/recording_settings/{id_jso}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

