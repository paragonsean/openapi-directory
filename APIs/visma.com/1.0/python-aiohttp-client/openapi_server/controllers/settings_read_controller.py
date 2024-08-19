from typing import List, Dict
from aiohttp import web

from openapi_server.models.activity_category import ActivityCategory
from openapi_server.models.activity_type_model import ActivityTypeModel
from openapi_server.models.bank_account_output_model import BankAccountOutputModel
from openapi_server.models.business_unit_model import BusinessUnitModel
from openapi_server.models.communication_type_model import CommunicationTypeModel
from openapi_server.models.contact_role_model import ContactRoleModel
from openapi_server.models.cost_account_model import CostAccountModel
from openapi_server.models.cost_center_model import CostCenterModel
from openapi_server.models.country_model import CountryModel
from openapi_server.models.country_region_model import CountryRegionModel
from openapi_server.models.currency_output_model import CurrencyOutputModel
from openapi_server.models.custom_property_model import CustomPropertyModel
from openapi_server.models.customer_custom_property_selection_item_output_model import CustomerCustomPropertySelectionItemOutputModel
from openapi_server.models.exception_model import ExceptionModel
from openapi_server.models.expenses_class import ExpensesClass
from openapi_server.models.formatting_culture_model import FormattingCultureModel
from openapi_server.models.holiday_model import HolidayModel
from openapi_server.models.industry_model import IndustryModel
from openapi_server.models.invoice_status_model import InvoiceStatusModel
from openapi_server.models.invoice_template_model import InvoiceTemplateModel
from openapi_server.models.key_value_pair_of_string_and_sort_direction import KeyValuePairOfStringAndSortDirection
from openapi_server.models.keyword_category import KeywordCategory
from openapi_server.models.keyword_model import KeywordModel
from openapi_server.models.kpi_formula_category import KpiFormulaCategory
from openapi_server.models.kpi_formula_model_base import KpiFormulaModelBase
from openapi_server.models.language_model import LanguageModel
from openapi_server.models.lead_source_model import LeadSourceModel
from openapi_server.models.market_segment_model import MarketSegmentModel
from openapi_server.models.overtime_model import OvertimeModel
from openapi_server.models.overtime_price_model import OvertimePriceModel
from openapi_server.models.permission_profile_model import PermissionProfileModel
from openapi_server.models.phase_status_type_model import PhaseStatusTypeModel
from openapi_server.models.price_list_model import PriceListModel
from openapi_server.models.price_list_output_model import PriceListOutputModel
from openapi_server.models.pricelist_version_output_model import PricelistVersionOutputModel
from openapi_server.models.product_category_model import ProductCategoryModel
from openapi_server.models.product_country_settings_model import ProductCountrySettingsModel
from openapi_server.models.product_output_model import ProductOutputModel
from openapi_server.models.product_price_output_model import ProductPriceOutputModel
from openapi_server.models.product_type import ProductType
from openapi_server.models.project_billing_customer_model2 import ProjectBillingCustomerModel2
from openapi_server.models.project_custom_property_selection_item_output_model import ProjectCustomPropertySelectionItemOutputModel
from openapi_server.models.project_member_cost_exception_output_model import ProjectMemberCostExceptionOutputModel
from openapi_server.models.project_status_type_model import ProjectStatusTypeModel
from openapi_server.models.project_task_status_model import ProjectTaskStatusModel
from openapi_server.models.proposal_status_output_model import ProposalStatusOutputModel
from openapi_server.models.role_output_model import RoleOutputModel
from openapi_server.models.sales_account_model import SalesAccountModel
from openapi_server.models.sales_status_type import SalesStatusType
from openapi_server.models.sales_status_type_output_model import SalesStatusTypeOutputModel
from openapi_server.models.time_entry_type_model import TimeEntryTypeModel
from openapi_server.models.timezone_model import TimezoneModel
from openapi_server.models.travel_expense_type_country_settings_model import TravelExpenseTypeCountrySettingsModel
from openapi_server.models.travel_expense_type_output_model import TravelExpenseTypeOutputModel
from openapi_server.models.travel_price_output_model import TravelPriceOutputModel
from openapi_server.models.travel_reimbursement_status_model import TravelReimbursementStatusModel
from openapi_server.models.usage_model2 import UsageModel2
from openapi_server.models.user_custom_property_output_model import UserCustomPropertyOutputModel
from openapi_server.models.user_custom_property_selection_item_output_model import UserCustomPropertySelectionItemOutputModel
from openapi_server.models.vat_rate_output_model import VatRateOutputModel
from openapi_server.models.work_contract_output_model import WorkContractOutputModel
from openapi_server.models.work_hour_price_output_model import WorkHourPriceOutputModel
from openapi_server.models.work_type_output_model import WorkTypeOutputModel
from openapi_server import util


async def activity_types_get_activity_type(request: web.Request, guid) -> web.Response:
    """Get Activity Type by ID

    

    :param guid: GUID used to get the Activity Type.
    :type guid: str

    """
    return web.Response(status=200)


async def activity_types_get_activity_types(request: web.Request, active=None, page_token=None, row_count=None, changed_since=None, category=None) -> web.Response:
    """Get the Activity Types

    

    :param active: If not given, return all Activity Types, if given as true return only active Activity Types, if given as false returns only inactive Activity Types
    :type active: bool
    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param changed_since: Optional: Get activity types that have been added or changed after this date time (greater or equal).
    :type changed_since: str
    :param category: Optional: Category or multiple categories of activity types to search for. Default all.
    :type category: list | bytes

    """
    changed_since = util.deserialize_datetime(changed_since)
    category = [ActivityCategory.from_dict(d) for d in category]
    return web.Response(status=200)


async def bank_accounts_get_bank_account(request: web.Request, guid) -> web.Response:
    """Get bank account by ID.

    

    :param guid: GUID used to get the bank account.
    :type guid: str

    """
    return web.Response(status=200)


async def bank_accounts_get_bank_accounts(request: web.Request, company_guid=None, business_unit_guid=None, active=None, first_row=None, row_count=None, text_to_search=None, calculate_row_count=None, sortings=None) -> web.Response:
    """Get all bank accounts for current organization.

    

    :param company_guid: Optional: ID of the company.
    :type company_guid: str
    :param business_unit_guid: Optional: ID of the business unit.
    :type business_unit_guid: str
    :param active: If not given, returns all bank accounts, if given as true returns only active bank accounts, if given as false returns only inactive bank accounts.
    :type active: bool
    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param text_to_search: Optional: Text to search from bank account name.
    :type text_to_search: str
    :param calculate_row_count: Optional: Calculate total number of rows.
    :type calculate_row_count: bool
    :param sortings: Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;BankName&amp;sortings[0].value&#x3D;Desc &amp;sortings[1].key&#x3D;BusinessUnitName&amp;sortings[1].value&#x3D;Asc\&quot;.
    :type sortings: list | bytes

    """
    sortings = [KeyValuePairOfStringAndSortDirection.from_dict(d) for d in sortings]
    return web.Response(status=200)


