from typing import List, Dict
from aiohttp import web

from openapi_server.models.critical_illness_insurance_policy_type_model import CriticalIllnessInsurancePolicyTypeModel
from openapi_server.models.critical_illness_insurance_policy_types_model import CriticalIllnessInsurancePolicyTypesModel
from openapi_server import util


async def critical_illness_insurance_policy_types_get_by_country(request: web.Request, country) -> web.Response:
    """critical_illness_insurance_policy_types_get_by_country

    Description: This operation retrieves all Critical Illness Insurance Policy Types for the specified country.&lt;br /&gt;                Purpose: Provides access to the Critical Illness Insurance Policy Types including id and type description.

    :param country: The country used to filter Critical Illness Insurance Policy Types
    :type country: str

    """
    return web.Response(status=200)


async def critical_illness_insurance_policy_types_get_by_id(request: web.Request, id) -> web.Response:
    """critical_illness_insurance_policy_types_get_by_id

    Description: This operation retrieves the Critical Illness Insurance Policy Type for the specified id.&lt;br /&gt;                Purpose: Provides access to the Critical Illness Insurance Policy Types including id and type description.

    :param id: The ID of Critical Illness Insurance Policy Type used to retreive the Critical Illness Insurance Policy Type information
    :type id: int

    """
    return web.Response(status=200)
