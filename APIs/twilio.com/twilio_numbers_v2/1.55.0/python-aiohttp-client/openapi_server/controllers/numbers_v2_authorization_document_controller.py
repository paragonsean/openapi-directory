from typing import List, Dict
from aiohttp import web

from openapi_server.models.authorization_document_enum_status import AuthorizationDocumentEnumStatus
from openapi_server.models.list_authorization_document_response import ListAuthorizationDocumentResponse
from openapi_server.models.numbers_v2_authorization_document import NumbersV2AuthorizationDocument
from openapi_server import util


async def create_authorization_document(request: web.Request, address_sid, contact_phone_number, email, hosted_number_order_sids, cc_emails=None, contact_title=None) -> web.Response:
    """create_authorization_document

    Create an AuthorizationDocument for authorizing the hosting of phone number capabilities on Twilio&#39;s platform.

    :param address_sid: A 34 character string that uniquely identifies the Address resource that is associated with this AuthorizationDocument.
    :type address_sid: str
    :param contact_phone_number: The contact phone number of the person authorized to sign the Authorization Document.
    :type contact_phone_number: str
    :param email: Email that this AuthorizationDocument will be sent to for signing.
    :type email: str
    :param hosted_number_order_sids: A list of HostedNumberOrder sids that this AuthorizationDocument will authorize for hosting phone number capabilities on Twilio&#39;s platform.
    :type hosted_number_order_sids: List[str]
    :param cc_emails: Email recipients who will be informed when an Authorization Document has been sent and signed.
    :type cc_emails: List[str]
    :param contact_title: The title of the person authorized to sign the Authorization Document for this phone number.
    :type contact_title: str

    """
    return web.Response(status=200)


async def delete_authorization_document(request: web.Request, sid) -> web.Response:
    """delete_authorization_document

    Cancel the AuthorizationDocument request.

    :param sid: A 34 character string that uniquely identifies this AuthorizationDocument.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_authorization_document(request: web.Request, sid) -> web.Response:
    """fetch_authorization_document

    Fetch a specific AuthorizationDocument.

    :param sid: A 34 character string that uniquely identifies this AuthorizationDocument.
    :type sid: str

    """
    return web.Response(status=200)


async def list_authorization_document(request: web.Request, email=None, status=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_authorization_document

    Retrieve a list of AuthorizationDocuments belonging to the account initiating the request.

    :param email: Email that this AuthorizationDocument will be sent to for signing.
    :type email: str
    :param status: Status of an instance resource. It can hold one of the values: 1. opened 2. signing, 3. signed LOA, 4. canceled, 5. failed. See the section entitled [Status Values](https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/authorization-document-resource#status-values) for more information on each of these statuses.
    :type status: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