async def business_units_get_business_unit(request: web.Request, guid) -> web.Response:
    """Get businessUnit by ID.

    

    :param guid: GUID used to get the businessUnit.
    :type guid: str

    """
    return web.Response(status=200)


async def business_units_get_business_units(request: web.Request, active=None, company_guid=None, company_country_guid=None, first_row=None, row_count=None, text_to_search=None, changed_since=None, code=None, name=None) -> web.Response:
    """Get all the BusinessUnits

    

    :param active: If not given, return all BusinessUnits, if given as true return only active BusinessUnits, if given as false returns only inactive BusinessUnits
    :type active: bool
    :param company_guid: Optional: ID of the company to which the business units belong.
    :type company_guid: str
    :param company_country_guid: Optional: ID of the country in which the company of business units is located.
    :type company_country_guid: str
    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param text_to_search: Optional: Text to search from business unit name.
    :type text_to_search: str
    :param changed_since: Optional: Get business units that have been added or changed after this date time (greater or equal).
    :type changed_since: str
    :param code: Optional: Code of the business unit.
    :type code: str
    :param name: Optional: Name of the business unit.
    :type name: str

    """
    changed_since = util.deserialize_datetime(changed_since)
    return web.Response(status=200)


async def communication_types_get_communication_type(request: web.Request, guid) -> web.Response:
    """Get communication type by ID.

    

    :param guid: ID used to get the communication type.
    :type guid: str

    """
    return web.Response(status=200)


async def communication_types_get_communication_types(request: web.Request, active=None, first_row=None, row_count=None, text_to_search=None, calculate_row_count=None, sortings=None) -> web.Response:
    """Get all communication types.

    

    :param active: Filter the communication types. If true/false, only the active/inactive ones are returned. If null, all the communication types are returned.
    :type active: bool
    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param text_to_search: Optional: Text to search from communication type name.
    :type text_to_search: str
    :param calculate_row_count: Optional: Calculate total number of rows.
    :type calculate_row_count: bool
    :param sortings: Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;name&amp;sortings[0].value&#x3D;Asc\&quot;.
    :type sortings: list | bytes

    """
    sortings = [KeyValuePairOfStringAndSortDirection.from_dict(d) for d in sortings]
    return web.Response(status=200)


async def contact_roles_get_contact_role(request: web.Request, guid) -> web.Response:
    """Get contact role by ID.

    

    :param guid: Id used to get the contact role.
    :type guid: str

    """
    return web.Response(status=200)


async def contact_roles_get_contact_roles(request: web.Request, active=None, first_row=None, row_count=None, text_to_search=None, calculate_row_count=None) -> web.Response:
    """Get contact roles.

    

    :param active: If not given, return all contact roles, if given as true return only active contact roles, if given as false returns only inactive contact roles.
    :type active: bool
    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param text_to_search: Optional: Text to search from contact role name.
    :type text_to_search: str
    :param calculate_row_count: Optional: Calculate total number of rows.
    :type calculate_row_count: bool

    """
    return web.Response(status=200)


async def cost_accounts_get_cost_account(request: web.Request, guid) -> web.Response:
    """Get cost account by Guid.

    

    :param guid: Cost account&#39;s guid.
    :type guid: str

    """
    return web.Response(status=200)


async def cost_accounts_get_cost_accounts(request: web.Request, active=None, first_row=None, row_count=None, text_to_search=None, calculate_row_count=None, sortings=None) -> web.Response:
    """Get cost accounts.

    

    :param active: If not given, return all cost accounts, if given as true return only active cost accounts, if given as false returns only inactive cost accounts.
    :type active: bool
    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param text_to_search: Optional: Text to search from cost account name or identifier.
    :type text_to_search: str
    :param calculate_row_count: Optional: Calculate total number of rows.
    :type calculate_row_count: bool
    :param sortings: Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;Name&amp;sortings[0].value&#x3D;Desc &amp;sortings[1].key&#x3D;Identifier&amp;sortings[1].value&#x3D;Asc\&quot;.
    :type sortings: list | bytes

    """
    sortings = [KeyValuePairOfStringAndSortDirection.from_dict(d) for d in sortings]
    return web.Response(status=200)


async def cost_centers_get_cost_center(request: web.Request, guid) -> web.Response:
    """Get cost center by ID.

    

    :param guid: Id used to get the cost center.
    :type guid: str

    """
    return web.Response(status=200)


async def cost_centers_get_cost_centers(request: web.Request, active=None, first_row=None, row_count=None, text_to_search=None, changed_since=None, calculate_row_count=None, sortings=None, identifier=None, name=None) -> web.Response:
    """Get cost centers.

    

    :param active: If not given, return all cost centers, if given as true return only active cost centers, if given as false returns only inactive cost centers.
    :type active: bool
    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param text_to_search: Optional: Text to search from cost center name or identifier.
    :type text_to_search: str
    :param changed_since: Optional: Get cost centers that have been added or changed after this date time (greater or equal).
    :type changed_since: str
    :param calculate_row_count: Optional: Calculate total number of rows.
    :type calculate_row_count: bool
    :param sortings: Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;.
    :type sortings: list | bytes
    :param identifier: Optional: Identifier of the cost center.
    :type identifier: str
    :param name: Optional: Name of the cost center.
    :type name: str

    """
    changed_since = util.deserialize_datetime(changed_since)
    sortings = [KeyValuePairOfStringAndSortDirection.from_dict(d) for d in sortings]
    return web.Response(status=200)


async def countries_get_countries(request: web.Request, ) -> web.Response:
    """Get all the Countries.

    


    """
    return web.Response(status=200)


async def countries_get_country(request: web.Request, guid) -> web.Response:
    """Get country by ID.

    

    :param guid: GUID used to get the country.
    :type guid: str

    """
    return web.Response(status=200)


async def countries_get_country_by_code2(request: web.Request, code2) -> web.Response:
    """Get a country by ISO Alpha-2 code

    

    :param code2: Optional: ISO Alpha-2 code used to get a country.
    :type code2: str

    """
    return web.Response(status=200)


