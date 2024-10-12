# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_search_bolder_rental_housing(client):
    """Test case for search_bolder_rental_housing

    Search API for 'Boulder Rental Housing' entry type
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
                    ('search.db_bolder_rental_housing.propaddr1', 'search_db_bolder_rental_housing_propaddr1_example'),
                    ('search.db_bolder_rental_housing.rentaltype', 'search_db_bolder_rental_housing_rentaltype_example'),
                    ('search.db_bolder_rental_housing.bldgtype', 'search_db_bolder_rental_housing_bldgtype_example'),
                    ('search.db_bolder_rental_housing.dwellunits', 56),
                    ('search.db_bolder_rental_housing.roomunits', 56),
                    ('search.db_bolder_rental_housing.neighbrhd', 'search_db_bolder_rental_housing_neighbrhd_example'),
                    ('search.db_bolder_rental_housing.complexnm', 'search_db_bolder_rental_housing_complexnm_example'),
                    ('search.db_bolder_rental_housing.name', 'search_db_bolder_rental_housing_name_example'),
                    ('search.db_bolder_rental_housing.persontype', 'search_db_bolder_rental_housing_persontype_example'),
                    ('search.db_bolder_rental_housing.company', 'search_db_bolder_rental_housing_company_example'),
                    ('search.db_bolder_rental_housing.engcompl', 'search_db_bolder_rental_housing_engcompl_example'),
                    ('search.db_bolder_rental_housing.licenseexp', 'search_db_bolder_rental_housing_licenseexp_example'),
                    ('search.db_bolder_rental_housing.licensenum', 'search_db_bolder_rental_housing_licensenum_example'),
                    ('search.db_bolder_rental_housing.ppl1_coname', 'search_db_bolder_rental_housing_ppl1_coname_example'),
                    ('search.db_bolder_rental_housing.person_1', 'search_db_bolder_rental_housing_person_1_example'),
                    ('search.db_bolder_rental_housing.ppl1_role', 'search_db_bolder_rental_housing_ppl1_role_example'),
                    ('search.db_bolder_rental_housing.ppl2_coname', 'search_db_bolder_rental_housing_ppl2_coname_example'),
                    ('search.db_bolder_rental_housing.person_2', 'search_db_bolder_rental_housing_person_2_example'),
                    ('search.db_bolder_rental_housing.ppl2_role', 'search_db_bolder_rental_housing_ppl2_role_example'),
                    ('search.db_bolder_rental_housing.location', 'search_db_bolder_rental_housing_location_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/repository/search/type/bolder_rental_housing',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

