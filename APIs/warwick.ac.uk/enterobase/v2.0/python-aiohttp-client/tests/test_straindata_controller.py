# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_api_v20_database_straindata_get(client):
    """Test case for api_v20_database_straindata_get

    
    """
    params = [('continent', 'continent_example'),
                    ('offset', 0),
                    ('sample_accession', 'sample_accession_example'),
                    ('latitude', 3.4),
                    ('collection_month', 56),
                    ('strain_name', 'strain_name_example'),
                    ('lab_contact', 'lab_contact_example'),
                    ('sortorder', 'asc'),
                    ('n50', 56),
                    ('limit', 50),
                    ('serotype', 'serotype_example'),
                    ('region', 'region_example'),
                    ('country', 'country_example'),
                    ('collection_date', 56),
                    ('custom_fields', 'custom_fields_example'),
                    ('only_fields', ['only_fields_example']),
                    ('source_niche', 'source_niche_example'),
                    ('collection_year', 56),
                    ('secondary_sample_accession', 'secondary_sample_accession_example'),
                    ('source_details', 'source_details_example'),
                    ('substrains', True),
                    ('version', 56),
                    ('source_type', 'source_type_example'),
                    ('orderby', 'orderby_example'),
                    ('my_strains', True),
                    ('collection_time', 'collection_time_example'),
                    ('county', 'county_example'),
                    ('uberstrain', 'uberstrain_example'),
                    ('top_species', 'top_species_example'),
                    ('comment', 'comment_example'),
                    ('longitude', 3.4),
                    ('reldate', 56),
                    ('barcode', ['barcode_example']),
                    ('postcode', 'postcode_example'),
                    ('email', 'email_example'),
                    ('assembly_status', 'assembly_status_example'),
                    ('city', 'city_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v2.0/{database}/straindata'.format(database='database_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

