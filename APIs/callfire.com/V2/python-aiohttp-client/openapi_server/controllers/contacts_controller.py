from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_contact_list_contacts_request import AddContactListContactsRequest
from openapi_server.models.add_do_not_contact_request import AddDoNotContactRequest
from openapi_server.models.contact import Contact
from openapi_server.models.contact_history import ContactHistory
from openapi_server.models.contact_list import ContactList
from openapi_server.models.contact_list_page import ContactListPage
from openapi_server.models.contact_page import ContactPage
from openapi_server.models.create_contact_list_request import CreateContactListRequest
from openapi_server.models.do_not_contact import DoNotContact
from openapi_server.models.do_not_contact_page import DoNotContactPage
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.item_list_universal_do_not_contact import ItemListUniversalDoNotContact
from openapi_server.models.resource_id import ResourceId
from openapi_server.models.resource_id_list import ResourceIdList
from openapi_server.models.update_contact_list_request import UpdateContactListRequest
from openapi_server import util


async def add_contact_list_items(request: web.Request, id, body=None) -> web.Response:
    """Add contacts to a contact list

    Adds contacts to a contact list. Available contact sources are: list of the contact entities, list of ids of existing contacts in user&#39;s account, list of phone numbers in E.164 format (11-digits)

    :param id: An id of a contact list
    :type id: int
    :param body: A request object
    :type body: dict | bytes

    """
    body = AddContactListContactsRequest.from_dict(body)
    return web.Response(status=200)


async def add_do_not_contacts(request: web.Request, body=None) -> web.Response:
    """Add do not contact (dnc) numbers

    Add or update a list of Do Not Contact (DNC) contact entries. Can toggle whether the DNCs are enabled for calls/texts.

    :param body: AddDoNotContactsRequest object
    :type body: dict | bytes

    """
    body = AddDoNotContactRequest.from_dict(body)
    return web.Response(status=200)


async def create_contact_list(request: web.Request, fields=None, body=None) -> web.Response:
    """Create contact lists

    Creates a contact list for use with campaigns using 1 of 3 inputs. A List of Contact objects, a list of String E.164 numbers, or a list of CallFire contactIds can be used as the data source for the created contact list. After contact list is added into the CallFire system, contact lists goes through seven system safeguards that check the accuracy and consistency of the data. For example, our system checks that contact number is formatted correctly, is valid, is not duplicated in another contact list, or is not added on a specific DNC list. You can configure to keep/merge or remove contacts which do not complies these rules. If contacts were not added to a contact list after the validation, this means the data needs to be properly formatted and corrected before calling this API

    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str
    :param body: A request object
    :type body: dict | bytes

    """
    body = CreateContactListRequest.from_dict(body)
    return web.Response(status=200)


async def create_contact_list_from_file(request: web.Request, file, name=None, use_custom_fields=None) -> web.Response:
    """Create contact list from file

    Creates a contact list to be used with campaigns through uploading a .csv file. Returns the id of created list

    :param file: CSV file to be uploaded
    :type file: str
    :param name: A name of a contact list
    :type name: str
    :param use_custom_fields: A flag to indicate how to define property names for contacts. If true, uses the field and property names exactly as defined. If false will assign custom properties and fields to A, B, C, etc
    :type use_custom_fields: bool

    """
    return web.Response(status=200)


async def create_contacts(request: web.Request, body=None) -> web.Response:
    """Create contacts

    Creates contacts in CallFire system. Only values from the next list can be used as external system parameter in contact creation: **NATION_BUILDER, SALES_FORCE_CONTACTS, SALES_FORCE_LEADS, SALES_FORCE_REPORTS, ZOHO, MAIL_CHIMP**. See [contacts validation rules](https://www.callfire.com/help/docs/getting-started/managing-contacts/validating-contacts#section1)

    :param body: A list of a contact objects
    :type body: list | bytes

    """
    body = [Contact.from_dict(d) for d in body]
    return web.Response(status=200)


async def delete_contact(request: web.Request, id) -> web.Response:
    """Delete a contact

    Deletes a contact instance from account

    :param id: An Id of a contact
    :type id: int

    """
    return web.Response(status=200)


