from typing import List, Dict
from aiohttp import web

from openapi_server.models.address_model import AddressModel
from openapi_server.models.contact_communication_model import ContactCommunicationModel
from openapi_server.models.contact_keyword_model import ContactKeywordModel
from openapi_server.models.contact_model import ContactModel
from openapi_server.models.customer_country_settings_input_model import CustomerCountrySettingsInputModel
from openapi_server.models.customer_country_settings_output_model import CustomerCountrySettingsOutputModel
from openapi_server.models.customer_custom_value_model import CustomerCustomValueModel
from openapi_server.models.customer_market_segment_model import CustomerMarketSegmentModel
from openapi_server.models.customer_model import CustomerModel
from openapi_server.models.customer_sales_note_input_model import CustomerSalesNoteInputModel
from openapi_server.models.customer_sales_note_output_model import CustomerSalesNoteOutputModel
from openapi_server.models.exception_model import ExceptionModel
from openapi_server.models.patch_operation import PatchOperation
from openapi_server import util


async def addresses_patch_address(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) an address or a part of it.

    

    :param guid: ID of the address.
    :type guid: str
    :param body: JSON patch document of AddressModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def addresses_post_customer_address(request: web.Request, customer_guid, body=None) -> web.Response:
    """Insert an address.

    

    :param customer_guid: ID of the customer to add the address for.
    :type customer_guid: str
    :param body: AddressModel.
    :type body: dict | bytes

    """
    body = AddressModel.from_dict(body)
    return web.Response(status=200)


async def contact_communications_patch_contact_communication(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a contact&#39;s communication or a part of it.

    

    :param guid: ID of the contact&#39;s communication.
    :type guid: str
    :param body: JSON Patch document of ContactCommunicationModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def contact_communications_post_contact_communication(request: web.Request, body=None) -> web.Response:
    """Insert a communication for a contact.

    

    :param body: ContactCommunicationModel.
    :type body: dict | bytes

    """
    body = ContactCommunicationModel.from_dict(body)
    return web.Response(status=200)


async def contacts_patch_contact(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) an contact or a part of it.

    

    :param guid: ID of the contact.
    :type guid: str
    :param body: JSON patch document of ContactModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def contacts_post_contact(request: web.Request, body=None) -> web.Response:
    """Insert a contact.

    

    :param body: ContactModel.
    :type body: dict | bytes

    """
    body = ContactModel.from_dict(body)
    return web.Response(status=200)


async def customer_country_settings_patch_customer_country_settings(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a customer country setting.

    

    :param guid: ID of the customer country setting.
    :type guid: str
    :param body: JSON patch document of CustomerCountrySettingsModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def customer_country_settings_post_customer_country_settings(request: web.Request, body=None) -> web.Response:
    """Insert a customer country setting.

    

    :param body: CustomerCountrySettingsModel.
    :type body: dict | bytes

    """
    body = CustomerCountrySettingsInputModel.from_dict(body)
    return web.Response(status=200)


async def customer_custom_values_patch_customer_custom_value(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a customer custom value or a part of it.

    

    :param guid: ID of the customer custom value Can also be comma separate list of IDs to patch multiple customer custom values with one call. When multiple IDs are given, returns model which has list of succeeded customer custom values and list of errors.
    :type guid: str
    :param body: JSON Patch document of CustomerCustomValueModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def customer_custom_values_post_customer_custom_value(request: web.Request, body=None) -> web.Response:
    """Insert a customer custom value.

    

    :param body: CustomerCustomValueModel.
    :type body: dict | bytes

    """
    body = CustomerCustomValueModel.from_dict(body)
    return web.Response(status=200)


async def customer_market_segments_post_customer_market_segment(request: web.Request, body=None) -> web.Response:
    """Add a market segment for customer.

    

    :param body: CustomerMarketSegmentModel.
    :type body: dict | bytes

    """
    body = CustomerMarketSegmentModel.from_dict(body)
    return web.Response(status=200)


async def customers_patch_customer(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) an customer or a part of it.

    

    :param guid: ID of the customer.
    :type guid: str
    :param body: JSON patch document of CustomerModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def customers_post_customer(request: web.Request, body=None) -> web.Response:
    """Insert a customer.

    

    :param body: CustomerModel.
    :type body: dict | bytes

    """
    body = CustomerModel.from_dict(body)
    return web.Response(status=200)


async def keywords_link_keyword_to_contact(request: web.Request, contact_guid, guid) -> web.Response:
    """Link existing keyword to contact

    

    :param contact_guid: 
    :type contact_guid: str
    :param guid: 
    :type guid: str

    """
    return web.Response(status=200)


async def sales_notes_patch_customer_sales_note(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a customer sales note or a part of it.

    

    :param guid: ID of the customer sales note.
    :type guid: str
    :param body: JSON patch document of customer sales note model.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def sales_notes_post_customer_sales_notes(request: web.Request, body=None) -> web.Response:
    """Insert a customer sales note.

    

    :param body: SalesNoteOutputModel
    :type body: dict | bytes

    """
    body = CustomerSalesNoteInputModel.from_dict(body)
    return web.Response(status=200)
