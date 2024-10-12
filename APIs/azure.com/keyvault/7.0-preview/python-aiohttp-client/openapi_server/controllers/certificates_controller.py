from typing import List, Dict
from aiohttp import web

from openapi_server.models.backup_certificate_result import BackupCertificateResult
from openapi_server.models.certificate_bundle import CertificateBundle
from openapi_server.models.certificate_create_parameters import CertificateCreateParameters
from openapi_server.models.certificate_import_parameters import CertificateImportParameters
from openapi_server.models.certificate_issuer_list_result import CertificateIssuerListResult
from openapi_server.models.certificate_issuer_set_parameters import CertificateIssuerSetParameters
from openapi_server.models.certificate_issuer_update_parameters import CertificateIssuerUpdateParameters
from openapi_server.models.certificate_list_result import CertificateListResult
from openapi_server.models.certificate_merge_parameters import CertificateMergeParameters
from openapi_server.models.certificate_operation import CertificateOperation
from openapi_server.models.certificate_operation_update_parameter import CertificateOperationUpdateParameter
from openapi_server.models.certificate_policy import CertificatePolicy
from openapi_server.models.certificate_restore_parameters import CertificateRestoreParameters
from openapi_server.models.certificate_update_parameters import CertificateUpdateParameters
from openapi_server.models.contacts import Contacts
from openapi_server.models.deleted_certificate_bundle import DeletedCertificateBundle
from openapi_server.models.issuer_bundle import IssuerBundle
from openapi_server.models.key_vault_error import KeyVaultError
from openapi_server import util


async def backup_certificate(request: web.Request, certificate_name, api_version) -> web.Response:
    """Backs up the specified certificate.

    Requests that a backup of the specified certificate be downloaded to the client. All versions of the certificate will be downloaded. This operation requires the certificates/backup permission.

    :param certificate_name: The name of the certificate.
    :type certificate_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def create_certificate(request: web.Request, certificate_name, api_version, parameters) -> web.Response:
    """Creates a new certificate.

    If this is the first version, the certificate resource is created. This operation requires the certificates/create permission.

    :param certificate_name: The name of the certificate.
    :type certificate_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param parameters: The parameters to create a certificate.
    :type parameters: dict | bytes

    """
    parameters = CertificateCreateParameters.from_dict(parameters)
    return web.Response(status=200)


async def delete_certificate(request: web.Request, certificate_name, api_version) -> web.Response:
    """Deletes a certificate from a specified key vault.

    Deletes all versions of a certificate object along with its associated policy. Delete certificate cannot be used to remove individual versions of a certificate object. This operation requires the certificates/delete permission.

    :param certificate_name: The name of the certificate.
    :type certificate_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def delete_certificate_contacts(request: web.Request, api_version) -> web.Response:
    """Deletes the certificate contacts for a specified key vault.

    Deletes the certificate contacts for a specified key vault certificate. This operation requires the certificates/managecontacts permission.

    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def delete_certificate_issuer(request: web.Request, issuer_name, api_version) -> web.Response:
    """Deletes the specified certificate issuer.

    The DeleteCertificateIssuer operation permanently removes the specified certificate issuer from the vault. This operation requires the certificates/manageissuers/deleteissuers permission.

    :param issuer_name: The name of the issuer.
    :type issuer_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def delete_certificate_operation(request: web.Request, certificate_name, api_version) -> web.Response:
    """Deletes the creation operation for a specific certificate.

    Deletes the creation operation for a specified certificate that is in the process of being created. The certificate is no longer created. This operation requires the certificates/update permission.

    :param certificate_name: The name of the certificate.
    :type certificate_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_certificate(request: web.Request, certificate_name, certificate_version, api_version) -> web.Response:
    """Gets information about a certificate.

    Gets information about a specific certificate. This operation requires the certificates/get permission.

    :param certificate_name: The name of the certificate in the given vault.
    :type certificate_name: str
    :param certificate_version: The version of the certificate.
    :type certificate_version: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_certificate_contacts(request: web.Request, api_version) -> web.Response:
    """Lists the certificate contacts for a specified key vault.

    The GetCertificateContacts operation returns the set of certificate contact resources in the specified key vault. This operation requires the certificates/managecontacts permission.

    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_certificate_issuer(request: web.Request, issuer_name, api_version) -> web.Response:
    """Lists the specified certificate issuer.

    The GetCertificateIssuer operation returns the specified certificate issuer resources in the specified key vault. This operation requires the certificates/manageissuers/getissuers permission.

    :param issuer_name: The name of the issuer.
    :type issuer_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_certificate_issuers(request: web.Request, api_version, maxresults=None) -> web.Response:
    """List certificate issuers for a specified key vault.

    The GetCertificateIssuers operation returns the set of certificate issuer resources in the specified key vault. This operation requires the certificates/manageissuers/getissuers permission.

    :param api_version: Client API version.
    :type api_version: str
    :param maxresults: Maximum number of results to return in a page. If not specified the service will return up to 25 results.
    :type maxresults: int

    """
    return web.Response(status=200)


async def get_certificate_operation(request: web.Request, certificate_name, api_version) -> web.Response:
    """Gets the creation operation of a certificate.

    Gets the creation operation associated with a specified certificate. This operation requires the certificates/get permission.

    :param certificate_name: The name of the certificate.
    :type certificate_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_certificate_policy(request: web.Request, certificate_name, api_version) -> web.Response:
    """Lists the policy for a certificate.

    The GetCertificatePolicy operation returns the specified certificate policy resources in the specified key vault. This operation requires the certificates/get permission.

    :param certificate_name: The name of the certificate in a given key vault.
    :type certificate_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_certificate_versions(request: web.Request, certificate_name, api_version, maxresults=None) -> web.Response:
    """List the versions of a certificate.

    The GetCertificateVersions operation returns the versions of a certificate in the specified key vault. This operation requires the certificates/list permission.

    :param certificate_name: The name of the certificate.
    :type certificate_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param maxresults: Maximum number of results to return in a page. If not specified the service will return up to 25 results.
    :type maxresults: int

    """
    return web.Response(status=200)


