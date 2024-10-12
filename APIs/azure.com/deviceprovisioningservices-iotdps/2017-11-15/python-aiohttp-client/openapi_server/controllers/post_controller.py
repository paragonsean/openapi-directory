from typing import List, Dict
from aiohttp import web

from openapi_server.models.certificate_response import CertificateResponse
from openapi_server.models.error_details import ErrorDetails
from openapi_server.models.name_availability_info import NameAvailabilityInfo
from openapi_server.models.operation_inputs import OperationInputs
from openapi_server.models.shared_access_signature_authorization_rule_access_rights_description import SharedAccessSignatureAuthorizationRuleAccessRightsDescription
from openapi_server.models.shared_access_signature_authorization_rule_list_result import SharedAccessSignatureAuthorizationRuleListResult
from openapi_server.models.verification_code_request import VerificationCodeRequest
from openapi_server.models.verification_code_response import VerificationCodeResponse
from openapi_server import util


async def dps_certificate_generate_verification_code(request: web.Request, certificate_name, if_match, subscription_id, resource_group_name, provisioning_service_name, api_version, certificate_name2=None, certificate_raw_bytes=None, certificate_is_verified=None, certificate_purpose=None, certificate_created=None, certificate_last_updated=None, certificate_has_private_key=None, certificate_nonce=None) -> web.Response:
    """dps_certificate_generate_verification_code

    Generate verification code for Proof of Possession.

    :param certificate_name: The mandatory logical name of the certificate, that the provisioning service uses to access.
    :type certificate_name: str
    :param if_match: ETag of the certificate. This is required to update an existing certificate, and ignored while creating a brand new certificate.
    :type if_match: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: name of resource group.
    :type resource_group_name: str
    :param provisioning_service_name: Name of provisioning service.
    :type provisioning_service_name: str
    :param api_version: The version of the API.
    :type api_version: str
    :param certificate_name2: Common Name for the certificate.
    :type certificate_name2: str
    :param certificate_raw_bytes: Raw data of certificate.
    :type certificate_raw_bytes: str
    :param certificate_is_verified: Indicates if the certificate has been verified by owner of the private key.
    :type certificate_is_verified: bool
    :param certificate_purpose: Description mentioning the purpose of the certificate.
    :type certificate_purpose: str
    :param certificate_created: Certificate creation time.
    :type certificate_created: str
    :param certificate_last_updated: Certificate last updated time.
    :type certificate_last_updated: str
    :param certificate_has_private_key: Indicates if the certificate contains private key.
    :type certificate_has_private_key: bool
    :param certificate_nonce: Random number generated to indicate Proof of Possession.
    :type certificate_nonce: str

    """
    certificate_created = util.deserialize_datetime(certificate_created)
    certificate_last_updated = util.deserialize_datetime(certificate_last_updated)
    return web.Response(status=200)


async def dps_certificate_verify_certificate(request: web.Request, certificate_name, if_match, subscription_id, resource_group_name, provisioning_service_name, api_version, request, certificate_name2=None, certificate_raw_bytes=None, certificate_is_verified=None, certificate_purpose=None, certificate_created=None, certificate_last_updated=None, certificate_has_private_key=None, certificate_nonce=None) -> web.Response:
    """Verify certificate&#39;s private key possession.

    Verifies the certificate&#39;s private key possession by providing the leaf cert issued by the verifying pre uploaded certificate.

    :param certificate_name: The mandatory logical name of the certificate, that the provisioning service uses to access.
    :type certificate_name: str
    :param if_match: ETag of the certificate.
    :type if_match: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: Resource group name.
    :type resource_group_name: str
    :param provisioning_service_name: Provisioning service name.
    :type provisioning_service_name: str
    :param api_version: The version of the API.
    :type api_version: str
    :param request: The name of the certificate
    :type request: dict | bytes
    :param certificate_name2: Common Name for the certificate.
    :type certificate_name2: str
    :param certificate_raw_bytes: Raw data of certificate.
    :type certificate_raw_bytes: str
    :param certificate_is_verified: Indicates if the certificate has been verified by owner of the private key.
    :type certificate_is_verified: bool
    :param certificate_purpose: Describe the purpose of the certificate.
    :type certificate_purpose: str
    :param certificate_created: Certificate creation time.
    :type certificate_created: str
    :param certificate_last_updated: Certificate last updated time.
    :type certificate_last_updated: str
    :param certificate_has_private_key: Indicates if the certificate contains private key.
    :type certificate_has_private_key: bool
    :param certificate_nonce: Random number generated to indicate Proof of Possession.
    :type certificate_nonce: str

    """
    request = VerificationCodeRequest.from_dict(request)
    certificate_created = util.deserialize_datetime(certificate_created)
    certificate_last_updated = util.deserialize_datetime(certificate_last_updated)
    return web.Response(status=200)


async def iot_dps_resource_check_provisioning_service_name_availability(request: web.Request, subscription_id, api_version, arguments) -> web.Response:
    """Check if a provisioning service name is available.

    Check if a provisioning service name is available. This will validate if the name is syntactically valid and if the name is usable

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param api_version: The version of the API.
    :type api_version: str
    :param arguments: Set the name parameter in the OperationInputs structure to the name of the provisioning service to check.
    :type arguments: dict | bytes

    """
    arguments = OperationInputs.from_dict(arguments)
    return web.Response(status=200)


async def iot_dps_resource_list_keys(request: web.Request, provisioning_service_name, subscription_id, resource_group_name, api_version) -> web.Response:
    """Get the security metadata for a provisioning service.

    List the primary and secondary keys for a provisioning service.

    :param provisioning_service_name: The provisioning service name to get the shared access keys for.
    :type provisioning_service_name: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: resource group name
    :type resource_group_name: str
    :param api_version: The version of the API.
    :type api_version: str

    """
    return web.Response(status=200)


async def iot_dps_resource_list_keys_for_key_name(request: web.Request, provisioning_service_name, key_name, subscription_id, resource_group_name, api_version) -> web.Response:
    """Get a shared access policy by name from a provisioning service.

    List primary and secondary keys for a specific key name

    :param provisioning_service_name: Name of the provisioning service.
    :type provisioning_service_name: str
    :param key_name: Logical key name to get key-values for.
    :type key_name: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the provisioning service.
    :type resource_group_name: str
    :param api_version: The version of the API.
    :type api_version: str

    """
    return web.Response(status=200)
