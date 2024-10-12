# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_search_committee_donations(client):
    """Test case for search_committee_donations

    Search API for 'Committee Donations' entry type
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
                    ('search.db_committee_donations.committee', 'search_db_committee_donations_committee_example'),
                    ('search.db_committee_donations.amount', 3.4),
                    ('search.db_committee_donations.recipient', 'search_db_committee_donations_recipient_example'),
                    ('search.db_committee_donations.date', 'search_db_committee_donations_date_example'),
                    ('search.db_committee_donations.city', 'search_db_committee_donations_city_example'),
                    ('search.db_committee_donations.state', 'search_db_committee_donations_state_example'),
                    ('search.db_committee_donations.zip_code', 'search_db_committee_donations_zip_code_example'),
                    ('search.db_committee_donations.employer', 'search_db_committee_donations_employer_example'),
                    ('search.db_committee_donations.occupation', 'search_db_committee_donations_occupation_example'),
                    ('search.db_committee_donations.location', 'search_db_committee_donations_location_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/repository/search/type/committee_donations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

