from typing import List, Dict
from aiohttp import web

from openapi_server.models.exception_model import ExceptionModel
from openapi_server.models.license_user_type import LicenseUserType
from openapi_server.models.resource_allocation_criteria_model import ResourceAllocationCriteriaModel
from openapi_server.models.resource_allocation_output_model import ResourceAllocationOutputModel
from openapi_server.models.role_allocation_output_model import RoleAllocationOutputModel
from openapi_server.models.sales_progress import SalesProgress
from openapi_server import util


async def resource_allocations_get_resource_allocation(request: web.Request, guid) -> web.Response:
    """Get resource allocation by ID

    

    :param guid: GUID used to get the resource allocation.
    :type guid: str

    """
    return web.Response(status=200)


async def resource_allocations_get_resource_allocations(request: web.Request, row_count=None, page_token=None, changed_since=None) -> web.Response:
    """Get resource allocations

    

    :param row_count: Optional: Number of rows to fetch.
    :type row_count: int
    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param changed_since: Optional: Get resource allocations that have been added or changed after this date time (greater or equal).
    :type changed_since: str

    """
    changed_since = util.deserialize_datetime(changed_since)
    return web.Response(status=200)


async def resource_allocations_get_resource_allocations_by_phase_guid(request: web.Request, phase_guid, start_date=None, end_date=None, changed_since=None, user_license_types=None, project_guid=None, user_guid=None, project_business_unit_guid=None, user_business_unit_guid=None, project_manager_user_guid=None, user_tag_guid=None, use_sales_probability=None, project_status_type_guid=None, project_tag_guid=None, superior_user_guid=None, sales_status_type_guid=None, resource_allocation_guid=None, sales_progress=None, row_count=None, page_token=None) -> web.Response:
    """Get resource allocations for a phase with required filters (startDate and endDate or changedSince, max 30 days to be fetched at once)

    

    :param phase_guid: 
    :type phase_guid: str
    :param start_date: Get resource allocations with startDate. Using startDate and endDate or changedSince parameters are required to fetch a maximum of 30 days
    :type start_date: str
    :param end_date: Get resource allocations with endDate. Using startDate and endDate or changedSince parameters are required to fetch a maximum of 30 days
    :type end_date: str
    :param changed_since: Optional: Get resource allocations that have been added or changed after this date time (greater or equal).
    :type changed_since: str
    :param user_license_types: 
    :type user_license_types: list | bytes
    :param project_guid: 
    :type project_guid: str
    :param user_guid: 
    :type user_guid: str
    :param project_business_unit_guid: 
    :type project_business_unit_guid: str
    :param user_business_unit_guid: 
    :type user_business_unit_guid: str
    :param project_manager_user_guid: 
    :type project_manager_user_guid: str
    :param user_tag_guid: 
    :type user_tag_guid: str
    :param use_sales_probability: 
    :type use_sales_probability: bool
    :param project_status_type_guid: 
    :type project_status_type_guid: str
    :param project_tag_guid: 
    :type project_tag_guid: str
    :param superior_user_guid: 
    :type superior_user_guid: str
    :param sales_status_type_guid: 
    :type sales_status_type_guid: str
    :param resource_allocation_guid: 
    :type resource_allocation_guid: str
    :param sales_progress: 
    :type sales_progress: dict | bytes
    :param row_count: Optional: Number of rows to fetch.
    :type row_count: int
    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    changed_since = util.deserialize_datetime(changed_since)
    user_license_types = [LicenseUserType.from_dict(d) for d in user_license_types]
    sales_progress = .from_dict(sales_progress)
    return web.Response(status=200)


async def resource_allocations_get_resource_allocations_by_project_guid(request: web.Request, project_guid, start_date=None, end_date=None, changed_since=None, user_license_types=None, phase_guid=None, user_guid=None, project_business_unit_guid=None, user_business_unit_guid=None, project_manager_user_guid=None, user_tag_guid=None, use_sales_probability=None, project_status_type_guid=None, project_tag_guid=None, superior_user_guid=None, sales_status_type_guid=None, resource_allocation_guid=None, sales_progress=None, row_count=None, page_token=None) -> web.Response:
    """Get resource allocations for a project with required filters (startDate and endDate or changedSince, max 30 days to be fetched at once)

    

    :param project_guid: 
    :type project_guid: str
    :param start_date: Get resource allocations with startDate. Using startDate and endDate or changedSince parameters are required to fetch a maximum of 30 days
    :type start_date: str
    :param end_date: Get resource allocations with endDate. Using startDate and endDate or changedSince parameters are required to fetch a maximum of 30 days
    :type end_date: str
    :param changed_since: Optional: Get resource allocations that have been added or changed after this date time (greater or equal).
    :type changed_since: str
    :param user_license_types: 
    :type user_license_types: list | bytes
    :param phase_guid: 
    :type phase_guid: str
    :param user_guid: 
    :type user_guid: str
    :param project_business_unit_guid: 
    :type project_business_unit_guid: str
    :param user_business_unit_guid: 
    :type user_business_unit_guid: str
    :param project_manager_user_guid: 
    :type project_manager_user_guid: str
    :param user_tag_guid: 
    :type user_tag_guid: str
    :param use_sales_probability: 
    :type use_sales_probability: bool
    :param project_status_type_guid: 
    :type project_status_type_guid: str
    :param project_tag_guid: 
    :type project_tag_guid: str
    :param superior_user_guid: 
    :type superior_user_guid: str
    :param sales_status_type_guid: 
    :type sales_status_type_guid: str
    :param resource_allocation_guid: 
    :type resource_allocation_guid: str
    :param sales_progress: 
    :type sales_progress: dict | bytes
    :param row_count: Optional: Number of rows to fetch.
    :type row_count: int
    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    changed_since = util.deserialize_datetime(changed_since)
    user_license_types = [LicenseUserType.from_dict(d) for d in user_license_types]
    sales_progress = .from_dict(sales_progress)
    return web.Response(status=200)


