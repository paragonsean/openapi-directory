# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.erreur import Erreur


pytestmark = pytest.mark.asyncio

async def test_get_campagne(client):
    """Test case for get_campagne

    Retourne les SMS envoyés sur une période donnée
    """
    params = [('keyid', 'keyid_example'),
                    ('rapportCampagne', 'rapport_campagne_example'),
                    ('date_deb', 'date_deb_example'),
                    ('date_fin', 'date_fin_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/cgi-bin/campagne',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

