from typing import List, Dict
from aiohttp import web

from openapi_server.models.citation_detail import CitationDetail
from openapi_server.models.contributor1 import Contributor1
from openapi_server.models.preprint import Preprint
from openapi_server.models.styled_citation import StyledCitation
from openapi_server import util


async def preprints_bibliographic_contributors_list(request: web.Request, preprint_id) -> web.Response:
    """List all Bibliographic Contributors

    A paginated list of the Preprint&#39;s Bibliographic Contributors, sorted by their index. Contributors are users who can make changes to the Preprint. Contributors with WRITE permissions may edit preprint details, and ADMIN Contributors may add or remove other Contributors.  Contributors are categorized as either \&quot;bibliographic\&quot; or \&quot;non-bibliographic\&quot;. From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.  Note that if an anonymous view_only key is being used to view the list of contributors, the user relationship will not be exposed and the contributor ID will be an empty string.  #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of 10 contributors. Each resource in the array contains the full representation of the contributor, meaning additional requests to a contributor&#39;s detail view are not necessary. Additionally, the full representation of the user this contributor represents is automatically embedded within the &#x60;data&#x60; key of the response.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Filtering You can optionally request that the response only include contributors that match your filters by utilizing the &#x60;filter&#x60; query parameter, e.g. https://api.osf.io/v2/preprints/y9jdt/contributors/?filter[bibliographic]&#x3D;true.  Contributors may be filtered by their &#x60;bibliographic&#x60; and &#x60;permission&#x60; attributes.

    :param preprint_id: The unique identifier of the preprint.
    :type preprint_id: str

    """
    return web.Response(status=200)


async def preprints_citation_list(request: web.Request, preprint_id) -> web.Response:
    """Retrieve citation details

    The citation details for a preprint, in CSL format. #### Returns Returns a JSON object with a &#x60;data&#x60; key that contains the representation of the details necessary for the preprint citation.

    :param preprint_id: The unique identifier of the preprint whose citation you wish to retrieve.
    :type preprint_id: str

    """
    return web.Response(status=200)


async def preprints_citation_read(request: web.Request, style_id, preprint_id) -> web.Response:
    """Retrieve a styled citation

    The citation for a preprint in a specific style. #### Returns Returns a JSON object with a &#x60;data&#x60; key that contains the representation of the preprint citation, in the requested style.

    :param style_id: The unique identifier of the citation style.
    :type style_id: str
    :param preprint_id: The unique identifier of the preprint.
    :type preprint_id: str

    """
    return web.Response(status=200)


async def preprints_contributor_read(request: web.Request, preprint_id, user_id) -> web.Response:
    """Retrieve a contributor

    Retrieves the details of a contributor on this Preprint. Contributors are categorized as either \&quot;bibliographic\&quot; or \&quot;non-bibliographic\&quot;. From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.  Note that if an anonymous view_only key is being used to view the list of contributors, the user relationship will not be exposed and the contributor ID will be an empty string. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested contributor, if the request is successful.  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

    :param preprint_id: The unique identifier of the Preprint.
    :type preprint_id: str
    :param user_id: The unique identifier of the user.
    :type user_id: str

    """
    return web.Response(status=200)


async def preprints_contributors_create(request: web.Request, preprint_id, body) -> web.Response:
    """Create a Contributor

    Adds a contributor to a Preprint, effectively creating a relationship between the Preprint and a user.  Contributors are users who can make changes to the Preprint. Contributors with WRITE permissions may edit preprint details, and ADMIN Contributors may add or remove other Contributors.  Contributors are categorized as either \&quot;bibliographic\&quot; or \&quot;non-bibliographic\&quot; contributors. From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not. #### Permissions Only project administrators can add contributors to a Preprint. #### Required A relationship object with a &#x60;data&#x60; key, containing the &#x60;users&#x60; type and valid user ID is required.  All attributes describing the relationship between the Preprint and the user are optional. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the new contributor, if the request is successful.  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

    :param preprint_id: The unique identifier of the Preprint.
    :type preprint_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Contributor1.from_dict(body)
    return web.Response(status=200)


async def preprints_contributors_list(request: web.Request, preprint_id) -> web.Response:
    """List all Contributors for a Preprint

    A paginated list of the Preprint&#39;s Contributors, sorted by their index.  Contributors are users who can make changes to the Preprint. Contributors with WRITE permissions may edit preprint details, and ADMIN Contributors may add or remove other Contributors.  Contributors are categorized as either \&quot;bibliographic\&quot; or \&quot;non-bibliographic\&quot;. From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.  Note that if an anonymous view_only key is being used to view the list of Contributors, the user relationship will not be exposed and the Contributor ID will be an empty string.  #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of 10 contributors. Each resource in the array contains the full representation of the contributor, meaning additional requests to a contributor&#39;s detail view are not necessary. Additionally, the full representation of the user this contributor represents is automatically embedded within the &#x60;data&#x60; key of the response.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Filtering You can optionally request that the response only include contributors that match your filters by utilizing the &#x60;filter&#x60; query parameter, e.g. https://api.osf.io/v2/preprints/y9jdt/contributors/?filter[bibliographic]&#x3D;true.  Contributors may be filtered by their &#x60;bibliographic&#x60; and &#x60;permission&#x60; attributes.

    :param preprint_id: The unique identifier of the preprint.
    :type preprint_id: str

    """
    return web.Response(status=200)


async def preprints_create(request: web.Request, body) -> web.Response:
    """Create a preprint

    Creates a new preprint. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the created preprint, if the request is successful.  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes]() to understand why this request may have failed.

    :param body: 
    :type body: dict | bytes

    """
    body = Preprint.from_dict(body)
    return web.Response(status=200)


async def preprints_list(request: web.Request, ) -> web.Response:
    """List all preprints

     A paginated list of preprints from all preprint providers. The returned preprints are sorted by their creation date, with the most recent preprints appearing first. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of 10 preprints. Each resource in the array is a separate preprint object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  This request should never return an error. #### Filtering You can optionally request that the response only include preprints that match your filters by utilizing the &#x60;filter&#x60; query parameter, e.g. https://api.osf.io/v2/preprints/?filter[provider]&#x3D;socarxiv.  Preprints may be filtered by their &#x60;id&#x60;, &#x60;is_published&#x60;, &#x60;date_created&#x60;, &#x60;date_modified&#x60;, and &#x60;provider&#x60;.


    """
    return web.Response(status=200)


async def preprints_partial_update(request: web.Request, preprint_id, body) -> web.Response:
    """Update a preprint

    Updates the specified preprint by setting the values of the parameters passed. Any parameters not provided will be left unchanged. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the new representation of the updated preprint, if the request is successful.  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes]() to understand why this request may have failed.

    :param preprint_id: The unique identifier of the preprint.
    :type preprint_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def preprints_read(request: web.Request, preprint_id) -> web.Response:
    """Retrieve a preprint

    Retrieves the details of a preprint. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested preprint, if the request is successful.  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

    :param preprint_id: The unique identifier of the preprint.
    :type preprint_id: str

    """
    return web.Response(status=200)
