# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_keywords_get_project_keywords(client):
    """Test case for keywords_get_project_keywords

    Get all the keywords for project.
    """
    params = [('active', True),
                    ('sortings', [openapi_server.KeyValuePairOfStringAndSortDirection()])]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projects/{project_guid}/keywords'.format(project_guid='project_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_overtime_prices_get_overtime_prices_for_project(client):
    """Test case for overtime_prices_get_overtime_prices_for_project

    Get all the overtimePrices for a project.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projects/{project_guid}/overtimeprices'.format(project_guid='project_guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_phase_members_get_all_deleted_phase_members(client):
    """Test case for phase_members_get_all_deleted_phase_members

    Get all deleted phase members
    """
    params = [('deletedSince', '2013-10-20T19:20:30+01:00'),
                    ('pageToken', 'page_token_example'),
                    ('rowCount', 56),
                    ('isUserActive', True)]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/deletedphasemembers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_phase_members_get_all_phase_members(client):
    """Test case for phase_members_get_all_phase_members

    Get all active phase members
    """
    params = [('changedSince', '2013-10-20T19:20:30+01:00'),
                    ('pageToken', 'page_token_example'),
                    ('rowCount', 56),
                    ('isUserActive', True)]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/phasemembers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_phase_members_get_phase_members(client):
    """Test case for phase_members_get_phase_members

    Get phase members
    """
    params = [('pageToken', 'page_token_example'),
                    ('rowCount', 56),
                    ('isActive', True),
                    ('isUserActive', True)]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/phases/{phase_guid}/phasemembers'.format(phase_guid='phase_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_phases_get_phase(client):
    """Test case for phases_get_phase

    Get phase by ID
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/phases/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_phases_get_phases(client):
    """Test case for phases_get_phases

    Get the phases.
    """
    params = [('pageToken', 'page_token_example'),
                    ('rowCount', 56),
                    ('changedSince', '2013-10-20T19:20:30+01:00'),
                    ('code', ''),
                    ('projectGuids', ['project_guids_example'])]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/phases',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_phases_get_project_phases(client):
    """Test case for phases_get_project_phases

    Get project's phases as flat list
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projects/{guid}/phaseswithhierarchy'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_phases_get_root_phases(client):
    """Test case for phases_get_root_phases

    Get a list of root phases with information about hierarchy.
    """
    params = [('pageToken', 'page_token_example'),
                    ('rowCount', 56),
                    ('customerGuids', ['customer_guids_example']),
                    ('projectGuids', ['project_guids_example']),
                    ('projectKeywordGuids', ['project_keyword_guids_example']),
                    ('projectStatusTypeGuids', ['project_status_type_guids_example']),
                    ('salesPersonGuids', ['sales_person_guids_example']),
                    ('projectOwnerGuids', ['project_owner_guids_example']),
                    ('businessUnitGuids', ['business_unit_guids_example']),
                    ('customerOwnerGuids', ['customer_owner_guids_example']),
                    ('salesStatusTypeGuids', ['sales_status_type_guids_example']),
                    ('openProjects', True),
                    ('projectMemberUserGuids', ['project_member_user_guids_example'])]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/rootphaseswithhierarchy',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_prices_get_product_prices_for_project(client):
    """Test case for product_prices_get_product_prices_for_project

    Get all the productPrices for a project.
    """
    params = [('fromPricelistOnly', False),
                    ('firstRow', 0),
                    ('rowCount', 56),
                    ('textToSearch', ''),
                    ('calculateRowCount', False),
                    ('isAvailable', True),
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
        path='/rest-api/v1/projects/{project_guid}/productprices'.format(project_guid='project_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_get_searched_products(client):
    """Test case for products_get_searched_products

    Gets available products for the given project where price information comes from projects price list
    """
    params = [('rowCount', 56),
                    ('pageToken', 'page_token_example'),
                    ('type', openapi_server.ProductType()),
                    ('includeProductsFromRegistry', False)]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projects/{project_guid}/productsforproject'.format(project_guid='project_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_billing_customers_get_work_hour_prices_for_project(client):
    """Test case for project_billing_customers_get_work_hour_prices_for_project

    Get all the billing customers for a project
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projects/{project_guid}/projectbillingcustomers'.format(project_guid='project_guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_custom_values_get_project_custom_value(client):
    """Test case for project_custom_values_get_project_custom_value

    Get project custom value by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projects/customvalues/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_custom_values_get_project_custom_values(client):
    """Test case for project_custom_values_get_project_custom_values

    Get the project custom values.
    """
    params = [('firstRow', 0),
                    ('rowCount', 56),
                    ('active', True),
                    ('target', ['target_example']),
                    ('calculateRowCount', False),
                    ('sortings', [openapi_server.KeyValuePairOfStringAndSortDirection()])]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projects/{project_guid}/customvalues'.format(project_guid='project_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_forecasts_get_forecast(client):
    """Test case for project_forecasts_get_forecast

    Get project forecast by ID
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projectforecasts/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_forecasts_get_forecasts(client):
    """Test case for project_forecasts_get_forecasts

    Get the project forecasts
    """
    params = [('startDate', '2013-10-20T19:20:30+01:00'),
                    ('endDate', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projects/{project_guid}/projectforecasts'.format(project_guid='project_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_invoice_settings_get_project_invoice_setting_0(client):
    """Test case for project_invoice_settings_get_project_invoice_setting_0

    Get project invoice settings by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projectinvoicesettings/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_invoice_settings_get_project_invoice_settings_0(client):
    """Test case for project_invoice_settings_get_project_invoice_settings_0

    Get project invoice settings by project ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projects/{project_guid}/projectinvoicesettings'.format(project_guid='project_guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_member_cost_exceptions_get_project_member_cost_exceptions_for_project(client):
    """Test case for project_member_cost_exceptions_get_project_member_cost_exceptions_for_project

    Get all cost exceptions of project members for a project.
    """
    params = [('userGuid', 'user_guid_example'),
                    ('firstRow', 0),
                    ('rowCount', 56)]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projects/{project_guid}/projectmembercostexceptions'.format(project_guid='project_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_products_get_project_products(client):
    """Test case for project_products_get_project_products

    Get project products
    """
    params = [('includeProductsFromRegistry', False),
                    ('pageToken', 'page_token_example'),
                    ('rowCount', 56),
                    ('active', True)]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projects/{project_guid}/projectproducts'.format(project_guid='project_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_work_hour_prices_get_project_work_hour_price(client):
    """Test case for project_work_hour_prices_get_project_work_hour_price

    Get project work hour price by ID
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projectworkhourprices/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_work_hour_prices_get_work_hour_prices_for_project(client):
    """Test case for project_work_hour_prices_get_work_hour_prices_for_project

    Get all the work hour prices for a project
    """
    params = [('fromPricelistOnly', False),
                    ('isAvailable', True),
                    ('changedSince', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projects/{project_guid}/projectworkhourprices'.format(project_guid='project_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_work_types_get_project_worktypes(client):
    """Test case for project_work_types_get_project_worktypes

    Get project work types.
    """
    params = [('includeWorktypesFromRegistry', False),
                    ('firstRow', 0),
                    ('rowCount', 56),
                    ('active', True),
                    ('textToSearch', ''),
                    ('changedSince', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projects/{project_guid}/projectworktypes'.format(project_guid='project_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_get_customer_projects(client):
    """Test case for projects_get_customer_projects

    Get customer's projects
    """
    params = [('pageToken', 'page_token_example'),
                    ('rowCount', 56),
                    ('isBillable', True),
                    ('currencyGuids', ['currency_guids_example']),
                    ('projectGuids', ['project_guids_example']),
                    ('projectKeywordGuids', ['project_keyword_guids_example']),
                    ('projectStatusTypeGuids', ['project_status_type_guids_example']),
                    ('salesPersonGuids', ['sales_person_guids_example']),
                    ('projectOwnerGuids', ['project_owner_guids_example']),
                    ('businessUnitGuids', ['business_unit_guids_example']),
                    ('minimumBillableAmount', 3.4),
                    ('customerOwnerGuids', ['customer_owner_guids_example']),
                    ('invoiceableDate', '2013-10-20T19:20:30+01:00'),
                    ('marketSegmentationGuids', ['market_segmentation_guids_example']),
                    ('salesStatusTypeGuids', ['sales_status_type_guids_example']),
                    ('isClosed', True),
                    ('hasRecurringFees', True),
                    ('companyCurrencyGuids', ['company_currency_guids_example']),
                    ('projectMemberUserGuids', ['project_member_user_guids_example']),
                    ('numbers', [56])]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/customers/{customer_guid}/projects'.format(customer_guid='customer_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_get_project(client):
    """Test case for projects_get_project

    Get project by ID
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projects/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_get_projects(client):
    """Test case for projects_get_projects

    Get all the projects
    """
    params = [('pageToken', 'page_token_example'),
                    ('rowCount', 56),
                    ('currencyGuid', 'currency_guid_example'),
                    ('changedSince', '2013-10-20T19:20:30+01:00'),
                    ('isBillable', True),
                    ('customerGuids', ['customer_guids_example']),
                    ('projectGuids', ['project_guids_example']),
                    ('projectKeywordGuids', ['project_keyword_guids_example']),
                    ('projectStatusTypeGuids', ['project_status_type_guids_example']),
                    ('salesPersonGuids', ['sales_person_guids_example']),
                    ('projectOwnerGuids', ['project_owner_guids_example']),
                    ('businessUnitGuids', ['business_unit_guids_example']),
                    ('minimumBillableAmount', 3.4),
                    ('customerOwnerGuids', ['customer_owner_guids_example']),
                    ('invoiceableDate', '2013-10-20T19:20:30+01:00'),
                    ('marketSegmentationGuids', ['market_segmentation_guids_example']),
                    ('salesStatusTypeGuids', ['sales_status_type_guids_example']),
                    ('isClosed', True),
                    ('hasRecurringFees', True),
                    ('companyCurrencyGuids', ['company_currency_guids_example']),
                    ('projectMemberUserGuids', ['project_member_user_guids_example']),
                    ('numbers', [56]),
                    ('internal', True)]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projects',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_get_sales_cases(client):
    """Test case for projects_get_sales_cases

    Gets the sales cases (sales status is in progress)
    """
    params = [('pageToken', 'page_token_example'),
                    ('rowCount', 56),
                    ('customerGuids', ['customer_guids_example']),
                    ('currencyGuids', ['currency_guids_example']),
                    ('projectGuids', ['project_guids_example']),
                    ('projectKeywordGuids', ['project_keyword_guids_example']),
                    ('projectStatusTypeGuids', ['project_status_type_guids_example']),
                    ('salesPersonGuids', ['sales_person_guids_example']),
                    ('projectOwnerGuids', ['project_owner_guids_example']),
                    ('businessUnitGuids', ['business_unit_guids_example']),
                    ('minimumBillableAmount', 3.4),
                    ('customerOwnerGuids', ['customer_owner_guids_example']),
                    ('invoiceableDate', '2013-10-20T19:20:30+01:00'),
                    ('marketSegmentationGuids', ['market_segmentation_guids_example']),
                    ('salesStatusTypeGuids', ['sales_status_type_guids_example']),
                    ('isClosed', True),
                    ('hasRecurringFees', True),
                    ('companyCurrencyGuids', ['company_currency_guids_example']),
                    ('projectMemberUserGuids', ['project_member_user_guids_example']),
                    ('numbers', [56])]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/salescases',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_proposal_fees_get_proposal_fee(client):
    """Test case for proposal_fees_get_proposal_fee

    Get the proposal fee rows by guid
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/proposalfeerows/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_proposal_fees_get_proposal_fees(client):
    """Test case for proposal_fees_get_proposal_fees

    Get the proposal fee rows.
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
        path='/rest-api/v1/proposalfeerows',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_proposal_fees_get_proposal_fees_for_proposal(client):
    """Test case for proposal_fees_get_proposal_fees_for_proposal

    Get all the proposal fee rows for a proposal
    """
    params = [('pageToken', 'page_token_example'),
                    ('rowCount', 56)]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/proposals/{proposal_guid}/proposalfeerows'.format(proposal_guid='proposal_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_proposal_settings_get_proposal_settings(client):
    """Test case for proposal_settings_get_proposal_settings

    Get settings for a proposal
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/proposals/{guid}/proposalsettings'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_proposal_subtotals_get_proposal_subtotal(client):
    """Test case for proposal_subtotals_get_proposal_subtotal

    Get Proposal subtotal by ID
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/proposalsubtotals/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_proposal_subtotals_get_proposal_subtotals(client):
    """Test case for proposal_subtotals_get_proposal_subtotals

    Get the proposal subtotals.
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
        path='/rest-api/v1/proposalsubtotals',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_proposal_subtotals_get_proposal_subtotals_for_proposal(client):
    """Test case for proposal_subtotals_get_proposal_subtotals_for_proposal

    Get all the proposal subtotals for a proposal
    """
    params = [('pageToken', 'page_token_example'),
                    ('rowCount', 56)]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/proposals/{proposal_guid}/proposalsubtotals'.format(proposal_guid='proposal_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_proposal_workhours_get_proposal_work_hours(client):
    """Test case for proposal_workhours_get_proposal_work_hours

    Get the proposal work rows.
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
        path='/rest-api/v1/proposalworkrows',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_proposal_workhours_get_proposal_work_hours_for_proposal(client):
    """Test case for proposal_workhours_get_proposal_work_hours_for_proposal

    Get all the proposal work rows.
    """
    params = [('pageToken', 'page_token_example'),
                    ('rowCount', 56)]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/proposals/{proposal_guid}/proposalworkrows'.format(proposal_guid='proposal_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_proposal_workhours_get_proposal_workhour(client):
    """Test case for proposal_workhours_get_proposal_workhour

    Get the proposal work row by guid.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/proposalworkrows/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_proposals_get_proposal(client):
    """Test case for proposals_get_proposal

    Get Proposal by ID
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/proposals/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_proposals_get_proposals(client):
    """Test case for proposals_get_proposals

    Get all the proposals
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
        path='/rest-api/v1/proposals',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_proposals_get_proposals_for_project(client):
    """Test case for proposals_get_proposals_for_project

    Get all the proposals for a project
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
        path='/rest-api/v1/projects/{project_guid}/proposals'.format(project_guid='project_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_notes_get_all_customer_sales_notes(client):
    """Test case for sales_notes_get_all_customer_sales_notes

    Get the sales notes by customer guid.
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
        path='/rest-api/v1/customers/{customer_guid}/salesnotes'.format(customer_guid='customer_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_notes_get_project_sales_note(client):
    """Test case for sales_notes_get_project_sales_note

    Get project sales note by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projectsalesnotes/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_notes_get_project_sales_notes(client):
    """Test case for sales_notes_get_project_sales_notes

    Get the sales notes of a case.
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
        path='/rest-api/v1/projects/{project_guid}/projectsalesnotes'.format(project_guid='project_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_status_history_get_sales_status_history(client):
    """Test case for sales_status_history_get_sales_status_history

    Get the sales status history for a project
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projects/{project_guid}/salesstatushistory'.format(project_guid='project_guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_team_productivity_get_team_productivity(client):
    """Test case for team_productivity_get_team_productivity

    Get team productivity of a project.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projects/{project_guid}/teamproductivity'.format(project_guid='project_guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_travel_expense_types_get_searched_travel_expense_types(client):
    """Test case for travel_expense_types_get_searched_travel_expense_types

    Search active travel expense types of project by part of the name or code.
    """
    params = [('textToSearch', ''),
                    ('firstRow', 56),
                    ('rowCount', 56),
                    ('userGuid', 'user_guid_example'),
                    ('expenseClass', openapi_server.ExpensesClass())]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projects/{project_guid}/travelexpensetypes'.format(project_guid='project_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_travel_prices_get_travel_prices_for_project(client):
    """Test case for travel_prices_get_travel_prices_for_project

    Get all the travel prices for a project.
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
        path='/rest-api/v1/projects/{project_guid}/travelprices'.format(project_guid='project_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_work_types_get_phase_work_types(client):
    """Test case for work_types_get_phase_work_types

    Get all work types that are available for a phase (for work hour entry)
    """
    params = [('pageToken', 'page_token_example'),
                    ('rowCount', 56),
                    ('userGuid', 'user_guid_example')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/phases/{phase_guid}/worktypes'.format(phase_guid='phase_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_work_types_get_searched_worktypes(client):
    """Test case for work_types_get_searched_worktypes

    Search active work types by part of the name or code.
    """
    params = [('firstRow', 56),
                    ('rowCount', 56),
                    ('textToSearch', '')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projects/{project_guid}/worktypesforproject'.format(project_guid='project_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

