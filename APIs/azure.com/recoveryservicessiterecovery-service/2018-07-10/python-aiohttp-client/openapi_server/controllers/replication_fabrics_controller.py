from typing import List, Dict
from aiohttp import web

from openapi_server.models.fabric import Fabric
from openapi_server.models.fabric_collection import FabricCollection
from openapi_server.models.fabric_creation_input import FabricCreationInput
from openapi_server.models.failover_process_server_request import FailoverProcessServerRequest
from openapi_server.models.renew_certificate_input import RenewCertificateInput
from openapi_server import util


async def replication_fabrics_check_consistency(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name) -> web.Response:
    """Checks the consistency of the ASR fabric.

    The operation to perform a consistency check on the fabric.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Fabric name.
    :type fabric_name: str

    """
    return web.Response(status=200)


async def replication_fabrics_create(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, input) -> web.Response:
    """Creates an Azure Site Recovery fabric.

    The operation to create an Azure Site Recovery fabric (for e.g. Hyper-V site)

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Name of the ASR fabric.
    :type fabric_name: str
    :param input: Fabric creation input.
    :type input: dict | bytes

    """
    input = FabricCreationInput.from_dict(input)
    return web.Response(status=200)


async def replication_fabrics_delete(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name) -> web.Response:
    """Deletes the site.

    The operation to delete or remove an Azure Site Recovery fabric.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: ASR fabric to delete
    :type fabric_name: str

    """
    return web.Response(status=200)


async def replication_fabrics_get(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name) -> web.Response:
    """Gets the details of an ASR fabric.

    Gets the details of an Azure Site Recovery fabric.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Fabric name.
    :type fabric_name: str

    """
    return web.Response(status=200)


async def replication_fabrics_list(request: web.Request, api_version, resource_name, resource_group_name, subscription_id) -> web.Response:
    """Gets the list of ASR fabrics

    Gets a list of the Azure Site Recovery fabrics in the vault.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def replication_fabrics_migrate_to_aad(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name) -> web.Response:
    """Migrates the site to AAD.

    The operation to migrate an Azure Site Recovery fabric to AAD.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: ASR fabric to migrate.
    :type fabric_name: str

    """
    return web.Response(status=200)


async def replication_fabrics_purge(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name) -> web.Response:
    """Purges the site.

    The operation to purge(force delete) an Azure Site Recovery fabric.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: ASR fabric to purge.
    :type fabric_name: str

    """
    return web.Response(status=200)


async def replication_fabrics_reassociate_gateway(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, failover_process_server_request) -> web.Response:
    """Perform failover of the process server.

    The operation to move replications from a process server to another process server.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: The name of the fabric containing the process server.
    :type fabric_name: str
    :param failover_process_server_request: The input to the failover process server operation.
    :type failover_process_server_request: dict | bytes

    """
    failover_process_server_request = FailoverProcessServerRequest.from_dict(failover_process_server_request)
    return web.Response(status=200)


async def replication_fabrics_renew_certificate(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, renew_certificate) -> web.Response:
    """Renews certificate for the fabric.

    Renews the connection certificate for the ASR replication fabric.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: fabric name to renew certs for.
    :type fabric_name: str
    :param renew_certificate: Renew certificate input.
    :type renew_certificate: dict | bytes

    """
    renew_certificate = RenewCertificateInput.from_dict(renew_certificate)
    return web.Response(status=200)
