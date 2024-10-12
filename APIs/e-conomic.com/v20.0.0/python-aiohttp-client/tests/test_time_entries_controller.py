# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.time_entry_numbers_collection import TimeEntryNumbersCollection


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_approve_time_entries(client):
    """Test case for approve_time_entries

    Approve a list of Time entries
    """
    body = {"numbers":[1,2,3]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'X-AgreementGrantToken': 'special-key',
        'X-AppSecretToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v20.0.0/timeentries/approve',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

