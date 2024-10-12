# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.abschlussbelegdaten import Abschlussbelegdaten
from openapi_server.models.beleg import Beleg
from openapi_server.models.belegdaten import Belegdaten
from openapi_server.models.belege import Belege


pytestmark = pytest.mark.asyncio

async def test_add_beleg(client):
    """Test case for add_beleg

    
    """
    body = {"Rabatte":[{"Betrag-Brutto":6,"Betrag-Netto":7,"Satz":"NORMAL","Bezeichnung":"Bezeichnung"},{"Betrag-Brutto":6,"Betrag-Netto":7,"Satz":"NORMAL","Bezeichnung":"Bezeichnung"}],"Unternehmen-Kopfzeile":"Unternehmen-Kopfzeile","Storno-Beleg-UUID":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","Unternehmen-Adresse1":"Unternehmen-Adresse1","Unternehmen-Adresse2":"Unternehmen-Adresse2","Notizen":["Notizen","Notizen"],"Externer-Beleg-Referenz":"Externer-Beleg-Referenz","Storno-Text":"Storno-Text","Training":True,"Unternehmen-Ort":"Unternehmen-Ort","Kunde":"Kunde","Unternehmen-ID-Typ":"steuernummer","Unternehmen-Name":"Unternehmen-Name","Zahlungen":[{"Betrag":1,"Referenz":"Referenz","Bezeichnung":"Bezeichnung"},{"Betrag":1,"Referenz":"Referenz","Bezeichnung":"Bezeichnung"}],"Externer-Beleg-Bezeichnung":"Externer-Beleg-Bezeichnung","Externer-Beleg-Belegkreis":"Externer-Beleg-Belegkreis","Unternehmen-Fusszeile":"Unternehmen-Fusszeile","Posten":[{"Satz":"NORMAL","NettoBetrag":1,"Externer-Beleg-Bezeichnung":"Externer-Beleg-Bezeichnung","Externer-Beleg-Belegkreis":"Externer-Beleg-Belegkreis","Menge":1,"BruttoBetrag":1,"Externer-Beleg-Referenz":"Externer-Beleg-Referenz","Bezeichnung":"Bezeichnung"},{"Satz":"NORMAL","NettoBetrag":1,"Externer-Beleg-Bezeichnung":"Externer-Beleg-Bezeichnung","Externer-Beleg-Belegkreis":"Externer-Beleg-Belegkreis","Menge":1,"BruttoBetrag":1,"Externer-Beleg-Referenz":"Externer-Beleg-Referenz","Bezeichnung":"Bezeichnung"}],"Storno":True,"Unternehmen-ID":"Unternehmen-ID","Unternehmen-PLZ":"Unternehmen-PLZ"}
    headers = { 
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/registrierkassen/{registrierkasse_uuid}/belege/{beleg_uuid}'.format(registrierkasse_uuid='registrierkasse_uuid_example', beleg_uuid='beleg_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_belege_beleg_uuid_get(client):
    """Test case for belege_beleg_uuid_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/belege/{beleg_uuid}'.format(beleg_uuid='beleg_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_abschluss(client):
    """Test case for create_abschluss

    
    """
    body = {"Abschluss-Beginn-Datum-Uhrzeit":"Abschluss-Beginn-Datum-Uhrzeit","Abschluss-Ende-Datum-Uhrzeit":"Abschluss-Ende-Datum-Uhrzeit"}
    headers = { 
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/registrierkassen/{registrierkasse_uuid}/abschluss'.format(registrierkasse_uuid='registrierkasse_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_beleg(client):
    """Test case for get_beleg

    
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/registrierkassen/{registrierkasse_uuid}/belege/{beleg_uuid}'.format(registrierkasse_uuid='registrierkasse_uuid_example', beleg_uuid='beleg_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_belege(client):
    """Test case for get_belege

    
    """
    params = [('format', export),
                    ('order', asc),
                    ('limit', 56),
                    ('offset', 0),
                    ('before', 'before_example'),
                    ('after', 'after_example'),
                    ('gte', 56),
                    ('lte', 56)]
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/registrierkassen/{registrierkasse_uuid}/belege'.format(registrierkasse_uuid='registrierkasse_uuid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

