# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bioassays import Bioassays


pytestmark = pytest.mark.asyncio

async def test_get_bioassays_using_get(client):
    """Test case for get_bioassays_using_get

    Get pubchem bioassays
    """
    params = [('accession', ['accession_example']),
                    ('assayPubchemId', ['assay_pubchem_id_example']),
                    ('limit', 1),
                    ('ncbiProteinId', ['ncbi_protein_id_example']),
                    ('page', 0)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Tools/crossbar/pubchem/bioassays',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

