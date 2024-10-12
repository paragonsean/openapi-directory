# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_search_boulder2017_election_contributions(client):
    """Test case for search_boulder2017_election_contributions

    Search API for 'Boulder 2017 Election Contributions' entry type
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
                    ('search.db_boulder_2017_election_contributions.committee', 'search_db_boulder_2017_election_contributions_committee_example'),
                    ('search.db_boulder_2017_election_contributions.last_name', 'search_db_boulder_2017_election_contributions_last_name_example'),
                    ('search.db_boulder_2017_election_contributions.first_name', 'search_db_boulder_2017_election_contributions_first_name_example'),
                    ('search.db_boulder_2017_election_contributions.street', 'search_db_boulder_2017_election_contributions_street_example'),
                    ('search.db_boulder_2017_election_contributions.city', 'search_db_boulder_2017_election_contributions_city_example'),
                    ('search.db_boulder_2017_election_contributions.state', 'search_db_boulder_2017_election_contributions_state_example'),
                    ('search.db_boulder_2017_election_contributions.zip', 'search_db_boulder_2017_election_contributions_zip_example'),
                    ('search.db_boulder_2017_election_contributions.contribution_type', 'search_db_boulder_2017_election_contributions_contribution_type_example'),
                    ('search.db_boulder_2017_election_contributions.from_candidate', 'search_db_boulder_2017_election_contributions_from_candidate_example'),
                    ('search.db_boulder_2017_election_contributions.date', 'search_db_boulder_2017_election_contributions_date_example'),
                    ('search.db_boulder_2017_election_contributions.amount', 3.4),
                    ('search.db_boulder_2017_election_contributions.match_amount', 3.4),
                    ('search.db_boulder_2017_election_contributions.ytd_amount', 3.4),
                    ('search.db_boulder_2017_election_contributions.location', 'search_db_boulder_2017_election_contributions_location_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/repository/search/type/boulder_2017_election_contributions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

