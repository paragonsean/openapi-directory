from typing import List, Dict
from aiohttp import web

from openapi_server.models.exception_model import ExceptionModel
from openapi_server import util


async def activity_types_delete_activity_type(request: web.Request, guid, move_usages_to_guid=None) -> web.Response:
    """Delete an activity type.

    Returns: No Content (204) if succeeded. Not found (404) if activity type can&#39;t be found.

    :param guid: ID for the activity type to delete
    :type guid: str
    :param move_usages_to_guid: Optional: ID of the activity type to which to move usages of this activity type. Default null. If activity type is in use and usages aren&#39;t moved the deletion might fail.
    :type move_usages_to_guid: str

    """
    return web.Response(status=200)


async def communication_types_delete_communication_type(request: web.Request, guid) -> web.Response:
    """Deletes a communication type.

    Returns: No Content (204) if succeeded.

    :param guid: GUID used to delete the communication type.
    :type guid: str

    """
    return web.Response(status=200)


async def contact_roles_delete_contact_role(request: web.Request, guid, move_usages_to_guid=None) -> web.Response:
    """Delete a contact role.

    Returns: No Content (204) if succeeded. Not found (404) if contact role can&#39;t be found.

    :param guid: ID for the contact role to delete.
    :type guid: str
    :param move_usages_to_guid: Optional: ID of the contact role to which to move usages of this contact role. Default null. If contact role is in use and usages aren&#39;t moved the deletion might fail.
    :type move_usages_to_guid: str

    """
    return web.Response(status=200)


async def cost_accounts_delete_cost_account(request: web.Request, guid) -> web.Response:
    """Delete a cost account.

    Returns: No Content (204) if succeeded. Not found (404) if cost account can&#39;t be found.

    :param guid: ID for the cost account to delete.
    :type guid: str

    """
    return web.Response(status=200)


async def cost_centers_delete_cost_center(request: web.Request, guid) -> web.Response:
    """Delete a cost center.

    Returns: No Content (204) if succeeded. Not found (404) if cost center can&#39;t be found.

    :param guid: ID for the cost center to delete.
    :type guid: str

    """
    return web.Response(status=200)


async def customer_custom_properties_delete_customer_custom_property(request: web.Request, guid) -> web.Response:
    """Deletes a customer custom property.

    Returns: No Content (204) if succeeded.

    :param guid: GUID used to delete the customer custom property.
    :type guid: str

    """
    return web.Response(status=200)


async def customer_custom_property_selection_items_delete_customer_custom_property_selection_item(request: web.Request, guid) -> web.Response:
    """Deletes a customer custom property selection item.

    Returns: No Content (204) if succeeded.

    :param guid: GUID used to delete the customer custom property selection item.
    :type guid: str

    """
    return web.Response(status=200)


async def industries_delete_industry(request: web.Request, guid, move_usages_to_guid=None) -> web.Response:
    """Delete an industry.

    Returns: No Content (204) if succeeded. Not found (404) if industry can&#39;t be found.

    :param guid: ID for the industry to delete.
    :type guid: str
    :param move_usages_to_guid: Optional: ID of the industry to which to move usages of this industry. Default null. If industry is in use and usages aren&#39;t moved the deletion might fail.
    :type move_usages_to_guid: str

    """
    return web.Response(status=200)


async def invoice_statuses_delete_invoice_status(request: web.Request, guid) -> web.Response:
    """Delete an invoice status.

    Returns: No Content (204) if succeeded. Not found (404) if invoice status can&#39;t be found.

    :param guid: ID for the invoice status to delete.
    :type guid: str

    """
    return web.Response(status=200)


async def keywords_delete_keyword(request: web.Request, guid, move_usages_to_guid=None) -> web.Response:
    """Delete keyword by ID. It will also be deleted from any entity it is used in (Project, etc.)

    Returns: No Content (204) if succeeded.

    :param guid: GUID used to get the keyword.
    :type guid: str
    :param move_usages_to_guid: Optional: ID of the keyword to which to move usages of this keyword. Default null. If keyword is in use and usages aren&#39;t moved the deletion might fail.
    :type move_usages_to_guid: str

    """
    return web.Response(status=200)


async def lead_sources_delete_lead_source(request: web.Request, guid, move_usages_to_guid=None) -> web.Response:
    """Delete a lead source.

    Returns: No Content (204) if succeeded. Not found (404) if lead source can&#39;t be found.

    :param guid: ID for the lead source to delete.
    :type guid: str
    :param move_usages_to_guid: Optional: ID of the lead source to which to move usages of this lead source. Default null. If industry is in use and usages aren&#39;t moved the deletion might fail.
    :type move_usages_to_guid: str

    """
    return web.Response(status=200)


