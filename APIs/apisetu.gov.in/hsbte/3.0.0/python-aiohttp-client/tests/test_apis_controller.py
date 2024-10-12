# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.dgmst400_response import Dgmst400Response
from openapi_server.models.dgmst401_response import Dgmst401Response
from openapi_server.models.dgmst404_response import Dgmst404Response
from openapi_server.models.dgmst500_response import Dgmst500Response
from openapi_server.models.dgmst502_response import Dgmst502Response
from openapi_server.models.dgmst503_response import Dgmst503Response
from openapi_server.models.dgmst504_response import Dgmst504Response
from openapi_server.models.dgmst_request import DgmstRequest


pytestmark = pytest.mark.asyncio

async def test_dgmst(client):
    """Test case for dgmst

    Degree/ Diploma Marksheet
    """
    body = openapi_server.DgmstRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/hsbte/v3/dgmst/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

