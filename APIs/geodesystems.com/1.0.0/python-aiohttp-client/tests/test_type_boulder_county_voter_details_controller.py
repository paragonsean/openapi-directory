# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_search_boulder_county_voter_details(client):
    """Test case for search_boulder_county_voter_details

    Search API for 'Boulder County Voter Details' entry type
    """
    params = [('text', 'text_example'),
                    ('name', 'name_example'),
                    ('description', 'description_example'),
                    ('fromdate', '2013-10-20T19:20:30+01:00'),
                    ('todate', '2013-10-20T19:20:30+01:00'),
                    ('createdate.from', '2013-10-20T19:20:30+01:00'),
                    ('createdate.to', '2013-10-20T19:20:30+01:00'),
                    ('changedate.from', '2013-10-20T19:20:30+01:00'),
                    ('changedate.to', '2013-10-20T19:20:30+01:00'),
                    ('group', 'group_example'),
                    ('filesuffix', 'filesuffix_example'),
                    ('maxlatitude', 3.4),
                    ('minlongitude', 3.4),
                    ('minlatitude', 3.4),
                    ('maxlongitude', 3.4),
                    ('max', 56),
                    ('skip', 56),
                    ('search.db_boulder_county_voter_details.first_name', 'search_db_boulder_county_voter_details_first_name_example'),
                    ('search.db_boulder_county_voter_details.last_name', 'search_db_boulder_county_voter_details_last_name_example'),
                    ('search.db_boulder_county_voter_details.registration_date', 'search_db_boulder_county_voter_details_registration_date_example'),
                    ('search.db_boulder_county_voter_details.last_updated_date', 'search_db_boulder_county_voter_details_last_updated_date_example'),
                    ('search.db_boulder_county_voter_details.residential_address', 'search_db_boulder_county_voter_details_residential_address_example'),
                    ('search.db_boulder_county_voter_details.residential_city', 'search_db_boulder_county_voter_details_residential_city_example'),
                    ('search.db_boulder_county_voter_details.mailing_zip_code', 'search_db_boulder_county_voter_details_mailing_zip_code_example'),
                    ('search.db_boulder_county_voter_details.voter_status', 'search_db_boulder_county_voter_details_voter_status_example'),
                    ('search.db_boulder_county_voter_details.party', 'search_db_boulder_county_voter_details_party_example'),
                    ('search.db_boulder_county_voter_details.gender', 'search_db_boulder_county_voter_details_gender_example'),
                    ('search.db_boulder_county_voter_details.birth_year', 56),
                    ('search.db_boulder_county_voter_details.precinct_code', 'search_db_boulder_county_voter_details_precinct_code_example'),
                    ('search.db_boulder_county_voter_details.congressional', 'search_db_boulder_county_voter_details_congressional_example'),
                    ('search.db_boulder_county_voter_details.state_senate', 'search_db_boulder_county_voter_details_state_senate_example'),
                    ('search.db_boulder_county_voter_details.state_house', 'search_db_boulder_county_voter_details_state_house_example'),
                    ('search.db_boulder_county_voter_details.municipality', 'search_db_boulder_county_voter_details_municipality_example'),
                    ('search.db_boulder_county_voter_details.city_ward_district', 'search_db_boulder_county_voter_details_city_ward_district_example'),
                    ('search.db_boulder_county_voter_details.school_district', 'search_db_boulder_county_voter_details_school_district_example'),
                    ('search.db_boulder_county_voter_details.location', 'search_db_boulder_county_voter_details_location_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/repository/search/type/boulder_county_voter_details',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

