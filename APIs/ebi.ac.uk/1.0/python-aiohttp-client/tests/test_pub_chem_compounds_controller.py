# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.pubchem_compounds import PubchemCompounds


pytestmark = pytest.mark.asyncio

async def test_get_compounds_using_get(client):
    """Test case for get_compounds_using_get

    Get pubchem compounds
    """
    params = [('canonicalSmiles', ['canonical_smiles_example']),
                    ('cid', ['cid_example']),
                    ('inchiKey', ['inchi_key_example']),
                    ('limit', 10),
                    ('page', 0)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Tools/crossbar/pubchem/compounds',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