async def resource_allocations_get_resource_allocations_by_user_guid(request: web.Request, user_guid, start_date=None, end_date=None, changed_since=None, user_license_types=None, phase_guid=None, project_guid=None, project_business_unit_guid=None, user_business_unit_guid=None, project_manager_user_guid=None, user_tag_guid=None, use_sales_probability=None, project_status_type_guid=None, project_tag_guid=None, superior_user_guid=None, sales_status_type_guid=None, resource_allocation_guid=None, sales_progress=None, row_count=None, page_token=None) -> web.Response:
    """Get resource allocations for a user with required filters (startDate and endDate or changedSince, max 30 days to be fetched at once)

    

    :param user_guid: 
    :type user_guid: str
    :param start_date: Get resource allocations with startDate. Using startDate and endDate or changedSince parameters are required to fetch a maximum of 30 days
    :type start_date: str
    :param end_date: Get resource allocations with endDate. Using startDate and endDate or changedSince parameters are required to fetch a maximum of 30 days
    :type end_date: str
    :param changed_since: Optional: Get resource allocations that have been added or changed after this date time (greater or equal).
    :type changed_since: str
    :param user_license_types: 
    :type user_license_types: list | bytes
    :param phase_guid: 
    :type phase_guid: str
    :param project_guid: 
    :type project_guid: str
    :param project_business_unit_guid: 
    :type project_business_unit_guid: str
    :param user_business_unit_guid: 
    :type user_business_unit_guid: str
    :param project_manager_user_guid: 
    :type project_manager_user_guid: str
    :param user_tag_guid: 
    :type user_tag_guid: str
    :param use_sales_probability: 
    :type use_sales_probability: bool
    :param project_status_type_guid: 
    :type project_status_type_guid: str
    :param project_tag_guid: 
    :type project_tag_guid: str
    :param superior_user_guid: 
    :type superior_user_guid: str
    :param sales_status_type_guid: 
    :type sales_status_type_guid: str
    :param resource_allocation_guid: 
    :type resource_allocation_guid: str
    :param sales_progress: 
    :type sales_progress: dict | bytes
    :param row_count: Optional: Number of rows to fetch.
    :type row_count: int
    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    changed_since = util.deserialize_datetime(changed_since)
    user_license_types = [LicenseUserType.from_dict(d) for d in user_license_types]
    sales_progress = .from_dict(sales_progress)
    return web.Response(status=200)


async def resource_allocations_post_resource_allocations(request: web.Request, row_count=None, page_token=None, changed_since=None, body=None) -> web.Response:
    """Get resource allocations (its POST because of being able to accommodate more filters)

    

    :param row_count: Optional: Number of rows to fetch.
    :type row_count: int
    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param changed_since: Optional: Get resource allocations that have been added or changed after this date time (greater or equal).
    :type changed_since: str
    :param body: resourceAllocationCriteriaModel
    :type body: dict | bytes

    """
    changed_since = util.deserialize_datetime(changed_since)
    body = ResourceAllocationCriteriaModel.from_dict(body)
    return web.Response(status=200)


async def role_allocations_get_role_allocation(request: web.Request, guid) -> web.Response:
    """Get role allocation by GUID.

    

    :param guid: ID used to get the role allocation.
    :type guid: str

    """
    return web.Response(status=200)


async def role_allocations_get_role_allocations(request: web.Request, start_date, end_date=None, page_token=None, row_count=None, use_sales_probability=None, role_guids=None, phase_guids=None, project_guids=None) -> web.Response:
    """Get role allocations.

    

    :param start_date: Starting date from which to get the role allocations. If end date is not specified on the role allocation then it will be compared with phase end date.
    :type start_date: str
    :param end_date: Optional: Ending date to which to get the role allocations. If start date is not specified on the role allocation then it will be compared with phase start date.
    :type end_date: str
    :param page_token: Optional: Page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: How many rows to fetch, Default all.
    :type row_count: int
    :param use_sales_probability: Optional: Calculates the hours based on sales probability set for the project. Default is true.
    :type use_sales_probability: bool
    :param role_guids: Optional: Role IDs.
    :type role_guids: List[str]
    :param phase_guids: Optional: Phase IDs.
    :type phase_guids: List[str]
    :param project_guids: Optional: Project IDs.
    :type project_guids: List[str]

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    return web.Response(status=200)
