# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.erreur import Erreur
from openapi_server.models.repertoir_ecreatereponse import REPERTOIREcreatereponse
from openapi_server.models.repertoir_ecreaterequest import REPERTOIREcreaterequest
from openapi_server.models.repertoir_emodifreponse import REPERTOIREmodifreponse
from openapi_server.models.repertoir_emodifrequest import REPERTOIREmodifrequest


pytestmark = pytest.mark.asyncio

async def test_repertoire(client):
    """Test case for repertoire

    Gestion repertoire (modification)
    """
    body = {"keyid":"VOTRE_KEYID","num":["06123456789","07123456789"],"repertoireEdit":"add","repertoireId":"VOTRE_REPERTOIRE_ID"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/cgi-bin/repertoire',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repertoire_crea(client):
    """Test case for repertoire_crea

    Gestion repertoire (creation)
    """
    body = {"keyid":"VOTRE_KEYID","repertoireEdit":"create","repertoireNom":"Repertoire de test"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/cgi-bin/repertoire',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

