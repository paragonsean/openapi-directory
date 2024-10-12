# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.erreur import Erreur
from openapi_server.models.subaccount_request import SubaccountRequest
from openapi_server.models.subaccount_response import SubaccountResponse


pytestmark = pytest.mark.asyncio

async def test_subaccount_edit(client):
    """Test case for subaccount_edit

    Edit a subaccount
    """
    body = {"subAccountCountryCode":"subAccountCountryCode","subAccountRestrictionStop":"0","subAccountKeyId":"subAccountKeyId","subAccountPrice":"subAccountPrice","keyid":"keyid","subAccountAddCredit":"subAccountAddCredit","subAccountRestrictionTime":"0","subAccountEdit":"setPrice"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/cgi-bin/subaccount',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