async def market_segments_delete_market_segment(request: web.Request, guid, move_usages_to_guid=None) -> web.Response:
    """Delete a market segment.

    Returns: No Content (204) if succeeded. Not found (404) if market segment can&#39;t be found.

    :param guid: ID for the market segment to delete.
    :type guid: str
    :param move_usages_to_guid: Optional: ID of the lead source to which to move usages of this market segment. Default null.
    :type move_usages_to_guid: str

    """
    return web.Response(status=200)


async def overtimes_delete_overtime(request: web.Request, guid) -> web.Response:
    """Delete an overtime.

    Returns: No Content (204) if succeeded. Not found (404) if overtime can&#39;t be found.

    :param guid: ID for the overtime to delete.
    :type guid: str

    """
    return web.Response(status=200)


async def phase_status_types_delete_phase_status_type(request: web.Request, guid, move_usages_to_guid=None) -> web.Response:
    """Delete a phase status type

    Returns: No Content (204) if succeeded. Not found (404) if phase status type can&#39;t be found.

    :param guid: ID for the phase status type to delete
    :type guid: str
    :param move_usages_to_guid: Optional: ID of the phase status type to which to move usages of this phase status type. Default null. If phase status type is in use and usages aren&#39;t moved the deletion might fail.
    :type move_usages_to_guid: str

    """
    return web.Response(status=200)


async def product_categories_delete_product_category(request: web.Request, guid) -> web.Response:
    """Delete a product category.

    Returns: No Content (204) if succeeded. Not found (404) if product category can&#39;t be found.

    :param guid: ID for the product category to delete.
    :type guid: str

    """
    return web.Response(status=200)


async def product_country_settings_delete_product_country_setting(request: web.Request, guid) -> web.Response:
    """Deletes a product country setting

    Returns: No Content (204) if succeeded. Not found (404) if product country setting can&#39;t be found.

    :param guid: GUID used to delete the product country setting.
    :type guid: str

    """
    return web.Response(status=200)


async def products_delete_product(request: web.Request, guid) -> web.Response:
    """Delete a product.

    Returns: No Content (204) if succeeded. Not found (404) if product can&#39;t be found.

    :param guid: ID for the product to delete.
    :type guid: str

    """
    return web.Response(status=200)


async def project_billing_customers_delete_project_billing_customer(request: web.Request, guid) -> web.Response:
    """Deletes a project billing customer.

    Returns: No Content (204) if succeeded.

    :param guid: GUID of the project billing customer to remove.
    :type guid: str

    """
    return web.Response(status=200)


async def project_custom_properties_delete_project_custom_property(request: web.Request, guid) -> web.Response:
    """Deletes a project custom property.

    Returns: No Content (204) if succeeded.

    :param guid: GUID used to delete the project custom property.
    :type guid: str

    """
    return web.Response(status=200)


async def project_custom_property_selection_items_delete_project_custom_property_selection_item(request: web.Request, guid) -> web.Response:
    """Deletes a project custom property selection item.

    Returns: No Content (204) if succeeded.

    :param guid: GUID used to delete the project custom property selection item.
    :type guid: str

    """
    return web.Response(status=200)


async def project_member_cost_exceptions_delete(request: web.Request, guid) -> web.Response:
    """Deletes a project member cost exception.

    Deletes project member cost exception. Returns: No Content (204) if succeeded.

    :param guid: GUID used to delete the project member cost exception.
    :type guid: str

    """
    return web.Response(status=200)


async def project_status_types_delete_project_status_type(request: web.Request, guid, move_usages_to_guid=None) -> web.Response:
    """Delete a projectStatusType

    Returns: No Content (204) if succeeded. Not found (404) if projectStatusType can&#39;t be found.

    :param guid: ID for the projectStatusType to delete
    :type guid: str
    :param move_usages_to_guid: Optional: ID of the project status type to which to move usages of this project status type. Default null. If project status type is in use and usages aren&#39;t moved the deletion might fail.
    :type move_usages_to_guid: str

    """
    return web.Response(status=200)


async def project_task_statuses_delete_project_task_status(request: web.Request, guid, move_usages_to_guid=None) -> web.Response:
    """Delete a project task status.

    Returns: No Content (204) if succeeded. Not found (404) if product can&#39;t be found.

    :param guid: ID for the project task status to delete.
    :type guid: str
    :param move_usages_to_guid: Optional: ID of the project task status to which to move usages of this project task status. Default null.
    :type move_usages_to_guid: str

    """
    return web.Response(status=200)


async def proposal_statuses_delete_proposal_status(request: web.Request, guid, move_usages_to_guid=None) -> web.Response:
    """Delete an proposal status

    Returns: No Content (204) if succeeded. Not found (404) if proposal status can&#39;t be found.

    :param guid: ID for the proposal status to delete
    :type guid: str
    :param move_usages_to_guid: Optional: ID of the proposal status to which to move usages of this proposal status. Default null. If proposal status is in use and usages aren&#39;t moved the deletion might fail.
    :type move_usages_to_guid: str

    """
    return web.Response(status=200)


