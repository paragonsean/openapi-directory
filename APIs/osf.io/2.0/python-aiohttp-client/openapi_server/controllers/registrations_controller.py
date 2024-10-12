from typing import List, Dict
from aiohttp import web

from openapi_server.models.citation_detail import CitationDetail
from openapi_server.models.citation_style import CitationStyle
from openapi_server.models.comment import Comment
from openapi_server.models.contributor import Contributor
from openapi_server.models.file import File
from openapi_server.models.identifier import Identifier
from openapi_server.models.institution import Institution
from openapi_server.models.log import Log
from openapi_server.models.node import Node
from openapi_server.models.registration import Registration
from openapi_server.models.view_only_links import ViewOnlyLinks
from openapi_server.models.wiki import Wiki
from openapi_server import util


async def registrations_children_list(request: web.Request, registration_id) -> web.Response:
    """List all child registrations

     A paginated list of children of a registration.  The list consists of the next level child registrations for the given registration. The returned registrations are sorted by their &#x60;date_modified&#x60;, with the most recently updated child registrations appearing first.  The list will include child registrations that are public, as well as child registrations that are private, if the authenticated user has permission to view them. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of up to 10 child registrations. If the given registration has zero child registrations, the &#x60;data&#x60; key will contain an empty array. Each resource in the array is a separate registration object and contains the full representation of the child registration.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  #### Filtering You can optionally request that the response only include registrations that match your filters by utilizing the &#x60;filter&#x60; query parameter, e.g. https://api.osf.io/v2/registrations/wucr8/children/?filter[title]&#x3D;reproducibility.  Registrations may be filtered by their &#x60;id&#x60;, &#x60;title&#x60;, &#x60;category&#x60;, &#x60;description&#x60;, &#x60;public&#x60;, &#x60;tags&#x60;, &#x60;date_created&#x60;, &#x60;date_modified&#x60;, &#x60;root&#x60;, &#x60;parent&#x60;, and &#x60;contributors&#x60;.  Most fields are string fields and will be filtered using simple substring matching. Public is a boolean field, and can be filtered using truthy values, such as **true**, **false**, **0** or **1**. Note that quoting true or false in the query will cause the match to fail.

    :param registration_id: The unique identifier of the registration.
    :type registration_id: str

    """
    return web.Response(status=200)


async def registrations_citation_read(request: web.Request, registration_id, citation_id) -> web.Response:
    """Retrieve a citation

    Retrieves the citation style details for a registration, in CSL format. #### Returns Returns a JSON object with a &#x60;data&#x60; key that contains the representation of the details necessary for the citation style.

    :param registration_id: The unique identifier of the registration.
    :type registration_id: str
    :param citation_id: The unique identifier of the citation.
    :type citation_id: str

    """
    return web.Response(status=200)


async def registrations_citations_list(request: web.Request, registration_id) -> web.Response:
    """List all citation styles

     A paginated list of the registration&#39;s alternative citation styles  #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of up to 10 citation styles. Each resource in the array is a separate citation styles object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Filtering You can optionally request that the response only include citation styles that match your filters by utilizing the &#x60;filter&#x60; query parameter, e.g. https://api.osf.io/v2/registrations/wucr8/citations/?filter[title]&#x3D;open.  Citation styles may be filtered by their &#x60;id&#x60;, &#x60;title&#x60;, &#x60;short-title&#x60;, and &#x60;summary&#x60;.

    :param registration_id: The unique identifier of the registration.
    :type registration_id: str

    """
    return web.Response(status=200)


