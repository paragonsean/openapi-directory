from typing import List, Dict
from aiohttp import web

from openapi_server.models.deleted_phase_member_output_model import DeletedPhaseMemberOutputModel
from openapi_server.models.exception_model import ExceptionModel
from openapi_server.models.expenses_class import ExpensesClass
from openapi_server.models.key_value_pair_of_string_and_sort_direction import KeyValuePairOfStringAndSortDirection
from openapi_server.models.overtime_price_model import OvertimePriceModel
from openapi_server.models.phase_member_output_model import PhaseMemberOutputModel
from openapi_server.models.phase_model_with_hierarchy_info import PhaseModelWithHierarchyInfo
from openapi_server.models.phase_output_model import PhaseOutputModel
from openapi_server.models.product_for_project_output_model import ProductForProjectOutputModel
from openapi_server.models.product_price_output_model import ProductPriceOutputModel
from openapi_server.models.product_type import ProductType
from openapi_server.models.project_billing_customer_model import ProjectBillingCustomerModel
from openapi_server.models.project_custom_value_model import ProjectCustomValueModel
from openapi_server.models.project_forecast_output_model import ProjectForecastOutputModel
from openapi_server.models.project_invoice_settings_output_model import ProjectInvoiceSettingsOutputModel
from openapi_server.models.project_keyword_model import ProjectKeywordModel
from openapi_server.models.project_member_cost_exception_output_model import ProjectMemberCostExceptionOutputModel
from openapi_server.models.project_output_model import ProjectOutputModel
from openapi_server.models.project_product_output_model import ProjectProductOutputModel
from openapi_server.models.project_sales_note_output_model import ProjectSalesNoteOutputModel
from openapi_server.models.project_work_hour_price_output_model import ProjectWorkHourPriceOutputModel
from openapi_server.models.project_work_type_model import ProjectWorkTypeModel
from openapi_server.models.proposal_fee_row_output_model import ProposalFeeRowOutputModel
from openapi_server.models.proposal_output_model import ProposalOutputModel
from openapi_server.models.proposal_settings_output_model import ProposalSettingsOutputModel
from openapi_server.models.proposal_subtotal_output_model import ProposalSubtotalOutputModel
from openapi_server.models.proposal_workhour_row_output_model import ProposalWorkhourRowOutputModel
from openapi_server.models.sales_note_output_model import SalesNoteOutputModel
from openapi_server.models.sales_status_history_output_model import SalesStatusHistoryOutputModel
from openapi_server.models.team_productivity_output_model import TeamProductivityOutputModel
from openapi_server.models.travel_expense_type_output_model import TravelExpenseTypeOutputModel
from openapi_server.models.travel_price_output_model import TravelPriceOutputModel
from openapi_server.models.work_type_output_model import WorkTypeOutputModel
from openapi_server.models.worktype_for_project_output_model import WorktypeForProjectOutputModel
from openapi_server import util


async def keywords_get_project_keywords(request: web.Request, project_guid, active=None, sortings=None) -> web.Response:
    """Get all the keywords for project.

    

    :param project_guid: ID of the project for which keywords are requested.
    :type project_guid: str
    :param active: If not given, return all Keywords, if given as true return only active Keywords, if given as false returns only inactive Keywords.
    :type active: bool
    :param sortings: Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;Keyword&amp;sortings[0].value&#x3D;Desc\&quot;.
    :type sortings: list | bytes

    """
    sortings = [KeyValuePairOfStringAndSortDirection.from_dict(d) for d in sortings]
    return web.Response(status=200)


async def overtime_prices_get_overtime_prices_for_project(request: web.Request, project_guid) -> web.Response:
    """Get all the overtimePrices for a project.

    

    :param project_guid: 
    :type project_guid: str

    """
    return web.Response(status=200)


