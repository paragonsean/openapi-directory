# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.comptage_reponse import ComptageReponse
from openapi_server.models.comptage_request import ComptageRequest
from openapi_server.models.erreur import Erreur


pytestmark = pytest.mark.asyncio

async def test_comptage(client):
    """Test case for comptage

    Compter le nombre de caractère 
    """
    body = {"comptage":"1","emetteur":"iSendPro","keyid":"VOTRE_KEYID","num":"0600123456","sms":"Bonjour! Bienvenue sur iSendPro!"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/cgi-bin/comptage',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

