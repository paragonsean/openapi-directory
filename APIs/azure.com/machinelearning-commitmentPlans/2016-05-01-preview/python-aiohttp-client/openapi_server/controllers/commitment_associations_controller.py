from typing import List, Dict
from aiohttp import web

from openapi_server.models.commitment_association import CommitmentAssociation
from openapi_server.models.commitment_association_list_result import CommitmentAssociationListResult
from openapi_server.models.move_commitment_association_request import MoveCommitmentAssociationRequest
from openapi_server import util


async def commitment_associations_get(request: web.Request, subscription_id, resource_group_name, commitment_plan_name, commitment_association_name, api_version) -> web.Response:
    """commitment_associations_get

    Get a commitment association.

    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param commitment_plan_name: The Azure ML commitment plan name.
    :type commitment_plan_name: str
    :param commitment_association_name: The commitment association name.
    :type commitment_association_name: str
    :param api_version: The version of the Microsoft.MachineLearning resource provider API to use.
    :type api_version: str

    """
    return web.Response(status=200)


async def commitment_associations_list(request: web.Request, subscription_id, resource_group_name, commitment_plan_name, api_version, skip_token=None) -> web.Response:
    """commitment_associations_list

    Get all commitment associations for a parent commitment plan.

    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param commitment_plan_name: The Azure ML commitment plan name.
    :type commitment_plan_name: str
    :param api_version: The version of the Microsoft.MachineLearning resource provider API to use.
    :type api_version: str
    :param skip_token: Continuation token for pagination.
    :type skip_token: str

    """
    return web.Response(status=200)


async def commitment_associations_move(request: web.Request, subscription_id, resource_group_name, commitment_plan_name, commitment_association_name, api_version, move_payload) -> web.Response:
    """commitment_associations_move

    Re-parent a commitment association from one commitment plan to another.

    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param commitment_plan_name: The Azure ML commitment plan name.
    :type commitment_plan_name: str
    :param commitment_association_name: The commitment association name.
    :type commitment_association_name: str
    :param api_version: The version of the Microsoft.MachineLearning resource provider API to use.
    :type api_version: str
    :param move_payload: The move request payload.
    :type move_payload: dict | bytes

    """
    move_payload = MoveCommitmentAssociationRequest.from_dict(move_payload)
    return web.Response(status=200)
