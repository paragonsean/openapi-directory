# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_search_boulder_consulting_services(client):
    """Test case for search_boulder_consulting_services

    Search API for 'Boulder Consulting Services Database' entry type
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
                    ('search.db_boulder_consulting_services.fund', 'search_db_boulder_consulting_services_fund_example'),
                    ('search.db_boulder_consulting_services.department', 'search_db_boulder_consulting_services_department_example'),
                    ('search.db_boulder_consulting_services.organization', 'search_db_boulder_consulting_services_organization_example'),
                    ('search.db_boulder_consulting_services.object', 'search_db_boulder_consulting_services_object_example'),
                    ('search.db_boulder_consulting_services.project', 'search_db_boulder_consulting_services_project_example'),
                    ('search.db_boulder_consulting_services.account_description', 'search_db_boulder_consulting_services_account_description_example'),
                    ('search.db_boulder_consulting_services.date', 'search_db_boulder_consulting_services_date_example'),
                    ('search.db_boulder_consulting_services.amount', 3.4),
                    ('search.db_boulder_consulting_services.purchase_order', 'search_db_boulder_consulting_services_purchase_order_example'),
                    ('search.db_boulder_consulting_services.vendor_name', 'search_db_boulder_consulting_services_vendor_name_example'),
                    ('search.db_boulder_consulting_services.comment', 'search_db_boulder_consulting_services_comment_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/repository/search/type/boulder_consulting_services',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

