from typing import List, Dict
from aiohttp import web

from openapi_server.models.blob_container import BlobContainer
from openapi_server.models.immutability_policy import ImmutabilityPolicy
from openapi_server.models.lease_container_request import LeaseContainerRequest
from openapi_server.models.lease_container_response import LeaseContainerResponse
from openapi_server.models.legal_hold import LegalHold
from openapi_server.models.list_container_items import ListContainerItems
from openapi_server import util


async def blob_containers_clear_legal_hold(request: web.Request, resource_group_name, account_name, container_name, api_version, subscription_id, legal_hold) -> web.Response:
    """blob_containers_clear_legal_hold

    Clears legal hold tags. Clearing the same or non-existent tag results in an idempotent operation. ClearLegalHold clears out only the specified tags in the request.

    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :type account_name: str
    :param container_name: The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
    :type container_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param legal_hold: The LegalHold property that will be clear from a blob container.
    :type legal_hold: dict | bytes

    """
    legal_hold = LegalHold.from_dict(legal_hold)
    return web.Response(status=200)


async def blob_containers_create(request: web.Request, resource_group_name, account_name, container_name, api_version, subscription_id, blob_container) -> web.Response:
    """blob_containers_create

    Creates a new container under the specified account as described by request body. The container resource includes metadata and properties for that container. It does not include a list of the blobs contained by the container. 

    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :type account_name: str
    :param container_name: The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
    :type container_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param blob_container: Properties of the blob container to create.
    :type blob_container: dict | bytes

    """
    blob_container = BlobContainer.from_dict(blob_container)
    return web.Response(status=200)


async def blob_containers_create_or_update_immutability_policy(request: web.Request, resource_group_name, account_name, container_name, immutability_policy_name, api_version, subscription_id, if_match=None, parameters=None) -> web.Response:
    """blob_containers_create_or_update_immutability_policy

    Creates or updates an unlocked immutability policy. ETag in If-Match is honored if given but not required for this operation.

    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :type account_name: str
    :param container_name: The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
    :type container_name: str
    :param immutability_policy_name: The name of the blob container immutabilityPolicy within the specified storage account. ImmutabilityPolicy Name must be &#39;default&#39;
    :type immutability_policy_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param if_match: The entity state (ETag) version of the immutability policy to update. A value of \&quot;*\&quot; can be used to apply the operation only if the immutability policy already exists. If omitted, this operation will always be applied.
    :type if_match: str
    :param parameters: The ImmutabilityPolicy Properties that will be created or updated to a blob container.
    :type parameters: dict | bytes

    """
    parameters = ImmutabilityPolicy.from_dict(parameters)
    return web.Response(status=200)


