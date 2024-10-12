from typing import List, Dict
from aiohttp import web

from openapi_server.models.address_model import AddressModel
from openapi_server.models.contact_communication_model import ContactCommunicationModel
from openapi_server.models.contact_model import ContactModel
from openapi_server.models.customer_country_settings_output_model import CustomerCountrySettingsOutputModel
from openapi_server.models.customer_custom_value_model import CustomerCustomValueModel
from openapi_server.models.customer_market_segment_model import CustomerMarketSegmentModel
from openapi_server.models.customer_model import CustomerModel
from openapi_server.models.customer_sales_note_output_model import CustomerSalesNoteOutputModel
from openapi_server.models.exception_model import ExceptionModel
from openapi_server.models.key_value_pair_of_string_and_object import KeyValuePairOfStringAndObject
from openapi_server.models.key_value_pair_of_string_and_sort_direction import KeyValuePairOfStringAndSortDirection
from openapi_server.models.keyword_model import KeywordModel
from openapi_server.models.sales_note_output_model import SalesNoteOutputModel
from openapi_server import util


async def addresses_get_address(request: web.Request, guid) -> web.Response:
    """Get address by ID.

    

    :param guid: GUID used to get the address.
    :type guid: str

    """
    return web.Response(status=200)


async def addresses_get_addresses(request: web.Request, first_row=None, row_count=None, calculate_row_count=None, changed_since=None) -> web.Response:
    """Get the addresses.

    

    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param calculate_row_count: Optional: Calculate total number of rows.
    :type calculate_row_count: bool
    :param changed_since: Optional: Get addresses that have been added or changed after this date time (greater or equal).
    :type changed_since: str

    """
    changed_since = util.deserialize_datetime(changed_since)
    return web.Response(status=200)


async def addresses_get_contact_address(request: web.Request, contact_guid) -> web.Response:
    """Get contact person&#39;s address

    

    :param contact_guid: ID for the contact person
    :type contact_guid: str

    """
    return web.Response(status=200)


async def addresses_get_customer_addresses(request: web.Request, customer_guid, first_row=None, row_count=None, calculate_row_count=None) -> web.Response:
    """Get customer&#39;s addresses

    

    :param customer_guid: ID for the customer.
    :type customer_guid: str
    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param calculate_row_count: Optional: Calculate total number of rows.
    :type calculate_row_count: bool

    """
    return web.Response(status=200)


async def contact_communications_get_communication(request: web.Request, guid) -> web.Response:
    """Get contact communication by ID.

    

    :param guid: GUID used to get the contact communication.
    :type guid: str

    """
    return web.Response(status=200)


async def contact_communications_get_communications(request: web.Request, active=None, first_row=None, row_count=None, text_to_search=None, changed_since=None) -> web.Response:
    """Get all contact communications.

    

    :param active: If not given, return all contact communications, if given as true return only active contact communications, if given as false returns only inactive contact communications.
    :type active: bool
    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param text_to_search: Optional: Text to search from contact communication value.
    :type text_to_search: str
    :param changed_since: Optional: Get contact communications that have been added or changed after this date time (greater or equal).
    :type changed_since: str

    """
    changed_since = util.deserialize_datetime(changed_since)
    return web.Response(status=200)


async def contact_communications_get_communications2(request: web.Request, contact_guid, active=None) -> web.Response:
    """Get all communications for a contact.

    

    :param contact_guid: Whose communications are requested.
    :type contact_guid: str
    :param active: If not given, return all contact communications, if given as true return only active contact communications, if given as false returns only inactive contact communications.
    :type active: bool

    """
    return web.Response(status=200)


async def contacts_get_contact(request: web.Request, guid) -> web.Response:
    """Get contact by ID.

    

    :param guid: GUID used to get the contact.
    :type guid: str

    """
    return web.Response(status=200)


