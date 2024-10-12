# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_v20_database_strains_barcode_get_request import ApiV20DatabaseStrainsBarcodeGetRequest


pytestmark = pytest.mark.asyncio

async def test_api_v20_database_strains_barcode_get(client):
    """Test case for api_v20_database_strains_barcode_get

    
    """
    body = openapi_server.ApiV20DatabaseStrainsBarcodeGetRequest()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2.0/{database}/strains/{barcode}'.format(database='database_example', barcode='barcode_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v20_database_strains_barcode_post(client):
    """Test case for api_v20_database_strains_barcode_post

    
    """
    body = openapi_server.ApiV20DatabaseStrainsBarcodeGetRequest()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2.0/{database}/strains/{barcode}'.format(database='database_example', barcode='barcode_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v20_database_strains_barcode_put(client):
    """Test case for api_v20_database_strains_barcode_put

    
    """
    body = openapi_server.ApiV20DatabaseStrainsBarcodeGetRequest()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2.0/{database}/strains/{barcode}'.format(database='database_example', barcode='barcode_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v20_database_strains_get(client):
    """Test case for api_v20_database_strains_get

    
    """
    params = [('continent', 'continent_example'),
                    ('offset', 0),
                    ('sample_accession', 'sample_accession_example'),
                    ('latitude', 3.4),
                    ('collection_month', 56),
                    ('antigenic_formulas', 'antigenic_formulas_example'),
                    ('strain_name', 'strain_name_example'),
                    ('lab_contact', 'lab_contact_example'),
                    ('sortorder', 'asc'),
                    ('limit', 50),
                    ('serotype', 'serotype_example'),
                    ('region', 'region_example'),
                    ('country', 'country_example'),
                    ('collection_date', 56),
                    ('return_all', True),
                    ('only_fields', ['only_fields_example']),
                    ('source_niche', 'source_niche_example'),
                    ('collection_year', 56),
                    ('secondary_sample_accession', 'secondary_sample_accession_example'),
                    ('source_details', 'source_details_example'),
                    ('substrains', True),
                    ('version', 56),
                    ('source_type', 'source_type_example'),
                    ('orderby', 'barcode'),
                    ('my_strains', True),
                    ('collection_time', 'collection_time_example'),
                    ('county', 'county_example'),
                    ('uberstrain', 'uberstrain_example'),
                    ('comment', 'comment_example'),
                    ('longitude', 3.4),
                    ('reldate', 56),
                    ('assembly_barcode', 'assembly_barcode_example'),
                    ('barcode', ['barcode_example']),
                    ('postcode', 'postcode_example'),
                    ('city', 'city_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v2.0/{database}/strains'.format(database='database_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

