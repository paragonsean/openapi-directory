# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.patient import Patient


pytestmark = pytest.mark.asyncio

async def test_get_basic_patient_details(client):
    """Test case for get_basic_patient_details

    Get Basic Patient Information
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/patient/{user_id}/basic'.format(user_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