async def delete_contact_list(request: web.Request, id) -> web.Response:
    """Delete a contact list

    Deletes a contact list, included contacts will not be deleted.

    :param id: An id of the contact list to be deleted
    :type id: int

    """
    return web.Response(status=200)


async def delete_do_not_contact(request: web.Request, number) -> web.Response:
    """Delete do not contact (dnc) number. If number contains commas treat as list of numbers

    Delete a Do Not Contact (DNC) contact entry.

    :param number: Number associated with Do Not Contact (DNC) entry.
    :type number: str

    """
    return web.Response(status=200)


async def delete_do_not_contacts_by_source(request: web.Request, source) -> web.Response:
    """Delete do not contact (dnc) numbers contained in source.

    Delete Do Not Contact (DNC) contact entries contained in source.

    :param source: Source associated with Do Not Contact (DNC) entry.
    :type source: str

    """
    return web.Response(status=200)


async def find_contact_lists(request: web.Request, fields=None, limit=None, offset=None, name=None, exact_match=None, contact_count=None, order_by=None) -> web.Response:
    """Find contact lists

    Searches for all contact lists which are available for the current user. Returns a paged list of contact lists

    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str
    :param limit: To set the maximum number of records to return in a paged list response. The default is 100
    :type limit: int
    :param offset: Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
    :type offset: int
    :param name: A name or a partial name of a contact list
    :type name: str
    :param exact_match: ~
    :type exact_match: bool
    :param contact_count: ~
    :type contact_count: int
    :param order_by: ~
    :type order_by: str

    """
    return web.Response(status=200)


async def find_contacts(request: web.Request, fields=None, limit=None, offset=None, id=None, number=None, contact_list_id=None, property_name=None, property_value=None) -> web.Response:
    """Find contacts

    Find user&#39;s contacts by id, contact list, or on any property name. Returns a paged list of contacts

    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str
    :param limit: To set the maximum number of records to return in a paged list response. The default is 100
    :type limit: int
    :param offset: Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
    :type offset: int
    :param id: A list of contact IDs. If the id parameter is included, the other query parameters are ignored.
    :type id: List[int]
    :param number: Multiple contact numbers can be specified. If the number parameter is included, the other query parameters are ignored.
    :type number: List[str]
    :param contact_list_id: Filters contacts by a particular contact list
    :type contact_list_id: int
    :param property_name: Name of a contact property to search by
    :type property_name: str
    :param property_value: Value of a contact property to search by
    :type property_value: str

    """
    return web.Response(status=200)


async def find_do_not_contacts(request: web.Request, fields=None, limit=None, offset=None, prefix=None, campaign_id=None, source=None, call=None, text=None, inbound_call=None, inbound_text=None, number=None) -> web.Response:
    """Find do not contact (dnc) items

    Searches for all Do Not Contact (DNC) objects created by user. These DoNotContact entries only affect calls/texts/campaigns on this account. Returns a paged list of DoNotContact objects

    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str
    :param limit: To set the maximum number of records to return in a paged list response. The default is 100
    :type limit: int
    :param offset: Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
    :type offset: int
    :param prefix: Prefix (1-10 digits) of phone numbers
    :type prefix: str
    :param campaign_id: A campaign id which was used to send a message to a DNC number
    :type campaign_id: int
    :param source: A DNC source name to search for DNCs
    :type source: str
    :param call: Show only Do-Not-Call numbers
    :type call: bool
    :param text: Show only Do-Not-Text numbers
    :type text: bool
    :param inbound_call: ~
    :type inbound_call: bool
    :param inbound_text: ~
    :type inbound_text: bool
    :param number: ~
    :type number: List[str]

    """
    return web.Response(status=200)


async def get_contact(request: web.Request, id, fields=None) -> web.Response:
    """Find a specific contact

    Returns a Contact instance for a given contact id. Deleted contacts can be still retrieved but will be marked as deleted. Deleted contacts will not be shown in search request.

    :param id: An id of a contact
    :type id: int
    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str

    """
    return web.Response(status=200)


