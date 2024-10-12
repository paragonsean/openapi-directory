# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_search2017_boulder_election_expenditures(client):
    """Test case for search2017_boulder_election_expenditures

    Search API for '2017 Boulder Election Expenditures' entry type
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
                    ('search.db_2017_boulder_election_expenditures.committee', 'search_db_2017_boulder_election_expenditures_committee_example'),
                    ('search.db_2017_boulder_election_expenditures.transaction_date', 'search_db_2017_boulder_election_expenditures_transaction_date_example'),
                    ('search.db_2017_boulder_election_expenditures.name', 'search_db_2017_boulder_election_expenditures_name_example'),
                    ('search.db_2017_boulder_election_expenditures.street', 'search_db_2017_boulder_election_expenditures_street_example'),
                    ('search.db_2017_boulder_election_expenditures.city', 'search_db_2017_boulder_election_expenditures_city_example'),
                    ('search.db_2017_boulder_election_expenditures.state', 'search_db_2017_boulder_election_expenditures_state_example'),
                    ('search.db_2017_boulder_election_expenditures.zip', 'search_db_2017_boulder_election_expenditures_zip_example'),
                    ('search.db_2017_boulder_election_expenditures.expenditure', 3.4),
                    ('search.db_2017_boulder_election_expenditures.purpose', 'search_db_2017_boulder_election_expenditures_purpose_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/repository/search/type/2017_boulder_election_expenditures',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

