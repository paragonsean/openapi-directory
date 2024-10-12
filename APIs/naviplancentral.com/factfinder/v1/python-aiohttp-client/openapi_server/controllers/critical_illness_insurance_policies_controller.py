from typing import List, Dict
from aiohttp import web

from openapi_server.models.critical_illness_insurance_policies_model import CriticalIllnessInsurancePoliciesModel
from openapi_server.models.critical_illness_insurance_policy_model import CriticalIllnessInsurancePolicyModel
from openapi_server.models.critical_illness_insurance_policy_with_id_model import CriticalIllnessInsurancePolicyWithIdModel
from openapi_server import util


async def critical_illness_insurance_policies_delete_by_id(request: web.Request, id) -> web.Response:
    """critical_illness_insurance_policies_delete_by_id

    Description: The operation removes a Critical Illness Insurance Policy tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of a Critical Illness Insurance Policy from a Fact Finder.

    :param id: The Critical Illness Insurance Policy ID used to identify which Critical Illness Insurance Policy to remove
    :type id: int

    """
    return web.Response(status=200)


async def critical_illness_insurance_policies_get_by_id(request: web.Request, id) -> web.Response:
    """critical_illness_insurance_policies_get_by_id

    Description: This operation retrieves a single Critical Illness Insurance Policy for the specified Critical Illness Insurance Policy ID.&lt;br /&gt;                Purpose: Provides access to the Critical Illness Insurance Policy including description and policy type.

    :param id: The ID of the Critical Illness Insurance Policy used to retreive the Critical Illness Insurance Policy
    :type id: int

    """
    return web.Response(status=200)


async def critical_illness_insurance_policies_get_critical_illness_insurance_policies_by_fact_finder_id_by_factfinderid(request: web.Request, fact_finder_id) -> web.Response:
    """critical_illness_insurance_policies_get_critical_illness_insurance_policies_by_fact_finder_id_by_factfinderid

    Description: This operation retrieves all Critical Illness Insurance Policies for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Critical Illness Insurance Policies including description and policy type.

    :param fact_finder_id: The ID of the Fact Finder used to retrieve Critical Illness Insurance Policies
    :type fact_finder_id: int

    """
    return web.Response(status=200)


async def critical_illness_insurance_policies_post_by_model(request: web.Request, model) -> web.Response:
    """critical_illness_insurance_policies_post_by_model

    Description: The operation creates a Critical Illness Insurance Policy.&lt;br /&gt;                Purpose: Allows for creation of Critical Illness Insurance Policies on a Fact Finder.

    :param model: The Critical Illness Insurance Policy to be added to the Fact Finder
    :type model: dict | bytes

    """
    model = CriticalIllnessInsurancePolicyModel.from_dict(model)
    return web.Response(status=200)


async def critical_illness_insurance_policies_put_by_id_model(request: web.Request, id, model) -> web.Response:
    """critical_illness_insurance_policies_put_by_id_model

    Description: The operation updates a Critical Illness Insurance Policy.&lt;br /&gt;                Purpose: Allows for complete replacement of a Critical Illness Insurance Policy on a Fact Finder.

    :param id: The existing Critical Illness Insurance Policy ID used to identify which Critical Illness Insurance Policy to update
    :type id: int
    :param model: The Critical Illness Insurance Policy to be updated on a Fact Finder
    :type model: dict | bytes

    """
    model = CriticalIllnessInsurancePolicyModel.from_dict(model)
    return web.Response(status=200)
