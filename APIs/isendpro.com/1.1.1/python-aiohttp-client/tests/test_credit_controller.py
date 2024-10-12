# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.credit_response import CreditResponse
from openapi_server.models.erreur import Erreur


pytestmark = pytest.mark.asyncio

async def test_get_credit(client):
    """Test case for get_credit

    Interrogation credit
    """
    params = [('keyid', 'keyid_example'),
                    ('credit', 'credit_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/cgi-bin/credit',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

