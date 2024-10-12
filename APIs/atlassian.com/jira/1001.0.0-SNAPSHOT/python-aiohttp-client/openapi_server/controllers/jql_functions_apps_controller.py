from typing import List, Dict
from aiohttp import web

from openapi_server.models.jql_function_precomputation_update_request_bean import JqlFunctionPrecomputationUpdateRequestBean
from openapi_server.models.page_bean_jql_function_precomputation_bean import PageBeanJqlFunctionPrecomputationBean
from openapi_server import util


async def get_precomputations(request: web.Request, function_key=None, start_at=None, max_results=None, order_by=None, filter=None) -> web.Response:
    """Get precomputations (apps)

    Returns the list of a function&#39;s precomputations along with information about when they were created, updated, and last used. Each precomputation has a &#x60;value&#x60; \\- the JQL fragment to replace the custom function clause with.  **[Permissions](#permissions) required:** This API is only accessible to apps and apps can only inspect their own functions.

    :param function_key: The function key in format:   *  Forge: &#x60;ari:cloud:ecosystem::extension/[App ID]/[Environment ID]/static/[Function key from manifest]&#x60;.  *  Connect: &#x60;[App key]__[Module key]&#x60;.
    :type function_key: List[str]
    :param start_at: The index of the first item to return in a page of results (page offset).
    :type start_at: int
    :param max_results: The maximum number of items to return per page.
    :type max_results: int
    :param order_by: Not supported yet.
    :type order_by: str
    :param filter: Not supported yet.
    :type filter: str

    """
    return web.Response(status=200)


async def update_precomputations(request: web.Request, body) -> web.Response:
    """Update precomputations (apps)

    Update the precomputation value of a function created by a Forge/Connect app.  **[Permissions](#permissions) required:** An API for apps to update their own precomputations.

    :param body: 
    :type body: dict | bytes

    """
    body = JqlFunctionPrecomputationUpdateRequestBean.from_dict(body)
    return web.Response(status=200)
