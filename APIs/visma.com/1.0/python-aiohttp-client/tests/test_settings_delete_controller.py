# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.exception_model import ExceptionModel


pytestmark = pytest.mark.asyncio

async def test_activity_types_delete_activity_type(client):
    """Test case for activity_types_delete_activity_type

    Delete an activity type.
    """
    params = [('moveUsagesToGuid', 'move_usages_to_guid_example')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest-api/v1/activitytypes/{guid}'.format(guid='guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_communication_types_delete_communication_type(client):
    """Test case for communication_types_delete_communication_type

    Deletes a communication type.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest-api/v1/communicationtypes/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contact_roles_delete_contact_role(client):
    """Test case for contact_roles_delete_contact_role

    Delete a contact role.
    """
    params = [('moveUsagesToGuid', 'move_usages_to_guid_example')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest-api/v1/contactroles/{guid}'.format(guid='guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cost_accounts_delete_cost_account(client):
    """Test case for cost_accounts_delete_cost_account

    Delete a cost account.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest-api/v1/costaccounts/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cost_centers_delete_cost_center(client):
    """Test case for cost_centers_delete_cost_center

    Delete a cost center.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest-api/v1/costcenters/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customer_custom_properties_delete_customer_custom_property(client):
    """Test case for customer_custom_properties_delete_customer_custom_property

    Deletes a customer custom property.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest-api/v1/customers/customproperties/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customer_custom_property_selection_items_delete_customer_custom_property_selection_item(client):
    """Test case for customer_custom_property_selection_items_delete_customer_custom_property_selection_item

    Deletes a customer custom property selection item.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest-api/v1/customers/customproperties/customercustompropertyselectionitems/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_industries_delete_industry(client):
    """Test case for industries_delete_industry

    Delete an industry.
    """
    params = [('moveUsagesToGuid', 'move_usages_to_guid_example')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest-api/v1/industries/{guid}'.format(guid='guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoice_statuses_delete_invoice_status(client):
    """Test case for invoice_statuses_delete_invoice_status

    Delete an invoice status.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest-api/v1/invoicestatuses/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_keywords_delete_keyword(client):
    """Test case for keywords_delete_keyword

    Delete keyword by ID. It will also be deleted from any entity it is used in (Project, etc.)
    """
    params = [('moveUsagesToGuid', 'move_usages_to_guid_example')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest-api/v1/keywords/{guid}'.format(guid='guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lead_sources_delete_lead_source(client):
    """Test case for lead_sources_delete_lead_source

    Delete a lead source.
    """
    params = [('moveUsagesToGuid', 'move_usages_to_guid_example')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest-api/v1/leadsources/{guid}'.format(guid='guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_market_segments_delete_market_segment(client):
    """Test case for market_segments_delete_market_segment

    Delete a market segment.
    """
    params = [('moveUsagesToGuid', 'move_usages_to_guid_example')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest-api/v1/marketsegments/{guid}'.format(guid='guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_overtimes_delete_overtime(client):
    """Test case for overtimes_delete_overtime

    Delete an overtime.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest-api/v1/overtimes/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_phase_status_types_delete_phase_status_type(client):
    """Test case for phase_status_types_delete_phase_status_type

    Delete a phase status type
    """
    params = [('moveUsagesToGuid', 'move_usages_to_guid_example')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest-api/v1/phasestatustypes/{guid}'.format(guid='guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_categories_delete_product_category(client):
    """Test case for product_categories_delete_product_category

    Delete a product category.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest-api/v1/productcategories/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_country_settings_delete_product_country_setting(client):
    """Test case for product_country_settings_delete_product_country_setting

    Deletes a product country setting
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest-api/v1/productcountrysettings/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_delete_product(client):
    """Test case for products_delete_product

    Delete a product.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest-api/v1/products/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_billing_customers_delete_project_billing_customer(client):
    """Test case for project_billing_customers_delete_project_billing_customer

    Deletes a project billing customer.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest-api/v1/projectbillingcustomers/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_custom_properties_delete_project_custom_property(client):
    """Test case for project_custom_properties_delete_project_custom_property

    Deletes a project custom property.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest-api/v1/projects/customproperties/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_custom_property_selection_items_delete_project_custom_property_selection_item(client):
    """Test case for project_custom_property_selection_items_delete_project_custom_property_selection_item

    Deletes a project custom property selection item.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest-api/v1/projects/customproperties/projectcustompropertyselectionitems/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_member_cost_exceptions_delete(client):
    """Test case for project_member_cost_exceptions_delete

    Deletes a project member cost exception.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest-api/v1/projectmembercostexceptions/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_status_types_delete_project_status_type(client):
    """Test case for project_status_types_delete_project_status_type

    Delete a projectStatusType
    """
    params = [('moveUsagesToGuid', 'move_usages_to_guid_example')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest-api/v1/projectstatustypes/{guid}'.format(guid='guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_task_statuses_delete_project_task_status(client):
    """Test case for project_task_statuses_delete_project_task_status

    Delete a project task status.
    """
    params = [('moveUsagesToGuid', 'move_usages_to_guid_example')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest-api/v1/projecttaskstatuses/{guid}'.format(guid='guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_proposal_statuses_delete_proposal_status(client):
    """Test case for proposal_statuses_delete_proposal_status

    Delete an proposal status
    """
    params = [('moveUsagesToGuid', 'move_usages_to_guid_example')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest-api/v1/proposalstatuses/{guid}'.format(guid='guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_roles_delete_role(client):
    """Test case for roles_delete_role

    Delete a role.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest-api/v1/roles/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_accounts_delete_sales_account(client):
    """Test case for sales_accounts_delete_sales_account

    Delete a sales account.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest-api/v1/salesaccounts/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_status_types_delete_sales_status_type(client):
    """Test case for sales_status_types_delete_sales_status_type

    Delete an sales status type.
    """
    params = [('moveUsagesToGuid', 'move_usages_to_guid_example')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest-api/v1/salesstatustypes/{guid}'.format(guid='guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_time_entry_types_delete_time_entry_type(client):
    """Test case for time_entry_types_delete_time_entry_type

    Deletes a time entry type.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest-api/v1/timeentrytypes/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_travel_expense_type_country_settings_delete_travel_expense_type_country_setting(client):
    """Test case for travel_expense_type_country_settings_delete_travel_expense_type_country_setting

    Deletes a travel expense type country setting
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest-api/v1/travelexpensetypecountrysettings/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_travel_expense_types_delete_travel_expense_type(client):
    """Test case for travel_expense_types_delete_travel_expense_type

    Deletes a travel expense type.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest-api/v1/travelexpensetypes/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_travel_reimbursement_status_delete_travel_reimbursement_status(client):
    """Test case for travel_reimbursement_status_delete_travel_reimbursement_status

    Delete a travel reimbursement status.
    """
    params = [('moveUsagesToGuid', 'move_usages_to_guid_example')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest-api/v1/travelreimbursementstatuses/{guid}'.format(guid='guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_custom_properties_delete_user_custom_property(client):
    """Test case for user_custom_properties_delete_user_custom_property

    Deletes a user custom property.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest-api/v1/users/customproperties/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_custom_property_selection_items_delete_user_custom_property_selection_item(client):
    """Test case for user_custom_property_selection_items_delete_user_custom_property_selection_item

    Deletes a user custom property selection item.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest-api/v1/users/customproperties/usercustompropertyselectionitems/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vat_rates_delete_vat_rate(client):
    """Test case for vat_rates_delete_vat_rate

    Delete a vat rate
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest-api/v1/vatrates/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_work_contracts_delete_work_contract(client):
    """Test case for work_contracts_delete_work_contract

    Delete a work contract.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest-api/v1/workcontracts/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_work_types_delete_work_type(client):
    """Test case for work_types_delete_work_type

    Deletes a work type.
    """
    params = [('moveUsagesToGuid', 'move_usages_to_guid_example')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest-api/v1/worktypes/{guid}'.format(guid='guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

