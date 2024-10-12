# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.rsbyc400_response import Rsbyc400Response
from openapi_server.models.rsbyc401_response import Rsbyc401Response
from openapi_server.models.rsbyc404_response import Rsbyc404Response
from openapi_server.models.rsbyc500_response import Rsbyc500Response
from openapi_server.models.rsbyc502_response import Rsbyc502Response
from openapi_server.models.rsbyc503_response import Rsbyc503Response
from openapi_server.models.rsbyc504_response import Rsbyc504Response
from openapi_server.models.rsbyc_request import RsbycRequest


pytestmark = pytest.mark.asyncio

async def test_rsbyc(client):
    """Test case for rsbyc

    Health Card/ Certificate
    """
    body = openapi_server.RsbycRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/hpsbys/v3/rsbyc/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