async def blob_containers_delete(request: web.Request, resource_group_name, account_name, container_name, api_version, subscription_id) -> web.Response:
    """blob_containers_delete

    Deletes specified container under its account.

    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :type account_name: str
    :param container_name: The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
    :type container_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def blob_containers_delete_immutability_policy(request: web.Request, resource_group_name, account_name, container_name, immutability_policy_name, api_version, subscription_id, if_match) -> web.Response:
    """blob_containers_delete_immutability_policy

    Aborts an unlocked immutability policy. The response of delete has immutabilityPeriodSinceCreationInDays set to 0. ETag in If-Match is required for this operation. Deleting a locked immutability policy is not allowed, only way is to delete the container after deleting all blobs inside the container.

    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :type account_name: str
    :param container_name: The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
    :type container_name: str
    :param immutability_policy_name: The name of the blob container immutabilityPolicy within the specified storage account. ImmutabilityPolicy Name must be &#39;default&#39;
    :type immutability_policy_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param if_match: The entity state (ETag) version of the immutability policy to update. A value of \&quot;*\&quot; can be used to apply the operation only if the immutability policy already exists. If omitted, this operation will always be applied.
    :type if_match: str

    """
    return web.Response(status=200)


async def blob_containers_extend_immutability_policy(request: web.Request, resource_group_name, account_name, container_name, api_version, subscription_id, if_match, parameters=None) -> web.Response:
    """blob_containers_extend_immutability_policy

    Extends the immutabilityPeriodSinceCreationInDays of a locked immutabilityPolicy. The only action allowed on a Locked policy will be this action. ETag in If-Match is required for this operation.

    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :type account_name: str
    :param container_name: The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
    :type container_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param if_match: The entity state (ETag) version of the immutability policy to update. A value of \&quot;*\&quot; can be used to apply the operation only if the immutability policy already exists. If omitted, this operation will always be applied.
    :type if_match: str
    :param parameters: The ImmutabilityPolicy Properties that will be extended for a blob container.
    :type parameters: dict | bytes

    """
    parameters = ImmutabilityPolicy.from_dict(parameters)
    return web.Response(status=200)


async def blob_containers_get(request: web.Request, resource_group_name, account_name, container_name, api_version, subscription_id) -> web.Response:
    """blob_containers_get

    Gets properties of a specified container. 

    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :type account_name: str
    :param container_name: The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
    :type container_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def blob_containers_get_immutability_policy(request: web.Request, resource_group_name, account_name, container_name, immutability_policy_name, api_version, subscription_id, if_match=None) -> web.Response:
    """blob_containers_get_immutability_policy

    Gets the existing immutability policy along with the corresponding ETag in response headers and body.

    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :type account_name: str
    :param container_name: The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
    :type container_name: str
    :param immutability_policy_name: The name of the blob container immutabilityPolicy within the specified storage account. ImmutabilityPolicy Name must be &#39;default&#39;
    :type immutability_policy_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param if_match: The entity state (ETag) version of the immutability policy to update. A value of \&quot;*\&quot; can be used to apply the operation only if the immutability policy already exists. If omitted, this operation will always be applied.
    :type if_match: str

    """
    return web.Response(status=200)


async def blob_containers_lease(request: web.Request, resource_group_name, account_name, container_name, api_version, subscription_id, parameters=None) -> web.Response:
    """blob_containers_lease

    The Lease Container operation establishes and manages a lock on a container for delete operations. The lock duration can be 15 to 60 seconds, or can be infinite.

    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :type account_name: str
    :param container_name: The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
    :type container_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param parameters: Lease Container request body.
    :type parameters: dict | bytes

    """
    parameters = LeaseContainerRequest.from_dict(parameters)
    return web.Response(status=200)


async def blob_containers_list(request: web.Request, resource_group_name, account_name, api_version, subscription_id) -> web.Response:
    """blob_containers_list

    Lists all containers and does not support a prefix like data plane. Also SRP today does not return continuation token.

    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :type account_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def blob_containers_lock_immutability_policy(request: web.Request, resource_group_name, account_name, container_name, api_version, subscription_id, if_match) -> web.Response:
    """blob_containers_lock_immutability_policy

    Sets the ImmutabilityPolicy to Locked state. The only action allowed on a Locked policy is ExtendImmutabilityPolicy action. ETag in If-Match is required for this operation.

    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :type account_name: str
    :param container_name: The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
    :type container_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param if_match: The entity state (ETag) version of the immutability policy to update. A value of \&quot;*\&quot; can be used to apply the operation only if the immutability policy already exists. If omitted, this operation will always be applied.
    :type if_match: str

    """
    return web.Response(status=200)


async def blob_containers_set_legal_hold(request: web.Request, resource_group_name, account_name, container_name, api_version, subscription_id, legal_hold) -> web.Response:
    """blob_containers_set_legal_hold

    Sets legal hold tags. Setting the same tag results in an idempotent operation. SetLegalHold follows an append pattern and does not clear out the existing tags that are not specified in the request.

    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :type account_name: str
    :param container_name: The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
    :type container_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param legal_hold: The LegalHold property that will be set to a blob container.
    :type legal_hold: dict | bytes

    """
    legal_hold = LegalHold.from_dict(legal_hold)
    return web.Response(status=200)


async def blob_containers_update(request: web.Request, resource_group_name, account_name, container_name, api_version, subscription_id, blob_container) -> web.Response:
    """blob_containers_update

    Updates container properties as specified in request body. Properties not mentioned in the request will be unchanged. Update fails if the specified container doesn&#39;t already exist. 

    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :type account_name: str
    :param container_name: The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
    :type container_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param blob_container: Properties to update for the blob container.
    :type blob_container: dict | bytes

    """
    blob_container = BlobContainer.from_dict(blob_container)
    return web.Response(status=200)
