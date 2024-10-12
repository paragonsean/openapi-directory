from typing import List, Dict
from aiohttp import web

from openapi_server.models.booking_field_list_view_model import BookingFieldListViewModel
from openapi_server.models.country_view_model import CountryViewModel
from openapi_server.models.custom_field_definition_list_view_model import CustomFieldDefinitionListViewModel
from openapi_server.models.customer_input_model import CustomerInputModel
from openapi_server.models.customer_list_view_model import CustomerListViewModel
from openapi_server.models.customer_update_model import CustomerUpdateModel
from openapi_server.models.customer_view_model import CustomerViewModel
from openapi_server.models.state_view_model import StateViewModel
from openapi_server import util


async def consumer_v1_customers_bookingfields_get(request: web.Request, location_id=None) -> web.Response:
    """Get Customer Booking Fields

    &lt;p&gt;Use this endpoint to return &lt;b&gt;Customer Booking Fields&lt;/b&gt;. Customer booking fields are stored with each customer object. They are used when the information collected during the booking is for a particular customer. Customer Booking Fields include any custom customer fields you define and want to capture with the Booking.&lt;/p&gt;

    :param location_id: id of business location, defaults to primary business location
    :type location_id: str

    """
    return web.Response(status=200)


async def consumer_v1_customers_countries_get(request: web.Request, ) -> web.Response:
    """List Country Codes

    &lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Countries with their associated Country Code&lt;/b&gt;. Country codes are based on the 2-character ANSI standard. If your countries of operation are not currently listed, contact us at &lt;i&gt;&lt;b&gt;support@onsched.com&lt;/b&gt;&lt;/i&gt;.&lt;/p&gt;


    """
    return web.Response(status=200)


async def consumer_v1_customers_customfields_get(request: web.Request, location_id=None, lead_questions=None) -> web.Response:
    """Get Customer Custom Fields

    &lt;p&gt;Use this endpoint to return &lt;b&gt;Customer Custom Fields&lt;/b&gt;. Customer custom fields are stored with the customer object. They are used when the information collected during the booking is specific to a particular customer.&lt;/p&gt;

    :param location_id: id of business location, defaults to primary business location
    :type location_id: str
    :param lead_questions: A true/false indicator to filter on custom fields used for lead questions
    :type lead_questions: bool

    """
    return web.Response(status=200)


async def consumer_v1_customers_get(request: web.Request, location_id=None, group_id=None, email=None, lastname=None, deleted=None, offset=None, limit=None) -> web.Response:
    """List Customers

    &lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Customers&lt;/b&gt;. The results are returned in pages. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further.&lt;/p&gt;

    :param location_id: id of business location, defaults to primary business location
    :type location_id: str
    :param group_id: Filter by groupId
    :type group_id: str
    :param email: Filter by email address
    :type email: str
    :param lastname: Filter by lastname
    :type lastname: str
    :param deleted: Filter by deleted status
    :type deleted: bool
    :param offset: Starting row of page, default 0
    :type offset: int
    :param limit: Page limit default 20, max 100
    :type limit: int

    """
    return web.Response(status=200)


async def consumer_v1_customers_id_delete(request: web.Request, id) -> web.Response:
    """Delete Customer

    &lt;p&gt;Use this endpoint to permanently &lt;b&gt;Delete&lt;/b&gt; a Customer object. A valid &lt;b&gt;customer id&lt;/b&gt; is required.&lt;/p&gt;

    :param id: id of customer object
    :type id: str

    """
    return web.Response(status=200)


async def consumer_v1_customers_id_get(request: web.Request, id) -> web.Response:
    """Get Customer

    &lt;p&gt;Use this endpoint to return a &lt;b&gt;Customer&lt;/b&gt; object. A valid &lt;b&gt;customer id&lt;/b&gt; is required. Find customer id&#39;s by using the &lt;i&gt;GET /consumer/v1/customers&lt;/i&gt; endpoint.&lt;/p&gt;

    :param id: id of customer object
    :type id: str

    """
    return web.Response(status=200)


async def consumer_v1_customers_id_put(request: web.Request, id, body=None) -> web.Response:
    """Update Customer

    &lt;p&gt;Use this endpoint to &lt;b&gt;Update&lt;/b&gt; a Customer object. A valid &lt;b&gt;customer id&lt;/b&gt; is required. Note: Blank fields are not changed.&lt;/p&gt;

    :param id: id of customer object
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CustomerUpdateModel.from_dict(body)
    return web.Response(status=200)


async def consumer_v1_customers_post(request: web.Request, body=None) -> web.Response:
    """Create Customer

    &lt;p&gt;Use this endpoint to &lt;b&gt;Create&lt;/b&gt; a new Customer. A customer object is automatically created with the first appointment booking if it doesn&#39;t already exist. If not specified, the business location id defaults to the primary business location.&lt;/p&gt;  &lt;p&gt;Required Fields: &lt;b&gt;Email&lt;/b&gt; and &lt;b&gt;Name&lt;/b&gt; or &lt;b&gt;First and Lastname&lt;/b&gt; depending on customer type. Type 0 &#x3D; Person, Type 1 &#x3D; Business. For type 0, the firstname and lastname fields are used. For type 1, the Name field is used, and the name field is also used to populate the lastname.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes

    """
    body = CustomerInputModel.from_dict(body)
    return web.Response(status=200)


async def consumer_v1_customers_states_get(request: web.Request, country=None) -> web.Response:
    """List Country States

    &lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Countries with their associated State Codes&lt;/b&gt;. Supply a country code to filter results further. If states for your countries of operation are not currently listed, contact us at &lt;i&gt;&lt;b&gt;support@onsched.com&lt;/b&gt;&lt;/i&gt;.&lt;/p&gt;

    :param country: 
    :type country: str

    """
    return web.Response(status=200)
