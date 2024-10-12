from typing import List, Dict
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
from openapi_server import util


async def activity_types_patch_activity_type(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) an Activity Type or a part of it

    

    :param guid: ID of the Activity Type
    :type guid: str
    :param body: JSON patch document of ActivityTypeModel
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def activity_types_post_activity_type(request: web.Request, body=None) -> web.Response:
    """Insert an Activity type.

    

    :param body: Activity type
    :type body: dict | bytes

    """
    body = ActivityTypeModel.from_dict(body)
    return web.Response(status=200)


async def business_units_patch_business_unit(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) an businessUnit or a part of it.

    

    :param guid: ID of the businessUnit.
    :type guid: str
    :param body: JSON patch document of BusinessUnitModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def communication_types_patch_communication_type(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a communication type or a part of it.

    

    :param guid: ID of the communication type.
    :type guid: str
    :param body: JSON Patch document of CommunicationTypeModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def communication_types_post_communication_type(request: web.Request, body=None) -> web.Response:
    """Insert a communication type.

    

    :param body: CommunicationTypeModel.
    :type body: dict | bytes

    """
    body = CommunicationTypeModel.from_dict(body)
    return web.Response(status=200)


async def contact_roles_patch_contact_role(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a contact role or a part of it.

    

    :param guid: ID of the contact role.
    :type guid: str
    :param body: JSON patch document of ContactRoleModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def contact_roles_post_contact_role(request: web.Request, body=None) -> web.Response:
    """Insert a contact role.

    

    :param body: ContactRoleModel.
    :type body: dict | bytes

    """
    body = ContactRoleModel.from_dict(body)
    return web.Response(status=200)


async def cost_accounts_patch_cost_account(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a cost account or a part of it.

    

    :param guid: ID of the cost account.
    :type guid: str
    :param body: JSON patch document of CostAccountModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def cost_accounts_post_cost_account(request: web.Request, body=None) -> web.Response:
    """Insert a cost account.

    

    :param body: CostAccountModel.
    :type body: dict | bytes

    """
    body = CostAccountModel.from_dict(body)
    return web.Response(status=200)


async def cost_centers_patch_cost_center(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a cost center or a part of it.

    

    :param guid: ID of the cost center.
    :type guid: str
    :param body: JSON patch document of CostCenterModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def cost_centers_post_cost_center(request: web.Request, body=None) -> web.Response:
    """Insert a cost center.

    

    :param body: CostCenterModel.
    :type body: dict | bytes

    """
    body = CostCenterModel.from_dict(body)
    return web.Response(status=200)


async def currencies_patch_currency(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) an currency or a part of it.

    

    :param guid: ID of the currency.
    :type guid: str
    :param body: JSON patch document of CurrencyModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def customer_custom_properties_patch_customer_custom_property(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a customer custom property or a part of it.

    

    :param guid: ID of the customer custom property Can also be comma separate list of IDs to patch multiple customer custom properties with one call. When multiple IDs are given, returns model which has list of succeeded customer custom properties and list of errors.
    :type guid: str
    :param body: JSON Patch document of CustomerCustomPropertyModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def customer_custom_properties_post_customer_custom_property(request: web.Request, body=None) -> web.Response:
    """Insert a customer custom property.

    

    :param body: CustomerCustomPropertyModel.
    :type body: dict | bytes

    """
    body = CustomPropertyModel.from_dict(body)
    return web.Response(status=200)


async def customer_custom_property_selection_items_patch_customer_custom_property_selection_item(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a customer custom property selection item or a part of it.

    

    :param guid: ID of the customer custom property selection item.
    :type guid: str
    :param body: JSON Patch document of CustomerCustomPropertySelectionItemInputModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def customer_custom_property_selection_items_post_customer_custom_property_selection_item(request: web.Request, body=None) -> web.Response:
    """Insert a customer custom property selection item.

    

    :param body: CustomPropertySelectionItemInputModel.
    :type body: dict | bytes

    """
    body = CustomerCustomPropertySelectionItemInputModel.from_dict(body)
    return web.Response(status=200)


async def industries_patch_industry(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) an industry or a part of it.

    

    :param guid: ID of the industry.
    :type guid: str
    :param body: JSON Patch document of IndustryModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def industries_post_industry(request: web.Request, body=None) -> web.Response:
    """Insert an industry.

    

    :param body: IndustryModel.
    :type body: dict | bytes

    """
    body = IndustryModel.from_dict(body)
    return web.Response(status=200)


async def invoice_statuses_patch_invoice_status(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) an Invoice status or a part of it.

    

    :param guid: ID of the Invoice status.
    :type guid: str
    :param body: JSON patch document of InvoiceStatusModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def invoice_statuses_post_invoice_status(request: web.Request, body=None) -> web.Response:
    """Insert a invoice status.

    

    :param body: InvoiceStatusModel.
    :type body: dict | bytes

    """
    body = InvoiceStatusModel.from_dict(body)
    return web.Response(status=200)


async def keywords_patch_keyword(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a keyword or a part of it.

    

    :param guid: ID of the keyword.
    :type guid: str
    :param body: JSON Patch document.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def keywords_post_keyword(request: web.Request, body=None) -> web.Response:
    """Insert a keyword.

    

    :param body: KeywordModel.
    :type body: dict | bytes

    """
    body = KeywordModel.from_dict(body)
    return web.Response(status=200)


async def lead_sources_patch_lead_source(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) an lead source or a part of it.

    

    :param guid: ID of the lead source.
    :type guid: str
    :param body: JSON patch document of LeadSourceModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def lead_sources_post_lead_source(request: web.Request, body=None) -> web.Response:
    """Insert a lead source.

    

    :param body: LeadSourceModel.
    :type body: dict | bytes

    """
    body = LeadSourceModel.from_dict(body)
    return web.Response(status=200)


async def market_segments_patch_market_segment(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) an Market Segment or a part of it.

    

    :param guid: ID of the Market Segment.
    :type guid: str
    :param body: JSON patch document of MarketSegmentModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def market_segments_post_market_segment(request: web.Request, body=None) -> web.Response:
    """Insert a market segment.

    

    :param body: MarketSegmentModel.
    :type body: dict | bytes

    """
    body = MarketSegmentModel.from_dict(body)
    return web.Response(status=200)


async def overtimes_patch_overtime(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) an overtime or a part of it.

    

    :param guid: ID of the overtime.
    :type guid: str
    :param body: JSON patch document of OvertimeModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def overtimes_post_overtime(request: web.Request, body=None) -> web.Response:
    """Insert an overtime.

    

    :param body: OvertimeModel.
    :type body: dict | bytes

    """
    body = OvertimeModel.from_dict(body)
    return web.Response(status=200)


async def phase_status_types_patch_phase_status_type(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a phase status type or a part of it

    

    :param guid: ID of the phase status type
    :type guid: str
    :param body: JSON patch document of TaskStatusTypeModel
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def phase_status_types_post_phase_status_type(request: web.Request, body=None) -> web.Response:
    """Insert a phase status type

    

    :param body: PhaseStatusTypeModel
    :type body: dict | bytes

    """
    body = PhaseStatusTypeModel.from_dict(body)
    return web.Response(status=200)


async def product_categories_patch_product_category(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a product category or a part of it.

    

    :param guid: ID of the product category.
    :type guid: str
    :param body: JSON patch document of ProductCategoryModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def product_categories_post_product_category(request: web.Request, body=None) -> web.Response:
    """Insert a product category.

    

    :param body: ProductCategoryModel.
    :type body: dict | bytes

    """
    body = ProductCategoryModel.from_dict(body)
    return web.Response(status=200)


async def product_country_settings_patch_product_country_settings(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a product country setting

    

    :param guid: ID of the product country setting
    :type guid: str
    :param body: JSON patch document of ProductCountrySettingsModel
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def product_country_settings_post_product_country_settings(request: web.Request, body=None) -> web.Response:
    """Insert a product country setting

    

    :param body: ProductCountrySettingsModel
    :type body: dict | bytes

    """
    body = ProductCountrySettingsModel.from_dict(body)
    return web.Response(status=200)


async def products_patch_product(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) an product or a part of it.

    

    :param guid: ID of the product.
    :type guid: str
    :param body: JSON patch document of ProductModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def products_post_product(request: web.Request, body=None) -> web.Response:
    """Insert a product.

    

    :param body: ProductModel.
    :type body: dict | bytes

    """
    body = ProductInputModel.from_dict(body)
    return web.Response(status=200)


async def project_billing_customers_patch_project_billing_customer(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a project billing customer.

    

    :param guid: ID of the project billing customer.
    :type guid: str
    :param body: JSON patch document of ProjectBillingCustomerModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def project_billing_customers_post_project_billing_customer(request: web.Request, body=None) -> web.Response:
    """Insert a billing customer for a project.

    

    :param body: ProjectBillingCustomerModel.
    :type body: dict | bytes

    """
    body = ProjectBillingCustomerModel2.from_dict(body)
    return web.Response(status=200)


async def project_custom_properties_patch_project_custom_property(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a project custom property or a part of it.

    

    :param guid: ID of the project custom property Can also be comma separate list of IDs to patch multiple project custom properties with one call. When multiple IDs are given, returns model which has list of succeeded project custom properties and list of errors.
    :type guid: str
    :param body: JSON Patch document of ProjectCustomPropertyModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def project_custom_properties_post_project_custom_property(request: web.Request, body=None) -> web.Response:
    """Insert a project custom property.

    

    :param body: ProjectCustomPropertyModel.
    :type body: dict | bytes

    """
    body = CustomPropertyModel.from_dict(body)
    return web.Response(status=200)


async def project_custom_property_selection_items_patch_project_custom_property_selection_item(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a project custom property selection item or a part of it.

    

    :param guid: ID of the project custom property selection item.
    :type guid: str
    :param body: JSON Patch document of ProjectCustomPropertySelectionItemInputModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def project_custom_property_selection_items_post_project_custom_property_selection_item(request: web.Request, body=None) -> web.Response:
    """Insert a project custom property selection item.

    

    :param body: CustomPropertySelectionItemInputModel.
    :type body: dict | bytes

    """
    body = ProjectCustomPropertySelectionItemInputModel.from_dict(body)
    return web.Response(status=200)


async def project_member_cost_exceptions_patch(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) project member cost exception.

    

    :param guid: ID of the project member cost exception.
    :type guid: str
    :param body: JSON Patch document of ProjectMemberCostExceptionModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def project_member_cost_exceptions_post(request: web.Request, body=None) -> web.Response:
    """Add a cost exception to a project member.

    

    :param body: ProjectMemberCostExceptionModel.
    :type body: dict | bytes

    """
    body = ProjectMemberCostExceptionInputModel.from_dict(body)
    return web.Response(status=200)


async def project_status_types_patch_project_status_type(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a projectStatusType or a part of it

    

    :param guid: ID of the projectStatusType
    :type guid: str
    :param body: JSON patch document of ProjectStatusTypeModel
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def project_status_types_post_project_status_type(request: web.Request, body=None) -> web.Response:
    """Insert a project status type

    

    :param body: ProjectStatusTypeModel
    :type body: dict | bytes

    """
    body = ProjectStatusTypeModel.from_dict(body)
    return web.Response(status=200)


async def project_task_statuses_patch_project_task_status(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) an Project task status or a part of it.

    

    :param guid: ID of the Project task status.
    :type guid: str
    :param body: JSON patch document of ProjectTaskStatusModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def project_task_statuses_post_project_task_status(request: web.Request, body=None) -> web.Response:
    """Insert a project task status.

    

    :param body: ProjectTaskStatusModel.
    :type body: dict | bytes

    """
    body = ProjectTaskStatusModel.from_dict(body)
    return web.Response(status=200)


async def proposal_statuses_patch_proposal_status(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) an Proposal status or a part of it

    

    :param guid: ID of the Proposal status
    :type guid: str
    :param body: JSON patch document of ProposalStatusModel
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def proposal_statuses_post_proposal_status(request: web.Request, body=None) -> web.Response:
    """Insert a proposal status

    

    :param body: ProposalStatusModel
    :type body: dict | bytes

    """
    body = ProposalStatusInputModel.from_dict(body)
    return web.Response(status=200)


async def roles_patch_role(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a role or a part of it.

    

    :param guid: ID of the role.
    :type guid: str
    :param body: JSON patch document of RoleInputModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def roles_post_role(request: web.Request, body=None) -> web.Response:
    """Insert a role.

    

    :param body: RoleInputModel.
    :type body: dict | bytes

    """
    body = RoleInputModel.from_dict(body)
    return web.Response(status=200)


async def sales_accounts_patch_sales_account(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a sales account or a part of it.

    

    :param guid: ID of the sales account.
    :type guid: str
    :param body: JSON patch document of SalesAccountModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def sales_accounts_post_sales_account(request: web.Request, body=None) -> web.Response:
    """Insert a sales account.

    

    :param body: SalesAccountModel.
    :type body: dict | bytes

    """
    body = SalesAccountModel.from_dict(body)
    return web.Response(status=200)


async def sales_status_types_patch_sales_status_type(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) an sales status type or a part of it

    

    :param guid: ID of the sales status type
    :type guid: str
    :param body: JSON patch document of salesStatusType
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def sales_status_types_post_sales_status_type(request: web.Request, body=None) -> web.Response:
    """Insert a sales status type

    

    :param body: salesStatusType
    :type body: dict | bytes

    """
    body = SalesStatusTypeInputModel.from_dict(body)
    return web.Response(status=200)


async def time_entry_types_patch_time_entry_type(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a time entry type or a part of it.

    

    :param guid: ID of the time entry type.
    :type guid: str
    :param body: JSON Patch document of TimeEntryTypeModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def time_entry_types_post_time_entry_type(request: web.Request, body=None) -> web.Response:
    """Insert a time entry type.

    

    :param body: TimeEntryTypeModel.
    :type body: dict | bytes

    """
    body = TimeEntryTypeModel.from_dict(body)
    return web.Response(status=200)


async def travel_expense_type_country_settings_patch_travel_expense_type_country_settings(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a travel expense type country setting

    

    :param guid: ID of the travel expense type country setting
    :type guid: str
    :param body: JSON patch document of TravelExpenseTypeCountrySettingsModel
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def travel_expense_type_country_settings_post_travel_expense_type_country_settings(request: web.Request, body=None) -> web.Response:
    """Insert a travel expense type country setting

    

    :param body: Travel expense type country setting model
    :type body: dict | bytes

    """
    body = TravelExpenseTypeCountrySettingsModel.from_dict(body)
    return web.Response(status=200)


async def travel_expense_types_patch_travel_expense_type(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) an travel expense type or a part of it.

    

    :param guid: Guid of the travel expense type.
    :type guid: str
    :param body: JSON patch document of TravelExpenseTypeInputModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def travel_expense_types_post_travel_expense_type(request: web.Request, body=None) -> web.Response:
    """Insert a new travel expense type.

    

    :param body: TravelExpenseTypeInputModel.
    :type body: dict | bytes

    """
    body = TravelExpenseTypeInputModel.from_dict(body)
    return web.Response(status=200)


async def travel_reimbursement_status_patch_travel_reimbursement_status(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a travel reimbursement status or a part of it.

    

    :param guid: ID of the travel reimbursement status.
    :type guid: str
    :param body: JSON patch document of TravelReimbursementStatusModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def travel_reimbursement_status_post_travel_reimbursement_status(request: web.Request, body=None) -> web.Response:
    """Insert a travel reimbursement status.

    

    :param body: TravelReimbursementStatusModel.
    :type body: dict | bytes

    """
    body = TravelReimbursementStatusModel.from_dict(body)
    return web.Response(status=200)


async def user_custom_properties_patch_user_custom_property(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a user custom property or a part of it.

    

    :param guid: ID of the user custom property Can also be comma separate list of IDs to patch multiple user custom properties with one call. When multiple IDs are given, returns model which has list of succeeded user custom properties and list of errors.
    :type guid: str
    :param body: JSON Patch document of UserCustomPropertyModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def user_custom_properties_post_user_custom_property(request: web.Request, body=None) -> web.Response:
    """Insert a user custom property.

    

    :param body: UserCustomPropertyModel.
    :type body: dict | bytes

    """
    body = UserCustomPropertyInputModel.from_dict(body)
    return web.Response(status=200)


async def user_custom_property_selection_items_patch_user_custom_property_selection_item(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a user custom property selection item or a part of it.

    

    :param guid: ID of the user custom property selection item.
    :type guid: str
    :param body: JSON Patch document of UserCustomPropertySelectionItemInputModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def user_custom_property_selection_items_post_user_custom_property_selection_item(request: web.Request, body=None) -> web.Response:
    """Insert a user custom property selection item.

    

    :param body: UserPropertySelectionItemInputModel.
    :type body: dict | bytes

    """
    body = UserCustomPropertySelectionItemInputModel.from_dict(body)
    return web.Response(status=200)


async def vat_rates_patch_vat_rate(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a vat rate or a part of it

    

    :param guid: GUID of the vat rate
    :type guid: str
    :param body: JSON Patch document of ValueAddedTaxModel
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def vat_rates_post_vat_rate(request: web.Request, body=None) -> web.Response:
    """Insert a vat rate

    

    :param body: VatRateInputModel
    :type body: dict | bytes

    """
    body = VatRateInputModel.from_dict(body)
    return web.Response(status=200)


async def work_contracts_patch_work_contract(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a work contract or a part of it.

    

    :param guid: ID of the work contract.
    :type guid: str
    :param body: JSON patch document of WorkContractOutputModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def work_contracts_post_work_contract(request: web.Request, reset_flextime=None, body=None) -> web.Response:
    """Insert a work contract.

    

    :param reset_flextime: Optional. Reset flextime to zero when new work contract starts or keep the flextime value. Default true &#x3D; reset flextime.
    :type reset_flextime: bool
    :param body: WorkContractOutputModel.
    :type body: dict | bytes

    """
    body = WorkContractInputModel.from_dict(body)
    return web.Response(status=200)


async def work_types_patch_work_type(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a work type or a part of it.

    

    :param guid: ID of the work type.
    :type guid: str
    :param body: JSON Patch document of WorkTypeModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def work_types_post_work_type(request: web.Request, body=None) -> web.Response:
    """Insert a work type.

    

    :param body: WorkTypeModel.
    :type body: dict | bytes

    """
    body = WorkTypeInputModel.from_dict(body)
    return web.Response(status=200)
