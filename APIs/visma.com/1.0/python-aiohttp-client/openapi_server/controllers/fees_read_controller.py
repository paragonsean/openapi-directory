from typing import List, Dict
from aiohttp import web

from openapi_server.models.billable_period import BillablePeriod
from openapi_server.models.deleted_project_fee_model import DeletedProjectFeeModel
from openapi_server.models.exception_model import ExceptionModel
from openapi_server.models.flat_rate_output_model import FlatRateOutputModel
from openapi_server.models.product_type import ProductType
from openapi_server.models.project_fee_output_model import ProjectFeeOutputModel
from openapi_server.models.project_recurring_fee_rule_output_model import ProjectRecurringFeeRuleOutputModel
from openapi_server import util


async def flat_rates_get_all_flat_rates(request: web.Request, page_token=None, row_count=None, changed_since=None, invoice_guid=None) -> web.Response:
    """Get all flat rates

    

    :param page_token: Optional: Page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param changed_since: Optional: Get flat rates that have been added or changed after this date time (greater or equal).
    :type changed_since: str
    :param invoice_guid: Optional: Get flat rates by invoice guid. Default all.
    :type invoice_guid: str

    """
    changed_since = util.deserialize_datetime(changed_since)
    return web.Response(status=200)


async def flat_rates_get_flatrate(request: web.Request, guid) -> web.Response:
    """Get flat rate.

    

    :param guid: Id of the flat rate.
    :type guid: str

    """
    return web.Response(status=200)


async def flat_rates_get_flatrates_for_project(request: web.Request, project_guid) -> web.Response:
    """Get project&#39;s flat rates.

    

    :param project_guid: Id of the project.
    :type project_guid: str

    """
    return web.Response(status=200)


async def project_fees_get_deleted_project_fees(request: web.Request, page_token=None, row_count=None, project_guids=None, user_guids=None, deleted_since=None) -> web.Response:
    """Get the deleted project fees.

    

    :param page_token: 
    :type page_token: str
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param project_guids: Optional: ID of the project for the deleted project fees to be fetched. If not provided, returns for all projects. Default all.
    :type project_guids: List[str]
    :param user_guids: Optional: ID of the user. If not provided, returns for all users. Default all.
    :type user_guids: List[str]
    :param deleted_since: Optional: Get project fees that have been deleted after this date time (greater or equal).
    :type deleted_since: str

    """
    deleted_since = util.deserialize_datetime(deleted_since)
    return web.Response(status=200)


async def project_fees_get_project_fee(request: web.Request, guid) -> web.Response:
    """Get projectFee by ID.

    

    :param guid: Id used to get the projectFee.
    :type guid: str

    """
    return web.Response(status=200)


async def project_fees_get_project_fees_by_token(request: web.Request, page_token=None, row_count=None, changed_since=None) -> web.Response:
    """Get the project fees.

    

    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: Number of rows to fetch
    :type row_count: int
    :param changed_since: Optional: Get project fees that have been added or changed after this date time (greater or equal).
    :type changed_since: str

    """
    changed_since = util.deserialize_datetime(changed_since)
    return web.Response(status=200)


async def project_fees_get_project_fees_for_project(request: web.Request, project_guid, page_token=None, row_count=None, product_type=None, is_billable=None, is_billed=None, invoiceable_date=None, include_recurring_rules=None, is_billable_period_in_future=None) -> web.Response:
    """Get all the project fees for a project

    

    :param project_guid: ID of the project.
    :type project_guid: str
    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: Number of rows to fetch.
    :type row_count: int
    :param product_type: Optional: ProjectFee&#39;s product type. if given, it filters the projectFees by the given type. FixedFees (Own work), Materials (Products), Subcontracting
    :type product_type: dict | bytes
    :param is_billable: Optional: Filter the project fees. If true/false, only the billable/non-billable ones are returned. If null, all are returned. Default is null.
    :type is_billable: bool
    :param is_billed: Optional: Filter the project fees. If true/false, only the ones that are/are not invoiced are returned. If null, all are returned. Default is null.
    :type is_billed: bool
    :param invoiceable_date: Optional: Filter the project fees. When given, only the ones that are invoiceable before or on the given date are returned. Default is null.
    :type invoiceable_date: str
    :param include_recurring_rules: Optional: Also fetches recurring rules along with project fees. Default is false.
    :type include_recurring_rules: bool
    :param is_billable_period_in_future: Optional. Filter the project fees. If true/false, only the ones that will be billable in the future are returned. If null, all are returned. Default is false.
    :type is_billable_period_in_future: bool

    """
    product_type = .from_dict(product_type)
    invoiceable_date = util.deserialize_datetime(invoiceable_date)
    return web.Response(status=200)


