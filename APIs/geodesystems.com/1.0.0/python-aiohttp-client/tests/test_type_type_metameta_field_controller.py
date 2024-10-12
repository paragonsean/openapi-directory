# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_search_type_metameta_field(client):
    """Test case for search_type_metameta_field

    Search API for 'Metadata Field' entry type
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
                    ('search.type_metameta_field.field_index', 56),
                    ('search.type_metameta_field.field_id', 'search_type_metameta_field_field_id_example'),
                    ('search.type_metameta_field.datatype', 'search_type_metameta_field_datatype_example'),
                    ('search.type_metameta_field.enumeration_values', 'search_type_metameta_field_enumeration_values_example'),
                    ('search.type_metameta_field.properties', 'search_type_metameta_field_properties_example'),
                    ('search.type_metameta_field.database_column_size', 56),
                    ('search.type_metameta_field.missing', 'search_type_metameta_field_missing_example'),
                    ('search.type_metameta_field.unit', 'search_type_metameta_field_unit_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/repository/search/type/type_metameta_field',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