async def countries_get_country_by_code3(request: web.Request, code3) -> web.Response:
    """Get a country by ISO Alpha-3 code

    

    :param code3: Optional: ISO Alpha-3 code used to get a country.
    :type code3: str

    """
    return web.Response(status=200)


async def countries_get_country_by_name(request: web.Request, country_name) -> web.Response:
    """Get a country by name

    

    :param country_name: Optional: English country name.
    :type country_name: str

    """
    return web.Response(status=200)


async def countries_get_country_region(request: web.Request, guid) -> web.Response:
    """Get country region by ID.

    

    :param guid: GUID used to get the country region.
    :type guid: str

    """
    return web.Response(status=200)


async def countries_get_country_regions(request: web.Request, country_guid) -> web.Response:
    """Get all the Country regions for a country.

    

    :param country_guid: GUID of the country.
    :type country_guid: str

    """
    return web.Response(status=200)


async def currencies_get_currencies(request: web.Request, active=None, first_row=None, row_count=None, text_to_search=None, calculate_row_count=None, sortings=None) -> web.Response:
    """Get all the Currencies

    

    :param active: If not given, return all Currencies, if given as true return only active Currencies, if given as false returns only inactive Currencies.
    :type active: bool
    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param text_to_search: Optional: Text based search applied to the result. Matches currency name and code.
    :type text_to_search: str
    :param calculate_row_count: Optional: Calculate total number of rows.
    :type calculate_row_count: bool
    :param sortings: Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;name&amp;sortings[0].value&#x3D;Asc\&quot;. Using additional sorting fields \&quot;CreatedDate\&quot; and / or \&quot;LastUpdatedDate\&quot; as keys sort currencies without a timestamp provided when sorting with other date fields.
    :type sortings: list | bytes

    """
    sortings = [KeyValuePairOfStringAndSortDirection.from_dict(d) for d in sortings]
    return web.Response(status=200)


async def currencies_get_currency(request: web.Request, guid) -> web.Response:
    """Get currency by ID.

    

    :param guid: GUID used to get the currency.
    :type guid: str

    """
    return web.Response(status=200)


async def customer_custom_properties_get_customer_custom_properties(request: web.Request, first_row=None, row_count=None, active=None, text_to_search=None, is_in_use=None, calculate_row_count=None, sortings=None) -> web.Response:
    """Get the customer custom properties.

    

    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param active: Optional: Get only active or inactive customer properties.
    :type active: bool
    :param text_to_search: Optional: Text to search from custom property name.
    :type text_to_search: str
    :param is_in_use: Optional: Is the customer property used in any custom property usage.
    :type is_in_use: bool
    :param calculate_row_count: Optional: Calculate total number of rows.
    :type calculate_row_count: bool
    :param sortings: Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (sub-model fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;Name&amp;sortings[0].value&#x3D;Desc&amp;sortings[1].key&#x3D;Number&amp;sortings[1].value&#x3D;Asc\&quot;.
    :type sortings: list | bytes

    """
    sortings = [KeyValuePairOfStringAndSortDirection.from_dict(d) for d in sortings]
    return web.Response(status=200)


async def customer_custom_properties_get_customer_custom_property(request: web.Request, guid) -> web.Response:
    """Get customer custom property by ID.

    

    :param guid: Id used to get the customer custom property.
    :type guid: str

    """
    return web.Response(status=200)


async def customer_custom_property_selection_items_get_customer_custom_property_selection_item(request: web.Request, guid) -> web.Response:
    """Get customer custom property selection item by ID.

    

    :param guid: Id used to get the customer custom property selection item.
    :type guid: str

    """
    return web.Response(status=200)


async def customer_custom_property_selection_items_get_customer_custom_property_selection_items(request: web.Request, custom_property_guid, row_count=None, is_active=None, page_token=None, changed_since=None) -> web.Response:
    """Get the customer custom properties.

    

    :param custom_property_guid: Custom property id used to get the customer custom property selection items.
    :type custom_property_guid: str
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param is_active: Optional: Get only active or inactive selection items.
    :type is_active: bool
    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param changed_since: Optional: Get custom property selection items that have been added or changed after this date time (greater or equal).
    :type changed_since: str

    """
    changed_since = util.deserialize_datetime(changed_since)
    return web.Response(status=200)


async def formatting_cultures_get_formatting_culture(request: web.Request, guid) -> web.Response:
    """Get formatting culture by ID.

    

    :param guid: GUID used to get the formatting culture.
    :type guid: str

    """
    return web.Response(status=200)


async def formatting_cultures_get_formattings(request: web.Request, ) -> web.Response:
    """Get all the Formatting Cultures

    


    """
    return web.Response(status=200)


async def holidays_get_holidays(request: web.Request, year=None, country_guid=None) -> web.Response:
    """Get holidays.

    

    :param year: Optional: Holidays for this year only. Default: all years.
    :type year: int
    :param country_guid: Optional: Holidays for this country only. Default local.
    :type country_guid: str

    """
    return web.Response(status=200)


