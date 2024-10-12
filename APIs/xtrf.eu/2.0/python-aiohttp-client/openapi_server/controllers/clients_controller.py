from typing import List, Dict
from aiohttp import web

from openapi_server.models.access_token_dto import AccessTokenDTO
from openapi_server.models.access_token_request_dto import AccessTokenRequestDTO
from openapi_server.models.address_dto import AddressDTO
from openapi_server.models.contact_dto import ContactDTO
from openapi_server.models.custom_field_dto import CustomFieldDTO
from openapi_server.models.customer_dto import CustomerDTO
from openapi_server.models.customer_person_dto import CustomerPersonDTO
from openapi_server.models.entity_with_name_dto import EntityWithNameDTO
from openapi_server.models.person_contact_dto import PersonContactDTO
from openapi_server import util


async def create2(request: web.Request, body) -> web.Response:
    """Creates a new person.

    Creates a new person. Required fields are presented in the example. Other fields (from PUT) may also be specified here.

    :param body: Brand new person.
    :type body: dict | bytes

    """
    body = CustomerPersonDTO.from_dict(body)
    return web.Response(status=200)


async def create3(request: web.Request, body) -> web.Response:
    """Creates a new client.

    Creates a new client. All available fields are presented in PUT request.&lt;p&gt;   Required fields:   &lt;ul&gt;     &lt;li&gt;name&lt;/li&gt;     &lt;li&gt;fullName&lt;/li&gt;     &lt;li&gt;contact -&gt; emails -&gt; primary&lt;/li&gt;   &lt;/ul&gt; &lt;/p&gt; 

    :param body: Created user object
    :type body: dict | bytes

    """
    body = CustomerDTO.from_dict(body)
    return web.Response(status=200)


async def delete3(request: web.Request, person_id) -> web.Response:
    """Removes a person.

    Removes a person.

    :param person_id: person&#39;s internal identifier
    :type person_id: int

    """
    return web.Response(status=200)


async def delete4(request: web.Request, price_list_id) -> web.Response:
    """Removes a customer price list.

    Removes a customer price list.

    :param price_list_id: customer price list&#39;s internal identifier
    :type price_list_id: int

    """
    return web.Response(status=200)


async def delete5(request: web.Request, customer_id) -> web.Response:
    """Removes a client.

    Removes a client.

    :param customer_id: client&#39;s internal identifier
    :type customer_id: int

    """
    return web.Response(status=200)


async def generate_single_use_sign_in_token(request: web.Request, body) -> web.Response:
    """Generates a single use sign-in token.

    Generates a single use sign-in token for the customer person found for given login or e-mail. Returns &#39;url&#39; and &#39;token&#39; which allows to sign-in to customer portal as this person. Token is valid for two minutes and can be used only once. To sign-in to customer portal you should post &#39;token&#39; provided as the &#39;accessToken&#39; form param to the &#39;url&#39; using POST method.Detailed description is available in the Customer API &lt;a href&#x3D;\&quot;/api-doc/customer-api/authentication\&quot;&gt;authentication&lt;/a&gt;.

    :param body: Generated sign-in token.
    :type body: dict | bytes

    """
    body = AccessTokenRequestDTO.from_dict(body)
    return web.Response(status=200)


async def get_address(request: web.Request, customer_id) -> web.Response:
    """Returns address of a given client.

    Returns address of a given client.

    :param customer_id: client&#39;s internal identifier
    :type customer_id: int

    """
    return web.Response(status=200)


async def get_all_ids1(request: web.Request, updated_since=None) -> web.Response:
    """Returns persons&#39; internal identifiers.

    Returns persons&#39; internal identifiers.

    :param updated_since: only persons modified since this timestamp
    :type updated_since: int

    """
    return web.Response(status=200)


async def get_all_ids2(request: web.Request, updated_since=None, name_equals=None, email_equals=None) -> web.Response:
    """Returns clients&#39; internal identifiers.

    Returns clients&#39; internal identifiers.

    :param updated_since: only clients modified since this timestamp
    :type updated_since: int
    :param name_equals: exact name of client
    :type name_equals: str
    :param email_equals: exact email of client
    :type email_equals: str

    """
    return web.Response(status=200)


async def get_all_names_with_ids(request: web.Request, updated_since=None) -> web.Response:
    """Returns list of simple clients representations

    Returns list of simple clients representations

    :param updated_since: only clients modified since this timestamp
    :type updated_since: int

    """
    return web.Response(status=200)


async def get_by_id1(request: web.Request, person_id) -> web.Response:
    """Returns person details.

    Returns person details.

    :param person_id: person&#39;s internal identifier
    :type person_id: int

    """
    return web.Response(status=200)


async def get_by_id2(request: web.Request, customer_id, embed=None) -> web.Response:
    """Returns client details.

    Returns client details.

    :param customer_id: client&#39;s internal identifier
    :type customer_id: int
    :param embed: list of additional fields which should be embedded in the response (available options: persons)
    :type embed: str

    """
    return web.Response(status=200)


async def get_categories(request: web.Request, customer_id) -> web.Response:
    """Returns categories of a given client.

    Returns categories of a given client.

    :param customer_id: client&#39;s internal identifier
    :type customer_id: int

    """
    return web.Response(status=200)


async def get_contact(request: web.Request, person_id) -> web.Response:
    """Returns contact of a given person.

    Returns contact of a given person.

    :param person_id: person&#39;s internal identifier
    :type person_id: int

    """
    return web.Response(status=200)


