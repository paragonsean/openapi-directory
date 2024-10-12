# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_search_community_resource(client):
    """Test case for search_community_resource

    Search API for 'Facility' entry type
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
                    ('search.community_resource.resource_type', 'search_community_resource_resource_type_example'),
                    ('search.community_resource.address', 'search_community_resource_address_example'),
                    ('search.community_resource.city', 'search_community_resource_city_example'),
                    ('search.community_resource.state', 'search_community_resource_state_example'),
                    ('search.community_resource.zipcode', 'search_community_resource_zipcode_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/repository/search/type/community_resource',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

