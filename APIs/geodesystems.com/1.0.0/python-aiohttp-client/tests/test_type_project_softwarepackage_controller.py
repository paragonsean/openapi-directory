# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_search_project_softwarepackage(client):
    """Test case for search_project_softwarepackage

    Search API for 'Software Tool' entry type
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
                    ('search.project_softwarepackage.software_use', 'search_project_softwarepackage_software_use_example'),
                    ('search.project_softwarepackage.software_type', 'search_project_softwarepackage_software_type_example'),
                    ('search.project_softwarepackage.domain', 'search_project_softwarepackage_domain_example'),
                    ('search.project_softwarepackage.platform', 'search_project_softwarepackage_platform_example'),
                    ('search.project_softwarepackage.license', 'search_project_softwarepackage_license_example'),
                    ('search.project_softwarepackage.status', 'search_project_softwarepackage_status_example'),
                    ('search.project_softwarepackage.capabilities', 'search_project_softwarepackage_capabilities_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/repository/search/type/project_softwarepackage',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