async def holidays_get_holidays_by_time_period(request: web.Request, start_date=None, end_date=None, country_guid=None) -> web.Response:
    """Get holidays with start and end date.

    

    :param start_date: Start date for holidays.
    :type start_date: str
    :param end_date: End date for holidays.
    :type end_date: str
    :param country_guid: Optional: Holidays for this country only. Default local.
    :type country_guid: str

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    return web.Response(status=200)


async def industries_get_industries(request: web.Request, active=None, first_row=None, row_count=None, text_to_search=None, calculate_row_count=None) -> web.Response:
    """Get all the industries.

    

    :param active: If not given, return all industries, if given as true return only active industries, if given as false returns only inactive industries.
    :type active: bool
    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param text_to_search: Optional: Text to search from industry name.
    :type text_to_search: str
    :param calculate_row_count: Optional: Calculate total number of rows.
    :type calculate_row_count: bool

    """
    return web.Response(status=200)


async def industries_get_industry(request: web.Request, guid) -> web.Response:
    """Get industry by ID.

    

    :param guid: GUID used to get the industry.
    :type guid: str

    """
    return web.Response(status=200)


async def invoice_statuses_get_invoice_status(request: web.Request, guid) -> web.Response:
    """Get Invoice status by ID.

    

    :param guid: GUID used to get the Invoice status.
    :type guid: str

    """
    return web.Response(status=200)


async def invoice_statuses_get_invoice_statuses(request: web.Request, active=None, first_row=None, row_count=None, text_to_search=None, calculate_row_count=None, sortings=None) -> web.Response:
    """Get invoice statuses.

    

    :param active: Filter the invoice statuses. If true/false, only the active/inactive ones are returned. If null, all the invoice statuses are returned.
    :type active: bool
    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param text_to_search: Optional: Text to search from invoice status name.
    :type text_to_search: str
    :param calculate_row_count: Optional: Calculate total number of rows.
    :type calculate_row_count: bool
    :param sortings: Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;Name&amp;sortings[0].value&#x3D;Desc\&quot;.
    :type sortings: list | bytes

    """
    sortings = [KeyValuePairOfStringAndSortDirection.from_dict(d) for d in sortings]
    return web.Response(status=200)


async def invoice_templates_get_invoice_template(request: web.Request, guid) -> web.Response:
    """Get invoice template by ID.

    

    :param guid: ID of the invoice template.
    :type guid: str

    """
    return web.Response(status=200)


async def invoice_templates_get_invoice_templates(request: web.Request, active=None, first_row=None, row_count=None, text_to_search=None, calculate_row_count=None, sortings=None) -> web.Response:
    """Get invoice templates.

    

    :param active: 
    :type active: bool
    :param first_row: 
    :type first_row: int
    :param row_count: 
    :type row_count: int
    :param text_to_search: 
    :type text_to_search: str
    :param calculate_row_count: 
    :type calculate_row_count: bool
    :param sortings: 
    :type sortings: list | bytes

    """
    sortings = [KeyValuePairOfStringAndSortDirection.from_dict(d) for d in sortings]
    return web.Response(status=200)


async def keywords_get_keyword(request: web.Request, guid) -> web.Response:
    """Get keyword by ID.

    

    :param guid: GUID used to get the keyword.
    :type guid: str

    """
    return web.Response(status=200)


async def keywords_get_keywords(request: web.Request, category=None, active=None, first_row=None, row_count=None, text_to_search=None, changed_since=None, calculate_row_count=None, sortings=None, keyword=None) -> web.Response:
    """Get all the keywords.

    

    :param category: Optional: category of the keyword.
    :type category: dict | bytes
    :param active: If not given, return all Keywords, if given as true return only active Keywords, if given as false returns only inactive Keywords.
    :type active: bool
    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param text_to_search: Optional: Text to search from keyword.
    :type text_to_search: str
    :param changed_since: Optional: Get keywords that have been added or changed after this date time (greater or equal).
    :type changed_since: str
    :param calculate_row_count: Optional: Calculate total number of rows.
    :type calculate_row_count: bool
    :param sortings: Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;.
    :type sortings: list | bytes
    :param keyword: Optional: Keyword name.
    :type keyword: str

    """
    category = .from_dict(category)
    changed_since = util.deserialize_datetime(changed_since)
    sortings = [KeyValuePairOfStringAndSortDirection.from_dict(d) for d in sortings]
    return web.Response(status=200)


async def kpi_formulas_get_kpi_formulas(request: web.Request, category=None, is_active=None, first_row=None, row_count=None, text_to_search=None, sortings=None, include_definition=None, changed_since=None) -> web.Response:
    """Get saved KPI formulas.

    

    :param category: Optional: Category of KPI formula (Project, Invoice, User).
    :type category: dict | bytes
    :param is_active: Optional: return with given active status. Default is to return all.
    :type is_active: bool
    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param text_to_search: Optional: Text to search.
    :type text_to_search: str
    :param sortings: Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;Name&amp;sortings[0].value&#x3D;Desc\&quot;.
    :type sortings: list | bytes
    :param include_definition: Optional: Include definition to response. Default false.
    :type include_definition: bool
    :param changed_since: Optional: Get KPI formulas that have been added or changed after this date time (greater or equal).
    :type changed_since: str

    """
    category = .from_dict(category)
    sortings = [KeyValuePairOfStringAndSortDirection.from_dict(d) for d in sortings]
    changed_since = util.deserialize_datetime(changed_since)
    return web.Response(status=200)


async def languages_get_language(request: web.Request, guid) -> web.Response:
    """Get language by ID

    

    :param guid: GUID used to get the language.
    :type guid: str

    """
    return web.Response(status=200)


async def languages_get_languages(request: web.Request, is_invoice_language=None) -> web.Response:
    """Get all the languages

    

    :param is_invoice_language: Optional: which languages to fetch. only invoice languages or non invoice languages?, default all.
    :type is_invoice_language: bool

    """
    return web.Response(status=200)


async def lead_sources_get_lead_source(request: web.Request, guid) -> web.Response:
    """Get lead source by ID.

    

    :param guid: GUID used to get the lead source.
    :type guid: str

    """
    return web.Response(status=200)


async def lead_sources_get_lead_sources(request: web.Request, active=None, first_row=None, row_count=None, text_to_search=None, calculate_row_count=None) -> web.Response:
    """Get the lead sources.

    

    :param active: If not given, return all lead sources, if given as true return only active lead sources, if given as false returns only inactive lead sources.
    :type active: bool
    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param text_to_search: Optional: Text to search from lead source name.
    :type text_to_search: str
    :param calculate_row_count: Optional: Calculate total number of rows.
    :type calculate_row_count: bool

    """
    return web.Response(status=200)


async def market_segments_get_market_segment(request: web.Request, guid) -> web.Response:
    """Get Market Segment by ID.

    

    :param guid: GUID used to get the Market Segment.
    :type guid: str

    """
    return web.Response(status=200)


async def market_segments_get_market_segments(request: web.Request, active=None, first_row=None, row_count=None, text_to_search=None, calculate_row_count=None, include_child_segments=None) -> web.Response:
    """Get the Market Segments.

    

    :param active: If not given, return all Market Segments, if given as true return only active Market Segments, if given as false returns only inactive Market Segments.
    :type active: bool
    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param text_to_search: Optional: Text to search from market segment name.
    :type text_to_search: str
    :param calculate_row_count: Optional: Calculate total number of rows.
    :type calculate_row_count: bool
    :param include_child_segments: Optional: Include also child market segments. If false returns only parent segments. Default true.
    :type include_child_segments: bool

    """
    return web.Response(status=200)


async def overtime_prices_get_overtime_price(request: web.Request, guid) -> web.Response:
    """Get overtime price by ID.

    

    :param guid: Id used to get the overtime price.
    :type guid: str

    """
    return web.Response(status=200)


async def overtime_prices_get_overtime_prices(request: web.Request, pricelist_version_guid) -> web.Response:
    """Get all the overtime prices for a price list version.

    

    :param pricelist_version_guid: 
    :type pricelist_version_guid: str

    """
    return web.Response(status=200)


async def overtimes_get_overtime(request: web.Request, guid) -> web.Response:
    """Get overtime definition by ID.

    

    :param guid: Id used to get the overtime definition.
    :type guid: str

    """
    return web.Response(status=200)


async def overtimes_get_overtimes(request: web.Request, active=None, first_row=None, row_count=None, text_to_search=None, calculate_row_count=None, sortings=None) -> web.Response:
    """Get overtime definitions.

    

    :param active: If not given, return all overtime definitions, if given as true return only active overtime definitions, if given as false returns only inactive overtime definitions.
    :type active: bool
    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default all.
    :type row_count: int
    :param text_to_search: Optional: Text to search from overtime name.
    :type text_to_search: str
    :param calculate_row_count: Optional: Calculate total number of rows.
    :type calculate_row_count: bool
    :param sortings: Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;name&amp;sortings[0].value&#x3D;Asc\&quot;\&quot;.
    :type sortings: list | bytes

    """
    sortings = [KeyValuePairOfStringAndSortDirection.from_dict(d) for d in sortings]
    return web.Response(status=200)


async def permission_profiles_get_permission_profile(request: web.Request, guid) -> web.Response:
    """Get Permission Profile by ID.

    

    :param guid: GUID used to get the Permission Profile.
    :type guid: str

    """
    return web.Response(status=200)


async def permission_profiles_get_permission_profiles(request: web.Request, active=None, first_row=None, row_count=None, text_to_search=None, calculate_row_count=None, sortings=None) -> web.Response:
    """Get the Permission Profiles.

    

    :param active: If not given, return all Permission Profiles, if given as true return only active Permission Profiles, if given as false returns only inactive Permission Profiles.
    :type active: bool
    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param text_to_search: Optional: Text to search from permission profile name.
    :type text_to_search: str
    :param calculate_row_count: Optional: Calculate total number of rows.
    :type calculate_row_count: bool
    :param sortings: Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;name&amp;sortings[0].value&#x3D;Asc&amp;sortings[1].key&#x3D;isActive&amp;sortings[1].value&#x3D;Asc\&quot;.
    :type sortings: list | bytes

    """
    sortings = [KeyValuePairOfStringAndSortDirection.from_dict(d) for d in sortings]
    return web.Response(status=200)


async def phase_status_types_get_phase_status_type(request: web.Request, guid) -> web.Response:
    """Get phase status type by GUID

    

    :param guid: Id used to get the phase status type.
    :type guid: str

    """
    return web.Response(status=200)


async def phase_status_types_get_phase_status_types(request: web.Request, active=None, first_row=None, row_count=None, text_to_search=None, calculate_row_count=None, sortings=None) -> web.Response:
    """Get phase status types

    

    :param active: If not given, return all phase status types, if given as true return only active phase status types, if given as false returns only inactive phase status types
    :type active: bool
    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default all.
    :type row_count: int
    :param text_to_search: 
    :type text_to_search: str
    :param calculate_row_count: 
    :type calculate_row_count: bool
    :param sortings: 
    :type sortings: list | bytes

    """
    sortings = [KeyValuePairOfStringAndSortDirection.from_dict(d) for d in sortings]
    return web.Response(status=200)


async def price_list_versions_get_pricelist_version(request: web.Request, guid) -> web.Response:
    """Get a price list version by guid.

    

    :param guid: 
    :type guid: str

    """
    return web.Response(status=200)


async def price_list_versions_get_pricelist_versions_by_pricelist(request: web.Request, pricelist_guid) -> web.Response:
    """Get all price list versions of a price list.

    

    :param pricelist_guid: 
    :type pricelist_guid: str

    """
    return web.Response(status=200)


async def price_lists_get_price_list(request: web.Request, guid) -> web.Response:
    """Get price list by GUID.

    

    :param guid: ID used to get the price list.
    :type guid: str

    """
    return web.Response(status=200)


async def price_lists_get_pricelists(request: web.Request, active=None, first_row=None, row_count=None, text_to_search=None, currency_guid=None, calculate_row_count=None, sortings=None, name=None) -> web.Response:
    """Get all price lists.

    

    :param active: If not given, return all price lists, if given as true return only active price lists, if given as false returns only inactive price lists.
    :type active: bool
    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param text_to_search: Optional: Text to search from price list name.
    :type text_to_search: str
    :param currency_guid: Optional: ID of the price list currency.
    :type currency_guid: str
    :param calculate_row_count: Optional: Calculate total number of rows.
    :type calculate_row_count: bool
    :param sortings: Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;.
    :type sortings: list | bytes
    :param name: Optional: Name of the price list.
    :type name: str

    """
    sortings = [KeyValuePairOfStringAndSortDirection.from_dict(d) for d in sortings]
    return web.Response(status=200)


async def product_categories_get_product_categories(request: web.Request, active=None, first_row=None, row_count=None, text_to_search=None, changed_since=None, calculate_row_count=None, sortings=None) -> web.Response:
    """Get product categories.

    

    :param active: If not given, return all Product categories, if given as true return only active Product categories, if given as false returns only inactive Product categories.
    :type active: bool
    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default all.
    :type row_count: int
    :param text_to_search: Optional: Text to search from product category name or code.
    :type text_to_search: str
    :param changed_since: Optional: Get product categories that have been added or changed after this date time (greater or equal).
    :type changed_since: str
    :param calculate_row_count: Optional: Calculate total number of rows.
    :type calculate_row_count: bool
    :param sortings: Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: ?sortings[0].key&#x3D;Name&amp;sortings[0].value&#x3D;Desc &amp;sortings[1].key&#x3D;Code&amp;sortings[1].value&#x3D;Asc.
    :type sortings: list | bytes

    """
    changed_since = util.deserialize_datetime(changed_since)
    sortings = [KeyValuePairOfStringAndSortDirection.from_dict(d) for d in sortings]
    return web.Response(status=200)


async def product_categories_get_product_category(request: web.Request, guid) -> web.Response:
    """Get product category by ID.

    

    :param guid: Id used to get the product category.
    :type guid: str

    """
    return web.Response(status=200)


async def product_country_settings_get_product_country_settings(request: web.Request, product_guid) -> web.Response:
    """Get all the country settings for a product

    

    :param product_guid: GUID of the product.
    :type product_guid: str

    """
    return web.Response(status=200)


async def product_prices_get_product_price(request: web.Request, guid) -> web.Response:
    """Get product price by ID.

    

    :param guid: Id used to get the product price.
    :type guid: str

    """
    return web.Response(status=200)


async def product_prices_get_product_prices(request: web.Request, pricelist_version_guid, from_pricelist_only=None, first_row=None, row_count=None, text_to_search=None, calculate_row_count=None, product_code=None, product_guids=None, is_volume_priced=None, product_category_guids=None, product_types=None) -> web.Response:
    """Get all the product prices for a price list version.

    

    :param pricelist_version_guid: ID of the price list version.
    :type pricelist_version_guid: str
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


