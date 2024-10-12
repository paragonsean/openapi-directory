from typing import List, Dict
from aiohttp import web

from openapi_server.models.certificate_representation import CertificateRepresentation
from openapi_server.models.key_store_config import KeyStoreConfig
from openapi_server import util


async def realm_clients_id_certificates_attr_download_post(request: web.Request, realm, id, attr, body) -> web.Response:
    """Get a keystore file for the client, containing private key and public certificate

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str
    :param attr: 
    :type attr: str
    :param body: Keystore configuration as JSON
    :type body: dict | bytes

    """
    body = KeyStoreConfig.from_dict(body)
    return web.Response(status=200)


async def realm_clients_id_certificates_attr_generate_and_download_post(request: web.Request, realm, id, attr, body) -> web.Response:
    """Generate a new keypair and certificate, and get the private key file   Generates a keypair and certificate and serves the private key in a specified keystore format.

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str
    :param attr: 
    :type attr: str
    :param body: Keystore configuration as JSON
    :type body: dict | bytes

    """
    body = KeyStoreConfig.from_dict(body)
    return web.Response(status=200)


async def realm_clients_id_certificates_attr_generate_post(request: web.Request, realm, id, attr) -> web.Response:
    """Generate a new certificate with new key pair

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str
    :param attr: 
    :type attr: str

    """
    return web.Response(status=200)


async def realm_clients_id_certificates_attr_get(request: web.Request, realm, id, attr) -> web.Response:
    """Get key info

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str
    :param attr: 
    :type attr: str

    """
    return web.Response(status=200)


async def realm_clients_id_certificates_attr_upload_certificate_post(request: web.Request, realm, id, attr) -> web.Response:
    """Upload only certificate, not private key

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str
    :param attr: 
    :type attr: str

    """
    return web.Response(status=200)


async def realm_clients_id_certificates_attr_upload_post(request: web.Request, realm, id, attr) -> web.Response:
    """Upload certificate and eventually private key

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str
    :param attr: 
    :type attr: str

    """
    return web.Response(status=200)
