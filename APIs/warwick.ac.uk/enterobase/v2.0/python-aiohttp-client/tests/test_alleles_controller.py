# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_api_v20_database_scheme_alleles_get(client):
    """Test case for api_v20_database_scheme_alleles_get

    
    """
    params = [('barcode', ['barcode_example']),
                    ('locus', 'locus_example'),
                    ('offset', 0),
                    ('allele_id', 'allele_id_example'),
                    ('only_fields', ['only_fields_example']),
                    ('seq', 'seq_example'),
                    ('reldate', 56),
                    ('limit', 50)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v2.0/{database}/{scheme}/alleles'.format(database='database_example', scheme='scheme_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