async def phase_members_get_all_deleted_phase_members(request: web.Request, deleted_since=None, page_token=None, row_count=None, is_user_active=None) -> web.Response:
    """Get all deleted phase members

    Use root phase to get project members.

    :param deleted_since: Optional: Get phase members that have been added or changed after this date time (greater or equal).
    :type deleted_since: str
    :param page_token: Optional: Page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: How many rows to fetch.
    :type row_count: int
    :param is_user_active: Optional: Is the user active. Default nothing &#x3D; all.
    :type is_user_active: bool

    """
    deleted_since = util.deserialize_datetime(deleted_since)
    return web.Response(status=200)


async def phase_members_get_all_phase_members(request: web.Request, changed_since=None, page_token=None, row_count=None, is_user_active=None) -> web.Response:
    """Get all active phase members

    Use root phase to get project members.

    :param changed_since: Optional: Get phase members that have been added or changed after this date time (greater or equal).
    :type changed_since: str
    :param page_token: Optional: Page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: How many rows to fetch.
    :type row_count: int
    :param is_user_active: Optional: Is the user active. Default nothing &#x3D; all.
    :type is_user_active: bool

    """
    changed_since = util.deserialize_datetime(changed_since)
    return web.Response(status=200)


async def phase_members_get_phase_members(request: web.Request, phase_guid, page_token=None, row_count=None, is_active=None, is_user_active=None) -> web.Response:
    """Get phase members

    Use root phase to get project members.

    :param phase_guid: GUID of the phase.
    :type phase_guid: str
    :param page_token: Optional: Page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: How many rows to fetch.
    :type row_count: int
    :param is_active: Optional: Is the member active on the phase. Filters only root phase members. Default nothing &#x3D; all.
    :type is_active: bool
    :param is_user_active: Optional: Is the user active. Default nothing &#x3D; all.
    :type is_user_active: bool

    """
    return web.Response(status=200)


async def phases_get_phase(request: web.Request, guid) -> web.Response:
    """Get phase by ID

    

    :param guid: Id used to get the phase.
    :type guid: str

    """
    return web.Response(status=200)


async def phases_get_phases(request: web.Request, page_token=None, row_count=None, changed_since=None, code=None, project_guids=None) -> web.Response:
    """Get the phases.

    

    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param changed_since: Optional: Get phases that have been added or changed after this date time (greater or equal).
    :type changed_since: str
    :param code: Optional: Code of the phase.
    :type code: str
    :param project_guids: Optional: List of project ids.
    :type project_guids: List[str]

    """
    changed_since = util.deserialize_datetime(changed_since)
    return web.Response(status=200)


async def phases_get_project_phases(request: web.Request, guid) -> web.Response:
    """Get project&#39;s phases as flat list

    

    :param guid: Id of the project.
    :type guid: str

    """
    return web.Response(status=200)


async def phases_get_root_phases(request: web.Request, page_token=None, row_count=None, customer_guids=None, project_guids=None, project_keyword_guids=None, project_status_type_guids=None, sales_person_guids=None, project_owner_guids=None, business_unit_guids=None, customer_owner_guids=None, sales_status_type_guids=None, open_projects=None, project_member_user_guids=None) -> web.Response:
    """Get a list of root phases with information about hierarchy.

    

    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param customer_guids: 
    :type customer_guids: List[str]
    :param project_guids: 
    :type project_guids: List[str]
    :param project_keyword_guids: 
    :type project_keyword_guids: List[str]
    :param project_status_type_guids: 
    :type project_status_type_guids: List[str]
    :param sales_person_guids: 
    :type sales_person_guids: List[str]
    :param project_owner_guids: 
    :type project_owner_guids: List[str]
    :param business_unit_guids: 
    :type business_unit_guids: List[str]
    :param customer_owner_guids: 
    :type customer_owner_guids: List[str]
    :param sales_status_type_guids: 
    :type sales_status_type_guids: List[str]
    :param open_projects: 
    :type open_projects: bool
    :param project_member_user_guids: 
    :type project_member_user_guids: List[str]

    """
    return web.Response(status=200)


