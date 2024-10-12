from typing import List, Dict
from aiohttp import web

from openapi_server.models.containers_quota_info import ContainersQuotaInfo
from openapi_server.models.containers_quota_list import ContainersQuotaList
from openapi_server.models.containers_usage_info import ContainersUsageInfo
from openapi_server import util


async def containers_quota_get(request: web.Request, x_auth_token, x_auth_project_id) -> web.Response:
    """Retrieve organization and space specific quota

    Retrieve the quota that is assigned to the organization and space.

    :param x_auth_token: The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token.
    :type x_auth_token: str
    :param x_auth_project_id: The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID.
    :type x_auth_project_id: str

    """
    return web.Response(status=200)


async def containers_quota_put(request: web.Request, x_auth_token, x_auth_project_id, body) -> web.Response:
    """Update space quota

    This endpoint updates the quota that is allocated to a Bluemix space.    **Note**: Only paid accounts are eligbile to update the space quota. If you are using a free-trial account, upgrade to a paid account first.

    :param x_auth_token: The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token.
    :type x_auth_token: str
    :param x_auth_project_id: The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID.
    :type x_auth_project_id: str
    :param body: The space quota details that you want to update.
    :type body: dict | bytes

    """
    body = ContainersQuotaList.from_dict(body)
    return web.Response(status=200)


async def containers_usage_get(request: web.Request, x_auth_token, x_auth_project_id) -> web.Response:
    """List container sizes and quota limits

    This endpoint returns a list of available container sizes and the quota limit and usage for the space.   - Container sizes: A list of available container sizes indicating the amount of container memory, disk space and virtual CPUs that can be assigned to the container. - Quota limit: Lists the number of containers, public IP addresses, available container memory, and virtual CPUS that are allocated to a space.  - Quota usage: Lists the current number of containers, images, and public IP addresses in a space that is counted towards your quota limit. 

    :param x_auth_token: The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token.
    :type x_auth_token: str
    :param x_auth_project_id: The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID.
    :type x_auth_project_id: str

    """
    return web.Response(status=200)
