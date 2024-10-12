# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_search_jeopardy(client):
    """Test case for search_jeopardy

    Search API for 'Jeopardy' entry type
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
                    ('search.db_jeopardy.question', 'search_db_jeopardy_question_example'),
                    ('search.db_jeopardy.answer', 'search_db_jeopardy_answer_example'),
                    ('search.db_jeopardy.round', 'search_db_jeopardy_round_example'),
                    ('search.db_jeopardy.category', 'search_db_jeopardy_category_example'),
                    ('search.db_jeopardy.air_date', 'search_db_jeopardy_air_date_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/repository/search/type/jeopardy',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