async def products_get_product(request: web.Request, guid) -> web.Response:
    """Get product by ID.

    

    :param guid: GUID used to get the product.
    :type guid: str

    """
    return web.Response(status=200)


async def products_get_products(request: web.Request, row_count=None, page_token=None, type=None, is_active=None, code=None, changed_since=None) -> web.Response:
    """Get all the Products

    

    :param row_count: Optional: Number of rows to fetch
    :type row_count: int
    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param type: Product type. if given, it filters the products by the given type.
    :type type: dict | bytes
    :param is_active: If not given, return all Products, if given as true return only isActive Products, if given as false returns only inactive Products
    :type is_active: bool
    :param code: Optional: Code of the product.
    :type code: str
    :param changed_since: Optional: Get products that have been added or changed after this date time (greater or equal).
    :type changed_since: str

    """
    type = .from_dict(type)
    changed_since = util.deserialize_datetime(changed_since)
    return web.Response(status=200)


async def project_billing_customers_get_project_billing_customer(request: web.Request, guid) -> web.Response:
    """Get a project billing customer.

    

    :param guid: ID of the project billing customer.
    :type guid: str

    """
    return web.Response(status=200)


async def project_custom_properties_get_project_custom_properties(request: web.Request, first_row=None, row_count=None, active=None, text_to_search=None, is_in_use=None, calculate_row_count=None, sortings=None) -> web.Response:
    """Get the project custom properties.

    

    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param active: Optional: Get only active or inactive project properties.
    :type active: bool
    :param text_to_search: Optional: Text to search from custom property name.
    :type text_to_search: str
    :param is_in_use: Optional: Is the customer property used in any custom property usage.
    :type is_in_use: bool
    :param calculate_row_count: Optional: Calculate total number of rows.
    :type calculate_row_count: bool
    :param sortings: Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (sub-model fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;Name&amp;sortings[0].value&#x3D;Desc&amp;sortings[1].key&#x3D;Number&amp;sortings[1].value&#x3D;Asc\&quot;.
    :type sortings: list | bytes

    """
    sortings = [KeyValuePairOfStringAndSortDirection.from_dict(d) for d in sortings]
    return web.Response(status=200)


