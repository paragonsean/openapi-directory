# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.erreur import Erreur
from openapi_server.models.hlr_reponse import HLRReponse
from openapi_server.models.hl_rrequest import HLRrequest


pytestmark = pytest.mark.asyncio

async def test_get_hlr(client):
    """Test case for get_hlr

    Vérifier la validité d'un numéro
    """
    body = {"getHLR":"1","keyid":"VOTRE_KEYID","num":["06123456789","06345687899"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/cgi-bin/hlr',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

