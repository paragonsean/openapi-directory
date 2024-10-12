# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_search_property_sales(client):
    """Test case for search_property_sales

    Search API for 'Property Sales' entry type
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
                    ('search.db_property_sales.property_address', 'search_db_property_sales_property_address_example'),
                    ('search.db_property_sales.city', 'search_db_property_sales_city_example'),
                    ('search.db_property_sales.zipcode', 'search_db_property_sales_zipcode_example'),
                    ('search.db_property_sales.sale_price', 3.4),
                    ('search.db_property_sales.sale_date', 'search_db_property_sales_sale_date_example'),
                    ('search.db_property_sales.seller', 'search_db_property_sales_seller_example'),
                    ('search.db_property_sales.buyer', 'search_db_property_sales_buyer_example'),
                    ('search.db_property_sales.type', 'search_db_property_sales_type_example'),
                    ('search.db_property_sales.building_description', 'search_db_property_sales_building_description_example'),
                    ('search.db_property_sales.building_design', 'search_db_property_sales_building_design_example'),
                    ('search.db_property_sales.subdivision', 'search_db_property_sales_subdivision_example'),
                    ('search.db_property_sales.location', 'search_db_property_sales_location_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/repository/search/type/property_sales',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