async def contacts_get_contacts(request: web.Request, active=None, first_row=None, row_count=None, text_to_search=None, search_criterias=None, sortings=None, changed_since=None) -> web.Response:
    """Get all the contact persons.

    

    :param active: If not given, return all Contact persons, if given as true return only active Contact persons, if given as false returns only inactive Contact persons.
    :type active: bool
    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param text_to_search: Optional: Text to search from contact person&#39;s name or communication method (i.e. phone number or email address).
    :type text_to_search: str
    :param search_criterias: Optional: Search criterias.
    :type search_criterias: list | bytes
    :param sortings: Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;FirstName&amp;sortings[0].value&#x3D;Desc &amp;sortings[1].key&#x3D;LastName&amp;sortings[1].value&#x3D;Asc\&quot;.
    :type sortings: list | bytes
    :param changed_since: Optional: Get contact persons that have been added or changed after this date time (greater or equal).
    :type changed_since: str

    """
    search_criterias = [KeyValuePairOfStringAndObject.from_dict(d) for d in search_criterias]
    sortings = [KeyValuePairOfStringAndSortDirection.from_dict(d) for d in sortings]
    changed_since = util.deserialize_datetime(changed_since)
    return web.Response(status=200)


async def contacts_get_customer_contacts(request: web.Request, customer_guid, active=None, first_row=None, row_count=None, text_to_search=None) -> web.Response:
    """Get the contact persons for a customer.

    

    :param customer_guid: Customer guid used to get the contact persons.
    :type customer_guid: str
    :param active: If not given, return all Contact persons, if given as true return only active Contact persons, if given as false returns only inactive Contact persons.
    :type active: bool
    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param text_to_search: Optional: Text to search from contact person&#39;s name or communication method (i.e. phone number or email address).
    :type text_to_search: str

    """
    return web.Response(status=200)


async def customer_country_settings_get_customer_country_settings(request: web.Request, customer_guid) -> web.Response:
    """Get all the country settings for a customer.

    

    :param customer_guid: GUID of the customer.
    :type customer_guid: str

    """
    return web.Response(status=200)


async def customer_custom_values_get_customer_custom_value(request: web.Request, guid) -> web.Response:
    """Get customer custom value by ID.

    

    :param guid: Id used to get the customer custom value.
    :type guid: str

    """
    return web.Response(status=200)


async def customer_custom_values_get_customer_custom_values(request: web.Request, customer_guid, first_row=None, row_count=None, active=None, target=None, calculate_row_count=None, sortings=None) -> web.Response:
    """Get the customer custom values.

    

    :param customer_guid: ID of the customer.
    :type customer_guid: str
    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param active: Optional: Get only values of active or inactive customer custom properties.
    :type active: bool
    :param target: List of target for which to get the values.
    :type target: List[str]
    :param calculate_row_count: Optional: Calculate total number of rows.
    :type calculate_row_count: bool
    :param sortings: Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (sub-model fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;Name&amp;sortings[0].value&#x3D;Desc&amp;sortings[1].key&#x3D;Number&amp;sortings[1].value&#x3D;Asc\&quot;.
    :type sortings: list | bytes

    """
    sortings = [KeyValuePairOfStringAndSortDirection.from_dict(d) for d in sortings]
    return web.Response(status=200)


async def customer_market_segments_get_all_customer_market_segments(request: web.Request, first_row=None, row_count=None, text_to_search=None, parent_market_segment_guid=None, include_parent_level=None) -> web.Response:
    """Get all Customer Market Segments.

    

    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param text_to_search: Optional: Text to search from customer market segment name.
    :type text_to_search: str
    :param parent_market_segment_guid: Optional: Fetches all children of a parent based on parent market segment guid.
    :type parent_market_segment_guid: str
    :param include_parent_level: Optional: Returns only child segments when false. Has no effect if parentMarketSegmentGuid parameter is defined. Default &#x3D; true.
    :type include_parent_level: bool

    """
    return web.Response(status=200)