async def registrations_comments_list(request: web.Request, registration_id) -> web.Response:
    """List all comments

     A paginated list of the registration&#39;s comments.  The returned comments are sorted by their creation date, with the most recent comments appearing first. #### Permissions Comments of public registrations are given read-only access to everyone.  If the comment-level is &#x60;private&#x60;, only registration contributors have permission to comment.  If the comment-level is &#x60;public&#x60;, any logged-in OSF user can comment.  Comments of private registrations are only visible to contributors and administrators on the registration. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of comment objects. Each resource in the array is a separate comment object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Filtering You can optionally request that the response only include comments that match your filters by utilizing the &#x60;filter&#x60; query parameter, e.g. https://api.osf.io/v2/registrations/wuerf/comments/?filter[target]&#x3D;wuerf  Comments may be filtered by their &#x60;deleted&#x60;, &#x60;target&#x60;, &#x60;date_created&#x60;, &#x60;date_modified&#x60;.  Most fields are string fields and will be filtered using simple substring matching. Deleted is a boolean field, and can be filtered using truthy values, such as **true**, **false**, **0** or **1**. Note that quoting &#x60;true&#x60; or &#x60;false&#x60; in the query will cause the match to fail.

    :param registration_id: The unique identifier of the registration.
    :type registration_id: str

    """
    return web.Response(status=200)


async def registrations_contributors_list(request: web.Request, registration_id) -> web.Response:
    """List all contributors

    A paginated list of all contributors on this registration. The returned contributors are sorted by their index.  Contributors are users who can make changes to the registration or, in the case of private registration, have read access to the registration.  Contributors are categorized as either \&quot;bibliographic\&quot; or \&quot;non-bibliographic\&quot;. From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed in the contributors list on the OSF, while non-bibliographic contributors are not.  Note that if an anonymous view_only key is being used to view the list of contributors, the user relationship will not be exposed and the contributor ID will be an empty string.  #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of up to 10 contributors. Each resource in the array contains the full representation of the contributor. Additionally, the full representation of the user this contributor represents is automatically embedded within the &#x60;data&#x60; key of the response.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Filtering You can optionally request that the response only include contributors that match your filters by utilizing the &#x60;filter&#x60; query parameter, e.g. https://api.osf.io/v2/registrations/wu3a4/contributors/?filter[bibliographic]&#x3D;true.  Contributors may be filtered by their &#x60;bibliographic&#x60; and &#x60;permission&#x60; attributes.

    :param registration_id: The unique identifier of the registration.
    :type registration_id: str

    """
    return web.Response(status=200)


async def registrations_contributors_read(request: web.Request, registration_id, user_id) -> web.Response:
    """Retrieve a contributor

    Retrieves the details of a contributor on this registration.  #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested contributor, if the request is successful.  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

    :param registration_id: The unique identifier of the registration.
    :type registration_id: str
    :param user_id: The unique identifier of the user.
    :type user_id: str

    """
    return web.Response(status=200)


async def registrations_files_list(request: web.Request, registration_id, provider) -> web.Response:
    """List all files

    List of all the registration&#39;s files/folders for a given storage provider.  #### Returns  Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of files. Each resource in the array is a separate file object and contains the full representation of the file.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  #### Filtering  You can optionally request that the response only include files that match your filters by utilizing the &#x60;filter&#x60; query parameter, e.g. https://api.osf.io/v2/registrations/wucr8/files/osfstorage/?filter[kind]&#x3D;file  Files may be filtered by &#x60;id&#x60;, &#x60;name&#x60;, &#x60;node&#x60;, &#x60;kind&#x60;, &#x60;path&#x60;, &#x60;provider&#x60;, &#x60;size&#x60;, and &#x60;last_touched&#x60;.

    :param registration_id: The unique identifier of the registration.
    :type registration_id: str
    :param provider: The unique identifier of the storage provider.
    :type provider: str

    """
    return web.Response(status=200)


async def registrations_files_read(request: web.Request, registration_id, provider, path) -> web.Response:
    """Retrieve a file

    Retrieves the details of a registration file for the given storage provider. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested registration file object, if the request is successful.  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

    :param registration_id: The unique identifier of the registration.
    :type registration_id: str
    :param provider: The unique identifier of the storage provider.
    :type provider: str
    :param path: The unique identifier of the file path.
    :type path: str

    """
    return web.Response(status=200)


