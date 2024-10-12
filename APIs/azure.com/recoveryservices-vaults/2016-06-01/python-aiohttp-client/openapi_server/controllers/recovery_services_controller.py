from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_name_availability_parameters import CheckNameAvailabilityParameters
from openapi_server.models.check_name_availability_result_resource import CheckNameAvailabilityResultResource
from openapi_server import util


async def recovery_services_check_name_availability(request: web.Request, subscription_id, resource_group_name, api_version, location, input) -> web.Response:
    """API to check for resource name availability.  A name is available if no other resource exists that has the same SubscriptionId, Resource Name and Type  or if one or more such resources exist, each of these must be GC&#39;d and their time of deletion be more than 24 Hours Ago

    

    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param location: Location of the resource
    :type location: str
    :param input: Contains information about Resource type and Resource name
    :type input: dict | bytes

    """
    input = CheckNameAvailabilityParameters.from_dict(input)
    return web.Response(status=200)
