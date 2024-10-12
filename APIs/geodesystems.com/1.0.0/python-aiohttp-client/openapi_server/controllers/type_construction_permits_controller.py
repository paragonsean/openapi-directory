from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def search_construction_permits(request: web.Request, text=None, name=None, description=None, fromdate=None, todate=None, createdate_from=None, createdate_to=None, changedate_from=None, changedate_to=None, group=None, filesuffix=None, maxlatitude=None, minlongitude=None, minlatitude=None, maxlongitude=None, max=None, skip=None, search_db_construction_permits_address=None, search_db_construction_permits_case_status=None, search_db_construction_permits_category=None, search_db_construction_permits_building_uses_and_work_scopes=None, search_db_construction_permits_permit_types=None, search_db_construction_permits_total_project_value=None, search_db_construction_permits_total_subpermit_value=None, search_db_construction_permits_applied=None, search_db_construction_permits_approved=None, search_db_construction_permits_issued=None, search_db_construction_permits_co_date=None, search_db_construction_permits_completion_date=None, search_db_construction_permits_new_res_unit=None, search_db_construction_permits_existing_res_unit=None, search_db_construction_permits_affordable_hsg_unit=None, search_db_construction_permits_new_sf=None, search_db_construction_permits_remodel_sf=None, search_db_construction_permits_narrative_description=None, search_db_construction_permits_primary_first_name=None, search_db_construction_permits_primary_last_name=None, search_db_construction_permits_primary_company=None, search_db_construction_permits_contractor_first_name=None, search_db_construction_permits_contractor_last_name=None, search_db_construction_permits_contractor_company=None, search_db_construction_permits_owner1_first_name=None, search_db_construction_permits_owner1_last_name=None, search_db_construction_permits_owner1_company=None, search_db_construction_permits_owner2_first_name=None, search_db_construction_permits_owner2_last_name=None, search_db_construction_permits_owner2_company=None) -> web.Response:
    """Search API for &#39;Construction Permits&#39; entry type

    API to search for entries of type Construction Permits

    :param text: Search text
    :type text: str
    :param name: Search name
    :type name: str
    :param description: Search description
    :type description: str
    :param fromdate: From date
    :type fromdate: str
    :param todate: To date
    :type todate: str
    :param createdate_from: Archive create date from
    :type createdate_from: str
    :param createdate_to: Archive create date to
    :type createdate_to: str
    :param changedate_from: Archive change date from
    :type changedate_from: str
    :param changedate_to: Archive change date to
    :type changedate_to: str
    :param group: Parent entry
    :type group: str
    :param filesuffix: File suffix
    :type filesuffix: str
    :param maxlatitude: Northern bounds of search
    :type maxlatitude: float
    :param minlongitude: Western bounds of search
    :type minlongitude: float
    :param minlatitude: Southern bounds of search
    :type minlatitude: float
    :param maxlongitude: Eastern bounds of search
    :type maxlongitude: float
    :param max: Max number of results
    :type max: int
    :param skip: Number to skip
    :type skip: int
    :param search_db_construction_permits_address: Address
    :type search_db_construction_permits_address: str
    :param search_db_construction_permits_case_status: Case Status
    :type search_db_construction_permits_case_status: str
    :param search_db_construction_permits_category: Category
    :type search_db_construction_permits_category: str
    :param search_db_construction_permits_building_uses_and_work_scopes: Building Uses And Work Scopes
    :type search_db_construction_permits_building_uses_and_work_scopes: str
    :param search_db_construction_permits_permit_types: Permit Types
    :type search_db_construction_permits_permit_types: str
    :param search_db_construction_permits_total_project_value: Total Project Value
    :type search_db_construction_permits_total_project_value: float
    :param search_db_construction_permits_total_subpermit_value: Total Subpermit Value
    :type search_db_construction_permits_total_subpermit_value: float
    :param search_db_construction_permits_applied: Applied
    :type search_db_construction_permits_applied: str
    :param search_db_construction_permits_approved: Approved
    :type search_db_construction_permits_approved: str
    :param search_db_construction_permits_issued: Issued
    :type search_db_construction_permits_issued: str
    :param search_db_construction_permits_co_date: Co Date
    :type search_db_construction_permits_co_date: str
    :param search_db_construction_permits_completion_date: Completion Date
    :type search_db_construction_permits_completion_date: str
    :param search_db_construction_permits_new_res_unit: New Res Unit
    :type search_db_construction_permits_new_res_unit: int
    :param search_db_construction_permits_existing_res_unit: Existing Res Unit
    :type search_db_construction_permits_existing_res_unit: int
    :param search_db_construction_permits_affordable_hsg_unit: Affordable Hsg Unit
    :type search_db_construction_permits_affordable_hsg_unit: int
    :param search_db_construction_permits_new_sf: New Sf
    :type search_db_construction_permits_new_sf: int
    :param search_db_construction_permits_remodel_sf: Remodel Sf
    :type search_db_construction_permits_remodel_sf: int
    :param search_db_construction_permits_narrative_description: Narrative Description
    :type search_db_construction_permits_narrative_description: str
    :param search_db_construction_permits_primary_first_name: Primary First Name
    :type search_db_construction_permits_primary_first_name: str
    :param search_db_construction_permits_primary_last_name: Primary Last Name
    :type search_db_construction_permits_primary_last_name: str
    :param search_db_construction_permits_primary_company: Primary Company
    :type search_db_construction_permits_primary_company: str
    :param search_db_construction_permits_contractor_first_name: Contractor First Name
    :type search_db_construction_permits_contractor_first_name: str
    :param search_db_construction_permits_contractor_last_name: Contractor Last Name
    :type search_db_construction_permits_contractor_last_name: str
    :param search_db_construction_permits_contractor_company: Contractor Company
    :type search_db_construction_permits_contractor_company: str
    :param search_db_construction_permits_owner1_first_name: Owner1 First Name
    :type search_db_construction_permits_owner1_first_name: str
    :param search_db_construction_permits_owner1_last_name: Owner1 Last Name
    :type search_db_construction_permits_owner1_last_name: str
    :param search_db_construction_permits_owner1_company: Owner1 Company
    :type search_db_construction_permits_owner1_company: str
    :param search_db_construction_permits_owner2_first_name: Owner2 First Name
    :type search_db_construction_permits_owner2_first_name: str
    :param search_db_construction_permits_owner2_last_name: Owner2 Last Name
    :type search_db_construction_permits_owner2_last_name: str
    :param search_db_construction_permits_owner2_company: Owner2 Company
    :type search_db_construction_permits_owner2_company: str

    """
    fromdate = util.deserialize_datetime(fromdate)
    todate = util.deserialize_datetime(todate)
    createdate_from = util.deserialize_datetime(createdate_from)
    createdate_to = util.deserialize_datetime(createdate_to)
    changedate_from = util.deserialize_datetime(changedate_from)
    changedate_to = util.deserialize_datetime(changedate_to)
    return web.Response(status=200)