async def project_fees_get_user_project_fees(request: web.Request, user_guid, page_token=None, row_count=None, product_type=None, is_billable=None, is_billed=None, invoiceable_date=None, has_phase=None, start_date=None, end_date=None) -> web.Response:
    """Get all the projectFees for a user

    

    :param user_guid: ID of the user.
    :type user_guid: str
    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: Number of rows to fetch.
    :type row_count: int
    :param product_type: Optional: ProjectFee&#39;s product type. if given, it filters the projectFees by the given type. FixedFees (Own work), Materials (Products), Subcontracting.
    :type product_type: dict | bytes
    :param is_billable: Optional: Filter the project fees. If true/false, only the billable/non-billable ones are returned. If null, all are returned. Default is null.
    :type is_billable: bool
    :param is_billed: Optional: Filter the project fees. If true/false, only the ones that are/are not invoiced are returned. If null, all are returned. Default is null.
    :type is_billed: bool
    :param invoiceable_date: Optional: Filter the project fees. When given, only the ones that are invoiceable before or on the given date are returned. Default is null.
    :type invoiceable_date: str
    :param has_phase: Optional: Filter the project fees. If true/false, only the ones are connected/not-connected to a phase are returned. If null, all are returned. Default is null.
    :type has_phase: bool
    :param start_date: Start date search criteria. Only get project fees that have event date from this date.
    :type start_date: str
    :param end_date: End date search criteria. Only get project fees that have event date until this date.
    :type end_date: str

    """
    product_type = .from_dict(product_type)
    invoiceable_date = util.deserialize_datetime(invoiceable_date)
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    return web.Response(status=200)


async def project_recurring_fee_rules_get_project_recurring_fee_rule(request: web.Request, guid, include_inactive=None) -> web.Response:
    """Get project&#39;s RecurringFeeRule by ID.

    

    :param guid: Id used to get the ProjectRecurringFeeRule.
    :type guid: str
    :param include_inactive: Indicates the rule should be returned even if it is not active. Default is false.
    :type include_inactive: bool

    """
    return web.Response(status=200)


async def project_recurring_fee_rules_get_project_recurring_fee_rules(request: web.Request, first_row=None, row_count=None, product_type=None, changed_since=None) -> web.Response:
    """Get the recurring fee rules.

    

    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param product_type: projectRecurringFeeRule&#39;s product type. if given, it filters the projectRecurringFeeRules by the given type.
    :type product_type: dict | bytes
    :param changed_since: Optional: Get recurring fee rules that have been added or changed after this date time (greater or equal).
    :type changed_since: str

    """
    product_type = .from_dict(product_type)
    changed_since = util.deserialize_datetime(changed_since)
    return web.Response(status=200)


async def project_recurring_fee_rules_get_project_recurring_fee_rules_for_project(request: web.Request, project_guid, product_type=None, first_row=None, row_count=None, is_billable_period_in_future=None, billable_time_period=None) -> web.Response:
    """Get all the Recurring Fee Rules for a project

    

    :param project_guid: ID of the project to get the recurring fee rules.
    :type project_guid: str
    :param product_type: projectRecurringFeeRule&#39;s product type. if given, it filters the projectRecurringFeeRules by the given type.
    :type product_type: dict | bytes
    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param is_billable_period_in_future: Optional. Filter the project recurring fee rules. If true/false, only the ones that will be billable in the future are returned. If null, all are returned. Default is false.
    :type is_billable_period_in_future: bool
    :param billable_time_period: the time period for any uninvoiced recurring rules.
    :type billable_time_period: dict | bytes

    """
    product_type = .from_dict(product_type)
    billable_time_period = .from_dict(billable_time_period)
    return web.Response(status=200)
