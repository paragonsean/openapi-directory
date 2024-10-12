# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_search_construction_permits(client):
    """Test case for search_construction_permits

    Search API for 'Construction Permits' entry type
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
                    ('search.db_construction_permits.address', 'search_db_construction_permits_address_example'),
                    ('search.db_construction_permits.case_status', 'search_db_construction_permits_case_status_example'),
                    ('search.db_construction_permits.category', 'search_db_construction_permits_category_example'),
                    ('search.db_construction_permits.building_uses_and_work_scopes', 'search_db_construction_permits_building_uses_and_work_scopes_example'),
                    ('search.db_construction_permits.permit_types', 'search_db_construction_permits_permit_types_example'),
                    ('search.db_construction_permits.total_project_value', 3.4),
                    ('search.db_construction_permits.total_subpermit_value', 3.4),
                    ('search.db_construction_permits.applied', 'search_db_construction_permits_applied_example'),
                    ('search.db_construction_permits.approved', 'search_db_construction_permits_approved_example'),
                    ('search.db_construction_permits.issued', 'search_db_construction_permits_issued_example'),
                    ('search.db_construction_permits.co_date', 'search_db_construction_permits_co_date_example'),
                    ('search.db_construction_permits.completion_date', 'search_db_construction_permits_completion_date_example'),
                    ('search.db_construction_permits.new_res_unit', 56),
                    ('search.db_construction_permits.existing_res_unit', 56),
                    ('search.db_construction_permits.affordable_hsg_unit', 56),
                    ('search.db_construction_permits.new_sf', 56),
                    ('search.db_construction_permits.remodel_sf', 56),
                    ('search.db_construction_permits.narrative_description', 'search_db_construction_permits_narrative_description_example'),
                    ('search.db_construction_permits.primary_first_name', 'search_db_construction_permits_primary_first_name_example'),
                    ('search.db_construction_permits.primary_last_name', 'search_db_construction_permits_primary_last_name_example'),
                    ('search.db_construction_permits.primary_company', 'search_db_construction_permits_primary_company_example'),
                    ('search.db_construction_permits.contractor_first_name', 'search_db_construction_permits_contractor_first_name_example'),
                    ('search.db_construction_permits.contractor_last_name', 'search_db_construction_permits_contractor_last_name_example'),
                    ('search.db_construction_permits.contractor_company', 'search_db_construction_permits_contractor_company_example'),
                    ('search.db_construction_permits.owner1_first_name', 'search_db_construction_permits_owner1_first_name_example'),
                    ('search.db_construction_permits.owner1_last_name', 'search_db_construction_permits_owner1_last_name_example'),
                    ('search.db_construction_permits.owner1_company', 'search_db_construction_permits_owner1_company_example'),
                    ('search.db_construction_permits.owner2_first_name', 'search_db_construction_permits_owner2_first_name_example'),
                    ('search.db_construction_permits.owner2_last_name', 'search_db_construction_permits_owner2_last_name_example'),
                    ('search.db_construction_permits.owner2_company', 'search_db_construction_permits_owner2_company_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/repository/search/type/construction_permits',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

