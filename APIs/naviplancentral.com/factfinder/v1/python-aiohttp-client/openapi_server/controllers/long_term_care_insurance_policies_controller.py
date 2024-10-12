from typing import List, Dict
from aiohttp import web

from openapi_server.models.long_term_care_insurance_policies_model import LongTermCareInsurancePoliciesModel
from openapi_server.models.long_term_care_insurance_policy_model import LongTermCareInsurancePolicyModel
from openapi_server.models.long_term_care_insurance_policy_with_id_model import LongTermCareInsurancePolicyWithIdModel
from openapi_server import util


async def long_term_care_insurance_policies_delete_by_id(request: web.Request, id) -> web.Response:
    """long_term_care_insurance_policies_delete_by_id

    Description: The operation removes a Long Term Care Insurance Policy tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of a Long Term Care Insurance Policy from a Fact Finder.

    :param id: The Long Term Care Insurance Policy ID used to identify which Long Term Care Insurance Policy to remove
    :type id: int

    """
    return web.Response(status=200)


async def long_term_care_insurance_policies_get_by_id(request: web.Request, id) -> web.Response:
    """long_term_care_insurance_policies_get_by_id

    Description: This operation retrieves a single Long Term Care Insurance Policy for the specified Long Term Care Insurance Policy ID.&lt;br /&gt;                Purpose: Provides access to the Long Term Care Insurance Policy including description and premium.

    :param id: The ID of the Long Term Care Insurance Policy used to retreive the Long Term Care Insurance Policy
    :type id: int

    """
    return web.Response(status=200)


async def long_term_care_insurance_policies_get_long_term_care_insurance_policies_by_fact_finder_id_by_factfinderid(request: web.Request, fact_finder_id) -> web.Response:
    """long_term_care_insurance_policies_get_long_term_care_insurance_policies_by_fact_finder_id_by_factfinderid

    Description: This operation retrieves all Long Term Care Insurance Policies for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Long Term Care Insurance Policies including description and premium.

    :param fact_finder_id: The ID of the Fact Finder used to retrieve Long Term Care Insurance Policies
    :type fact_finder_id: int

    """
    return web.Response(status=200)


async def long_term_care_insurance_policies_post_by_model(request: web.Request, model) -> web.Response:
    """long_term_care_insurance_policies_post_by_model

    Description: The operation creates a Long Term Care Insurance Policy.&lt;br /&gt;                Purpose: Allows for creation of Long Term Care Insurance Policies on a Fact Finder.

    :param model: The Long Term Care Insurance Policy to be added to the Fact Finder
    :type model: dict | bytes

    """
    model = LongTermCareInsurancePolicyModel.from_dict(model)
    return web.Response(status=200)


async def long_term_care_insurance_policies_put_by_id_model(request: web.Request, id, model) -> web.Response:
    """long_term_care_insurance_policies_put_by_id_model

    Description: The operation updates a Long Term Care Insurance Policy.&lt;br /&gt;                Purpose: Allows for complete replacement of a Long Term Care Insurance Policy on a Fact Finder.

    :param id: The existing Long Term Care Insurance Policy ID used to identify which Long Term Care Insurance Policy to update
    :type id: int
    :param model: The Long Term Care Insurance Policy to be updated on a Fact Finder
    :type model: dict | bytes

    """
    model = LongTermCareInsurancePolicyModel.from_dict(model)
    return web.Response(status=200)
