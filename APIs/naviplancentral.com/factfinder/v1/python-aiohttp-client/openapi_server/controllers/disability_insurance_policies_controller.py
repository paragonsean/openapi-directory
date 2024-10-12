from typing import List, Dict
from aiohttp import web

from openapi_server.models.disability_insurance_policies_model import DisabilityInsurancePoliciesModel
from openapi_server.models.disability_insurance_policy_model import DisabilityInsurancePolicyModel
from openapi_server.models.disability_insurance_policy_with_id_model import DisabilityInsurancePolicyWithIdModel
from openapi_server import util


async def disability_insurance_policies_delete_by_id(request: web.Request, id) -> web.Response:
    """disability_insurance_policies_delete_by_id

    Description: The operation removes a Disability Insurance Policy tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of a Disability Insurance Policy from a Fact Finder.

    :param id: The Disability Insurance Policy ID used to identify which Disability Insurance Policy to remove
    :type id: int

    """
    return web.Response(status=200)


async def disability_insurance_policies_get_by_id(request: web.Request, id) -> web.Response:
    """disability_insurance_policies_get_by_id

    Description: This operation retrieves a single Disability Insurance Policy for the specified Disability Insurance Policy ID.&lt;br /&gt;                Purpose: Provides access to the Disability Insurance Policy including description and policy type.

    :param id: The ID of the Disability Insurance Policy used to retreive the Disability Insurance Policy
    :type id: int

    """
    return web.Response(status=200)


async def disability_insurance_policies_get_disability_insurance_policies_by_fact_finder_id_by_factfinderid(request: web.Request, fact_finder_id) -> web.Response:
    """disability_insurance_policies_get_disability_insurance_policies_by_fact_finder_id_by_factfinderid

    Description: This operation retrieves all Disability Insurance Policies for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Disability Insurance Policies including description and policy type.

    :param fact_finder_id: The ID of the Fact Finder used to retrieve Disability Insurance Policies
    :type fact_finder_id: int

    """
    return web.Response(status=200)


async def disability_insurance_policies_post_by_model(request: web.Request, model) -> web.Response:
    """disability_insurance_policies_post_by_model

    Description: The operation creates a Disability Insurance Policy.&lt;br /&gt;                Purpose: Allows for creation of Disability Insurance Policies on a Fact Finder.

    :param model: The Disability Insurance Policy to be added to the Fact Finder
    :type model: dict | bytes

    """
    model = DisabilityInsurancePolicyModel.from_dict(model)
    return web.Response(status=200)


async def disability_insurance_policies_put_by_id_model(request: web.Request, id, model) -> web.Response:
    """disability_insurance_policies_put_by_id_model

    Description: The operation updates a Disability Insurance Policy.&lt;br /&gt;                Purpose: Allows for complete replacement of a Disability Insurance Policy on a Fact Finder.

    :param id: The existing Disability Insurance Policy ID used to identify which Disability Insurance Policy to update
    :type id: int
    :param model: The Disability Insurance Policy to be updated on a Fact Finder
    :type model: dict | bytes

    """
    model = DisabilityInsurancePolicyModel.from_dict(model)
    return web.Response(status=200)