async def project_custom_properties_get_project_custom_property(request: web.Request, guid) -> web.Response:
    """Get project custom property by ID.

    

    :param guid: Id used to get the project custom property.
    :type guid: str

    """
    return web.Response(status=200)


async def project_custom_property_selection_items_get_project_custom_property_selection_item(request: web.Request, guid) -> web.Response:
    """Get project custom property selection item by ID.

    

    :param guid: Id used to get the project custom property selection item.
    :type guid: str

    """
    return web.Response(status=200)


async def project_custom_property_selection_items_get_project_custom_property_selection_items(request: web.Request, custom_property_guid, row_count=None, is_active=None, page_token=None, changed_since=None) -> web.Response:
    """Get the project custom properties.

    

    :param custom_property_guid: Custom property id used to get the project custom property selection items.
    :type custom_property_guid: str
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param is_active: Optional: Get only active or inactive selection items.
    :type is_active: bool
    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param changed_since: Optional: Get custom property selection items that have been added or changed after this date time (greater or equal).
    :type changed_since: str

    """
    changed_since = util.deserialize_datetime(changed_since)
    return web.Response(status=200)


async def project_member_cost_exceptions_get_project_member_cost_exception(request: web.Request, guid) -> web.Response:
    """Get project member cost exception by ID.

    

    :param guid: GUID used to get the cost exception.
    :type guid: str

    """
    return web.Response(status=200)


async def project_status_types_get_project_status_type(request: web.Request, guid) -> web.Response:
    """Get projectStatusType by ID

    

    :param guid: GUID used to get the projectStatusType.
    :type guid: str

    """
    return web.Response(status=200)


async def project_status_types_get_project_status_types(request: web.Request, active=None, first_row=None, row_count=None, text_to_search=None, calculate_row_count=None, sortings=None) -> web.Response:
    """Get all the ProjectStatusTypes

    

    :param active: If not given, return all ProjectStatusTypes, if given as true return only active ProjectStatusTypes, if given as false returns only inactive ProjectStatusTypes
    :type active: bool
    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param text_to_search: Optional: Text to search from ProjectStatusType name.
    :type text_to_search: str
    :param calculate_row_count: Optional: Calculate total number of rows.
    :type calculate_row_count: bool
    :param sortings: Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;name&amp;sortings[0].value&#x3D;Asc&amp;sortings[1].key&#x3D;isActive&amp;sortings[1].value&#x3D;Asc\&quot;
    :type sortings: list | bytes

    """
    sortings = [KeyValuePairOfStringAndSortDirection.from_dict(d) for d in sortings]
    return web.Response(status=200)


async def project_task_statuses_get_project_task_status(request: web.Request, guid) -> web.Response:
    """Get Project task status by ID.

    

    :param guid: GUID used to get the Project task status.
    :type guid: str

    """
    return web.Response(status=200)


async def project_task_statuses_get_project_task_statuses(request: web.Request, active=None, first_row=None, row_count=None, text_to_search=None, calculate_row_count=None, sortings=None) -> web.Response:
    """Get the project task statuses.

    

    :param active: If not given, return all project task statuses, if given as true return only active project task statuses, if given as false returns only inactive project task statuses.
    :type active: bool
    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param text_to_search: Optional: Text to search from activity type name.
    :type text_to_search: str
    :param calculate_row_count: Optional: Calculate total number of rows.
    :type calculate_row_count: bool
    :param sortings: Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;name&amp;sortings[0].value&#x3D;Asc\&quot;.
    :type sortings: list | bytes

    """
    sortings = [KeyValuePairOfStringAndSortDirection.from_dict(d) for d in sortings]
    return web.Response(status=200)


async def proposal_statuses_get_proposal_status(request: web.Request, guid) -> web.Response:
    """Get Proposal status by ID

    

    :param guid: GUID used to get the Proposal status.
    :type guid: str

    """
    return web.Response(status=200)


async def proposal_statuses_get_proposal_statuses(request: web.Request, is_active=None, page_token=None, row_count=None, proposal_status_name=None) -> web.Response:
    """Get all the proposal statuses

    

    :param is_active: Optional: If not given, return all proposal statuses, if given as true return only active proposal statuses, if given as false returns only inactive proposal statuses.
    :type is_active: bool
    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param proposal_status_name: Optional: Search by proposal status name.
    :type proposal_status_name: str

    """
    return web.Response(status=200)


