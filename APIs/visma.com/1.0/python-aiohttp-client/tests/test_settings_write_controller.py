# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.activity_type_model import ActivityTypeModel
from openapi_server.models.business_unit_model import BusinessUnitModel
from openapi_server.models.communication_type_model import CommunicationTypeModel
from openapi_server.models.contact_role_model import ContactRoleModel
from openapi_server.models.cost_account_model import CostAccountModel
from openapi_server.models.cost_center_model import CostCenterModel
from openapi_server.models.currency_output_model import CurrencyOutputModel
from openapi_server.models.custom_property_model import CustomPropertyModel
from openapi_server.models.customer_custom_property_selection_item_input_model import CustomerCustomPropertySelectionItemInputModel
from openapi_server.models.customer_custom_property_selection_item_output_model import CustomerCustomPropertySelectionItemOutputModel
from openapi_server.models.exception_model import ExceptionModel
from openapi_server.models.industry_model import IndustryModel
from openapi_server.models.invoice_status_model import InvoiceStatusModel
from openapi_server.models.keyword_model import KeywordModel
from openapi_server.models.lead_source_model import LeadSourceModel
from openapi_server.models.market_segment_model import MarketSegmentModel
from openapi_server.models.overtime_model import OvertimeModel
from openapi_server.models.patch_operation import PatchOperation
from openapi_server.models.phase_status_type_model import PhaseStatusTypeModel
from openapi_server.models.product_category_model import ProductCategoryModel
from openapi_server.models.product_country_settings_model import ProductCountrySettingsModel
from openapi_server.models.product_input_model import ProductInputModel
from openapi_server.models.product_output_model import ProductOutputModel
from openapi_server.models.project_billing_customer_model2 import ProjectBillingCustomerModel2
from openapi_server.models.project_custom_property_selection_item_input_model import ProjectCustomPropertySelectionItemInputModel
from openapi_server.models.project_custom_property_selection_item_output_model import ProjectCustomPropertySelectionItemOutputModel
from openapi_server.models.project_member_cost_exception_input_model import ProjectMemberCostExceptionInputModel
from openapi_server.models.project_member_cost_exception_output_model import ProjectMemberCostExceptionOutputModel
from openapi_server.models.project_status_type_model import ProjectStatusTypeModel
from openapi_server.models.project_task_status_model import ProjectTaskStatusModel
from openapi_server.models.proposal_status_input_model import ProposalStatusInputModel
from openapi_server.models.proposal_status_output_model import ProposalStatusOutputModel
from openapi_server.models.role_input_model import RoleInputModel
from openapi_server.models.role_output_model import RoleOutputModel
from openapi_server.models.sales_account_model import SalesAccountModel
from openapi_server.models.sales_status_type_input_model import SalesStatusTypeInputModel
from openapi_server.models.sales_status_type_output_model import SalesStatusTypeOutputModel
from openapi_server.models.time_entry_type_model import TimeEntryTypeModel
from openapi_server.models.travel_expense_type_country_settings_model import TravelExpenseTypeCountrySettingsModel
from openapi_server.models.travel_expense_type_input_model import TravelExpenseTypeInputModel
from openapi_server.models.travel_expense_type_output_model import TravelExpenseTypeOutputModel
from openapi_server.models.travel_reimbursement_status_model import TravelReimbursementStatusModel
from openapi_server.models.user_custom_property_input_model import UserCustomPropertyInputModel
from openapi_server.models.user_custom_property_output_model import UserCustomPropertyOutputModel
from openapi_server.models.user_custom_property_selection_item_input_model import UserCustomPropertySelectionItemInputModel
from openapi_server.models.user_custom_property_selection_item_output_model import UserCustomPropertySelectionItemOutputModel
from openapi_server.models.vat_rate_input_model import VatRateInputModel
from openapi_server.models.vat_rate_output_model import VatRateOutputModel
from openapi_server.models.work_contract_input_model import WorkContractInputModel
from openapi_server.models.work_contract_output_model import WorkContractOutputModel
from openapi_server.models.work_type_input_model import WorkTypeInputModel
from openapi_server.models.work_type_output_model import WorkTypeOutputModel


pytestmark = pytest.mark.asyncio

