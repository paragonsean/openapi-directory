# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.molecules import Molecules


pytestmark = pytest.mark.asyncio

async def test_get_molecules_using_get(client):
    """Test case for get_molecules_using_get

    Get ChEMBL molecules
    """
    params = [('canonicalSmiles', ['canonical_smiles_example']),
                    ('inchiKey', ['inchi_key_example']),
                    ('limit', 10),
                    ('moleculeChemblId', ['molecule_chembl_id_example']),
                    ('page', 0)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Tools/crossbar/molecules',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

