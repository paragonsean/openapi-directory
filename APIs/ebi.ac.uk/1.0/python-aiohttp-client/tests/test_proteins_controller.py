# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.proteins import Proteins


pytestmark = pytest.mark.asyncio

async def test_get_proteins_using_get(client):
    """Test case for get_proteins_using_get

    Proteins collected from Uniprot for selective tax ids  HUMAN(9606), MOUSE(10090), RAT(10116), BOVINE(9913), ESCHERICHIA_COLI(83333), SUS_SCROFA(9823), MYCOBACTERIUM_TUBERCULOSIS(83332), ORYCTOLAGUS_CUNICULUS(9986), SACCHAROMYCES_CEREVISIAE(559292), CVHSA(694009) & SARS2(2697049)
    """
    params = [('accession', ['accession_example']),
                    ('ec', ['ec_example']),
                    ('fullName', ['full_name_example']),
                    ('gene', ['gene_example']),
                    ('go', ['go_example']),
                    ('interpro', ['interpro_example']),
                    ('limit', 10),
                    ('omim', ['omim_example']),
                    ('orphanet', ['orphanet_example']),
                    ('page', 0),
                    ('pfam', ['pfam_example']),
                    ('reactome', ['reactome_example']),
                    ('taxId', [56])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Tools/crossbar/proteins',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