async def test_activity_types_patch_activity_type(client):
    """Test case for activity_types_patch_activity_type

    Update (Patch) an Activity Type or a part of it
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/activitytypes/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_types_post_activity_type(client):
    """Test case for activity_types_post_activity_type

    Insert an Activity type.
    """
    body = {"isPaidLeave":True,"lastUpdatedBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"isDefault":True,"code":"code","createdBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"name":"name","createdDateTime":"2000-01-23T04:56:07.000+00:00","guid":"guid","lastUpdatedDateTime":"2000-01-23T04:56:07.000+00:00","category":"Personal","isActive":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/activitytypes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_business_units_patch_business_unit(client):
    """Test case for business_units_patch_business_unit

    Update (Patch) an businessUnit or a part of it.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/businessunits/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_communication_types_patch_communication_type(client):
    """Test case for communication_types_patch_communication_type

    Update (Patch) a communication type or a part of it.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/communicationtypes/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_communication_types_post_communication_type(client):
    """Test case for communication_types_post_communication_type

    Insert a communication type.
    """
    body = {"lastUpdatedBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"createdBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"name":"name","createdDateTime":"2000-01-23T04:56:07.000+00:00","guid":"guid","lastUpdatedDateTime":"2000-01-23T04:56:07.000+00:00","isActive":True,"type":"Phone"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/communicationtypes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contact_roles_patch_contact_role(client):
    """Test case for contact_roles_patch_contact_role

    Update (Patch) a contact role or a part of it.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/contactroles/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contact_roles_post_contact_role(client):
    """Test case for contact_roles_post_contact_role

    Insert a contact role.
    """
    body = {"lastUpdatedBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"createdBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"name":"name","createdDateTime":"2000-01-23T04:56:07.000+00:00","guid":"guid","lastUpdatedDateTime":"2000-01-23T04:56:07.000+00:00","isActive":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/contactroles',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cost_accounts_patch_cost_account(client):
    """Test case for cost_accounts_patch_cost_account

    Update (Patch) a cost account or a part of it.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/costaccounts/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cost_accounts_post_cost_account(client):
    """Test case for cost_accounts_post_cost_account

    Insert a cost account.
    """
    body = {"isTravelTypeDefault":True,"lastUpdatedBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"number":"number","createdBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"name":"name","createdDateTime":"2000-01-23T04:56:07.000+00:00","guid":"guid","lastUpdatedDateTime":"2000-01-23T04:56:07.000+00:00","isActive":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/costaccounts',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cost_centers_patch_cost_center(client):
    """Test case for cost_centers_patch_cost_center

    Update (Patch) a cost center or a part of it.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/costcenters/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cost_centers_post_cost_center(client):
    """Test case for cost_centers_post_cost_center

    Insert a cost center.
    """
    body = {"identifier":"identifier","lastUpdatedBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"isDefault":True,"createdBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"name":"name","createdDateTime":"2000-01-23T04:56:07.000+00:00","guid":"guid","lastUpdatedDateTime":"2000-01-23T04:56:07.000+00:00","isActive":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/costcenters',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_currencies_patch_currency(client):
    """Test case for currencies_patch_currency

    Update (Patch) an currency or a part of it.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/currencies/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customer_custom_properties_patch_customer_custom_property(client):
    """Test case for customer_custom_properties_patch_customer_custom_property

    Update (Patch) a customer custom property or a part of it.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/customers/customproperties/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customer_custom_properties_post_customer_custom_property(client):
    """Test case for customer_custom_properties_post_customer_custom_property

    Insert a customer custom property.
    """
    body = {"lastUpdatedBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"createdBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"name":"name","createdDateTime":"2000-01-23T04:56:07.000+00:00","guid":"guid","lastUpdatedDateTime":"2000-01-23T04:56:07.000+00:00","isActive":True,"type":"Numeric","parameters":"parameters","usageCount":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/customers/customproperties',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customer_custom_property_selection_items_patch_customer_custom_property_selection_item(client):
    """Test case for customer_custom_property_selection_items_patch_customer_custom_property_selection_item

    Update (Patch) a customer custom property selection item or a part of it.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/customers/customproperties/customercustompropertyselectionitems/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customer_custom_property_selection_items_post_customer_custom_property_selection_item(client):
    """Test case for customer_custom_property_selection_items_post_customer_custom_property_selection_item

    Insert a customer custom property selection item.
    """
    body = {"sortOrder":0,"customerCustomProperty":{"guid":"guid"},"name":"name","isActive":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/customers/customproperties/customercustompropertyselectionitems',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_industries_patch_industry(client):
    """Test case for industries_patch_industry

    Update (Patch) an industry or a part of it.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/industries/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_industries_post_industry(client):
    """Test case for industries_post_industry

    Insert an industry.
    """
    body = {"lastUpdatedBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"code":"code","createdBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"name":"name","createdDateTime":"2000-01-23T04:56:07.000+00:00","guid":"guid","lastUpdatedDateTime":"2000-01-23T04:56:07.000+00:00","isActive":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/industries',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoice_statuses_patch_invoice_status(client):
    """Test case for invoice_statuses_patch_invoice_status

    Update (Patch) an Invoice status or a part of it.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/invoicestatuses/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoice_statuses_post_invoice_status(client):
    """Test case for invoice_statuses_post_invoice_status

    Insert a invoice status.
    """
    body = {"lastUpdatedBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"isDefaultForCreditNote":True,"hasInvoiceNumber":True,"createdDateTime":"2000-01-23T04:56:07.000+00:00","isSent":True,"isActive":True,"isPaid":True,"isDefault":True,"isReadOnly":True,"createdBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"sortOrder":0,"name":"name","guid":"guid","lastUpdatedDateTime":"2000-01-23T04:56:07.000+00:00","isWaitingPayment":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/invoicestatuses',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_keywords_patch_keyword(client):
    """Test case for keywords_patch_keyword

    Update (Patch) a keyword or a part of it.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/keywords/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_keywords_post_keyword(client):
    """Test case for keywords_post_keyword

    Insert a keyword.
    """
    body = {"lastUpdatedBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"createdBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"createdDateTime":"2000-01-23T04:56:07.000+00:00","guid":"guid","lastUpdatedDateTime":"2000-01-23T04:56:07.000+00:00","category":"Project","isActive":True,"keyword":"keyword"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/keywords',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lead_sources_patch_lead_source(client):
    """Test case for lead_sources_patch_lead_source

    Update (Patch) an lead source or a part of it.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/leadsources/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lead_sources_post_lead_source(client):
    """Test case for lead_sources_post_lead_source

    Insert a lead source.
    """
    body = {"lastUpdatedBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"createdBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"name":"name","createdDateTime":"2000-01-23T04:56:07.000+00:00","guid":"guid","lastUpdatedDateTime":"2000-01-23T04:56:07.000+00:00","isActive":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/leadsources',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_market_segments_patch_market_segment(client):
    """Test case for market_segments_patch_market_segment

    Update (Patch) an Market Segment or a part of it.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/marketsegments/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_market_segments_post_market_segment(client):
    """Test case for market_segments_post_market_segment

    Insert a market segment.
    """
    body = {"lastUpdatedBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"createdBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"name":"name","createdDateTime":"2000-01-23T04:56:07.000+00:00","guid":"guid","lastUpdatedDateTime":"2000-01-23T04:56:07.000+00:00","isActive":True,"parentMarketSegment":{"name":"name","guid":"guid"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/marketsegments',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_overtimes_patch_overtime(client):
    """Test case for overtimes_patch_overtime

    Update (Patch) an overtime or a part of it.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/overtimes/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_overtimes_post_overtime(client):
    """Test case for overtimes_post_overtime

    Insert an overtime.
    """
    body = {"lastUpdatedBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"code":"code","multipliesUnitCost":False,"createdBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"percentage":0.8008281904610115,"name":"name","createdDateTime":"2000-01-23T04:56:07.000+00:00","guid":"guid","lastUpdatedDateTime":"2000-01-23T04:56:07.000+00:00","isActive":True,"includeInFlextime":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/overtimes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_phase_status_types_patch_phase_status_type(client):
    """Test case for phase_status_types_patch_phase_status_type

    Update (Patch) a phase status type or a part of it
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/phasestatustypes/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_phase_status_types_post_phase_status_type(client):
    """Test case for phase_status_types_post_phase_status_type

    Insert a phase status type
    """
    body = {"lastUpdatedBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"createdBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"sortOrder":0,"name":"name","createdDateTime":"2000-01-23T04:56:07.000+00:00","guid":"guid","lastUpdatedDateTime":"2000-01-23T04:56:07.000+00:00","isActive":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/phasestatustypes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_categories_patch_product_category(client):
    """Test case for product_categories_patch_product_category

    Update (Patch) a product category or a part of it.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/productcategories/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_categories_post_product_category(client):
    """Test case for product_categories_post_product_category

    Insert a product category.
    """
    body = {"lastUpdatedBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"isDefault":True,"code":"code","createdBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"name":"name","createdDateTime":"2000-01-23T04:56:07.000+00:00","guid":"guid","lastUpdatedDateTime":"2000-01-23T04:56:07.000+00:00","isActive":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/productcategories',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_country_settings_patch_product_country_settings(client):
    """Test case for product_country_settings_patch_product_country_settings

    Update (Patch) a product country setting
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/productcountrysettings/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_country_settings_post_product_country_settings(client):
    """Test case for product_country_settings_post_product_country_settings

    Insert a product country setting
    """
    body = {"country":{"name":"name","guid":"guid"},"lastUpdatedBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"product":{"name":"name","guid":"guid"},"createdBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"vatRate":0.8008281904610115,"createdDateTime":"2000-01-23T04:56:07.000+00:00","guid":"guid","lastUpdatedDateTime":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/productcountrysettings',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_patch_product(client):
    """Test case for products_patch_product

    Update (Patch) an product or a part of it.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/products/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_post_product(client):
    """Test case for products_post_product

    Insert a product.
    """
    body = {"unitPrice":{"amount":6.027456183070403,"currencyCode":"currencyCode"},"salesAccount":{"guid":"guid"},"code":"code","unitCost":{"amount":6.027456183070403,"currencyCode":"currencyCode"},"vatRate":0.8008281904610115,"name":"name","isActive":True,"type":"FixedFees","measurementUnit":"measurementUnit","proposalDescription":"proposalDescription","productCategory":{"guid":"guid"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/products',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_billing_customers_patch_project_billing_customer(client):
    """Test case for project_billing_customers_patch_project_billing_customer

    Update (Patch) a project billing customer.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/projectbillingcustomers/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_billing_customers_post_project_billing_customer(client):
    """Test case for project_billing_customers_post_project_billing_customer

    Insert a billing customer for a project.
    """
    body = {"canBeDeleted":True,"lastUpdatedBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"isDefault":True,"billingContact":{"name":"name","guid":"guid"},"createdBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"billingCustomer":{"eInvoiceOperator":"eInvoiceOperator","name":"name","eInvoiceAddress":"eInvoiceAddress","guid":"guid"},"createdDateTime":"2000-01-23T04:56:07.000+00:00","guid":"guid","project":{"name":"name","guid":"guid"},"billingAddress":{"country":"country","city":"city","postalCode":"postalCode","guid":"guid","addressline":"addressline"},"lastUpdatedDateTime":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/projectbillingcustomers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_custom_properties_patch_project_custom_property(client):
    """Test case for project_custom_properties_patch_project_custom_property

    Update (Patch) a project custom property or a part of it.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/projects/customproperties/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_custom_properties_post_project_custom_property(client):
    """Test case for project_custom_properties_post_project_custom_property

    Insert a project custom property.
    """
    body = {"lastUpdatedBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"createdBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"name":"name","createdDateTime":"2000-01-23T04:56:07.000+00:00","guid":"guid","lastUpdatedDateTime":"2000-01-23T04:56:07.000+00:00","isActive":True,"type":"Numeric","parameters":"parameters","usageCount":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/projects/customproperties',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_custom_property_selection_items_patch_project_custom_property_selection_item(client):
    """Test case for project_custom_property_selection_items_patch_project_custom_property_selection_item

    Update (Patch) a project custom property selection item or a part of it.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/projects/customproperties/projectcustompropertyselectionitems/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_custom_property_selection_items_post_project_custom_property_selection_item(client):
    """Test case for project_custom_property_selection_items_post_project_custom_property_selection_item

    Insert a project custom property selection item.
    """
    body = {"projectCustomProperty":{"guid":"guid"},"sortOrder":0,"name":"name","isActive":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/projects/customproperties/projectcustompropertyselectionitems',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_member_cost_exceptions_patch(client):
    """Test case for project_member_cost_exceptions_patch

    Update (Patch) project member cost exception.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/projectmembercostexceptions/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_member_cost_exceptions_post(client):
    """Test case for project_member_cost_exceptions_post

    Add a cost exception to a project member.
    """
    body = {"cost":{"amount":6.027456183070403,"currencyCode":"currencyCode"},"project":{"guid":"guid"},"user":{"guid":"guid"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/projectmembercostexceptions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_status_types_patch_project_status_type(client):
    """Test case for project_status_types_patch_project_status_type

    Update (Patch) a projectStatusType or a part of it
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/projectstatustypes/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_status_types_post_project_status_type(client):
    """Test case for project_status_types_post_project_status_type

    Insert a project status type
    """
    body = {"lastUpdatedBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"createdBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"sortOrder":0,"name":"name","createdDateTime":"2000-01-23T04:56:07.000+00:00","guid":"guid","lastUpdatedDateTime":"2000-01-23T04:56:07.000+00:00","isActive":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/projectstatustypes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_task_statuses_patch_project_task_status(client):
    """Test case for project_task_statuses_patch_project_task_status

    Update (Patch) an Project task status or a part of it.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/projecttaskstatuses/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_task_statuses_post_project_task_status(client):
    """Test case for project_task_statuses_post_project_task_status

    Insert a project task status.
    """
    body = {"lastUpdatedBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"isDefault":True,"createdBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"sortOrder":0,"name":"name","createdDateTime":"2000-01-23T04:56:07.000+00:00","guid":"guid","lastUpdatedDateTime":"2000-01-23T04:56:07.000+00:00","isActive":True,"isDone":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/projecttaskstatuses',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_proposal_statuses_patch_proposal_status(client):
    """Test case for proposal_statuses_patch_proposal_status

    Update (Patch) an Proposal status or a part of it
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/proposalstatuses/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_proposal_statuses_post_proposal_status(client):
    """Test case for proposal_statuses_post_proposal_status

    Insert a proposal status
    """
    body = {"isWon":True,"isDefault":True,"sortOrder":0,"name":"name","isLost":True,"isActive":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/proposalstatuses',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_roles_patch_role(client):
    """Test case for roles_patch_role

    Update (Patch) a role or a part of it.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/roles/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_roles_post_role(client):
    """Test case for roles_post_role

    Insert a role.
    """
    body = {"lastUpdatedBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"createdBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"name":"name","createdDateTime":"2000-01-23T04:56:07.000+00:00","guid":"guid","lastUpdatedDateTime":"2000-01-23T04:56:07.000+00:00","isActive":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/roles',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_accounts_patch_sales_account(client):
    """Test case for sales_accounts_patch_sales_account

    Update (Patch) a sales account or a part of it.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/salesaccounts/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_accounts_post_sales_account(client):
    """Test case for sales_accounts_post_sales_account

    Insert a sales account.
    """
    body = {"isWorkTypeDefault":True,"isTravelTypeDefault":True,"lastUpdatedBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"number":"number","createdBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"name":"name","createdDateTime":"2000-01-23T04:56:07.000+00:00","guid":"guid","isProductDefault":True,"lastUpdatedDateTime":"2000-01-23T04:56:07.000+00:00","isActive":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/salesaccounts',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_status_types_patch_sales_status_type(client):
    """Test case for sales_status_types_patch_sales_status_type

    Update (Patch) an sales status type or a part of it
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/salesstatustypes/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_status_types_post_sales_status_type(client):
    """Test case for sales_status_types_post_sales_status_type

    Insert a sales status type
    """
    body = {"salesState":"InProgress","isProposalDefault":False,"defaultProbability":0,"name":"name","isActive":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/salesstatustypes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_time_entry_types_patch_time_entry_type(client):
    """Test case for time_entry_types_patch_time_entry_type

    Update (Patch) a time entry type or a part of it.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/timeentrytypes/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_time_entry_types_post_time_entry_type(client):
    """Test case for time_entry_types_post_time_entry_type

    Insert a time entry type.
    """
    body = {"identifier":"identifier","lastUpdatedBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"createdBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"name":"name","createdDateTime":"2000-01-23T04:56:07.000+00:00","guid":"guid","lastUpdatedDateTime":"2000-01-23T04:56:07.000+00:00","isActive":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/timeentrytypes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_travel_expense_type_country_settings_patch_travel_expense_type_country_settings(client):
    """Test case for travel_expense_type_country_settings_patch_travel_expense_type_country_settings

    Update (Patch) a travel expense type country setting
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/travelexpensetypecountrysettings/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_travel_expense_type_country_settings_post_travel_expense_type_country_settings(client):
    """Test case for travel_expense_type_country_settings_post_travel_expense_type_country_settings

    Insert a travel expense type country setting
    """
    body = {"country":{"name":"name","guid":"guid"},"lastUpdatedBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"product":{"name":"name","guid":"guid"},"createdBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"purchaseVatRate":0.8008281904610115,"vatRate":6.027456183070403,"createdDateTime":"2000-01-23T04:56:07.000+00:00","guid":"guid","lastUpdatedDateTime":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/travelexpensetypecountrysettings',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_travel_expense_types_patch_travel_expense_type(client):
    """Test case for travel_expense_types_patch_travel_expense_type

    Update (Patch) an travel expense type or a part of it.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/travelexpensetypes/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_travel_expense_types_post_travel_expense_type(client):
    """Test case for travel_expense_types_post_travel_expense_type

    Insert a new travel expense type.
    """
    body = {"salesAccount":{"guid":"guid"},"code":"code","includeTime":True,"expenseClass":"Mileage","purchaseVatRate":0.8008281904610115,"unitCost":{"amount":6.027456183070403,"currencyCode":"currencyCode"},"vatRate":6.027456183070403,"name":"name","costAccount":{"guid":"guid"},"isActive":True,"measurementUnit":"measurementUnit","productCategory":{"guid":"guid"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/travelexpensetypes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_travel_reimbursement_status_patch_travel_reimbursement_status(client):
    """Test case for travel_reimbursement_status_patch_travel_reimbursement_status

    Update (Patch) a travel reimbursement status or a part of it.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/travelreimbursementstatuses/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_travel_reimbursement_status_post_travel_reimbursement_status(client):
    """Test case for travel_reimbursement_status_post_travel_reimbursement_status

    Insert a travel reimbursement status.
    """
    body = {"lastUpdatedBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"isDefault":True,"createdBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"isLocked":False,"sortOrder":0,"name":"name","createdDateTime":"2000-01-23T04:56:07.000+00:00","guid":"guid","lastUpdatedDateTime":"2000-01-23T04:56:07.000+00:00","isActive":True,"isApproved":False}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/travelreimbursementstatuses',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_custom_properties_patch_user_custom_property(client):
    """Test case for user_custom_properties_patch_user_custom_property

    Update (Patch) a user custom property or a part of it.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/users/customproperties/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_custom_properties_post_user_custom_property(client):
    """Test case for user_custom_properties_post_user_custom_property

    Insert a user custom property.
    """
    body = {"name":"name","permission":"View","isActive":True,"type":"Numeric","parameters":"parameters"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/users/customproperties',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_custom_property_selection_items_patch_user_custom_property_selection_item(client):
    """Test case for user_custom_property_selection_items_patch_user_custom_property_selection_item

    Update (Patch) a user custom property selection item or a part of it.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/users/customproperties/usercustompropertyselectionitems/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_custom_property_selection_items_post_user_custom_property_selection_item(client):
    """Test case for user_custom_property_selection_items_post_user_custom_property_selection_item

    Insert a user custom property selection item.
    """
    body = {"sortOrder":0,"name":"name","isActive":True,"userCustomProperty":{"guid":"guid"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/users/customproperties/usercustompropertyselectionitems',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vat_rates_patch_vat_rate(client):
    """Test case for vat_rates_patch_vat_rate

    Update (Patch) a vat rate or a part of it
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/vatrates/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vat_rates_post_vat_rate(client):
    """Test case for vat_rates_post_vat_rate

    Insert a vat rate
    """
    body = {"isDefault":True,"code":"code","percentage":0.8008281904610115,"countryGuid":"countryGuid","isActive":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/vatrates',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_work_contracts_patch_work_contract(client):
    """Test case for work_contracts_patch_work_contract

    Update (Patch) a work contract or a part of it.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/workcontracts/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_work_contracts_post_work_contract(client):
    """Test case for work_contracts_post_work_contract

    Insert a work contract.
    """
    body = {"flextimeLimitPerDay":6.027456183070403,"workWeek":["Monday","Monday"],"role":{"guid":"guid"},"endDate":"2000-01-23","dailyHours":0.8008281904610115,"hourCost":{"amount":1.4658129805029452,"currencyCode":"currencyCode"},"isFlextimeActive":True,"isOvertimeAllowed":True,"title":"title","user":{"guid":"guid"},"startDate":"2000-01-23"}
    params = [('resetFlextime', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/workcontracts',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_work_types_patch_work_type(client):
    """Test case for work_types_patch_work_type

    Update (Patch) a work type or a part of it.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/worktypes/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_work_types_post_work_type(client):
    """Test case for work_types_post_work_type

    Insert a work type.
    """
    body = {"isDefault":True,"salesAccount":{"guid":"guid"},"code":"code","isProductive":True,"name":"name","hourCost":{"amount":6.027456183070403,"currencyCode":"currencyCode"},"isActive":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/worktypes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