async def get_contact1(request: web.Request, customer_id) -> web.Response:
    """Returns contact of a given client.

    Returns contact of a given client.

    :param customer_id: client&#39;s internal identifier
    :type customer_id: int

    """
    return web.Response(status=200)


async def get_correspondence_address(request: web.Request, customer_id) -> web.Response:
    """Returns correspondence address of a given client.

    Returns correspondence address of a given client.

    :param customer_id: client&#39;s internal identifier
    :type customer_id: int

    """
    return web.Response(status=200)


async def get_custom_field(request: web.Request, customer_id, custom_field_key) -> web.Response:
    """Returns custom field of a given client.

    Returns custom field of a given client.

    :param customer_id: client&#39;s internal identifier
    :type customer_id: int
    :param custom_field_key: custom field&#39;s key
    :type custom_field_key: str

    """
    return web.Response(status=200)


async def get_custom_fields(request: web.Request, person_id) -> web.Response:
    """Returns custom fields of a given person.

    Returns custom fields of a given person.

    :param person_id: person&#39;s internal identifier
    :type person_id: int

    """
    return web.Response(status=200)


async def get_custom_fields1(request: web.Request, customer_id) -> web.Response:
    """Returns custom fields of a given client.

    Returns custom fields of a given client.

    :param customer_id: client&#39;s internal identifier
    :type customer_id: int

    """
    return web.Response(status=200)


async def get_industries(request: web.Request, customer_id) -> web.Response:
    """Returns industries of a given client.

    Returns industries of a given client.

    :param customer_id: client&#39;s internal identifier
    :type customer_id: int

    """
    return web.Response(status=200)


async def update1(request: web.Request, person_id, body) -> web.Response:
    """Updates an existing person.

    Only specified fields will be changed. One may not specify embeddable fields here - use separate API calls for updating them.

    :param person_id: person&#39;s internal identifier
    :type person_id: int
    :param body: Updated existing person.
    :type body: dict | bytes

    """
    body = CustomerPersonDTO.from_dict(body)
    return web.Response(status=200)


async def update2(request: web.Request, customer_id, body) -> web.Response:
    """Updates an existing client.

    Only specified fields will be changed (id is required). One may not specify embeddable fields here - use separate API calls for updating them.

    :param customer_id: client&#39;s internal identifier
    :type customer_id: int
    :param body: Updated client
    :type body: dict | bytes

    """
    body = CustomerDTO.from_dict(body)
    return web.Response(status=200)


async def update_address(request: web.Request, customer_id, body) -> web.Response:
    """Updates address of a given client.

    Updates address of a given client.

    :param customer_id: client&#39;s internal identifier
    :type customer_id: int
    :param body: Updated address of a given client.
    :type body: dict | bytes

    """
    body = AddressDTO.from_dict(body)
    return web.Response(status=200)


async def update_categories(request: web.Request, customer_id, body) -> web.Response:
    """Updates categories of a given client.

    Updates categories of a given client.

    :param customer_id: client&#39;s internal identifier
    :type customer_id: int
    :param body: Updated categories of a given client.

    """
    return web.Response(status=200)


async def update_contact(request: web.Request, person_id, body) -> web.Response:
    """Updates contact of a given person.

    Updates contact of a given person. Sets that this person uses specific address and contact (not the one from customer).

    :param person_id: person&#39;s internal identifier
    :type person_id: int
    :param body: Updated contact of a given person.
    :type body: dict | bytes

    """
    body = PersonContactDTO.from_dict(body)
    return web.Response(status=200)


async def update_contact1(request: web.Request, customer_id, body) -> web.Response:
    """Updates contact of a given client.

    Updates contact of a given client.

    :param customer_id: client&#39;s internal identifier
    :type customer_id: int
    :param body: Updated contact of a given client.
    :type body: dict | bytes

    """
    body = ContactDTO.from_dict(body)
    return web.Response(status=200)


async def update_correspondence_address(request: web.Request, customer_id, body) -> web.Response:
    """Updates correspondence address of a given client.

    Updates correspondence address of a given client.

    :param customer_id: client&#39;s internal identifier
    :type customer_id: int
    :param body: Updated address of a given client.
    :type body: dict | bytes

    """
    body = AddressDTO.from_dict(body)
    return web.Response(status=200)


async def update_custom_field(request: web.Request, customer_id, custom_field_key, body) -> web.Response:
    """Updates given custom field of a given client.

    Updates given custom field of a given client.

    :param customer_id: client&#39;s internal identifier
    :type customer_id: int
    :param custom_field_key: custom field&#39;s key
    :type custom_field_key: str
    :param body: Updated custom field of a given client.
    :type body: dict | bytes

    """
    body = CustomFieldDTO.from_dict(body)
    return web.Response(status=200)


async def update_custom_fields(request: web.Request, person_id, body) -> web.Response:
    """Updates custom fields of a given person.

    Updates custom fields of a given person.

    :param person_id: person&#39;s internal identifier
    :type person_id: int
    :param body: Updated custom fields of a given person.

    """
    return web.Response(status=200)


async def update_custom_fields1(request: web.Request, customer_id, body) -> web.Response:
    """Updates custom fields of a given client.

    Updates custom fields of a given client.

    :param customer_id: client&#39;s internal identifier
    :type customer_id: int
    :param body: Updated custom fields of a given client.

    """
    return web.Response(status=200)


async def update_industries(request: web.Request, customer_id, body) -> web.Response:
    """Updates industries of a given client.

    Updates industries of a given client.

    :param customer_id: client&#39;s internal identifier
    :type customer_id: int
    :param body: Updated industries of a given client.

    """
    return web.Response(status=200)
