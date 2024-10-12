# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_api_v20_database_scheme_sts_get(client):
    """Test case for api_v20_database_scheme_sts_get

    
    """
    params = [('barcode', ['barcode_example']),
                    ('st_id', 'st_id_example'),
                    ('offset', 0),
                    ('show_alleles', True),
                    ('only_fields', ['only_fields_example']),
                    ('reldate', 56),
                    ('limit', 50),
                    ('scheme', 'scheme_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v2.0/{database}/{scheme}/sts'.format(database='database_example', scheme2='scheme_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

