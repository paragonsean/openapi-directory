# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_search_bio_taxonomy(client):
    """Test case for search_bio_taxonomy

    Search API for 'Taxonomic Entry' entry type
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
                    ('search.bio_taxonomy.rank', 'search_bio_taxonomy_rank_example'),
                    ('search.bio_taxonomy.embl_code', 'search_bio_taxonomy_embl_code_example'),
                    ('search.bio_taxonomy.division', 'search_bio_taxonomy_division_example'),
                    ('search.bio_taxonomy.inherited_div', True),
                    ('search.bio_taxonomy.aliases', 'search_bio_taxonomy_aliases_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/repository/search/type/bio_taxonomy',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

