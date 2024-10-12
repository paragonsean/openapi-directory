# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_search_campaign_expenditures(client):
    """Test case for search_campaign_expenditures

    Search API for 'Campaign Expenditures' entry type
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
                    ('search.db_campaign_expenditures.committee', 'search_db_campaign_expenditures_committee_example'),
                    ('search.db_campaign_expenditures.amount', 3.4),
                    ('search.db_campaign_expenditures.party', 'search_db_campaign_expenditures_party_example'),
                    ('search.db_campaign_expenditures.recipient', 'search_db_campaign_expenditures_recipient_example'),
                    ('search.db_campaign_expenditures.city', 'search_db_campaign_expenditures_city_example'),
                    ('search.db_campaign_expenditures.state', 'search_db_campaign_expenditures_state_example'),
                    ('search.db_campaign_expenditures.zip_code', 'search_db_campaign_expenditures_zip_code_example'),
                    ('search.db_campaign_expenditures.transaction_date', 'search_db_campaign_expenditures_transaction_date_example'),
                    ('search.db_campaign_expenditures.purpose', 'search_db_campaign_expenditures_purpose_example'),
                    ('search.db_campaign_expenditures.memo_text', 'search_db_campaign_expenditures_memo_text_example'),
                    ('search.db_campaign_expenditures.location', 'search_db_campaign_expenditures_location_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/repository/search/type/campaign_expenditures',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

