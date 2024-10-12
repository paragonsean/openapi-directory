# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.erreur import Erreur


pytestmark = pytest.mark.asyncio

async def test_get_liste_noire(client):
    """Test case for get_liste_noire

    Retourne le liste noire
    """
    params = [('keyid', 'keyid_example'),
                    ('getListeNoire', 'get_liste_noire_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/cgi-bin/getlistenoire',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

