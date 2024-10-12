from typing import List, Dict
from aiohttp import web

from openapi_server.models.certificate_response import CertificateResponse
from openapi_server.models.certificates_response import CertificatesResponse
from openapi_server.models.create_certificate_request import CreateCertificateRequest
from openapi_server.models.create_certificate_response import CreateCertificateResponse
from openapi_server.models.update_certificate_request import UpdateCertificateRequest
from openapi_server import util


async def certificates_get(request: web.Request, sort=None, name=None, label_selector=None, type=None) -> web.Response:
    """Get all Certificates

    Returns all Certificate objects.

    :param sort: Can be used multiple times.
    :type sort: str
    :param name: Can be used to filter resources by their name. The response will only contain the resources matching the specified name
    :type name: str
    :param label_selector: Can be used to filter resources by labels. The response will only contain resources matching the label selector.
    :type label_selector: str
    :param type: Can be used multiple times. The response will only contain Certificates matching the type.
    :type type: str

    """
    return web.Response(status=200)


async def certificates_id_delete(request: web.Request, id) -> web.Response:
    """Delete a Certificate

    Deletes a Certificate.

    :param id: ID of the resource
    :type id: int

    """
    return web.Response(status=200)


async def certificates_id_get(request: web.Request, id) -> web.Response:
    """Get a Certificate

    Gets a specific Certificate object.

    :param id: ID of the resource
    :type id: int

    """
    return web.Response(status=200)


async def certificates_id_put(request: web.Request, id, body=None) -> web.Response:
    """Update a Certificate

    Updates the Certificate properties.  Note that when updating labels, the Certificate’s current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body.  Note: if the Certificate object changes during the request, the response will be a “conflict” error. 

    :param id: ID of the resource
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateCertificateRequest.from_dict(body)
    return web.Response(status=200)


async def certificates_post(request: web.Request, body=None) -> web.Response:
    """Create a Certificate

    Creates a new Certificate.  The default type **uploaded** allows for uploading your existing &#x60;certificate&#x60; and &#x60;private_key&#x60; in PEM format. You have to monitor its expiration date and handle renewal yourself.  In contrast, type **managed** requests a new Certificate from *Let&#39;s Encrypt* for the specified &#x60;domain_names&#x60;. Only domains managed by *Hetzner DNS* are supported. We handle renewal and timely alert the project owner via email if problems occur.  For type &#x60;managed&#x60; Certificates the &#x60;action&#x60; key of the response contains the Action that allows for tracking the issuance process. For type &#x60;uploaded&#x60; Certificates the &#x60;action&#x60; is always null. 

    :param body: 
    :type body: dict | bytes

    """
    body = CreateCertificateRequest.from_dict(body)
    return web.Response(status=200)
