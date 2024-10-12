from typing import List, Dict
from aiohttp import web

from openapi_server.models.disability_insurance_policy_type_model import DisabilityInsurancePolicyTypeModel
from openapi_server.models.disability_insurance_policy_types_model import DisabilityInsurancePolicyTypesModel
from openapi_server import util


async def disability_insurance_policy_types_get_by_country(request: web.Request, country) -> web.Response:
    """disability_insurance_policy_types_get_by_country

    Description: This operation retrieves all Disability Insurance Policy Types for the specified country.&lt;br /&gt;                Purpose: Provides access to the Disability Insurance Policy Types including id and type description.

    :param country: The country used to filter Disability Insurance Policy Types
    :type country: str

    """
    return web.Response(status=200)


async def disability_insurance_policy_types_get_by_id(request: web.Request, id) -> web.Response:
    """disability_insurance_policy_types_get_by_id

    Description: This operation retrieves all Disability Insurance Policy Types for the specified id.&lt;br /&gt;                Purpose: Provides access to the Disability Insurance Policy Types including id and type description.

    :param id: The ID of Disability Insurance Policy Type used to retreive the Disability Insurance Policy Type information
    :type id: int

    """
    return web.Response(status=200)