async def registrations_forks_create(request: web.Request, registration_id, body) -> web.Response:
    """Create a fork

    Creates a fork of the given registration.  Forking a project creates a copy of an existing registration and all of its contents. The fork always points back to the original registration, forming a network of registrations.  You might use a fork to copy another&#39;s work to build on and extend. For example, a professor may create an OSF project of materials for individual student use. Each student forks the project to have his or her own copy of the materials to start his/her own work.  When creating a fork, your fork will only contain public components of the current registration and components for which you are a contributor. Private components that you do not have access to will not be forked. #### Required There are no required attributes when creating a fork, as all of the forked registration&#39;s attributes will be copied from the current registration.  The &#x60;title&#x60; field is optional, with the default title being \&quot;Fork of \&quot; prepended to the current registration&#39;s title. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the complete representation of the forked registration, if the request is successful. If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

    :param registration_id: The unique identifier of the registration.
    :type registration_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Registration.from_dict(body)
    return web.Response(status=200)


async def registrations_forks_list(request: web.Request, registration_id) -> web.Response:
    """List all forks

     A paginated list of the registration’s forks  The returned forks are sorted by their &#x60;forked_date&#x60;, with the most recent forks appearing first.  Forking a registration creates a copy of an existing registration and all of its contents. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of up to 10 forks. If the current registration has no fork, the &#x60;data&#x60; key will contain an empty array. Each resource in the array is a separate registration object and contains the full representation of the registration&#39;s fork.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

    :param registration_id: The unique identifier of the registration.
    :type registration_id: str

    """
    return web.Response(status=200)


async def registrations_identifiers_list(request: web.Request, registration_id) -> web.Response:
    """List all identifiers

    A paginated list of the registration&#39;s identifiers. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of identifiers. Each resource in the array is a separate identifier object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Filtering  You can optionally request that the response only include registrations that match your filters by utilizing the &#x60;filter&#x60; query parameter, e.g. https://api.osf.io/v2/registrations/wucr8/identifiers/?filter[category]&#x3D;ark  Identifiers may be filtered by their &#x60;category&#x60; e.g &#x60;ark&#x60; or &#x60;doi&#x60;.

    :param registration_id: The unique identifier of the registration.
    :type registration_id: str

    """
    return web.Response(status=200)


async def registrations_institutions_list(request: web.Request, registration_id) -> web.Response:
    """List all institutions

    A paginated list of institutions affiliated with the registration. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of up to 10 affiliated institutions. Each resource in the array is a separate institution object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

    :param registration_id: The unique identifier of the registration.
    :type registration_id: str

    """
    return web.Response(status=200)


async def registrations_linked_nodes_list(request: web.Request, registration_id) -> web.Response:
    """List all linked nodes

    List of all nodes linked to the registration. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of up to 10 nodes. Each resource in the array is a separate node object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Filtering You can optionally request that the response only include nodes that match your filters by utilizing the &#x60;filter&#x60; query parameter, e.g. https://api.osf.io/v2/registrations/wucr8/linked_nodes/?filter[title]&#x3D;reproducibility/?filter[title]&#x3D;reproducibility.  Nodes may be filtered by their &#x60;title&#x60;, &#x60;category&#x60;, &#x60;description&#x60;, &#x60;public&#x60;, &#x60;registration&#x60;, or &#x60;tags&#x60;. &#x60;title&#x60;, &#x60;description&#x60;, and &#x60;category&#x60; are string fields and will be filteres using simple substring matching. &#x60;public&#x60;, &#x60;registration&#x60; are boolean and can be filtered using truthy values, such as &#x60;true&#x60;, &#x60;false&#x60;, &#x60;0&#x60;, &#x60;1&#x60;. &#x60;tags&#x60; is an array of simple strings.

    :param registration_id: The unique identifier of the registration.
    :type registration_id: str

    """
    return web.Response(status=200)


async def registrations_list(request: web.Request, ) -> web.Response:
    """List all registrations

    A paginated list of registrations on the OSF to which the user has access.  The returned registrations are those which are public or which the user has access to view.  Non-registered nodes cannot be accessed through this endpoint (use the [nodes](#Nodes_nodes_list) endpoints instead).  #### Registrations A registration on the OSF creates a frozen, time-stamped version of a project that cannot be edited or deleted. The *original project* can still be edited, while the registered version cannot.  Registrations can be made public immediately or embargoed for up to 4 years.  #### Withdrawals Registrations cannot be deleted, but they can be withdrawn. Withdrawing a registration removes the content of the registration but leaves behind basic metadata. A withdrawn registration will display a limited subset of information, namely, title, description, date_created, date_registered, date_withdrawn, registration, withdrawn, withdrawal_justification, and registration supplement. All other fields will be displayed as null. Additionally, the only relationship that remains accesible for a withdrawn registration is the contributors. All other relationships will return a **403 Forbidden** response. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of 10 registrations. Each resource in the array is a separate registration object and contains the full representation of the registration, meaning additional requests to a registration&#39;s detail view are not necessary.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  This request should never return an error. #### Filtering You can optionally request that the response only include registrations that match your filters by utilizing the &#x60;filter&#x60; query parameter, e.g. https://api.osf.io/v2/registrations/?filter[title]&#x3D;open.  Registrations may be filtered by their &#x60;id&#x60;, &#x60;title&#x60;, &#x60;category&#x60;, &#x60;description&#x60;, &#x60;public&#x60;, &#x60;tags&#x60;, &#x60;date_created&#x60;, &#x60;date_modified&#x60;, &#x60;root&#x60;, &#x60;parent&#x60;, and &#x60;contributors&#x60;.


    """
    return web.Response(status=200)


async def registrations_logs_list(request: web.Request, registration_id) -> web.Response:
    """List all logs

    A paginated list of the registration&#39;s logs.  The returned logs are sorted by their &#x60;date&#x60;, with the most recents logs appearing first.  #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of up to 10 logs. Each resource in the array is a separate logs object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Filtering You can optionally request that the response only include logs that match your filters by utilizing the &#x60;filter&#x60; query parameter, e.g. https://api.osf.io/v2/registrations/wucr8/logs/?filter[action]&#x3D;made_private.  Logs may be filtered by their &#x60;action&#x60;, and &#x60;date&#x60;.

    :param registration_id: The unique identifier of the registration.
    :type registration_id: str

    """
    return web.Response(status=200)


async def registrations_partial_update(request: web.Request, registration_id, body) -> web.Response:
    """Update a registration

    Updates a registration&#39;s privacy from **private** to **public**.  Registrations can be updated with either a **PUT** or **PATCH** request. The &#x60;public&#x60; field is the only field that can be modified on a registration  Registrations can only be turned from private to public, not vice versa. #### Permissions Only project administrators may update a registration. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the new representation of the updated registration, if the request is successful.  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

    :param registration_id: The unique identifier of the registration.
    :type registration_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Registration.from_dict(body)
    return web.Response(status=200)


async def registrations_providers_list(request: web.Request, registration_id) -> web.Response:
    """List all storage providers

    A paginated list of storage providers enabled on the registration  Users of the OSF may access their data on a [number of cloud-storage services](https://api.osf.io/v2/#storage-providers) that have integrations with the OSF. We call these **providers**. By default, every node has access to the OSF-provided storage but may use as many of the supported providers as desired.   #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of up to 10 files. Each resource in the array is a separate file object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  Note: In the OSF filesystem model, providers are treated as folders, but with special properties that distinguish them from regular folders. Every provider folder is considered a root folder, and may not be deleted through the regular file API.

    :param registration_id: The unique identifier of the registration.
    :type registration_id: str

    """
    return web.Response(status=200)


async def registrations_read(request: web.Request, registration_id) -> web.Response:
    """Retrieve a registration

    Retrieve the details of a given registration. #### Permissions Only project contributors may retrieve the details of a registration that is embargoed, or has not yet been made public. Attempting to retrieve a private registration for which you are not a contributor will result in a **403 Forbidden** response.  Authentication is not required to view the details of a public registration, as public registrations give read-only access to everyone. #### Registrations A registration on the OSF creates a frozen, time-stamped version of a project that cannot be edited or deleted. The *original project* can still be edited, while the registered version cannot.  Registrations can be made public immediately or embargoed for up to 4 years.  #### Withdrawals Registrations cannot be deleted, but they can be withdrawn. Withdrawing a registration removes the content of the registration but leaves behind basic metadata. A withdrawn registration will display a limited subset of information, namely, title, description, date_created, date_registered, date_withdrawn, registration, withdrawn, withdrawal_justification, and registration supplement. All other fields will be displayed as null. Additionally, the only relationship that remains accesible for a withdrawn registration is the contributors. All other relationships will return a **403 Forbidden** response. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested registration, if the request is successful.  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

    :param registration_id: The unique identifier of the registration.
    :type registration_id: str

    """
    return web.Response(status=200)


async def registrations_view_only_links_list(request: web.Request, registration_id) -> web.Response:
    """List all view only links

    A paginated list of view only links created for this registration. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of up to 10 view only links. Each resource in the array is a view only link object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  #### Permissions  View only links on a registration, public or private, are readable and writeable only by users that are administrators on the registration.  #### Filtering  You can optionally request that the response only include view only links that match your filters by utilizing the &#x60;filter&#x60; query parameter, e.g. https://api.osf.io/v2/registrations/wu3a4/view_only_links/?filter[anonymous]&#x3D;true.  View Only Links may be filtered based on their &#x60;name&#x60;, &#x60;anonymous&#x60; and &#x60;date_created&#x60; fields. Possible comparison operators include &#39;gt&#39; (greater than), &#39;gte&#39;(greater than or equal to), &#39;lt&#39; (less than) and &#39;lte&#39; (less than or equal to). The date must be in the format YYYY-MM-DD and the time is optional.

    :param registration_id: The unique identifier of the registration.
    :type registration_id: str

    """
    return web.Response(status=200)


async def registrations_view_only_links_read(request: web.Request, registration_id, link_id) -> web.Response:
    """Retrieve a view only link

    Retrieves the details of a view only link created from this registration. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested view only link, if the request is successful.  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed. #### Permissions  View only links on a registration, public or private, are readable and writeable only by users that are administrators on the registration.

    :param registration_id: The unique identifier of the registration.
    :type registration_id: str
    :param link_id: The unique identifier of the view only link.
    :type link_id: str

    """
    return web.Response(status=200)


async def registrations_wikis_list(request: web.Request, registration_id) -> web.Response:
    """List all wikis

    A paginated list of the registration&#39;s wiki pages #### Returns A list of all registration&#39;s current wiki page versions ordered by their date_modified. Each resource contains the full representation of the wiki, meaning additional requests to an individual wiki&#39;s detail view are not necessary.  If the request is unsuccessful, a JSON object with an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed. #### Filtering Wiki pages can be filtered based on their &#x60;name&#x60; and &#x60;date_modified&#x60; fields. + &#x60;filter[name]&#x3D;&lt;Str&gt;&#x60; -- filter wiki pages by name + &#x60;filter[date_modified][comparison_operator]&#x3D;YYYY-MM-DDTH:M:S&#x60; -- filter wiki pages based on date modified.  Possible comparison operators include &#39;gt&#39; (greater than), &#39;gte&#39;(greater than or equal to), &#39;lt&#39; (less than) and &#39;lte&#39; (less than or equal to). The date must be in the format YYYY-MM-DD and the time is optional.

    :param registration_id: The unique identifier of the registration.
    :type registration_id: str

    """
    return web.Response(status=200)
