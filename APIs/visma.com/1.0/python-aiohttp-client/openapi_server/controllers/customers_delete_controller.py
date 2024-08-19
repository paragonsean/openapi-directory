from typing import List, Dict
from aiohttp import web

from openapi_server.models.exception_model import ExceptionModel
from openapi_server import util


async def addresses_delete_address(request: web.Request, guid) -> web.Response:
    """Delete an address.

    Returns: No Content (204) if succeeded. Not found (404) if address can&#39;t be found.

    :param guid: ID for the address to delete.
    :type guid: str

    """
    return web.Response(status=200)


async def contact_communications_delete_contact_communication(request: web.Request, guid) -> web.Response:
    """Deletes contact&#39;s communication.

    Returns: No Content (204) if succeeded.

    :param guid: GUID used to delete the contact&#39;s communication.
    :type guid: str

    """
    return web.Response(status=200)


async def contacts_delete_contact(request: web.Request, guid) -> web.Response:
    """Deletes a contact.

    Returns: No Content (204) if succeeded.

    :param guid: GUID used to delete the contact.
    :type guid: str

    """
    return web.Response(status=200)


async def customer_country_settings_delete_customer_country_setting(request: web.Request, guid) -> web.Response:
    """Deletes a customer country setting.

    Returns: No Content (204) if succeeded. Not found (404) if customer country setting can&#39;t be found.

    :param guid: GUID used to delete the customer country setting.
    :type guid: str

    """
    return web.Response(status=200)


async def customer_custom_values_delete_customer_custom_value(request: web.Request, guid) -> web.Response:
    """Deletes a customer custom value.

    Returns: No Content (204) if succeeded.

    :param guid: GUID used to delete the customer custom value.
    :type guid: str

    """
    return web.Response(status=200)


async def customer_market_segments_delete_customer_market_segment(request: web.Request, guid) -> web.Response:
    """Deletes a customer market segment.

    Returns: No Content (204) if succeeded. Not found (404) if customer market segment can&#39;t be found.

    :param guid: ID for the customer market segment to delete.
    :type guid: str

    """
    return web.Response(status=200)


async def customers_delete_customer(request: web.Request, guid) -> web.Response:
    """Deletes a customer.

    Returns: No Content (204) if succeeded.

    :param guid: GUID used to delete the customer.
    :type guid: str

    """
    return web.Response(status=200)


async def keywords_delete_contact_keyword(request: web.Request, contact_guid, guid) -> web.Response:
    """Delete a keyword from the contact

    Returns: No Content (204) if succeeded. Not found (404) if the keyword or the link can&#39;t be found.

    :param contact_guid: 
    :type contact_guid: str
    :param guid: 
    :type guid: str

    """
    return web.Response(status=200)


async def sales_notes_delete_customer_sales_note(request: web.Request, guid) -> web.Response:
    """Deletes a customer sales note.

    Returns: No Content (204) if succeeded. OK (200) if note has child notes and can&#39;t be deleted. It is marked as IsDeleted &#x3D; true. Not found (404) if note can&#39;t be found.

    :param guid: GUID used to delete the customer sales note.
    :type guid: str

    """
    return web.Response(status=200)
