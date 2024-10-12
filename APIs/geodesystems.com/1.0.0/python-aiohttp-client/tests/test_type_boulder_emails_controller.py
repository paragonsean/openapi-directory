# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_search_boulder_emails(client):
    """Test case for search_boulder_emails

    Search API for 'Boulder Council Emails' entry type
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
                    ('search.db_boulder_emails.sent_from', 'search_db_boulder_emails_sent_from_example'),
                    ('search.db_boulder_emails.sent_to', 'search_db_boulder_emails_sent_to_example'),
                    ('search.db_boulder_emails.sent_cc', 'search_db_boulder_emails_sent_cc_example'),
                    ('search.db_boulder_emails.received_date', 'search_db_boulder_emails_received_date_example'),
                    ('search.db_boulder_emails.email_subject', 'search_db_boulder_emails_email_subject_example'),
                    ('search.db_boulder_emails.plain_text_body', 'search_db_boulder_emails_plain_text_body_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/repository/search/type/boulder_emails',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

