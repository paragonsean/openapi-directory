# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.govid400_response import Govid400Response
from openapi_server.models.govid401_response import Govid401Response
from openapi_server.models.govid404_response import Govid404Response
from openapi_server.models.govid500_response import Govid500Response
from openapi_server.models.govid502_response import Govid502Response
from openapi_server.models.govid503_response import Govid503Response
from openapi_server.models.govid504_response import Govid504Response
from openapi_server.models.govid_request import GovidRequest


pytestmark = pytest.mark.asyncio

async def test_govid(client):
    """Test case for govid

    ID Card
    """
    body = openapi_server.GovidRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/mcimindia/v3/govid/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_phcer(client):
    """Test case for phcer

    Pharmacist Registration Certificate
    """
    body = openapi_server.GovidRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/mcimindia/v3/phcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

