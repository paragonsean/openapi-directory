# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_search_propertydb(client):
    """Test case for search_propertydb

    Search API for 'Property Database' entry type
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
                    ('search.db_propertydb.property_id', 'search_db_propertydb_property_id_example'),
                    ('search.db_propertydb.owner', 'search_db_propertydb_owner_example'),
                    ('search.db_propertydb.address', 'search_db_propertydb_address_example'),
                    ('search.db_propertydb.city', 'search_db_propertydb_city_example'),
                    ('search.db_propertydb.state', 'search_db_propertydb_state_example'),
                    ('search.db_propertydb.value', 56),
                    ('search.db_propertydb.building_type', 'search_db_propertydb_building_type_example'),
                    ('search.db_propertydb.house_size', 56),
                    ('search.db_propertydb.lot_sqft', 56),
                    ('search.db_propertydb.lot_acres', 3.4),
                    ('search.db_propertydb.price_sqft', 3.4),
                    ('search.db_propertydb.location', 'search_db_propertydb_location_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/repository/search/type/propertydb',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