async def proposal_statuses_get_usage(request: web.Request, guid) -> web.Response:
    """Get usage for an proposal status.

    

    :param guid: GUID used to get the proposal status.
    :type guid: str

    """
    return web.Response(status=200)


async def roles_get_role(request: web.Request, guid) -> web.Response:
    """Get role by GUID.

    

    :param guid: Id used to get the role.
    :type guid: str

    """
    return web.Response(status=200)


async def roles_get_roles(request: web.Request, is_active=None, page_token=None, row_count=None, changed_since=None) -> web.Response:
    """Get roles.

    

    :param is_active: If not given, return all roles, if given as true return only active roles, if given as false returns only inactive roles.
    :type is_active: bool
    :param page_token: Optional: Page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: How many rows to fetch, Default all.
    :type row_count: int
    :param changed_since: Optional: Get roles that have been added or changed after this date time (greater or equal).
    :type changed_since: str

    """
    changed_since = util.deserialize_datetime(changed_since)
    return web.Response(status=200)


async def sales_accounts_get_sales_account(request: web.Request, guid) -> web.Response:
    """Get sales account by ID.

    

    :param guid: Id used to get the sales account.
    :type guid: str

    """
    return web.Response(status=200)


async def sales_accounts_get_sales_accounts(request: web.Request, active=None, first_row=None, row_count=None, text_to_search=None, calculate_row_count=None, sortings=None) -> web.Response:
    """Get sales accounts.

    

    :param active: If not given, return all Sales accounts, if given as true return only active Sales accounts, if given as false returns only inactive Sales accounts.
    :type active: bool
    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param text_to_search: Optional: Text to search from cost account name or identifier.
    :type text_to_search: str
    :param calculate_row_count: Optional: Calculate total number of rows.
    :type calculate_row_count: bool
    :param sortings: Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;Name&amp;sortings[0].value&#x3D;Desc &amp;sortings[1].key&#x3D;Identifier&amp;sortings[1].value&#x3D;Asc\&quot;.
    :type sortings: list | bytes

    """
    sortings = [KeyValuePairOfStringAndSortDirection.from_dict(d) for d in sortings]
    return web.Response(status=200)


async def sales_status_types_get_sales_status_type(request: web.Request, guid) -> web.Response:
    """Get sales status type by ID

    

    :param guid: GUID used to get the sales status type.
    :type guid: str

    """
    return web.Response(status=200)


async def sales_status_types_get_sales_status_types(request: web.Request, active=None, sales_state=None, first_row=None, row_count=None, text_to_search=None, calculate_row_count=None, sortings=None) -> web.Response:
    """Get all the sales status types

    

    :param active: If not given, return all sales status types, if given as true return only active sales status types, if given as false returns only inactive sales status types
    :type active: bool
    :param sales_state: Optional: Get sales status types of the sales state.
    :type sales_state: dict | bytes
    :param first_row: Optional: First row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param text_to_search: Optional: Text to search from sales status type name.
    :type text_to_search: str
    :param calculate_row_count: Optional: Calculate total number of rows.
    :type calculate_row_count: bool
    :param sortings: Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;Name&amp;sortings[0].value&#x3D;Desc &amp;sortings[1].key&#x3D;Code&amp;sortings[1].value&#x3D;Asc\&quot;
    :type sortings: list | bytes

    """
    sales_state = .from_dict(sales_state)
    sortings = [KeyValuePairOfStringAndSortDirection.from_dict(d) for d in sortings]
    return web.Response(status=200)


async def time_entry_types_get_time_entry_type(request: web.Request, guid) -> web.Response:
    """Get time entry type by ID.

    

    :param guid: ID used to get the time entry type.
    :type guid: str

    """
    return web.Response(status=200)


async def time_entry_types_get_time_entry_types(request: web.Request, active=None, first_row=None, row_count=None, text_to_search=None, calculate_row_count=None, sortings=None) -> web.Response:
    """Get all time entry types.

    

    :param active: Filter the time entry types. If true/false, only the active/inactive ones are returned. If null, all the time entry types are returned.
    :type active: bool
    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param text_to_search: Optional: Text to search from time entry type name.
    :type text_to_search: str
    :param calculate_row_count: Optional: Calculates the total row count.
    :type calculate_row_count: bool
    :param sortings: Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;name&amp;sortings[0].value&#x3D;Asc\&quot;.
    :type sortings: list | bytes

    """
    sortings = [KeyValuePairOfStringAndSortDirection.from_dict(d) for d in sortings]
    return web.Response(status=200)


async def timezones_get_timezone(request: web.Request, guid) -> web.Response:
    """Get timezone by ID.

    

    :param guid: GUID used to get the timezone.
    :type guid: str

    """
    return web.Response(status=200)


async def timezones_get_timezones(request: web.Request, ) -> web.Response:
    """Get all the timezones.

    


    """
    return web.Response(status=200)


async def travel_expense_type_country_settings_get_travel_expense_type_country_settings(request: web.Request, travel_expense_type_guid) -> web.Response:
    """Get all country settings for a travel expense type

    

    :param travel_expense_type_guid: Guid of the travel expense type.
    :type travel_expense_type_guid: str

    """
    return web.Response(status=200)


async def travel_expense_types_get_travel_expense_type(request: web.Request, guid) -> web.Response:
    """Get travel expense type by guid.

    

    :param guid: GUID used to get the travel expense type.
    :type guid: str

    """
    return web.Response(status=200)


async def travel_expense_types_get_travel_expense_types(request: web.Request, active=None, first_row=None, row_count=None, text_to_search=None, code=None, calculate_row_count=None, sortings=None) -> web.Response:
    """Get all the travel expense types.

    

    :param active: If not given, return all travel expense types, if given as true return only active travel expense types, if given as false returns only inactive travel expense types.
    :type active: bool
    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default all.
    :type row_count: int
    :param text_to_search: Searched string: part of name or code.
    :type text_to_search: str
    :param code: Optional: Code of the travel expense type.
    :type code: str
    :param calculate_row_count: Optional: Calculate total number of rows.
    :type calculate_row_count: bool
    :param sortings: Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;IsActive&amp;sortings[0].value&#x3D;Asc&amp;sortings[1].key&#x3D;Name&amp;sortings[1].value&#x3D;Desc.
    :type sortings: list | bytes

    """
    sortings = [KeyValuePairOfStringAndSortDirection.from_dict(d) for d in sortings]
    return web.Response(status=200)


