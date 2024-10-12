from typing import List, Dict
from aiohttp import web

from openapi_server.models.institution import Institution
from openapi_server.models.node import Node
from openapi_server.models.user import User
from openapi_server import util


async def institutions_detail(request: web.Request, institution_id) -> web.Response:
    """Retrieve an institution

    Retrieves the details of an institution #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested institution, if the request was successful.  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

    :param institution_id: The unique identifier of the institution you wish to retrieve.
    :type institution_id: str

    """
    return web.Response(status=200)


async def institutions_list(request: web.Request, ) -> web.Response:
    """List all institutions

     A paginated list of all verified institutions. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of 10 institutions. Each resource in the array is a separate institution object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  This request should never return an error. #### Filtering You can optionally request that the response only include institutions that match your filters by utilizing the &#x60;filter&#x60; query parameter, e.g. https://api.osf.io/v2/institutions/?filter[id]&#x3D;cos.  Institutions may be filtered by their &#x60;id&#x60;, &#x60;name&#x60;, and &#x60;auth_url&#x60;


    """
    return web.Response(status=200)


async def institutions_node_list(request: web.Request, institution_id) -> web.Response:
    """List all affiliated nodes

    A paginated list of all nodes affiliated with an institution. #### Versioning As of version &#x60;2.2&#x60;, affiliated components (in addition to affiliated top-level projects) are returned from this endpoint. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of 10 nodes. Each resource in the array is a separate nodes object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed. #### Filtering You can optionally request that the response only include nodes that match your filters by utilizing the &#x60;filter&#x60; query parameter, e.g. https://api.osf.io/v2/institutions/cos/nodes?filter[title]&#x3D;science.  Nodes may be filtered by their &#x60;id&#x60;, &#x60;title&#x60;, &#x60;description&#x60;, &#x60;public&#x60;, &#x60;tags&#x60;, &#x60;category&#x60;, &#x60;date_created&#x60;, &#x60;date_modified&#x60;, &#x60;root&#x60;, &#x60;parent&#x60;, &#x60;contributors&#x60;, and &#x60;preprint&#x60;

    :param institution_id: The unique identifier of the institution you wish to retrieve.
    :type institution_id: str

    """
    return web.Response(status=200)


async def institutions_registration_list(request: web.Request, institution_id) -> web.Response:
    """List all affiliated registrations

    A paginated list of all registrations affiliated with an institution. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of 10 registrations. Each resource in the array is a separate users object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed. #### Filtering You can optionally request that the response only include registrations that match your filters by utilizing the &#x60;filter&#x60; query parameter, e.g. https://api.osf.io/v2/institutions/cos/registrations?filter[title]&#x3D;science.  Registrations may be filtered by their  &#x60;id&#x60;, &#x60;title&#x60;, &#x60;description&#x60;, &#x60;public&#x60;, &#x60;tags&#x60;, &#x60;category&#x60;, &#x60;date_created&#x60;, &#x60;date_modified&#x60;, &#x60;root&#x60;, &#x60;parent&#x60;, &#x60;contributors&#x60;, and &#x60;preprint&#x60;

    :param institution_id: The unique identifier of the institution you wish to retrieve.
    :type institution_id: str

    """
    return web.Response(status=200)


async def institutions_users_list(request: web.Request, institution_id) -> web.Response:
    """List all affiliated users

    A paginated list of all users affiliated with an institution. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of 10 users. Each resource in the array is a separate users object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed. #### Filtering You can optionally request that the response only include users that match your filters by utilizing the &#x60;filter&#x60; query parameter, e.g. https://api.osf.io/v2/institutions/cos/users?filter[family_name]&#x3D;Nosek.  Users may be filtered by their &#x60;id&#x60;, &#x60;full_name&#x60;, &#x60;given_name&#x60;, &#x60;middle_names&#x60;, and &#x60;family_name&#x60;

    :param institution_id: The unique identifier of the institution you wish to retrieve.
    :type institution_id: str

    """
    return web.Response(status=200)