async def product_prices_get_product_prices_for_project(request: web.Request, project_guid, from_pricelist_only=None, first_row=None, row_count=None, text_to_search=None, calculate_row_count=None, is_available=None, product_code=None, product_guids=None, is_volume_priced=None, product_category_guids=None, product_types=None) -> web.Response:
    """Get all the productPrices for a project.

    

    :param project_guid: ID of the project.
    :type project_guid: str
    :param from_pricelist_only: If true return only prices from the price list, if false also returns prices from the products. Default is false.
    :type from_pricelist_only: bool
    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param text_to_search: Optional: Text to search from Product name.
    :type text_to_search: str
    :param calculate_row_count: Optional: Calculate the number of total rows. Default false &#x3D; total row count is returned as zero.
    :type calculate_row_count: bool
    :param is_available: Optional: If true, returns only prices that are available for the project, false returns price that are not available. Default all.
    :type is_available: bool
    :param product_code: Optional: Absolute search for products with specified product code.
    :type product_code: str
    :param product_guids: Optional: Search all product price(s) by products guid(s).
    :type product_guids: List[str]
    :param is_volume_priced: Optional: If true, return only volume priced products. If false, return all non volume priced products. Default is null, which means return all products.
    :type is_volume_priced: bool
    :param product_category_guids: Optional: Search product prices according to product category / categories by product category guid(s).
    :type product_category_guids: List[str]
    :param product_types: Optional: Search product prices according to product type / types.
    :type product_types: list | bytes

    """
    product_types = [ProductType.from_dict(d) for d in product_types]
    return web.Response(status=200)


async def products_get_searched_products(request: web.Request, project_guid, row_count=None, page_token=None, type=None, include_products_from_registry=None) -> web.Response:
    """Gets available products for the given project where price information comes from projects price list

    

    :param project_guid: Id of the project
    :type project_guid: str
    :param row_count: Optional: Number of rows to fetch
    :type row_count: int
    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param type: Product type. if given, it filters the products by the given type
    :type type: dict | bytes
    :param include_products_from_registry: Optional: If true returns all the products from registry with project specific prices. If false returns only products specified for the project with project specific prices. Default false.
    :type include_products_from_registry: bool

    """
    type = .from_dict(type)
    return web.Response(status=200)


async def project_billing_customers_get_work_hour_prices_for_project(request: web.Request, project_guid) -> web.Response:
    """Get all the billing customers for a project

    

    :param project_guid: 
    :type project_guid: str

    """
    return web.Response(status=200)


async def project_custom_values_get_project_custom_value(request: web.Request, guid) -> web.Response:
    """Get project custom value by ID.

    

    :param guid: Id used to get the project custom value.
    :type guid: str

    """
    return web.Response(status=200)


async def project_custom_values_get_project_custom_values(request: web.Request, project_guid, first_row=None, row_count=None, active=None, target=None, calculate_row_count=None, sortings=None) -> web.Response:
    """Get the project custom values.

    

    :param project_guid: ID of the project.
    :type project_guid: str
    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param active: Optional: Get only values of active or inactive project custom properties.
    :type active: bool
    :param target: List of target for which to get the values.
    :type target: List[str]
    :param calculate_row_count: Optional: Calculate total number of rows.
    :type calculate_row_count: bool
    :param sortings: Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (sub-model fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;Name&amp;sortings[0].value&#x3D;Desc&amp;sortings[1].key&#x3D;Number&amp;sortings[1].value&#x3D;Asc\&quot;.
    :type sortings: list | bytes

    """
    sortings = [KeyValuePairOfStringAndSortDirection.from_dict(d) for d in sortings]
    return web.Response(status=200)


async def project_forecasts_get_forecast(request: web.Request, guid) -> web.Response:
    """Get project forecast by ID

    

    :param guid: GUID used to get the project forecast.
    :type guid: str

    """
    return web.Response(status=200)