async def travel_prices_get_travel_price(request: web.Request, guid) -> web.Response:
    """Get travel price by ID.

    

    :param guid: Id used to get the travel price.
    :type guid: str

    """
    return web.Response(status=200)


async def travel_prices_get_travel_prices(request: web.Request, pricelist_version_guid, from_pricelist_only=None, expense_classes=None, first_row=None, row_count=None, text_to_search=None, calculate_row_count=None) -> web.Response:
    """Get all the travel prices for a price list version.

    

    :param pricelist_version_guid: ID of the price list version.
    :type pricelist_version_guid: str
    :param from_pricelist_only: If true return only prices from the price list, if false also returns prices from the products. Default is false.
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


async def travel_reimbursement_status_get_travel_reimbursement_status(request: web.Request, guid) -> web.Response:
    """Get the travel reimbursement statuses by guid.

    

    :param guid: reimbursement status id to get.
    :type guid: str

    """
    return web.Response(status=200)


async def travel_reimbursement_status_get_travel_reimbursement_statuses(request: web.Request, active=None, first_row=None, row_count=None, text_to_search=None, calculate_row_count=None, sortings=None) -> web.Response:
    """Get the travel reimbursement statuses.

    

    :param active: Optional: Filter the travel reimbursement statuses. If true/false, only the active/inactive ones are returned. If null, all the travel reimbursement statuses are returned.
    :type active: bool
    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param text_to_search: Optional: Text to search from travel reimbursement name.
    :type text_to_search: str
    :param calculate_row_count: Optional: Calculate total number of rows.
    :type calculate_row_count: bool
    :param sortings: Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;name&amp;sortings[0].value&#x3D;Asc\&quot;.
    :type sortings: list | bytes

    """
    sortings = [KeyValuePairOfStringAndSortDirection.from_dict(d) for d in sortings]
    return web.Response(status=200)


async def user_custom_properties_get_user_custom_properties(request: web.Request, page_token=None, row_count=None, is_active=None, is_in_use=None, changed_since=None) -> web.Response:
    """Get the user custom properties.

    

    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param is_active: Optional: Get only active or inactive user custom properties.
    :type is_active: bool
    :param is_in_use: Optional: Is the customer property used in any custom property usage.
    :type is_in_use: bool
    :param changed_since: Optional: Get custom properties that have been added or changed after this date time (greater or equal).
    :type changed_since: str

    """
    changed_since = util.deserialize_datetime(changed_since)
    return web.Response(status=200)


async def user_custom_properties_get_user_custom_property(request: web.Request, guid) -> web.Response:
    """Get user custom property by ID.

    

    :param guid: Id used to get the user custom property.
    :type guid: str

    """
    return web.Response(status=200)


async def user_custom_property_selection_items_get_user_custom_property_selection_item(request: web.Request, guid) -> web.Response:
    """Get user custom property selection item by ID.

    

    :param guid: Id used to get the user custom property selection item.
    :type guid: str

    """
    return web.Response(status=200)


async def user_custom_property_selection_items_get_user_custom_property_selection_items(request: web.Request, custom_property_guid, row_count=None, is_active=None, page_token=None, changed_since=None) -> web.Response:
    """Get the user custom properties.

    

    :param custom_property_guid: Custom property id used to get the user custom property selection items.
    :type custom_property_guid: str
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param is_active: Optional: Get only active or inactive selection items.
    :type is_active: bool
    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param changed_since: Optional: Get custom property selection items that have been added or changed after this date time (greater or equal).
    :type changed_since: str

    """
    changed_since = util.deserialize_datetime(changed_since)
    return web.Response(status=200)


async def vat_rates_get_vat_rate(request: web.Request, guid) -> web.Response:
    """Get a vat rate by GUID

    

    :param guid: GUID used to get the vat rate.
    :type guid: str

    """
    return web.Response(status=200)


async def vat_rates_get_vat_rates(request: web.Request, country_guid=None, active=None) -> web.Response:
    """Get all organization vat rates

    

    :param country_guid: If not given, return all vat rates in organizations country. If given return only for that country.
    :type country_guid: str
    :param active: If not given, return all vat rates, if given as true return only active ones, if given as false returns only inactive ones.
    :type active: bool

    """
    return web.Response(status=200)


async def work_contracts_get_work_contract(request: web.Request, guid) -> web.Response:
    """Get work contract by ID.

    

    :param guid: Id used to get the work contract.
    :type guid: str

    """
    return web.Response(status=200)


async def work_hour_prices_get_work_hour_price(request: web.Request, guid) -> web.Response:
    """Get work hour price by ID.

    

    :param guid: Id used to get the work hour price.
    :type guid: str

    """
    return web.Response(status=200)


async def work_hour_prices_get_work_hour_prices(request: web.Request, pricelist_version_guid, page_token=None, row_count=None, changed_since=None) -> web.Response:
    """Get all the workHourPrices for a price list version.

    

    :param pricelist_version_guid: Price list version identifier.
    :type pricelist_version_guid: str
    :param page_token: Optional: page token to fetch the next page..
    :type page_token: str
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param changed_since: Optional: Get prices that have been added or changed after this date time (greater or equal).
    :type changed_since: str

    """
    changed_since = util.deserialize_datetime(changed_since)
    return web.Response(status=200)


async def work_types_get_work_type(request: web.Request, guid) -> web.Response:
    """Get work type by ID.

    

    :param guid: Id used to get the work type.
    :type guid: str

    """
    return web.Response(status=200)


async def work_types_get_work_types(request: web.Request, active=None, productive=None, first_row=None, row_count=None, text_to_search=None, code=None, changed_since=None, calculate_row_count=None, sortings=None) -> web.Response:
    """Get all work types.

    

    :param active: Filter the work types. If true/false, only the active/inactive ones are returned. If null, all the work types are returned.
    :type active: bool
    :param productive: Filter the work types. If true/false, only the productive/non-productive ones are returned. If null, all the work types are returned.
    :type productive: bool
    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param text_to_search: Optional: Text to search from work type name or code.
    :type text_to_search: str
    :param code: Optional: Code of the work type.
    :type code: str
    :param changed_since: Optional: Get work types that have been added or changed after this date time (greater or equal).
    :type changed_since: str
    :param calculate_row_count: Optional: Calculate total number of rows.
    :type calculate_row_count: bool
    :param sortings: Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;name&amp;sortings[0].value&#x3D;Asc\&quot;.
    :type sortings: list | bytes

    """
    changed_since = util.deserialize_datetime(changed_since)
    sortings = [KeyValuePairOfStringAndSortDirection.from_dict(d) for d in sortings]
    return web.Response(status=200)
