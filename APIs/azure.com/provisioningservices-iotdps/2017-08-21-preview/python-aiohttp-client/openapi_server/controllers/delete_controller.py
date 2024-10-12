from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_details import ErrorDetails
from openapi_server import util


async def dps_certificate_delete(request: web.Request, subscription_id, resource_group_name, if_match, provisioning_service_name, certificate_name, api_version, certificate_name2=None, certificate_raw_bytes=None, certificate_is_verified=None, certificate_purpose=None, certificate_created=None, certificate_last_updated=None, certificate_has_private_key=None, certificate_nonce=None) -> web.Response:
    """dps_certificate_delete

    

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: Resource group identifier.
    :type resource_group_name: str
    :param if_match: ETag of the certificate
    :type if_match: str
    :param provisioning_service_name: The name of the provisioning service.
    :type provisioning_service_name: str
    :param certificate_name: This is a mandatory field, and is the logical name of the certificate that the provisioning service will access by.
    :type certificate_name: str
    :param api_version: The version of the API.
    :type api_version: str
    :param certificate_name2: This is optional, and it is the Common Name of the certificate.
    :type certificate_name2: str
    :param certificate_raw_bytes: Raw data within the certificate.
    :type certificate_raw_bytes: str
    :param certificate_is_verified: Indicates if certificate has been verified by owner of the private key.
    :type certificate_is_verified: bool
    :param certificate_purpose: A description that mentions the purpose of the certificate.
    :type certificate_purpose: str
    :param certificate_created: Time the certificate is created.
    :type certificate_created: str
    :param certificate_last_updated: Time the certificate is last updated.
    :type certificate_last_updated: str
    :param certificate_has_private_key: Indicates if the certificate contains a private key.
    :type certificate_has_private_key: bool
    :param certificate_nonce: Random number generated to indicate Proof of Possession.
    :type certificate_nonce: str

    """
    certificate_created = util.deserialize_datetime(certificate_created)
    certificate_last_updated = util.deserialize_datetime(certificate_last_updated)
    return web.Response(status=200)


async def iot_dps_resource_delete(request: web.Request, provisioning_service_name, subscription_id, resource_group_name, api_version) -> web.Response:
    """iot_dps_resource_delete

    

    :param provisioning_service_name: Name of provisioning service to delete.
    :type provisioning_service_name: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: Resource group identifier.
    :type resource_group_name: str
    :param api_version: The version of the API.
    :type api_version: str

    """
    return web.Response(status=200)