async def project_forecasts_get_forecasts(request: web.Request, project_guid, start_date=None, end_date=None) -> web.Response:
    """Get the project forecasts

    

    :param project_guid: project for the forecasts
    :type project_guid: str
    :param start_date: Start date of the date range for the forecasts
    :type start_date: str
    :param end_date: End date of the date range for the forecasts
    :type end_date: str

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    return web.Response(status=200)


async def project_invoice_settings_get_project_invoice_setting_0(request: web.Request, guid) -> web.Response:
    """Get project invoice settings by ID.

    

    :param guid: ID of the project invoice settings.
    :type guid: str

    """
    return web.Response(status=200)


async def project_invoice_settings_get_project_invoice_settings_0(request: web.Request, project_guid) -> web.Response:
    """Get project invoice settings by project ID.

    

    :param project_guid: ID of the project.
    :type project_guid: str

    """
    return web.Response(status=200)


async def project_member_cost_exceptions_get_project_member_cost_exceptions_for_project(request: web.Request, project_guid, user_guid=None, first_row=None, row_count=None) -> web.Response:
    """Get all cost exceptions of project members for a project.

    

    :param project_guid: Guid of the project.
    :type project_guid: str
    :param user_guid: Optional: Guid of the user.
    :type user_guid: str
    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int

    """
    return web.Response(status=200)


async def project_products_get_project_products(request: web.Request, project_guid, include_products_from_registry=None, page_token=None, row_count=None, active=None) -> web.Response:
    """Get project products

    This is the same as organization&#39;s list of products, unless the project has some specific products and UseProductsFromSetting in project model is set to false.

    :param project_guid: GUID of the project.
    :type project_guid: str
    :param include_products_from_registry: Optional: Includes products available from product registry
    :type include_products_from_registry: bool
    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: How many rows to fetch, Default all.
    :type row_count: int
    :param active: Fetch only active
    :type active: bool

    """
    return web.Response(status=200)


async def project_work_hour_prices_get_project_work_hour_price(request: web.Request, guid) -> web.Response:
    """Get project work hour price by ID

    

    :param guid: Id used to get the work hour price.
    :type guid: str

    """
    return web.Response(status=200)


async def project_work_hour_prices_get_work_hour_prices_for_project(request: web.Request, project_guid, from_pricelist_only=None, is_available=None, changed_since=None) -> web.Response:
    """Get all the work hour prices for a project

    

    :param project_guid: Guid of the project.
    :type project_guid: str
    :param from_pricelist_only: If true return only prices from the price list, if false also returns prices from the products. Default is false.
    :type from_pricelist_only: bool
    :param is_available: Optional: If true, returns only prices that are available for the project, false returns price that are not available. Default all.
    :type is_available: bool
    :param changed_since: Optional: Get project work hour prices that have been added or changed after this date time (greater or equal).
    :type changed_since: str

    """
    changed_since = util.deserialize_datetime(changed_since)
    return web.Response(status=200)


async def project_work_types_get_project_worktypes(request: web.Request, project_guid, include_worktypes_from_registry=None, first_row=None, row_count=None, active=None, text_to_search=None, changed_since=None) -> web.Response:
    """Get project work types.

    This is the same as organization&#39;s list of work types, unless the project has some specific work types and \&quot;UseWorktypesFromSetting\&quot; in project model is set to false.

    :param project_guid: GUID of the project.
    :type project_guid: str
    :param include_worktypes_from_registry: Include work types also from registry. If false, returns only project specific work types. Default false.
    :type include_worktypes_from_registry: bool
    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param active: If not given, return all work types, if given as true return only active work types, if given as false returns only inactive work types.
    :type active: bool
    :param text_to_search: Optional: Text to search from work type name.
    :type text_to_search: str
    :param changed_since: Optional: Get project work types that have been added or changed after this date time (greater or equal).
    :type changed_since: str

    """
    changed_since = util.deserialize_datetime(changed_since)
    return web.Response(status=200)


async def projects_get_customer_projects(request: web.Request, customer_guid, page_token=None, row_count=None, is_billable=None, currency_guids=None, project_guids=None, project_keyword_guids=None, project_status_type_guids=None, sales_person_guids=None, project_owner_guids=None, business_unit_guids=None, minimum_billable_amount=None, customer_owner_guids=None, invoiceable_date=None, market_segmentation_guids=None, sales_status_type_guids=None, is_closed=None, has_recurring_fees=None, company_currency_guids=None, project_member_user_guids=None, numbers=None) -> web.Response:
    """Get customer&#39;s projects

    

    :param customer_guid: Id of the customer.
    :type customer_guid: str
    :param page_token: 
    :type page_token: str
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param is_billable: Optional: When true fetch projects that have something to bill, when false nothing to bill. Default nothing &#x3D; all.
    :type is_billable: bool
    :param currency_guids: 
    :type currency_guids: List[str]
    :param project_guids: 
    :type project_guids: List[str]
    :param project_keyword_guids: 
    :type project_keyword_guids: List[str]
    :param project_status_type_guids: 
    :type project_status_type_guids: List[str]
    :param sales_person_guids: 
    :type sales_person_guids: List[str]
    :param project_owner_guids: 
    :type project_owner_guids: List[str]
    :param business_unit_guids: 
    :type business_unit_guids: List[str]
    :param minimum_billable_amount: 
    :type minimum_billable_amount: float
    :param customer_owner_guids: 
    :type customer_owner_guids: List[str]
    :param invoiceable_date: 
    :type invoiceable_date: str
    :param market_segmentation_guids: 
    :type market_segmentation_guids: List[str]
    :param sales_status_type_guids: 
    :type sales_status_type_guids: List[str]
    :param is_closed: 
    :type is_closed: bool
    :param has_recurring_fees: 
    :type has_recurring_fees: bool
    :param company_currency_guids: 
    :type company_currency_guids: List[str]
    :param project_member_user_guids: 
    :type project_member_user_guids: List[str]
    :param numbers: 
    :type numbers: List[int]

    """
    invoiceable_date = util.deserialize_datetime(invoiceable_date)
    return web.Response(status=200)


async def projects_get_project(request: web.Request, guid) -> web.Response:
    """Get project by ID

    

    :param guid: Id used to get the project.
    :type guid: str

    """
    return web.Response(status=200)


async def projects_get_projects(request: web.Request, page_token=None, row_count=None, currency_guid=None, changed_since=None, is_billable=None, customer_guids=None, project_guids=None, project_keyword_guids=None, project_status_type_guids=None, sales_person_guids=None, project_owner_guids=None, business_unit_guids=None, minimum_billable_amount=None, customer_owner_guids=None, invoiceable_date=None, market_segmentation_guids=None, sales_status_type_guids=None, is_closed=None, has_recurring_fees=None, company_currency_guids=None, project_member_user_guids=None, numbers=None, internal=None) -> web.Response:
    """Get all the projects

    

    :param page_token: 
    :type page_token: str
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param currency_guid: Optional: ID of project currency.
    :type currency_guid: str
    :param changed_since: Optional: Get projects that have been added or changed after this date time (greater or equal).
    :type changed_since: str
    :param is_billable: Optional: When true fetch projects that have something to bill, when false nothing to bill. Default nothing &#x3D; all.
    :type is_billable: bool
    :param customer_guids: 
    :type customer_guids: List[str]
    :param project_guids: 
    :type project_guids: List[str]
    :param project_keyword_guids: 
    :type project_keyword_guids: List[str]
    :param project_status_type_guids: 
    :type project_status_type_guids: List[str]
    :param sales_person_guids: 
    :type sales_person_guids: List[str]
    :param project_owner_guids: 
    :type project_owner_guids: List[str]
    :param business_unit_guids: 
    :type business_unit_guids: List[str]
    :param minimum_billable_amount: 
    :type minimum_billable_amount: float
    :param customer_owner_guids: 
    :type customer_owner_guids: List[str]
    :param invoiceable_date: 
    :type invoiceable_date: str
    :param market_segmentation_guids: 
    :type market_segmentation_guids: List[str]
    :param sales_status_type_guids: 
    :type sales_status_type_guids: List[str]
    :param is_closed: 
    :type is_closed: bool
    :param has_recurring_fees: 
    :type has_recurring_fees: bool
    :param company_currency_guids: 
    :type company_currency_guids: List[str]
    :param project_member_user_guids: 
    :type project_member_user_guids: List[str]
    :param numbers: 
    :type numbers: List[int]
    :param internal: Optional: Get internal / non-internal projects.
    :type internal: bool

    """
    changed_since = util.deserialize_datetime(changed_since)
    invoiceable_date = util.deserialize_datetime(invoiceable_date)
    return web.Response(status=200)


async def projects_get_sales_cases(request: web.Request, page_token=None, row_count=None, customer_guids=None, currency_guids=None, project_guids=None, project_keyword_guids=None, project_status_type_guids=None, sales_person_guids=None, project_owner_guids=None, business_unit_guids=None, minimum_billable_amount=None, customer_owner_guids=None, invoiceable_date=None, market_segmentation_guids=None, sales_status_type_guids=None, is_closed=None, has_recurring_fees=None, company_currency_guids=None, project_member_user_guids=None, numbers=None) -> web.Response:
    """Gets the sales cases (sales status is in progress)

    

    :param page_token: 
    :type page_token: str
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param customer_guids: 
    :type customer_guids: List[str]
    :param currency_guids: 
    :type currency_guids: List[str]
    :param project_guids: 
    :type project_guids: List[str]
    :param project_keyword_guids: 
    :type project_keyword_guids: List[str]
    :param project_status_type_guids: 
    :type project_status_type_guids: List[str]
    :param sales_person_guids: 
    :type sales_person_guids: List[str]
    :param project_owner_guids: 
    :type project_owner_guids: List[str]
    :param business_unit_guids: 
    :type business_unit_guids: List[str]
    :param minimum_billable_amount: 
    :type minimum_billable_amount: float
    :param customer_owner_guids: 
    :type customer_owner_guids: List[str]
    :param invoiceable_date: 
    :type invoiceable_date: str
    :param market_segmentation_guids: 
    :type market_segmentation_guids: List[str]
    :param sales_status_type_guids: 
    :type sales_status_type_guids: List[str]
    :param is_closed: 
    :type is_closed: bool
    :param has_recurring_fees: 
    :type has_recurring_fees: bool
    :param company_currency_guids: 
    :type company_currency_guids: List[str]
    :param project_member_user_guids: 
    :type project_member_user_guids: List[str]
    :param numbers: 
    :type numbers: List[int]

    """
    invoiceable_date = util.deserialize_datetime(invoiceable_date)
    return web.Response(status=200)


async def proposal_fees_get_proposal_fee(request: web.Request, guid) -> web.Response:
    """Get the proposal fee rows by guid

    

    :param guid: proposal fee row id to get
    :type guid: str

    """
    return web.Response(status=200)


async def proposal_fees_get_proposal_fees(request: web.Request, page_token=None, row_count=None, changed_since=None) -> web.Response:
    """Get the proposal fee rows.

    

    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param changed_since: Optional: Get proposal fee rows that have been added or changed after this date time (greater or equal).
    :type changed_since: str

    """
    changed_since = util.deserialize_datetime(changed_since)
    return web.Response(status=200)


async def proposal_fees_get_proposal_fees_for_proposal(request: web.Request, proposal_guid, page_token=None, row_count=None) -> web.Response:
    """Get all the proposal fee rows for a proposal

    

    :param proposal_guid: proposal id for which to get proposal fees rows.
    :type proposal_guid: str
    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: How many rows to fetch, Default all.
    :type row_count: int

    """
    return web.Response(status=200)


async def proposal_settings_get_proposal_settings(request: web.Request, guid) -> web.Response:
    """Get settings for a proposal

    

    :param guid: GUID used to get the Proposal.
    :type guid: str

    """
    return web.Response(status=200)


async def proposal_subtotals_get_proposal_subtotal(request: web.Request, guid) -> web.Response:
    """Get Proposal subtotal by ID

    

    :param guid: GUID used to get the Proposal subtotal.
    :type guid: str

    """
    return web.Response(status=200)


async def proposal_subtotals_get_proposal_subtotals(request: web.Request, page_token=None, row_count=None, changed_since=None) -> web.Response:
    """Get the proposal subtotals.

    

    :param page_token: Optional: Page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param changed_since: Optional: Get proposal subtotals that have been added or changed after this date time (greater or equal).
    :type changed_since: str

    """
    changed_since = util.deserialize_datetime(changed_since)
    return web.Response(status=200)


async def proposal_subtotals_get_proposal_subtotals_for_proposal(request: web.Request, proposal_guid, page_token=None, row_count=None) -> web.Response:
    """Get all the proposal subtotals for a proposal

    

    :param proposal_guid: proposal id for which to get proposal subtotals.
    :type proposal_guid: str
    :param page_token: Optional: Page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: How many rows to fetch, Default all.
    :type row_count: int

    """
    return web.Response(status=200)


async def proposal_workhours_get_proposal_work_hours(request: web.Request, page_token=None, row_count=None, changed_since=None) -> web.Response:
    """Get the proposal work rows.

    

    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param changed_since: Optional: Get proposal work rows that have been added or changed after this date time (greater or equal).
    :type changed_since: str

    """
    changed_since = util.deserialize_datetime(changed_since)
    return web.Response(status=200)


async def proposal_workhours_get_proposal_work_hours_for_proposal(request: web.Request, proposal_guid, page_token=None, row_count=None) -> web.Response:
    """Get all the proposal work rows.

    

    :param proposal_guid: proposal id for which to get proposal work rows.
    :type proposal_guid: str
    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: How many rows to fetch, Default all.
    :type row_count: int

    """
    return web.Response(status=200)


async def proposal_workhours_get_proposal_workhour(request: web.Request, guid) -> web.Response:
    """Get the proposal work row by guid.

    

    :param guid: proposal work row id to get.
    :type guid: str

    """
    return web.Response(status=200)


async def proposals_get_proposal(request: web.Request, guid) -> web.Response:
    """Get Proposal by ID

    

    :param guid: GUID used to get the Proposal.
    :type guid: str

    """
    return web.Response(status=200)


async def proposals_get_proposals(request: web.Request, page_token=None, row_count=None, changed_since=None) -> web.Response:
    """Get all the proposals

    

    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param changed_since: Optional: Get proposals that have been added or changed after this date time (greater or equal).
    :type changed_since: str

    """
    changed_since = util.deserialize_datetime(changed_since)
    return web.Response(status=200)


async def proposals_get_proposals_for_project(request: web.Request, project_guid, page_token=None, row_count=None, changed_since=None) -> web.Response:
    """Get all the proposals for a project

    

    :param project_guid: Project id for which to get proposals.
    :type project_guid: str
    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: How many rows to fetch, Default all.
    :type row_count: int
    :param changed_since: Optional: Get proposals that have been added or changed after this date time (greater or equal).
    :type changed_since: str

    """
    changed_since = util.deserialize_datetime(changed_since)
    return web.Response(status=200)


async def sales_notes_get_all_customer_sales_notes(request: web.Request, customer_guid, page_token=None, row_count=None, changed_since=None) -> web.Response:
    """Get the sales notes by customer guid.

    

    :param customer_guid: Customer guid used to get the notes.
    :type customer_guid: str
    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param changed_since: Optional: Get sales notes that have been added or changed after this date time (greater or equal).
    :type changed_since: str

    """
    changed_since = util.deserialize_datetime(changed_since)
    return web.Response(status=200)


async def sales_notes_get_project_sales_note(request: web.Request, guid) -> web.Response:
    """Get project sales note by ID.

    

    :param guid: GUID used to get the project sales note.
    :type guid: str

    """
    return web.Response(status=200)


async def sales_notes_get_project_sales_notes(request: web.Request, project_guid, page_token=None, row_count=None, changed_since=None) -> web.Response:
    """Get the sales notes of a case.

    

    :param project_guid: Project guid used to get the notes.
    :type project_guid: str
    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param changed_since: Optional: Get sales notes that have been added or changed after this date time (greater or equal).
    :type changed_since: str

    """
    changed_since = util.deserialize_datetime(changed_since)
    return web.Response(status=200)


async def sales_status_history_get_sales_status_history(request: web.Request, project_guid) -> web.Response:
    """Get the sales status history for a project

    

    :param project_guid: The project for which the sales status history is fetched.
    :type project_guid: str

    """
    return web.Response(status=200)


async def team_productivity_get_team_productivity(request: web.Request, project_guid) -> web.Response:
    """Get team productivity of a project.

    

    :param project_guid: GUID of the project.
    :type project_guid: str

    """
    return web.Response(status=200)


async def travel_expense_types_get_searched_travel_expense_types(request: web.Request, project_guid, text_to_search=None, first_row=None, row_count=None, user_guid=None, expense_class=None) -> web.Response:
    """Search active travel expense types of project by part of the name or code.

    

    :param project_guid: Id of the project.
    :type project_guid: str
    :param text_to_search: Searched string: part of name or code.
    :type text_to_search: str
    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default all.
    :type row_count: int
    :param user_guid: Optional: Id of the user to fetch travels for.
    :type user_guid: str
    :param expense_class: Optional: Expense class of the travel. Mileage/DailyAllowance/OtherTravelExpense.
    :type expense_class: dict | bytes

    """
    expense_class = .from_dict(expense_class)
    return web.Response(status=200)


async def travel_prices_get_travel_prices_for_project(request: web.Request, project_guid, from_pricelist_only=None, expense_classes=None, first_row=None, row_count=None, text_to_search=None, calculate_row_count=None) -> web.Response:
    """Get all the travel prices for a project.

    

    :param project_guid: ID of the project.
    :type project_guid: str
    :param from_pricelist_only: If true return only prices from the price list, if false also returns prices from the settings. Default is false.
    :type from_pricelist_only: bool
    :param expense_classes: Optional: List of expense classes to search by, defaults to all travel categories.
    :type expense_classes: list | bytes
    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param text_to_search: Optional: Text to search from Product name.
    :type text_to_search: str
    :param calculate_row_count: Optional: Calculate the number of total rows. Default false &#x3D; total row count is returned as zero.
    :type calculate_row_count: bool

    """
    expense_classes = [ExpensesClass.from_dict(d) for d in expense_classes]
    return web.Response(status=200)


async def work_types_get_phase_work_types(request: web.Request, phase_guid, page_token=None, row_count=None, user_guid=None) -> web.Response:
    """Get all work types that are available for a phase (for work hour entry)

    Only the active work types are included in the list, whether they come from organization settings or project specific work types.

    :param phase_guid: Id of the phase.
    :type phase_guid: str
    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: number of rows to fetch
    :type row_count: int
    :param user_guid: Id of the user for whom the work types are retrieved. Default is current user.
    :type user_guid: str

    """
    return web.Response(status=200)


async def work_types_get_searched_worktypes(request: web.Request, project_guid, first_row=None, row_count=None, text_to_search=None) -> web.Response:
    """Search active work types by part of the name or code.

    

    :param project_guid: Id of the case to which proposal is connected.
    :type project_guid: str
    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param text_to_search: Searched string: part of name or code.
    :type text_to_search: str

    """
    return web.Response(status=200)