async def get_contact_history(request: web.Request, id, limit=None, offset=None, fields=None) -> web.Response:
    """Find a contact&#39;s history

    Searches for all texts and calls attributed to a contact. Returns a list of calls and texts a contact has been involved with

    :param id: An Id of a contact
    :type id: int
    :param limit: To set the maximum number of records to return in a paged list response. The default is 100
    :type limit: int
    :param offset: Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
    :type offset: int
    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str

    """
    return web.Response(status=200)


async def get_contact_list(request: web.Request, id, fields=None) -> web.Response:
    """Find a specific contact list

    Returns a single ContactList instance for a given contact list id

    :param id: An id of a contact list to return
    :type id: int
    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str

    """
    return web.Response(status=200)


async def get_contact_list_items(request: web.Request, id, fields=None, limit=None, offset=None) -> web.Response:
    """Find contacts in a contact list

    Searches for all entries in a contact list with specified id. Returns a paged list of contact entries

    :param id: An id of a contact list
    :type id: int
    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str
    :param limit: To set the maximum number of records to return in a paged list response. The default is 100
    :type limit: int
    :param offset: Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
    :type offset: int

    """
    return web.Response(status=200)


async def get_do_not_contact(request: web.Request, number) -> web.Response:
    """Get do not contact (dnc)

    Get Do Not Contact (DNC) object create by user. This DoNotContact entry only affects calls/texts/campaigns on this account.

    :param number: Number associated with Do Not Contact (DNC) entry.
    :type number: str

    """
    return web.Response(status=200)


async def get_universal_do_not_contacts(request: web.Request, to_number, from_number=None, fields=None) -> web.Response:
    """Find universal do not contacts (udnc) associated with toNumber

    Searches for a UniversalDoNotContact object for a given phone number. Shows whether inbound/outbound actions are allowed for a given number

    :param to_number: A required destination phone number in E.164 format (11-digit). Example: 12132000384
    :type to_number: str
    :param from_number: An optional destination/source number for DNC, specified in E.164 format (11-digit). Example: 12132000384
    :type from_number: str
    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str

    """
    return web.Response(status=200)


async def remove_contact_list_item(request: web.Request, id, contact_id) -> web.Response:
    """Delete a contact from a contact list

    Deletes a single contact from a contact list

    :param id: An id of a contact list
    :type id: int
    :param contact_id: An id of a contact
    :type contact_id: int

    """
    return web.Response(status=200)


async def remove_contact_list_items(request: web.Request, id, contact_id=None) -> web.Response:
    """Delete contacts from a contact list

    Deletes contacts from a contact list. List the contact ids in request to delete multiple contacts with one request.

    :param id: A id of a contact list
    :type id: int
    :param contact_id: An id of a contact entity in the CallFire system
    :type contact_id: List[int]

    """
    return web.Response(status=200)


async def update_contact(request: web.Request, id, body=None) -> web.Response:
    """Update a contact

    Updates a single contact instance with id specified. See [contact validation rules](https://www.callfire.com/help/docs/getting-started/managing-contacts/validating-contacts#section1)

    :param id: An id of a contact
    :type id: int
    :param body: A contact object
    :type body: dict | bytes

    """
    body = Contact.from_dict(body)
    return web.Response(status=200)


async def update_contact_list(request: web.Request, id, body=None) -> web.Response:
    """Update a contact list

    Updates contact list instance.

    :param id: An id of contact list to update
    :type id: int
    :param body: A request object
    :type body: dict | bytes

    """
    body = UpdateContactListRequest.from_dict(body)
    return web.Response(status=200)


async def update_do_not_contact(request: web.Request, number, body=None) -> web.Response:
    """Update an individual do not contact (dnc) number

    Update a Do Not Contact (DNC) contact entry. Can toggle whether the DNC is enabled for calls/texts.

    :param number: ~
    :type number: str
    :param body: DoNotContact object
    :type body: dict | bytes

    """
    body = DoNotContact.from_dict(body)
    return web.Response(status=200)
