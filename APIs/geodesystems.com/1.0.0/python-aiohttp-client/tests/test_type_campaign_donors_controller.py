# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_search_campaign_donors(client):
    """Test case for search_campaign_donors

    Search API for 'Campaign Donors' entry type
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
                    ('search.db_campaign_donors.committee', 'search_db_campaign_donors_committee_example'),
                    ('search.db_campaign_donors.amount', 3.4),
                    ('search.db_campaign_donors.party', 'search_db_campaign_donors_party_example'),
                    ('search.db_campaign_donors.donor', 'search_db_campaign_donors_donor_example'),
                    ('search.db_campaign_donors.gender', 'search_db_campaign_donors_gender_example'),
                    ('search.db_campaign_donors.city', 'search_db_campaign_donors_city_example'),
                    ('search.db_campaign_donors.state', 'search_db_campaign_donors_state_example'),
                    ('search.db_campaign_donors.zip_code', 'search_db_campaign_donors_zip_code_example'),
                    ('search.db_campaign_donors.employer', 'search_db_campaign_donors_employer_example'),
                    ('search.db_campaign_donors.occupation', 'search_db_campaign_donors_occupation_example'),
                    ('search.db_campaign_donors.date', 'search_db_campaign_donors_date_example'),
                    ('search.db_campaign_donors.location', 'search_db_campaign_donors_location_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/repository/search/type/campaign_donors',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

