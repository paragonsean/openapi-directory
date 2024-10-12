from typing import List, Dict
from aiohttp import web

from openapi_server.models.contributor import Contributor
from openapi_server.models.draft_registration import DraftRegistration
from openapi_server.models.institution import Institution
from openapi_server.models.subject import Subject
from openapi_server import util


async def draft_registration_contributors_create(request: web.Request, draft_id, body) -> web.Response:
    """Add a contributor to a Draft Registration

    Adds a contributor to a Draft Registration, contributors can view, edit, register or delete a Draft Registration depending on their permissions. Contributors are categorized as either \&quot;bibliographic\&quot; or \&quot;non-bibliographic\&quot; contributors. From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not. #### Permissions Only project administrators can add contributors to a Draft Registration. #### Required A relationship object with a &#x60;data&#x60; key, containing the &#x60;users&#x60; type and valid user ID is required. All attributes describing the relationship between the node and the user are optional. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the new contributor, if the request is successful. If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

    :param draft_id: The unique identifier of the Draft Registration.
    :type draft_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Contributor.from_dict(body)
    return web.Response(status=200)


async def draft_registration_contributors_list(request: web.Request, draft_id) -> web.Response:
    """Retreive a list Contributors from a Draft Registration

    Retrieves the details of all given Contributors for a Draft Registration. Contributors are users who can make changes to the Draft Registration. Contributors are categorized as either \&quot;bibliographic\&quot; or \&quot;non-bibliographic\&quot;. From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.

    :param draft_id: The unique identifier of the Draft Registration.
    :type draft_id: str

    """
    return web.Response(status=200)


async def draft_registrations_create(request: web.Request, body) -> web.Response:
    """Create a Draft Registration

    This creates a Draft Registration that can be used to edit and register research. Draft Registrations contain Registration questions that will become part of the Registration. A Registration is a frozen version of the project that can never be deleted, but can be withdrawn and have it&#39;s metadata edited. A Draft Registration created by this endpoint will not have a Project linked with it by default, but if the user includes a &#x60;branched_from&#x60; attribute in their Draft Registration creation payload with the value of the &#x60;branched_from&#x60; being guid of a Project they have permissions for the Draft Registration will be linked to the Project. If you linked your Draft Registration on a Project, your original Project remains editable and will now have the Draft Registration linked to it.  #### Permissions Any user can create a Draft Registration. If the &#x60;branched_from&#x60; attribute is provided, then the user must be an ADMIN contributor on the Project being registered. #### Required Required fields for creating a Draft Registration include:  &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&#x60;schema_id&#x60; #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the created Draft Registration, if the request is successful.  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

    :param body: 
    :type body: dict | bytes

    """
    body = DraftRegistration.from_dict(body)
    return web.Response(status=200)


async def draft_registrations_draft_id_contributors_user_id_get(request: web.Request, draft_id, user_id) -> web.Response:
    """Retreive a Contributor from a Draft Registration

    Retrieves the details of a given contributor.  Contributors are users who can view or edit to the Draft Registrations.  Contributors are categorized as either \&quot;bibliographic\&quot; or \&quot;non-bibliographic\&quot;. From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.

    :param draft_id: The unique identifier of the Draft Registration.
    :type draft_id: str
    :param user_id: The unique identifier of the Contributor.
    :type user_id: str

    """
    return web.Response(status=200)


async def draft_registrations_draft_id_delete(request: web.Request, draft_id) -> web.Response:
    """Delete a draft registration

    Permanently deletes a draft registration. A draft that has already been registered cannot be deleted. #### Permissions Only draft registration contributors with ADMIN permissions may delete draft registrations #### Returns If the request is successful, no content is returned. If the request is unsuccessful, a JSON object with an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes]() to understand why this request may have failed.

    :param draft_id: The unique identifier of the draft registration.
    :type draft_id: str

    """
    return web.Response(status=200)


async def draft_registrations_draft_id_get(request: web.Request, draft_id) -> web.Response:
    """Retrieve a Draft Registration

    Retrieve the details of a given Draft Registration Draft Registrations contain Registration questions that will become part of the Registration. A Registration is a frozen version of the project that can never be deleted, but can be withdrawn and have it&#39;s metadata edited.  If you based your Draft Registration on a Project, your original Project remains editable but will now have the Draft Registration linked to it. #### Permissions Only draft registration contributors may view draft registrations. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested draft registration, if the request is successful.  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

    :param draft_id: The unique identifier of the draft registration.
    :type draft_id: str

    """
    return web.Response(status=200)


async def draft_registrations_draft_id_institutions_get(request: web.Request, draft_id) -> web.Response:
    """Retrieve Institutions afilliated with a Draft Registration

    Once a properly authenticated user has marked their registration as affiliated with an institution, that institution and any others added will appear in this list.

    :param draft_id: The unique identifier of the draft registration.
    :type draft_id: str

    """
    return web.Response(status=200)


async def draft_registrations_draft_id_patch(request: web.Request, draft_id, body) -> web.Response:
    """Update a Draft Registration

    Updates a Draft Registration by setting the values of the attributes specified in the request body. Any unspecified attributes will be left unchanged. Note this will not register or change the machine state of a Draft Registration, it can only edit the Draft Registration&#39;s attributes prior to its registration. #### Permissions Only draft registration contributors may view draft registrations and only draft registration contributors with WRITE or ADMIN permissions may update draft registrations. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the new representation of the updated draft registration, if the request is successful. If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

    :param draft_id: The unique identifier of the draft registration.
    :type draft_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def draft_registrations_read(request: web.Request, ) -> web.Response:
    """Retrieve a list of Draft Registrations

    Retrieve a list of all currently available Draft Registrations for that user. #### Permissions Only Draft Registration contributors may view draft registrations. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested draft registration, if the request is successful.  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.


    """
    return web.Response(status=200)


async def nodes_draft_registrations_read(request: web.Request, node_id, draft_id) -> web.Response:
    """Retrieve a Draft Registration

    Retrieve the details of a given draft registration. Draft Registrations contain Registration questions that will become part of the Registration. A Registration is a frozen version of the project that can never be deleted, but can be withdrawn and have it&#39;s metadata edited.  Your original project remains editable but will now have the draft registration linked to it. #### Permissions Only project administrators may view draft registrations. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested draft registration, if the request is successful.  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

    :param node_id: The unique identifier of the node.
    :type node_id: str
    :param draft_id: The unique identifier of the draft registration.
    :type draft_id: str

    """
    return web.Response(status=200)


async def nodes_draft_registrations_subjects(request: web.Request, draft_id) -> web.Response:
    """Retrieve Subjects associated with a Draft Registration

    This retrieves a list of subjects associated with a Draft Registration. Subjects are formatted here in a flat paginated list, but are hierarchical and nested by specificity of subject matter.

    :param draft_id: The unique identifier of the draft registration.
    :type draft_id: str

    """
    return web.Response(status=200)
