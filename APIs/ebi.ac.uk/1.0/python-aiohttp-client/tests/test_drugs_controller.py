# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.drugs import Drugs


pytestmark = pytest.mark.asyncio

async def test_get_drugs_using_get(client):
    """Test case for get_drugs_using_get

    drugs collected from Drugbank
    """
    params = [('accession', ['accession_example']),
                    ('chemblId', ['chembl_id_example']),
                    ('identifier', ['identifier_example']),
                    ('limit', 10),
                    ('name', ['name_example']),
                    ('page', 0),
                    ('pubchemCid', ['pubchem_cid_example'])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Tools/crossbar/drugs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

