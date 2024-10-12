# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.error_limit import ErrorLimit
from openapi_server.models.legal_agreement import LegalAgreement


pytestmark = pytest.mark.asyncio

async def test_get(client):
    """Test case for get

    Retrieve Legal Agreements for provided agreements keys
    """
    params = [('keys', ['keys_example'])]
    headers = { 
        'Accept': 'application/json',
        'x_private_label_id': 56,
        'x_market_id': 'en-US',
    }
    response = await client.request(
        method='GET',
        path='/v1/agreements',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

