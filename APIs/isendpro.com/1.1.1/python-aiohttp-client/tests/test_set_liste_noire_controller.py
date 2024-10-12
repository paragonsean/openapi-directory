# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.erreur import Erreur
from openapi_server.models.listenoire_reponse import LISTENOIREReponse


pytestmark = pytest.mark.asyncio

async def test_set_liste_noire(client):
    """Test case for set_liste_noire

    Ajoute un numero en liste noire
    """
    params = [('keyid', 'keyid_example'),
                    ('setlisteNoire', 'setliste_noire_example'),
                    ('num', 'num_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/cgi-bin/setlistenoire',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

