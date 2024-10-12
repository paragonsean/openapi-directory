from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_error import BatchError
from openapi_server.models.certificate import Certificate
from openapi_server.models.certificate_add_parameter import CertificateAddParameter
from openapi_server.models.certificate_list_result import CertificateListResult
from openapi_server import util


async def certificate_add(request: web.Request, api_version, certificate, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """Adds a certificate to the specified account.

    

    :param api_version: Client API Version.
    :type api_version: str
    :param certificate: The certificate to be added.
    :type certificate: dict | bytes
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str

    """
    certificate = CertificateAddParameter.from_dict(certificate)
    return web.Response(status=200)


async def certificate_cancel_deletion(request: web.Request, thumbprint_algorithm, thumbprint, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """Cancels a failed deletion of a certificate from the specified account.

    If you try to delete a certificate that is being used by a pool or compute node, the status of the certificate changes to deletefailed. If you decide that you want to continue using the certificate, you can use this operation to set the status of the certificate back to active. If you intend to delete the certificate, you do not need to run this operation after the deletion failed. You must make sure that the certificate is not being used by any resources, and then you can try again to delete the certificate.

    :param thumbprint_algorithm: The algorithm used to derive the thumbprint parameter. This must be sha1.
    :type thumbprint_algorithm: str
    :param thumbprint: The thumbprint of the certificate being deleted.
    :type thumbprint: str
    :param api_version: Client API Version.
    :type api_version: str
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str

    """
    return web.Response(status=200)


async def certificate_delete(request: web.Request, thumbprint_algorithm, thumbprint, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """Deletes a certificate from the specified account.

    You cannot delete a certificate if a resource (pool or compute node) is using it. Before you can delete a certificate, you must therefore make sure that the certificate is not associated with any existing pools, the certificate is not installed on any compute nodes (even if you remove a certificate from a pool, it is not removed from existing compute nodes in that pool until they restart), and no running tasks depend on the certificate. If you try to delete a certificate that is in use, the deletion fails. The certificate status changes to deletefailed. You can use Cancel Delete Certificate to set the status back to active if you decide that you want to continue using the certificate.

    :param thumbprint_algorithm: The algorithm used to derive the thumbprint parameter. This must be sha1.
    :type thumbprint_algorithm: str
    :param thumbprint: The thumbprint of the certificate to be deleted.
    :type thumbprint: str
    :param api_version: Client API Version.
    :type api_version: str
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
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
    :param select: An OData $select clause.
    :type select: str
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str

    """
    return web.Response(status=200)


async def certificate_list(request: web.Request, api_version, filter=None, select=None, maxresults=None, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """Lists all of the certificates that have been added to the specified account.

    

    :param api_version: Client API Version.
    :type api_version: str
    :param filter: An OData $filter clause.
    :type filter: str
    :param select: An OData $select clause.
    :type select: str
    :param maxresults: The maximum number of items to return in the response. A maximum of 1000 certificates can be returned.
    :type maxresults: int
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str

    """
    return web.Response(status=200)
