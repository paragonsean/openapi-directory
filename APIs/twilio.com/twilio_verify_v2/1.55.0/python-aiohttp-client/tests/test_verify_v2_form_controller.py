# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.form_enum_form_types import FormEnumFormTypes
from openapi_server.models.verify_v2_form import VerifyV2Form


pytestmark = pytest.mark.asyncio

async def test_fetch_form(client):
    """Test case for fetch_form

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/Forms/{form_type}'.format(form_type=openapi_server.FormEnumFormTypes()),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

