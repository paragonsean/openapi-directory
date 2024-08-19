# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_activity_types_get_activity_type(client):
    """Test case for activity_types_get_activity_type

    Get Activity Type by ID
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/activitytypes/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_types_get_activity_types(client):
    """Test case for activity_types_get_activity_types

    Get the Activity Types
    """
    params = [('active', True),
                    ('pageToken', 'page_token_example'),
                    ('rowCount', 56),
                    ('changedSince', '2013-10-20T19:20:30+01:00'),
                    ('category', [openapi_server.ActivityCategory()])]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/activitytypes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bank_accounts_get_bank_account(client):
    """Test case for bank_accounts_get_bank_account

    Get bank account by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/bankaccounts/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bank_accounts_get_bank_accounts(client):
    """Test case for bank_accounts_get_bank_accounts

    Get all bank accounts for current organization.
    """
    params = [('companyGuid', 'company_guid_example'),
                    ('businessUnitGuid', 'business_unit_guid_example'),
                    ('active', True),
                    ('firstRow', 0),
                    ('rowCount', 56),
                    ('textToSearch', ''),
                    ('calculateRowCount', False),
                    ('sortings', [openapi_server.KeyValuePairOfStringAndSortDirection()])]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/bankaccounts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_business_units_get_business_unit(client):
    """Test case for business_units_get_business_unit

    Get businessUnit by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/businessunits/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_business_units_get_business_units(client):
    """Test case for business_units_get_business_units

    Get all the BusinessUnits
    """
    params = [('active', True),
                    ('companyGuid', 'company_guid_example'),
                    ('companyCountryGuid', 'company_country_guid_example'),
                    ('firstRow', 0),
                    ('rowCount', 56),
                    ('textToSearch', ''),
                    ('changedSince', '2013-10-20T19:20:30+01:00'),
                    ('code', ''),
                    ('name', '')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/businessunits',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_communication_types_get_communication_type(client):
    """Test case for communication_types_get_communication_type

    Get communication type by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/communicationtypes/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_communication_types_get_communication_types(client):
    """Test case for communication_types_get_communication_types

    Get all communication types.
    """
    params = [('active', True),
                    ('firstRow', 0),
                    ('rowCount', 56),
                    ('textToSearch', ''),
                    ('calculateRowCount', False),
                    ('sortings', [openapi_server.KeyValuePairOfStringAndSortDirection()])]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/communicationtypes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contact_roles_get_contact_role(client):
    """Test case for contact_roles_get_contact_role

    Get contact role by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/contactroles/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contact_roles_get_contact_roles(client):
    """Test case for contact_roles_get_contact_roles

    Get contact roles.
    """
    params = [('active', True),
                    ('firstRow', 0),
                    ('rowCount', 56),
                    ('textToSearch', ''),
                    ('calculateRowCount', False)]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/contactroles',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cost_accounts_get_cost_account(client):
    """Test case for cost_accounts_get_cost_account

    Get cost account by Guid.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/costaccounts/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cost_accounts_get_cost_accounts(client):
    """Test case for cost_accounts_get_cost_accounts

    Get cost accounts.
    """
    params = [('active', True),
                    ('firstRow', 56),
                    ('rowCount', 56),
                    ('textToSearch', ''),
                    ('calculateRowCount', False),
                    ('sortings', [openapi_server.KeyValuePairOfStringAndSortDirection()])]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/costaccounts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cost_centers_get_cost_center(client):
    """Test case for cost_centers_get_cost_center

    Get cost center by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/costcenters/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cost_centers_get_cost_centers(client):
    """Test case for cost_centers_get_cost_centers

    Get cost centers.
    """
    params = [('active', True),
                    ('firstRow', 56),
                    ('rowCount', 56),
                    ('textToSearch', ''),
                    ('changedSince', '2013-10-20T19:20:30+01:00'),
                    ('calculateRowCount', False),
                    ('sortings', [openapi_server.KeyValuePairOfStringAndSortDirection()]),
                    ('identifier', ''),
                    ('name', '')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/costcenters',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_countries_get_countries(client):
    """Test case for countries_get_countries

    Get all the Countries.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/localization/countries',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_countries_get_country(client):
    """Test case for countries_get_country

    Get country by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/localization/countries/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_countries_get_country_by_code2(client):
    """Test case for countries_get_country_by_code2

    Get a country by ISO Alpha-2 code
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/localization/countries/{code2}'.format(code2='code2_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_countries_get_country_by_code3(client):
    """Test case for countries_get_country_by_code3

    Get a country by ISO Alpha-3 code
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/localization/countries/{code3}'.format(code3='code3_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_countries_get_country_by_name(client):
    """Test case for countries_get_country_by_name

    Get a country by name
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/localization/countries/{country_name}'.format(country_name='country_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_countries_get_country_region(client):
    """Test case for countries_get_country_region

    Get country region by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/localization/countryregions/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_countries_get_country_regions(client):
    """Test case for countries_get_country_regions

    Get all the Country regions for a country.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/localization/countries/{country_guid}/countryregions'.format(country_guid='country_guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_currencies_get_currencies(client):
    """Test case for currencies_get_currencies

    Get all the Currencies
    """
    params = [('active', True),
                    ('firstRow', 0),
                    ('rowCount', 56),
                    ('textToSearch', ''),
                    ('calculateRowCount', False),
                    ('sortings', [openapi_server.KeyValuePairOfStringAndSortDirection()])]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/currencies',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_currencies_get_currency(client):
    """Test case for currencies_get_currency

    Get currency by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/currencies/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customer_custom_properties_get_customer_custom_properties(client):
    """Test case for customer_custom_properties_get_customer_custom_properties

    Get the customer custom properties.
    """
    params = [('firstRow', 0),
                    ('rowCount', 56),
                    ('active', True),
                    ('textToSearch', ''),
                    ('isInUse', True),
                    ('calculateRowCount', False),
                    ('sortings', [openapi_server.KeyValuePairOfStringAndSortDirection()])]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/customers/customproperties',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customer_custom_properties_get_customer_custom_property(client):
    """Test case for customer_custom_properties_get_customer_custom_property

    Get customer custom property by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/customers/customproperties/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customer_custom_property_selection_items_get_customer_custom_property_selection_item(client):
    """Test case for customer_custom_property_selection_items_get_customer_custom_property_selection_item

    Get customer custom property selection item by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/customers/customproperties/customercustompropertyselectionitems/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customer_custom_property_selection_items_get_customer_custom_property_selection_items(client):
    """Test case for customer_custom_property_selection_items_get_customer_custom_property_selection_items

    Get the customer custom properties.
    """
    params = [('rowCount', 56),
                    ('isActive', True),
                    ('pageToken', 'page_token_example'),
                    ('changedSince', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/customers/customproperties/{custom_property_guid}/customercustompropertyselectionitems'.format(custom_property_guid='custom_property_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_formatting_cultures_get_formatting_culture(client):
    """Test case for formatting_cultures_get_formatting_culture

    Get formatting culture by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/localization/formattingcultures/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_formatting_cultures_get_formattings(client):
    """Test case for formatting_cultures_get_formattings

    Get all the Formatting Cultures
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/localization/formattingcultures',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_holidays_get_holidays(client):
    """Test case for holidays_get_holidays

    Get holidays.
    """
    params = [('year', 56),
                    ('countryGuid', 'country_guid_example')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/holidays',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_holidays_get_holidays_by_time_period(client):
    """Test case for holidays_get_holidays_by_time_period

    Get holidays with start and end date.
    """
    params = [('startDate', '2013-10-20T19:20:30+01:00'),
                    ('endDate', '2013-10-20T19:20:30+01:00'),
                    ('countryGuid', 'country_guid_example')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/holidaysbytimeperiod',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_industries_get_industries(client):
    """Test case for industries_get_industries

    Get all the industries.
    """
    params = [('active', True),
                    ('firstRow', 56),
                    ('rowCount', 56),
                    ('textToSearch', ''),
                    ('calculateRowCount', False)]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/industries',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_industries_get_industry(client):
    """Test case for industries_get_industry

    Get industry by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/industries/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoice_statuses_get_invoice_status(client):
    """Test case for invoice_statuses_get_invoice_status

    Get Invoice status by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/invoicestatuses/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoice_statuses_get_invoice_statuses(client):
    """Test case for invoice_statuses_get_invoice_statuses

    Get invoice statuses.
    """
    params = [('active', True),
                    ('firstRow', 56),
                    ('rowCount', 56),
                    ('textToSearch', ''),
                    ('calculateRowCount', False),
                    ('sortings', [openapi_server.KeyValuePairOfStringAndSortDirection()])]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/invoicestatuses',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoice_templates_get_invoice_template(client):
    """Test case for invoice_templates_get_invoice_template

    Get invoice template by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/invoicetemplates/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoice_templates_get_invoice_templates(client):
    """Test case for invoice_templates_get_invoice_templates

    Get invoice templates.
    """
    params = [('active', True),
                    ('firstRow', 56),
                    ('rowCount', 56),
                    ('textToSearch', ''),
                    ('calculateRowCount', False),
                    ('sortings', [openapi_server.KeyValuePairOfStringAndSortDirection()])]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/invoicetemplates',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_keywords_get_keyword(client):
    """Test case for keywords_get_keyword

    Get keyword by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/keywords/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_keywords_get_keywords(client):
    """Test case for keywords_get_keywords

    Get all the keywords.
    """
    params = [('category', openapi_server.KeywordCategory()),
                    ('active', True),
                    ('firstRow', 0),
                    ('rowCount', 56),
                    ('textToSearch', ''),
                    ('changedSince', '2013-10-20T19:20:30+01:00'),
                    ('calculateRowCount', False),
                    ('sortings', [openapi_server.KeyValuePairOfStringAndSortDirection()]),
                    ('keyword', '')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/keywords',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_kpi_formulas_get_kpi_formulas(client):
    """Test case for kpi_formulas_get_kpi_formulas

    Get saved KPI formulas.
    """
    params = [('category', openapi_server.KpiFormulaCategory()),
                    ('isActive', True),
                    ('firstRow', 0),
                    ('rowCount', 56),
                    ('textToSearch', ''),
                    ('sortings', [openapi_server.KeyValuePairOfStringAndSortDirection()]),
                    ('includeDefinition', False),
                    ('changedSince', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/kpiformulas',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_languages_get_language(client):
    """Test case for languages_get_language

    Get language by ID
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/localization/languages/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_languages_get_languages(client):
    """Test case for languages_get_languages

    Get all the languages
    """
    params = [('isInvoiceLanguage', True)]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/localization/languages',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lead_sources_get_lead_source(client):
    """Test case for lead_sources_get_lead_source

    Get lead source by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/leadsources/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lead_sources_get_lead_sources(client):
    """Test case for lead_sources_get_lead_sources

    Get the lead sources.
    """
    params = [('active', True),
                    ('firstRow', 56),
                    ('rowCount', 56),
                    ('textToSearch', ''),
                    ('calculateRowCount', False)]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/leadsources',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_market_segments_get_market_segment(client):
    """Test case for market_segments_get_market_segment

    Get Market Segment by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/marketsegments/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_market_segments_get_market_segments(client):
    """Test case for market_segments_get_market_segments

    Get the Market Segments.
    """
    params = [('active', True),
                    ('firstRow', 0),
                    ('rowCount', 56),
                    ('textToSearch', ''),
                    ('calculateRowCount', False),
                    ('includeChildSegments', True)]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/marketsegments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_overtime_prices_get_overtime_price(client):
    """Test case for overtime_prices_get_overtime_price

    Get overtime price by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/overtimeprices/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_overtime_prices_get_overtime_prices(client):
    """Test case for overtime_prices_get_overtime_prices

    Get all the overtime prices for a price list version.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/pricelistversions/{pricelist_version_guid}/overtimeprices'.format(pricelist_version_guid='pricelist_version_guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_overtimes_get_overtime(client):
    """Test case for overtimes_get_overtime

    Get overtime definition by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/overtimes/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_overtimes_get_overtimes(client):
    """Test case for overtimes_get_overtimes

    Get overtime definitions.
    """
    params = [('active', True),
                    ('firstRow', 56),
                    ('rowCount', 56),
                    ('textToSearch', ''),
                    ('calculateRowCount', False),
                    ('sortings', [openapi_server.KeyValuePairOfStringAndSortDirection()])]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/overtimes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_permission_profiles_get_permission_profile(client):
    """Test case for permission_profiles_get_permission_profile

    Get Permission Profile by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/permissionprofiles/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_permission_profiles_get_permission_profiles(client):
    """Test case for permission_profiles_get_permission_profiles

    Get the Permission Profiles.
    """
    params = [('active', True),
                    ('firstRow', 56),
                    ('rowCount', 56),
                    ('textToSearch', ''),
                    ('calculateRowCount', False),
                    ('sortings', [openapi_server.KeyValuePairOfStringAndSortDirection()])]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/permissionprofiles',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_phase_status_types_get_phase_status_type(client):
    """Test case for phase_status_types_get_phase_status_type

    Get phase status type by GUID
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/phasestatustypes/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_phase_status_types_get_phase_status_types(client):
    """Test case for phase_status_types_get_phase_status_types

    Get phase status types
    """
    params = [('active', True),
                    ('firstRow', 56),
                    ('rowCount', 56),
                    ('textToSearch', ''),
                    ('calculateRowCount', False),
                    ('sortings', [openapi_server.KeyValuePairOfStringAndSortDirection()])]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/phasestatustypes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_price_list_versions_get_pricelist_version(client):
    """Test case for price_list_versions_get_pricelist_version

    Get a price list version by guid.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/pricelistversions/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_price_list_versions_get_pricelist_versions_by_pricelist(client):
    """Test case for price_list_versions_get_pricelist_versions_by_pricelist

    Get all price list versions of a price list.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/pricelists/{pricelist_guid}/pricelistversions'.format(pricelist_guid='pricelist_guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_price_lists_get_price_list(client):
    """Test case for price_lists_get_price_list

    Get price list by GUID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/pricelists/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_price_lists_get_pricelists(client):
    """Test case for price_lists_get_pricelists

    Get all price lists.
    """
    params = [('active', True),
                    ('firstRow', 0),
                    ('rowCount', 56),
                    ('textToSearch', ''),
                    ('currencyGuid', 'currency_guid_example'),
                    ('calculateRowCount', False),
                    ('sortings', [openapi_server.KeyValuePairOfStringAndSortDirection()]),
                    ('name', '')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/pricelists',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_categories_get_product_categories(client):
    """Test case for product_categories_get_product_categories

    Get product categories.
    """
    params = [('active', True),
                    ('firstRow', 56),
                    ('rowCount', 56),
                    ('textToSearch', ''),
                    ('changedSince', '2013-10-20T19:20:30+01:00'),
                    ('calculateRowCount', False),
                    ('sortings', [openapi_server.KeyValuePairOfStringAndSortDirection()])]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/productcategories',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_categories_get_product_category(client):
    """Test case for product_categories_get_product_category

    Get product category by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/productcategories/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_country_settings_get_product_country_settings(client):
    """Test case for product_country_settings_get_product_country_settings

    Get all the country settings for a product
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/products/{product_guid}/productcountrysettings'.format(product_guid='product_guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_prices_get_product_price(client):
    """Test case for product_prices_get_product_price

    Get product price by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/productprices/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_prices_get_product_prices(client):
    """Test case for product_prices_get_product_prices

    Get all the product prices for a price list version.
    """
    params = [('fromPricelistOnly', False),
                    ('firstRow', 0),
                    ('rowCount', 56),
                    ('textToSearch', ''),
                    ('calculateRowCount', False),
                    ('productCode', ''),
                    ('productGuids', ['product_guids_example']),
                    ('isVolumePriced', True),
                    ('productCategoryGuids', ['product_category_guids_example']),
                    ('productTypes', [openapi_server.ProductType()])]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/pricelistversions/{pricelist_version_guid}/productprices'.format(pricelist_version_guid='pricelist_version_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_get_product(client):
    """Test case for products_get_product

    Get product by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/products/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_get_products(client):
    """Test case for products_get_products

    Get all the Products
    """
    params = [('rowCount', 56),
                    ('pageToken', 'page_token_example'),
                    ('type', openapi_server.ProductType()),
                    ('isActive', True),
                    ('code', 'code_example'),
                    ('changedSince', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/products',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_billing_customers_get_project_billing_customer(client):
    """Test case for project_billing_customers_get_project_billing_customer

    Get a project billing customer.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projectbillingcustomers/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_custom_properties_get_project_custom_properties(client):
    """Test case for project_custom_properties_get_project_custom_properties

    Get the project custom properties.
    """
    params = [('firstRow', 0),
                    ('rowCount', 56),
                    ('active', True),
                    ('textToSearch', ''),
                    ('isInUse', True),
                    ('calculateRowCount', False),
                    ('sortings', [openapi_server.KeyValuePairOfStringAndSortDirection()])]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projects/customproperties',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_custom_properties_get_project_custom_property(client):
    """Test case for project_custom_properties_get_project_custom_property

    Get project custom property by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projects/customproperties/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_custom_property_selection_items_get_project_custom_property_selection_item(client):
    """Test case for project_custom_property_selection_items_get_project_custom_property_selection_item

    Get project custom property selection item by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projects/customproperties/projectcustompropertyselectionitems/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_custom_property_selection_items_get_project_custom_property_selection_items(client):
    """Test case for project_custom_property_selection_items_get_project_custom_property_selection_items

    Get the project custom properties.
    """
    params = [('rowCount', 56),
                    ('isActive', True),
                    ('pageToken', 'page_token_example'),
                    ('changedSince', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projects/customproperties/{custom_property_guid}/projectcustompropertyselectionitems'.format(custom_property_guid='custom_property_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_member_cost_exceptions_get_project_member_cost_exception(client):
    """Test case for project_member_cost_exceptions_get_project_member_cost_exception

    Get project member cost exception by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projectmembercostexceptions/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_status_types_get_project_status_type(client):
    """Test case for project_status_types_get_project_status_type

    Get projectStatusType by ID
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projectstatustypes/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_status_types_get_project_status_types(client):
    """Test case for project_status_types_get_project_status_types

    Get all the ProjectStatusTypes
    """
    params = [('active', True),
                    ('firstRow', 56),
                    ('rowCount', 56),
                    ('textToSearch', ''),
                    ('calculateRowCount', False),
                    ('sortings', [openapi_server.KeyValuePairOfStringAndSortDirection()])]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projectstatustypes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_task_statuses_get_project_task_status(client):
    """Test case for project_task_statuses_get_project_task_status

    Get Project task status by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projecttaskstatuses/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_task_statuses_get_project_task_statuses(client):
    """Test case for project_task_statuses_get_project_task_statuses

    Get the project task statuses.
    """
    params = [('active', True),
                    ('firstRow', 0),
                    ('rowCount', 56),
                    ('textToSearch', ''),
                    ('calculateRowCount', False),
                    ('sortings', [openapi_server.KeyValuePairOfStringAndSortDirection()])]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projecttaskstatuses',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_proposal_statuses_get_proposal_status(client):
    """Test case for proposal_statuses_get_proposal_status

    Get Proposal status by ID
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/proposalstatuses/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_proposal_statuses_get_proposal_statuses(client):
    """Test case for proposal_statuses_get_proposal_statuses

    Get all the proposal statuses
    """
    params = [('isActive', True),
                    ('pageToken', 'page_token_example'),
                    ('rowCount', 56),
                    ('proposalStatusName', '')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/proposalstatuses',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_proposal_statuses_get_usage(client):
    """Test case for proposal_statuses_get_usage

    Get usage for an proposal status.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/proposalstatuses/{guid}/usage'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_roles_get_role(client):
    """Test case for roles_get_role

    Get role by GUID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/roles/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_roles_get_roles(client):
    """Test case for roles_get_roles

    Get roles.
    """
    params = [('isActive', True),
                    ('pageToken', 'page_token_example'),
                    ('rowCount', 56),
                    ('changedSince', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/roles',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_accounts_get_sales_account(client):
    """Test case for sales_accounts_get_sales_account

    Get sales account by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/salesaccounts/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_accounts_get_sales_accounts(client):
    """Test case for sales_accounts_get_sales_accounts

    Get sales accounts.
    """
    params = [('active', True),
                    ('firstRow', 56),
                    ('rowCount', 56),
                    ('textToSearch', ''),
                    ('calculateRowCount', False),
                    ('sortings', [openapi_server.KeyValuePairOfStringAndSortDirection()])]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/salesaccounts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_status_types_get_sales_status_type(client):
    """Test case for sales_status_types_get_sales_status_type

    Get sales status type by ID
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/salesstatustypes/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_status_types_get_sales_status_types(client):
    """Test case for sales_status_types_get_sales_status_types

    Get all the sales status types
    """
    params = [('active', True),
                    ('salesState', openapi_server.SalesStatusType()),
                    ('firstRow', 0),
                    ('rowCount', 56),
                    ('textToSearch', ''),
                    ('calculateRowCount', False),
                    ('sortings', [openapi_server.KeyValuePairOfStringAndSortDirection()])]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/salesstatustypes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_time_entry_types_get_time_entry_type(client):
    """Test case for time_entry_types_get_time_entry_type

    Get time entry type by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/timeentrytypes/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_time_entry_types_get_time_entry_types(client):
    """Test case for time_entry_types_get_time_entry_types

    Get all time entry types.
    """
    params = [('active', True),
                    ('firstRow', 0),
                    ('rowCount', 56),
                    ('textToSearch', ''),
                    ('calculateRowCount', False),
                    ('sortings', [openapi_server.KeyValuePairOfStringAndSortDirection()])]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/timeentrytypes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_timezones_get_timezone(client):
    """Test case for timezones_get_timezone

    Get timezone by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/localization/timezones/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_timezones_get_timezones(client):
    """Test case for timezones_get_timezones

    Get all the timezones.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/localization/timezones',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_travel_expense_type_country_settings_get_travel_expense_type_country_settings(client):
    """Test case for travel_expense_type_country_settings_get_travel_expense_type_country_settings

    Get all country settings for a travel expense type
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/travelexpensetypes/{travel_expense_type_guid}/travelexpensetypecountrysettings'.format(travel_expense_type_guid='travel_expense_type_guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_travel_expense_types_get_travel_expense_type(client):
    """Test case for travel_expense_types_get_travel_expense_type

    Get travel expense type by guid.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/travelexpensetypes/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_travel_expense_types_get_travel_expense_types(client):
    """Test case for travel_expense_types_get_travel_expense_types

    Get all the travel expense types.
    """
    params = [('active', True),
                    ('firstRow', 0),
                    ('rowCount', 56),
                    ('textToSearch', 'text_to_search_example'),
                    ('code', ''),
                    ('calculateRowCount', False),
                    ('sortings', [openapi_server.KeyValuePairOfStringAndSortDirection()])]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/travelexpensetypes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_travel_prices_get_travel_price(client):
    """Test case for travel_prices_get_travel_price

    Get travel price by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/travelprices/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_travel_prices_get_travel_prices(client):
    """Test case for travel_prices_get_travel_prices

    Get all the travel prices for a price list version.
    """
    params = [('fromPricelistOnly', False),
                    ('expenseClasses', [openapi_server.ExpensesClass()]),
                    ('firstRow', 0),
                    ('rowCount', 56),
                    ('textToSearch', ''),
                    ('calculateRowCount', False)]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/pricelistversions/{pricelist_version_guid}/travelprices'.format(pricelist_version_guid='pricelist_version_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_travel_reimbursement_status_get_travel_reimbursement_status(client):
    """Test case for travel_reimbursement_status_get_travel_reimbursement_status

    Get the travel reimbursement statuses by guid.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/travelreimbursementstatuses/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_travel_reimbursement_status_get_travel_reimbursement_statuses(client):
    """Test case for travel_reimbursement_status_get_travel_reimbursement_statuses

    Get the travel reimbursement statuses.
    """
    params = [('active', True),
                    ('firstRow', 0),
                    ('rowCount', 56),
                    ('textToSearch', ''),
                    ('calculateRowCount', False),
                    ('sortings', [openapi_server.KeyValuePairOfStringAndSortDirection()])]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/travelreimbursementstatuses',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_custom_properties_get_user_custom_properties(client):
    """Test case for user_custom_properties_get_user_custom_properties

    Get the user custom properties.
    """
    params = [('pageToken', 'page_token_example'),
                    ('rowCount', 56),
                    ('isActive', True),
                    ('isInUse', True),
                    ('changedSince', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/users/customproperties',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_custom_properties_get_user_custom_property(client):
    """Test case for user_custom_properties_get_user_custom_property

    Get user custom property by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/users/customproperties/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_custom_property_selection_items_get_user_custom_property_selection_item(client):
    """Test case for user_custom_property_selection_items_get_user_custom_property_selection_item

    Get user custom property selection item by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/users/customproperties/usercustompropertyselectionitems/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_custom_property_selection_items_get_user_custom_property_selection_items(client):
    """Test case for user_custom_property_selection_items_get_user_custom_property_selection_items

    Get the user custom properties.
    """
    params = [('rowCount', 56),
                    ('isActive', True),
                    ('pageToken', 'page_token_example'),
                    ('changedSince', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/users/customproperties/{custom_property_guid}/usercustompropertyselectionitems'.format(custom_property_guid='custom_property_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vat_rates_get_vat_rate(client):
    """Test case for vat_rates_get_vat_rate

    Get a vat rate by GUID
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/vatrates/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vat_rates_get_vat_rates(client):
    """Test case for vat_rates_get_vat_rates

    Get all organization vat rates
    """
    params = [('countryGuid', 'country_guid_example'),
                    ('active', True)]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/vatrates',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_work_contracts_get_work_contract(client):
    """Test case for work_contracts_get_work_contract

    Get work contract by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/workcontracts/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_work_hour_prices_get_work_hour_price(client):
    """Test case for work_hour_prices_get_work_hour_price

    Get work hour price by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/workhourprices/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_work_hour_prices_get_work_hour_prices(client):
    """Test case for work_hour_prices_get_work_hour_prices

    Get all the workHourPrices for a price list version.
    """
    params = [('pageToken', 'page_token_example'),
                    ('rowCount', 56),
                    ('changedSince', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/pricelistversions/{pricelist_version_guid}/workhourprices'.format(pricelist_version_guid='pricelist_version_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_work_types_get_work_type(client):
    """Test case for work_types_get_work_type

    Get work type by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/worktypes/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_work_types_get_work_types(client):
    """Test case for work_types_get_work_types

    Get all work types.
    """
    params = [('active', True),
                    ('productive', True),
                    ('firstRow', 0),
                    ('rowCount', 56),
                    ('textToSearch', ''),
                    ('code', ''),
                    ('changedSince', '2013-10-20T19:20:30+01:00'),
                    ('calculateRowCount', False),
                    ('sortings', [openapi_server.KeyValuePairOfStringAndSortDirection()])]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/worktypes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

