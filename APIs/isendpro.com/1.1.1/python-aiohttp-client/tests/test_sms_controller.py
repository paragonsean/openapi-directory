# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.erreur import Erreur
from openapi_server.models.sms_reponse import SMSReponse
from openapi_server.models.sms_request import SMSRequest
from openapi_server.models.sms_unique_request import SmsUniqueRequest


pytestmark = pytest.mark.asyncio

async def test_send_sms(client):
    """Test case for send_sms

    Envoyer un sms
    """
    body = {"emetteur":"iSendPro","keyid":"VOTRE_KEYID","num":"0600123456","sms":"Bonjour! Bienvenue sur iSendPro!"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/cgi-bin/sms',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send_sms_multi(client):
    """Test case for send_sms_multi

    Envoyer des SMS
    """
    body = {"emetteur":"iSendPro","keyid":"VOTRE_KEYID","num":["0600123456","0612345678"],"sms":"Bonjour! Bienvenue sur iSendPro!"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/cgi-bin/smsmulti',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

