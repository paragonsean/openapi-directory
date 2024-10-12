from typing import List, Dict
from aiohttp import web

from openapi_server.models.certificate_create_request import CertificateCreateRequest
from openapi_server.models.certificate_response import CertificateResponse
from openapi_server.models.certificates_response import CertificatesResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def certificates_create_instance(request: web.Request, body) -> web.Response:
    """certificates_create_instance

    

    :param body: Certificate representation
    :type body: dict | bytes

    """
    body = CertificateCreateRequest.from_dict(body)
    return web.Response(status=200)


async def certificates_delete_instance(request: web.Request, id) -> web.Response:
    """certificates_delete_instance

    

    :param id: the id of the requested resource
    :type id: str

    """
    return web.Response(status=200)


async def certificates_get_collection(request: web.Request, filter_certificate_type=None, filter_display_name=None, filter_serial_number=None, filter_id=None, sort=None, fields_certificates=None, limit=None) -> web.Response:
    """certificates_get_collection

    

    :param filter_certificate_type: filter by attribute &#39;certificateType&#39;
    :type filter_certificate_type: List[str]
    :param filter_display_name: filter by attribute &#39;displayName&#39;
    :type filter_display_name: List[str]
    :param filter_serial_number: filter by attribute &#39;serialNumber&#39;
    :type filter_serial_number: List[str]
    :param filter_id: filter by id(s)
    :type filter_id: List[str]
    :param sort: comma-separated list of sort expressions; resources will be sorted as specified
    :type sort: List[str]
    :param fields_certificates: the fields to include for returned resources of type certificates
    :type fields_certificates: List[str]
    :param limit: maximum resources per page
    :type limit: int

    """
    return web.Response(status=200)


async def certificates_get_instance(request: web.Request, id, fields_certificates=None) -> web.Response:
    """certificates_get_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_certificates: the fields to include for returned resources of type certificates
    :type fields_certificates: List[str]

    """
    return web.Response(status=200)
