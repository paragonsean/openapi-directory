from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_error import BatchError
from openapi_server.models.certificate import Certificate
from openapi_server.models.certificate_add_parameter import CertificateAddParameter
from openapi_server.models.certificate_list_result import CertificateListResult
from openapi_server import util


async def certificate_add(request: web.Request, api_version, body, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """certificate_add

    Adds a certificate to the specified account.

    :param api_version: Client API Version.
    :type api_version: str
    :param body: Specifies the certificate to be added.
    :type body: dict | bytes
    :param timeout: Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Specifies if the server should return the client-request-id identifier in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str

    """
    body = CertificateAddParameter.from_dict(body)
    return web.Response(status=200)


async def certificate_cancel_deletion(request: web.Request, thumbprint_algorithm, thumbprint, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """certificate_cancel_deletion

    Cancels a failed deletion of a certificate from the specified account.

    :param thumbprint_algorithm: The algorithm used to derive the thumbprint parameter. This must be sha1.
    :type thumbprint_algorithm: str
    :param thumbprint: The thumbprint of the certificate being deleted.
    :type thumbprint: str
    :param api_version: Client API Version.
    :type api_version: str
    :param timeout: Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Specifies if the server should return the client-request-id identifier in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str

    """
    return web.Response(status=200)


async def certificate_delete(request: web.Request, thumbprint_algorithm, thumbprint, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """certificate_delete

    Deletes a certificate from the specified account.

    :param thumbprint_algorithm: The algorithm used to derive the thumbprint parameter. This must be sha1.
    :type thumbprint_algorithm: str
    :param thumbprint: The thumbprint of the certificate to be deleted.
    :type thumbprint: str
    :param api_version: Client API Version.
    :type api_version: str
    :param timeout: Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Specifies if the server should return the client-request-id identifier in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str

    """
    return web.Response(status=200)


async def certificate_get(request: web.Request, thumbprint_algorithm, thumbprint, api_version, select=None, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """certificate_get

    Gets information about the specified certificate.

    :param thumbprint_algorithm: The algorithm used to derive the thumbprint parameter. This must be sha1.
    :type thumbprint_algorithm: str
    :param thumbprint: The thumbprint of the certificate to get.
    :type thumbprint: str
    :param api_version: Client API Version.
    :type api_version: str
    :param select: Sets an OData $select clause.
    :type select: str
    :param timeout: Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Specifies if the server should return the client-request-id identifier in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str

    """
    return web.Response(status=200)


async def certificate_list(request: web.Request, api_version, filter=None, select=None, maxresults=None, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """certificate_list

    Lists all of the certificates that have been added to the specified account.

    :param api_version: Client API Version.
    :type api_version: str
    :param filter: Sets an OData $filter clause.
    :type filter: str
    :param select: Sets an OData $select clause.
    :type select: str
    :param maxresults: Sets the maximum number of items to return in the response.
    :type maxresults: int
    :param timeout: Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Specifies if the server should return the client-request-id identifier in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str

    """
    return web.Response(status=200)
