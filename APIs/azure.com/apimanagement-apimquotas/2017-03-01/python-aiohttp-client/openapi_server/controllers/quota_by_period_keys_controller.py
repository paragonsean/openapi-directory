from typing import List, Dict
from aiohttp import web

from openapi_server.models.quota_by_counter_keys_list_default_response import QuotaByCounterKeysListDefaultResponse
from openapi_server.models.quota_counter_contract import QuotaCounterContract
from openapi_server.models.quota_counter_value_contract_properties import QuotaCounterValueContractProperties
from openapi_server import util


async def quota_by_period_keys_get(request: web.Request, quota_counter_key, quota_period_key, api_version) -> web.Response:
    """quota_by_period_keys_get

    Gets the value of the quota counter associated with the counter-key in the policy for the specific period in service instance.

    :param quota_counter_key: Quota counter key identifier.This is the result of expression defined in counter-key attribute of the quota-by-key policy.For Example, if you specify counter-key&#x3D;\&quot;boo\&quot; in the policy, then it’s accessible by \&quot;boo\&quot; counter key. But if it’s defined as counter-key&#x3D;\&quot;@(\&quot;b\&quot;+\&quot;a\&quot;)\&quot; then it will be accessible by \&quot;ba\&quot; key
    :type quota_counter_key: str
    :param quota_period_key: Quota period key identifier.
    :type quota_period_key: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def quota_by_period_keys_update(request: web.Request, quota_counter_key, quota_period_key, api_version, parameters) -> web.Response:
    """quota_by_period_keys_update

    Updates an existing quota counter value in the specified service instance.

    :param quota_counter_key: Quota counter key identifier.This is the result of expression defined in counter-key attribute of the quota-by-key policy.For Example, if you specify counter-key&#x3D;\&quot;boo\&quot; in the policy, then it’s accessible by \&quot;boo\&quot; counter key. But if it’s defined as counter-key&#x3D;\&quot;@(\&quot;b\&quot;+\&quot;a\&quot;)\&quot; then it will be accessible by \&quot;ba\&quot; key
    :type quota_counter_key: str
    :param quota_period_key: Quota period key identifier.
    :type quota_period_key: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param parameters: The value of the Quota counter to be applied on the specified period.
    :type parameters: dict | bytes

    """
    parameters = QuotaCounterValueContractProperties.from_dict(parameters)
    return web.Response(status=200)
