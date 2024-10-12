from typing import List, Dict
from aiohttp import web

from openapi_server.models.agent_pool import AgentPool
from openapi_server.models.list_agent_pools_response import ListAgentPoolsResponse
from openapi_server import util


async def storagetransfer_projects_agent_pools_create(request: web.Request, project_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, agent_pool_id=None, body=None) -> web.Response:
    """storagetransfer_projects_agent_pools_create

    Creates an agent pool resource.

    :param project_id: Required. The ID of the Google Cloud project that owns the agent pool.
    :type project_id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param agent_pool_id: Required. The ID of the agent pool to create. The &#x60;agent_pool_id&#x60; must meet the following requirements: * Length of 128 characters or less. * Not start with the string &#x60;goog&#x60;. * Start with a lowercase ASCII character, followed by: * Zero or more: lowercase Latin alphabet characters, numerals, hyphens (&#x60;-&#x60;), periods (&#x60;.&#x60;), underscores (&#x60;_&#x60;), or tildes (&#x60;~&#x60;). * One or more numerals or lowercase ASCII characters. As expressed by the regular expression: &#x60;^(?!goog)[a-z]([a-z0-9-._~]*[a-z0-9])?$&#x60;.
    :type agent_pool_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = AgentPool.from_dict(body)
    return web.Response(status=200)


async def storagetransfer_projects_agent_pools_delete(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """storagetransfer_projects_agent_pools_delete

    Deletes an agent pool.

    :param name: Required. The name of the agent pool to delete.
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str

    """
    return web.Response(status=200)


async def storagetransfer_projects_agent_pools_list(request: web.Request, project_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """storagetransfer_projects_agent_pools_list

    Lists agent pools.

    :param project_id: Required. The ID of the Google Cloud project that owns the job.
    :type project_id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: An optional list of query parameters specified as JSON text in the form of: &#x60;{\&quot;agentPoolNames\&quot;:[\&quot;agentpool1\&quot;,\&quot;agentpool2\&quot;,...]}&#x60; Since &#x60;agentPoolNames&#x60; support multiple values, its values must be specified with array notation. When the filter is either empty or not provided, the list returns all agent pools for the project.
    :type filter: str
    :param page_size: The list page size. The max allowed value is &#x60;256&#x60;.
    :type page_size: int
    :param page_token: The list page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def storagetransfer_projects_agent_pools_patch(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, update_mask=None, body=None) -> web.Response:
    """storagetransfer_projects_agent_pools_patch

    Updates an existing agent pool resource.

    :param name: Required. Specifies a unique string that identifies the agent pool. Format: &#x60;projects/{project_id}/agentPools/{agent_pool_id}&#x60;
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param update_mask: The [field mask] (https://developers.google.com/protocol-buffers/docs/reference/google.protobuf) of the fields in &#x60;agentPool&#x60; to update in this request. The following &#x60;agentPool&#x60; fields can be updated: * display_name * bandwidth_limit
    :type update_mask: str
    :param body: 
    :type body: dict | bytes

    """
    body = AgentPool.from_dict(body)
    return web.Response(status=200)