async def get_certificates(request: web.Request, api_version, maxresults=None, include_pending=None) -> web.Response:
    """List certificates in a specified key vault

    The GetCertificates operation returns the set of certificates resources in the specified key vault. This operation requires the certificates/list permission.

    :param api_version: Client API version.
    :type api_version: str
    :param maxresults: Maximum number of results to return in a page. If not specified the service will return up to 25 results.
    :type maxresults: int
    :param include_pending: Specifies whether to include certificates which are not completely provisioned.
    :type include_pending: bool

    """
    return web.Response(status=200)


async def import_certificate(request: web.Request, certificate_name, api_version, parameters) -> web.Response:
    """Imports a certificate into a specified key vault.

    Imports an existing valid certificate, containing a private key, into Azure Key Vault. The certificate to be imported can be in either PFX or PEM format. If the certificate is in PEM format the PEM file must contain the key as well as x509 certificates. This operation requires the certificates/import permission.

    :param certificate_name: The name of the certificate.
    :type certificate_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param parameters: The parameters to import the certificate.
    :type parameters: dict | bytes

    """
    parameters = CertificateImportParameters.from_dict(parameters)
    return web.Response(status=200)


async def merge_certificate(request: web.Request, certificate_name, api_version, parameters) -> web.Response:
    """Merges a certificate or a certificate chain with a key pair existing on the server.

    The MergeCertificate operation performs the merging of a certificate or certificate chain with a key pair currently available in the service. This operation requires the certificates/create permission.

    :param certificate_name: The name of the certificate.
    :type certificate_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param parameters: The parameters to merge certificate.
    :type parameters: dict | bytes

    """
    parameters = CertificateMergeParameters.from_dict(parameters)
    return web.Response(status=200)


async def restore_certificate(request: web.Request, api_version, parameters) -> web.Response:
    """Restores a backed up certificate to a vault.

    Restores a backed up certificate, and all its versions, to a vault. This operation requires the certificates/restore permission.

    :param api_version: Client API version.
    :type api_version: str
    :param parameters: The parameters to restore the certificate.
    :type parameters: dict | bytes

    """
    parameters = CertificateRestoreParameters.from_dict(parameters)
    return web.Response(status=200)


async def set_certificate_contacts(request: web.Request, api_version, contacts) -> web.Response:
    """Sets the certificate contacts for the specified key vault.

    Sets the certificate contacts for the specified key vault. This operation requires the certificates/managecontacts permission.

    :param api_version: Client API version.
    :type api_version: str
    :param contacts: The contacts for the key vault certificate.
    :type contacts: dict | bytes

    """
    contacts = Contacts.from_dict(contacts)
    return web.Response(status=200)


async def set_certificate_issuer(request: web.Request, issuer_name, api_version, parameter) -> web.Response:
    """Sets the specified certificate issuer.

    The SetCertificateIssuer operation adds or updates the specified certificate issuer. This operation requires the certificates/setissuers permission.

    :param issuer_name: The name of the issuer.
    :type issuer_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param parameter: Certificate issuer set parameter.
    :type parameter: dict | bytes

    """
    parameter = CertificateIssuerSetParameters.from_dict(parameter)
    return web.Response(status=200)


async def update_certificate(request: web.Request, certificate_name, certificate_version, api_version, parameters) -> web.Response:
    """Updates the specified attributes associated with the given certificate.

    The UpdateCertificate operation applies the specified update on the given certificate; the only elements updated are the certificate&#39;s attributes. This operation requires the certificates/update permission.

    :param certificate_name: The name of the certificate in the given key vault.
    :type certificate_name: str
    :param certificate_version: The version of the certificate.
    :type certificate_version: str
    :param api_version: Client API version.
    :type api_version: str
    :param parameters: The parameters for certificate update.
    :type parameters: dict | bytes

    """
    parameters = CertificateUpdateParameters.from_dict(parameters)
    return web.Response(status=200)


async def update_certificate_issuer(request: web.Request, issuer_name, api_version, parameter) -> web.Response:
    """Updates the specified certificate issuer.

    The UpdateCertificateIssuer operation performs an update on the specified certificate issuer entity. This operation requires the certificates/setissuers permission.

    :param issuer_name: The name of the issuer.
    :type issuer_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param parameter: Certificate issuer update parameter.
    :type parameter: dict | bytes

    """
    parameter = CertificateIssuerUpdateParameters.from_dict(parameter)
    return web.Response(status=200)


async def update_certificate_operation(request: web.Request, certificate_name, api_version, certificate_operation) -> web.Response:
    """Updates a certificate operation.

    Updates a certificate creation operation that is already in progress. This operation requires the certificates/update permission.

    :param certificate_name: The name of the certificate.
    :type certificate_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param certificate_operation: The certificate operation response.
    :type certificate_operation: dict | bytes

    """
    certificate_operation = CertificateOperationUpdateParameter.from_dict(certificate_operation)
    return web.Response(status=200)


async def update_certificate_policy(request: web.Request, certificate_name, api_version, certificate_policy) -> web.Response:
    """Updates the policy for a certificate.

    Set specified members in the certificate policy. Leave others as null. This operation requires the certificates/update permission.

    :param certificate_name: The name of the certificate in the given vault.
    :type certificate_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param certificate_policy: The policy for the certificate.
    :type certificate_policy: dict | bytes

    """
    certificate_policy = CertificatePolicy.from_dict(certificate_policy)
    return web.Response(status=200)
