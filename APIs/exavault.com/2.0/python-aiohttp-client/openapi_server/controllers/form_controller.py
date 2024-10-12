from typing import List, Dict
from aiohttp import web

from openapi_server.models.empty_response import EmptyResponse
from openapi_server.models.form_entry_response import FormEntryResponse
from openapi_server.models.form_response import FormResponse
from openapi_server.models.update_form_by_id_request_body import UpdateFormByIdRequestBody
from openapi_server import util


async def delete_form_message_by_id(request: web.Request, ev_api_key, ev_access_token, id) -> web.Response:
    """Delete a receive form submission

    Deletes a form submission entry, which represents one time that a visitor filled out the form and uploaded files. This deletes only the record of the submission (the date, the values entered in the form and the names of the files uploaded by the visitor).The share and any associated file resources will not be deleted by this.   **Notes**:  - Use the [GET /form/entries/{formId}](#operation/getFormMessageById) to list the submissions and obtain the ID of the entry you want to delete - You must have the [DeleteFormData permission](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions) in order to use this operation - It is not possible to un-delete data that is removed in this way 

    :param ev_api_key: API Key required to make the API call. 
    :type ev_api_key: str
    :param ev_access_token: Access token required to make the API call.
    :type ev_access_token: str
    :param id: ID of the entry to be deleted data for
    :type id: int

    """
    return web.Response(status=200)


async def get_form_by_id(request: web.Request, id, ev_api_key, ev_access_token, include=None) -> web.Response:
    """Get receive folder form by Id

    Returns the [file upload form](/docs/account/05-file-sharing/05-form-builder) assigned to a [receive folder](/docs/account/05-file-sharing/04-receive-folders). The form details will return all the input fields and their settings.   Use the &#x60;include&#x60; parameter (with the value **share**) to also retrieve the details of the associated receive folder.   **Note**  If you prefer to find a form by its shareHash, you can use the [GET /forms](#operation/getFormByShareHash) endpoint instead.  

    :param id: Form unique ID number.
    :type id: int
    :param ev_api_key: API key required to make the API call.
    :type ev_api_key: str
    :param ev_access_token: Access Token required to make the API call.
    :type ev_access_token: str
    :param include: Enter \&quot;**share**\&quot; to get information about associated receive folder.
    :type include: str

    """
    return web.Response(status=200)


async def get_form_by_share_hash(request: web.Request, ev_api_key, ev_access_token, share_hash, include=None) -> web.Response:
    """Get receive folder form settings

    Get the information for the [file upload form](/docs/account/05-file-sharing/05-form-builder) assigned to a [receive folder](/docs/account/05-file-sharing/04-receive-folders) by its shareHash. The form details will return all the input field settings and the CSS for the form.  Use the &#x60;include&#x60; parameter (with the value **share**) to also get the details of the associated receive folder.  **Note**  - If you prefer to find a form by its ID, you can use the [GET /forms/{id}](#operation/getFormById) endpoint instead.  

    :param ev_api_key: API key required to make the API call.
    :type ev_api_key: str
    :param ev_access_token: Access Token required to make the API call.
    :type ev_access_token: str
    :param share_hash: Share hash to retrieve the form for.
    :type share_hash: str
    :param include: Related record types to include in the response. Valid option is **share**
    :type include: str

    """
    return web.Response(status=200)


async def get_form_entries(request: web.Request, ev_api_key, ev_access_token, id, limit=None, offset=None) -> web.Response:
    """Get form data entries for a receive

    Returns the form data entries for a specific form for a receive. Optional parameters can be included in the call to manage larger data sets. 

    :param ev_api_key: API Key required to make the API call. 
    :type ev_api_key: str
    :param ev_access_token: Access token required to make the API call.
    :type ev_access_token: str
    :param id: ID of the form to retrieve entries for.
    :type id: int
    :param limit: Limit of records to be returned (for pagination)
    :type limit: int
    :param offset: Current offset of records (for pagination)
    :type offset: int

    """
    return web.Response(status=200)


async def update_form_by_id(request: web.Request, id, ev_api_key, ev_access_token, body=None) -> web.Response:
    """Updates a form with given parameters

    Add, update, or delete a form&#39;s parameters. This will alter how your users/customers will see and interact with the form when sending you files.   **Notes**  *This call will **replace** your current form in its entirety.* If you want to keep any existing elements unchanged, be sure to submit the call with an element&#39;s current settings to preserve them.                          

    :param id: Form unique ID number.
    :type id: int
    :param ev_api_key: API Key required to make the API call.
    :type ev_api_key: str
    :param ev_access_token: Access token required to make the API call.
    :type ev_access_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateFormByIdRequestBody.from_dict(body)
    return web.Response(status=200)
