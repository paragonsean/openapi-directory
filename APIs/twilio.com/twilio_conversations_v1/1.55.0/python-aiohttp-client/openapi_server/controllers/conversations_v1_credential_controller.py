from typing import List, Dict
from aiohttp import web

from openapi_server.models.conversations_v1_credential import ConversationsV1Credential
from openapi_server.models.credential_enum_push_type import CredentialEnumPushType
from openapi_server.models.list_credential_response import ListCredentialResponse
from openapi_server import util


async def create_credential(request: web.Request, type, api_key=None, certificate=None, friendly_name=None, private_key=None, sandbox=None, secret=None) -> web.Response:
    """create_credential

    Add a new push notification credential to your account

    :param type: 
    :type type: str
    :param api_key: [GCM only] The API key for the project that was obtained from the Google Developer console for your GCM Service application credential.
    :type api_key: str
    :param certificate: [APN only] The URL encoded representation of the certificate. For example,  &#x60;-----BEGIN CERTIFICATE----- MIIFnTCCBIWgAwIBAgIIAjy9H849+E8wDQYJKoZIhvcNAQEF.....A&#x3D;&#x3D; -----END CERTIFICATE-----&#x60;.
    :type certificate: str
    :param friendly_name: A descriptive string that you create to describe the new resource. It can be up to 64 characters long.
    :type friendly_name: str
    :param private_key: [APN only] The URL encoded representation of the private key. For example, &#x60;-----BEGIN RSA PRIVATE KEY----- MIIEpQIBAAKCAQEAuyf/lNrH9ck8DmNyo3fG... -----END RSA PRIVATE KEY-----&#x60;.
    :type private_key: str
    :param sandbox: [APN only] Whether to send the credential to sandbox APNs. Can be &#x60;true&#x60; to send to sandbox APNs or &#x60;false&#x60; to send to production.
    :type sandbox: bool
    :param secret: [FCM only] The **Server key** of your project from the Firebase console, found under Settings / Cloud messaging.
    :type secret: str

    """
    return web.Response(status=200)


async def delete_credential(request: web.Request, sid) -> web.Response:
    """delete_credential

    Remove a push notification credential from your account

    :param sid: A 34 character string that uniquely identifies this resource.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_credential(request: web.Request, sid) -> web.Response:
    """fetch_credential

    Fetch a push notification credential from your account

    :param sid: A 34 character string that uniquely identifies this resource.
    :type sid: str

    """
    return web.Response(status=200)


async def list_credential(request: web.Request, page_size=None, page=None, page_token=None) -> web.Response:
    """list_credential

    Retrieve a list of all push notification credentials on your account

    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_credential(request: web.Request, sid, api_key=None, certificate=None, friendly_name=None, private_key=None, sandbox=None, secret=None, type=None) -> web.Response:
    """update_credential

    Update an existing push notification credential on your account

    :param sid: A 34 character string that uniquely identifies this resource.
    :type sid: str
    :param api_key: [GCM only] The API key for the project that was obtained from the Google Developer console for your GCM Service application credential.
    :type api_key: str
    :param certificate: [APN only] The URL encoded representation of the certificate. For example,  &#x60;-----BEGIN CERTIFICATE----- MIIFnTCCBIWgAwIBAgIIAjy9H849+E8wDQYJKoZIhvcNAQEF.....A&#x3D;&#x3D; -----END CERTIFICATE-----&#x60;.
    :type certificate: str
    :param friendly_name: A descriptive string that you create to describe the new resource. It can be up to 64 characters long.
    :type friendly_name: str
    :param private_key: [APN only] The URL encoded representation of the private key. For example, &#x60;-----BEGIN RSA PRIVATE KEY----- MIIEpQIBAAKCAQEAuyf/lNrH9ck8DmNyo3fG... -----END RSA PRIVATE KEY-----&#x60;.
    :type private_key: str
    :param sandbox: [APN only] Whether to send the credential to sandbox APNs. Can be &#x60;true&#x60; to send to sandbox APNs or &#x60;false&#x60; to send to production.
    :type sandbox: bool
    :param secret: [FCM only] The **Server key** of your project from the Firebase console, found under Settings / Cloud messaging.
    :type secret: str
    :param type: 
    :type type: str

    """
    return web.Response(status=200)