async def roles_delete_role(request: web.Request, guid) -> web.Response:
    """Delete a role.

    Returns: No Content (204) if succeeded. Not found (404) if role can&#39;t be found.

    :param guid: ID for the role to delete.
    :type guid: str

    """
    return web.Response(status=200)


async def sales_accounts_delete_sales_account(request: web.Request, guid) -> web.Response:
    """Delete a sales account.

    Returns: No Content (204) if succeeded. Not found (404) if sales account can&#39;t be found.

    :param guid: ID for the sales account to delete.
    :type guid: str

    """
    return web.Response(status=200)


async def sales_status_types_delete_sales_status_type(request: web.Request, guid, move_usages_to_guid=None) -> web.Response:
    """Delete an sales status type.

    Returns: No Content (204) if succeeded. Not found (404) if sales status type can&#39;t be found.

    :param guid: ID for the sales status type to delete.
    :type guid: str
    :param move_usages_to_guid: Optional: ID of the sales status type to which to move usages of this sales status type. Default null. If sales status type is in use and usages aren&#39;t moved the deletion might fail.
    :type move_usages_to_guid: str

    """
    return web.Response(status=200)


async def time_entry_types_delete_time_entry_type(request: web.Request, guid) -> web.Response:
    """Deletes a time entry type.

    Returns: No Content (204) if succeeded.

    :param guid: GUID used to delete the time entry type.
    :type guid: str

    """
    return web.Response(status=200)


async def travel_expense_type_country_settings_delete_travel_expense_type_country_setting(request: web.Request, guid) -> web.Response:
    """Deletes a travel expense type country setting

    Returns: No Content (204) if succeeded. Not found (404) if travel expense type country setting can&#39;t be found.

    :param guid: GUID used to delete the travel expense type country setting.
    :type guid: str

    """
    return web.Response(status=200)


async def travel_expense_types_delete_travel_expense_type(request: web.Request, guid) -> web.Response:
    """Deletes a travel expense type.

    

    :param guid: Guid for the travel expense type to delete.
    :type guid: str

    """
    return web.Response(status=200)


async def travel_reimbursement_status_delete_travel_reimbursement_status(request: web.Request, guid, move_usages_to_guid=None) -> web.Response:
    """Delete a travel reimbursement status.

    Returns: No Content (204) if succeeded. Not found (404) if travel reimbursement status can&#39;t be found.

    :param guid: ID for the travel reimbursement status to delete.
    :type guid: str
    :param move_usages_to_guid: Optional: ID of the travel reimbursement status to which to move usages of this travel reimbursement status. Default null. If travel reimbursement status is in use and usages aren&#39;t moved the deletion might fail.
    :type move_usages_to_guid: str

    """
    return web.Response(status=200)


async def user_custom_properties_delete_user_custom_property(request: web.Request, guid) -> web.Response:
    """Deletes a user custom property.

    Returns: No Content (204) if succeeded.

    :param guid: GUID used to delete the user custom property.
    :type guid: str

    """
    return web.Response(status=200)


async def user_custom_property_selection_items_delete_user_custom_property_selection_item(request: web.Request, guid) -> web.Response:
    """Deletes a user custom property selection item.

    Returns: No Content (204) if succeeded.

    :param guid: GUID used to delete the user custom property selection item.
    :type guid: str

    """
    return web.Response(status=200)


async def vat_rates_delete_vat_rate(request: web.Request, guid) -> web.Response:
    """Delete a vat rate

    Returns: No Content (204) if succeeded. Bad Request (400) if vat rate is the default one. Not Found (404) if vat rate can&#39;t be found.

    :param guid: GUID for the vat rate to delete
    :type guid: str

    """
    return web.Response(status=200)


async def work_contracts_delete_work_contract(request: web.Request, guid) -> web.Response:
    """Delete a work contract.

    Returns: No Content (204) if succeeded. Not found (404) if work contract can&#39;t be found.

    :param guid: ID for the work contract to delete.
    :type guid: str

    """
    return web.Response(status=200)


async def work_types_delete_work_type(request: web.Request, guid, move_usages_to_guid=None) -> web.Response:
    """Deletes a work type.

    Returns: No Content (204) if succeeded.

    :param guid: GUID used to delete the work type.
    :type guid: str
    :param move_usages_to_guid: Optional: ID of the work type to which to move usages of this work type. Default null. If work type is in use and usages aren&#39;t moved the deletion might fail.
    :type move_usages_to_guid: str

    """
    return web.Response(status=200)
