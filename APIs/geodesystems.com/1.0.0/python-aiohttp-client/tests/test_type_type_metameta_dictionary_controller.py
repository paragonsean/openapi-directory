# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_search_type_metameta_dictionary(client):
    """Test case for search_type_metameta_dictionary

    Search API for 'Metadata Dictionary' entry type
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
                    ('search.type_metameta_dictionary.field_index', 56),
                    ('search.type_metameta_dictionary.dictionary_type', 'search_type_metameta_dictionary_dictionary_type_example'),
                    ('search.type_metameta_dictionary.short_name', 'search_type_metameta_dictionary_short_name_example'),
                    ('search.type_metameta_dictionary.super_type', 'search_type_metameta_dictionary_super_type_example'),
                    ('search.type_metameta_dictionary.isgroup', True),
                    ('search.type_metameta_dictionary.handler_class', 'search_type_metameta_dictionary_handler_class_example'),
                    ('search.type_metameta_dictionary.properties', 'search_type_metameta_dictionary_properties_example'),
                    ('search.type_metameta_dictionary.wiki_text', 'search_type_metameta_dictionary_wiki_text_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/repository/search/type/type_metameta_dictionary',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