async def customer_market_segments_get_customer_market_segment(request: web.Request, guid) -> web.Response:
    """Get the customer market segment.

    

    :param guid: Customer market segment guid.
    :type guid: str

    """
    return web.Response(status=200)


async def customer_market_segments_get_customer_market_segments(request: web.Request, customer_guid, first_row=None, row_count=None, include_market_segments_from_registry=None) -> web.Response:
    """Get the Market Segments for a customer.

    

    :param customer_guid: ID of the customer.
    :type customer_guid: str
    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param include_market_segments_from_registry: Optional: Return also the markets segments that are not in use for the customer.
    :type include_market_segments_from_registry: bool

    """
    return web.Response(status=200)


async def customers_get_customer(request: web.Request, guid) -> web.Response:
    """Get customer by GUID.

    

    :param guid: ID used to get the customer.
    :type guid: str

    """
    return web.Response(status=200)


async def customers_get_customers(request: web.Request, page_token=None, row_count=None, is_active=None, customer_owner_guids=None, is_internal=None, numbers=None, changed_since=None, email_addresses=None, customer_names=None) -> web.Response:
    """Get all the customers

    

    :param page_token: 
    :type page_token: str
    :param row_count: Optional: How many rows to fetch.
    :type row_count: int
    :param is_active: If not given, return all Customers, if given as true return only active Customers, if given as false returns only inactive Customers.
    :type is_active: bool
    :param customer_owner_guids: Optional: List of customer owner ids to search for. Default all.
    :type customer_owner_guids: List[str]
    :param is_internal: Optional: When true returns only internal customer
    :type is_internal: bool
    :param numbers: Optional: List of customer numbers.
    :type numbers: List[int]
    :param changed_since: Optional: Get customers that have been added or changed after this date time (greater or equal).
    :type changed_since: str
    :param email_addresses: Optional: Get customers where email address matches to any provided email address
    :type email_addresses: List[str]
    :param customer_names: Optional: Get customers where customer name matches to any provided customer name
    :type customer_names: List[str]

    """
    changed_since = util.deserialize_datetime(changed_since)
    return web.Response(status=200)


async def keywords_get_contact_keywords(request: web.Request, contact_guid, active=None, sortings=None) -> web.Response:
    """Get all the keywords for contact.

    

    :param contact_guid: ID of the user whose keywords are requested.
    :type contact_guid: str
    :param active: If not given, return all Keywords, if given as true return only active Keywords, if given as false returns only inactive Keywords.
    :type active: bool
    :param sortings: Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;Keyword&amp;sortings[0].value&#x3D;Desc\&quot;.
    :type sortings: list | bytes

    """
    sortings = [KeyValuePairOfStringAndSortDirection.from_dict(d) for d in sortings]
    return web.Response(status=200)


async def sales_notes_get_all_customer_sales_notes_0(request: web.Request, customer_guid, page_token=None, row_count=None, changed_since=None) -> web.Response:
    """Get the sales notes by customer guid.

    

    :param customer_guid: Customer guid used to get the notes.
    :type customer_guid: str
    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param changed_since: Optional: Get sales notes that have been added or changed after this date time (greater or equal).
    :type changed_since: str

    """
    changed_since = util.deserialize_datetime(changed_since)
    return web.Response(status=200)


async def sales_notes_get_customer_sales_note(request: web.Request, guid) -> web.Response:
    """Get customer sales note by ID.

    

    :param guid: GUID used to get the customer sales note.
    :type guid: str

    """
    return web.Response(status=200)


async def sales_notes_get_customer_sales_notes(request: web.Request, customer_guid, page_token=None, row_count=None, changed_since=None) -> web.Response:
    """Get the customer sales notes.

    

    :param customer_guid: Customer guid used to get the notes.
    :type customer_guid: str
    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param changed_since: Optional: Get sales notes that have been added or changed after this date time (greater or equal).
    :type changed_since: str

    """
    changed_since = util.deserialize_datetime(changed_since)
    return web.Response(status=200)
