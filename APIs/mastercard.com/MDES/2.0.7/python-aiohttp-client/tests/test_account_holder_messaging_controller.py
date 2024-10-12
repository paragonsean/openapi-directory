# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_holder_messaging_request import AccountHolderMessagingRequest
from openapi_server.models.account_holder_messaging_response_schema import AccountHolderMessagingResponseSchema
from openapi_server.models.errors_response import ErrorsResponse


pytestmark = pytest.mark.asyncio

async def test_accountholdermessaging_post(client):
    """Test case for accountholdermessaging_post

    
    """
    accountholder_messaging_request_schema = {"AccountHolderMessagingRequest":{"TokenUniqueReference":"DWSPMC00000000010906a349d9ca4eb1a4d53e3c90a11d9c","MessageExpiration":"2020-06-18T18:04:35-00:00","AuditInfo":{"Organization":"Solid Bank Inc","UserName":"John Smith","Phone":"5555551234","UserId":"A1435477"},"IssuerApplicationMessageDisplay":"FALSE","MessageLanguageCode":"en","MessageIdentifier":"6.598123486451347E27","MessageText":"You have earned a statement credit."}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/mdes/csapi/v2/accountholdermessaging',
        headers=headers,
        json=accountholder_messaging_request_schema,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

