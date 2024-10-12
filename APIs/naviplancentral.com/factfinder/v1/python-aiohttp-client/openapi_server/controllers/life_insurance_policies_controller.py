from typing import List, Dict
from aiohttp import web

from openapi_server.models.life_insurance_policies_model import LifeInsurancePoliciesModel
from openapi_server.models.life_insurance_policy_model import LifeInsurancePolicyModel
from openapi_server.models.life_insurance_policy_subaccount_model import LifeInsurancePolicySubaccountModel
from openapi_server.models.life_insurance_policy_subaccount_with_id_model import LifeInsurancePolicySubaccountWithIdModel
from openapi_server.models.life_insurance_policy_subaccounts_model import LifeInsurancePolicySubaccountsModel
from openapi_server.models.life_insurance_policy_with_id_model import LifeInsurancePolicyWithIdModel
from openapi_server import util


async def life_insurance_policies_delete_by_id(request: web.Request, id) -> web.Response:
    """life_insurance_policies_delete_by_id

    Description: The operation removes a Life Insurance Policy tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of a Life Insurance Policy and associated subaccounts from a Fact Finder.

    :param id: The Life Insurance Policy ID used to identify which Life Insurance Policy to remove
    :type id: int

    """
    return web.Response(status=200)


async def life_insurance_policies_delete_subaccount_by_lifeinsurancepolicyid_id(request: web.Request, life_insurance_policy_id, id) -> web.Response:
    """life_insurance_policies_delete_subaccount_by_lifeinsurancepolicyid_id

    Description: Deletes an existing Life Insurance Policy Subaccount for an existing Life Insurance Policy.&lt;br /&gt;                Purpose: Allows for removal of a subaccount from a Life Insurance Policy.

    :param life_insurance_policy_id: The ID of the Life Insurance Policy used to delete the Life Insurance Policy Subaccount.
    :type life_insurance_policy_id: int
    :param id: The ID of the Life Insurance Policy Subaccount.
    :type id: int

    """
    return web.Response(status=200)


async def life_insurance_policies_get_by_id(request: web.Request, id) -> web.Response:
    """life_insurance_policies_get_by_id

    Description: This operation retrieves a single Life Insurance Policy for the specified Life Insurance Policy ID.&lt;br /&gt;                Purpose: Provides access to the Life Insurance Policy including description and policy type.

    :param id: The ID of the Life Insurance Policy used to retreive the Life Insurance Policy
    :type id: int

    """
    return web.Response(status=200)


async def life_insurance_policies_get_life_insurance_policies_by_fact_finder_id_by_factfinderid(request: web.Request, fact_finder_id) -> web.Response:
    """life_insurance_policies_get_life_insurance_policies_by_fact_finder_id_by_factfinderid

    Description: This operation retrieves all Life Insurance Policies for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Life Insurance Policies including description and policy type.

    :param fact_finder_id: The ID of the Fact Finder used to retrieve Life Insurance Policies
    :type fact_finder_id: int

    """
    return web.Response(status=200)


async def life_insurance_policies_get_subaccount_by_lifeinsurancepolicyid_id(request: web.Request, life_insurance_policy_id, id) -> web.Response:
    """life_insurance_policies_get_subaccount_by_lifeinsurancepolicyid_id

    Description: Get a specific subaccount for an existing Life Insurance Policy.&lt;br /&gt;                Purpose: Provides access to the Life Insurance Policy subaccount.

    :param life_insurance_policy_id: The ID of the Life Insurance Policy used to retrieve the Life Insurance Policy Subaccount.
    :type life_insurance_policy_id: int
    :param id: The ID of the Life Insurance Policy Subaccount.
    :type id: int

    """
    return web.Response(status=200)


async def life_insurance_policies_get_subaccounts_by_lifeinsurancepolicyid(request: web.Request, life_insurance_policy_id) -> web.Response:
    """life_insurance_policies_get_subaccounts_by_lifeinsurancepolicyid

    Description: Get all the subaccounts for an existing Life Insurance Policy.&lt;br /&gt;                Purpose: Provides access to all the Life Insurance Policy subaccounts.

    :param life_insurance_policy_id: The ID of the Life Insurance Policy used to retrieve the Life Insurance Policy Subaccounts.
    :type life_insurance_policy_id: int

    """
    return web.Response(status=200)


async def life_insurance_policies_post_by_model(request: web.Request, model) -> web.Response:
    """life_insurance_policies_post_by_model

    Description: The operation creates a Life Insurance Policy.&lt;br /&gt;                Purpose: Allows for creation of Life Insurance Policies on a Fact Finder.

    :param model: The Life Insurance Policy to be added to the Fact Finder
    :type model: dict | bytes

    """
    model = LifeInsurancePolicyModel.from_dict(model)
    return web.Response(status=200)


async def life_insurance_policies_post_subaccount_by_lifeinsurancepolicyid_model(request: web.Request, life_insurance_policy_id, model) -> web.Response:
    """life_insurance_policies_post_subaccount_by_lifeinsurancepolicyid_model

    Description: Creates a subaccount and adds it to an existing Life Insurance Policy.&lt;br /&gt;                Purpose: Allows for creation of subaccount on a Life Insurance Policy.

    :param life_insurance_policy_id: The ID of the Life Insurance Policy used to create the Life Insurance Policy Subaccount.
    :type life_insurance_policy_id: int
    :param model: The Life Insurance Policy Subaccount model.
    :type model: dict | bytes

    """
    model = LifeInsurancePolicySubaccountModel.from_dict(model)
    return web.Response(status=200)


async def life_insurance_policies_put_by_id_model(request: web.Request, id, model) -> web.Response:
    """life_insurance_policies_put_by_id_model

    Description: The operation updates a Life Insurance Policy, deletes associated sub-accounts if the policy type changes.&lt;br /&gt;                Purpose: Allows for complete replacement of a Life Insurance Policy on a Fact Finder.

    :param id: The existing Life Insurance Policy ID used to identify which Life Insurance Policy to update
    :type id: int
    :param model: The Life Insurance Policy to be updated on a Fact Finder
    :type model: dict | bytes

    """
    model = LifeInsurancePolicyModel.from_dict(model)
    return web.Response(status=200)


async def life_insurance_policies_put_subaccount_by_lifeinsurancepolicyid_id_model(request: web.Request, life_insurance_policy_id, id, model) -> web.Response:
    """life_insurance_policies_put_subaccount_by_lifeinsurancepolicyid_id_model

    Description: Updates an existing Life Insurance Policy Subaccount for an existing Life Insurance Policy.&lt;br /&gt;                Purpose: Allows for complete replacement of a subaccount on a Life Insurance Policy.

    :param life_insurance_policy_id: The ID of the Life Insurance Policy used to update the Life Insurance Policy Subaccount.
    :type life_insurance_policy_id: int
    :param id: The ID of the Life Insurance Policy Subaccount.
    :type id: int
    :param model: The Life Insurance Policy Subaccount model.
    :type model: dict | bytes

    """
    model = LifeInsurancePolicySubaccountModel.from_dict(model)
    return web.Response(status=200)
