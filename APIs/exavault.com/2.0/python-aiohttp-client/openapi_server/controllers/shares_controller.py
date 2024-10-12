from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_share_request_body import AddShareRequestBody
from openapi_server.models.empty_response import EmptyResponse
from openapi_server.models.share_collection_response import ShareCollectionResponse
from openapi_server.models.share_response import ShareResponse
from openapi_server.models.update_share_request_body import UpdateShareRequestBody
from openapi_server import util


async def add_share(request: web.Request, ev_api_key, ev_access_token, body=None) -> web.Response:
    """Creates a share

    Creates a new share object for the given path in your account. We support three types of shares:    - A **shared folder** allows you to let outside parties access a folder in your account (including any files and nested subfolders) using just a link. Shared folders can be restricted; e.g. with an expiration date, password, download-only, etc. Shared folders are &#39;live&#39;; if someone makes a change to a file in your shared folder, it will be immediately reflected in your account, and vice-versa.   - A file **send** lets you send one or more files via an easy download link. File sends are different than shared folders because file sends are &#39;point in time&#39; -- the recipient will get the files as you sent them. If you later make a change to the source file, it will not be updated for the recipient.   - A **receive** folder lets you receive files into your account. You can either send users a link, or optionally [embed a customized form](/docs/account/05-file-sharing/05-upload-widget) on your website.    **How to send files from your computer using the API**:  In order to use the API to send files which are not already stored in your account, you&#39;ll need to follow a three-step process:  1. Use the [POST /shares](#operation/addShare) endpoint to set up your send, including password, recipients, expiration, etc. You must include **upload** among the permissions in the &#x60;accessMode&#x60; and set the &#x60;sendingLocalFiles&#x60; parameter to **true**. The response that is returned will include a \&quot;meta\&quot; attribute, which contains an **accessToken** attribute. This new access token is valid only for the send. 2. Use the [POST /resources/upload](#operation/uploadFile) endpoint to upload your files to the send you&#39;ve created. The \&quot;/\&quot; path represents the root of the share, not your home directory. **You must send the access token that you received from the first step in the &#x60;ev-access-token&#x60; header** 3. Use the [POST /shares/complete-send/{id}](#operation/completeDirectSend) endpoint to indicate that you have finished uploading files to your send. This will trigger the system to remove the **upload** permission from the share and send any invitation emails you set up in the first step of the process. **You must send YOUR access token in the &#x60;ev-access-token&#x60; header, not the temporary access token**  **Setting the Share Permissions**  Only 5 different combinations of permissions are valid for the &#x60;accessMode&#x60; object:  - **Upload Only**: This allows share visitors to upload to a share but do nothing else to the contained files. To use this mode, set &#x60;upload&#x60; to **true** and all other permissions to **false** - **Download Only**: This allows share visitors to download files from a share but do nothing else to the contained files. To use this mode, set &#x60;download&#x60; to **true** and all other permissions to **false** - **Upload and Download**: This allows share visitors to upload new files to the share or download files within the share, but not make any other changes to the share contents. To use this mode, set &#x60;upload&#x60; and &#x60;download&#x60; to **true** and set both &#x60;modify&#x60; and &#x60;delete&#x60; to **false** - **All but Delete**: This allows share visitors to make any changes to the contents of a share except deleting files. To use this mode, set &#x60;upload&#x60;, &#x60;download&#x60;, and &#x60;modify&#x60; to **true** and set &#x60;delete&#x60; to **false** - **Full Access**: This allows share visitors to make any changes to the contents of a share. To use this mode, set all 4 permissions &#x60;upload&#x60;, &#x60;download&#x60;, &#x60;modify&#x60;, and &#x60;delete&#x60; to **true**  Any other combination of permissions provided as the &#x60;accessMode&#x60; will be rejected as a bad request.  **Notes:**  Authenticated user requires [share permission](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions).

    :param ev_api_key: API Key required to make the API call.
    :type ev_api_key: str
    :param ev_access_token: Access token required to make the API call.
    :type ev_access_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddShareRequestBody.from_dict(body)
    return web.Response(status=200)


async def complete_direct_send(request: web.Request, ev_api_key, ev_access_token, id) -> web.Response:
    """Complete send files

    After uploading the file(s) to be sent, this method will trigger invitation emails and finish the send files setup. If you are not sending files from your own computer in a send, you will not need this step.    **How to send files from your computer using the API**:  In order to use the API to send files which are not already stored in your account, you&#39;ll need to follow a three-step process:  1. Use the [POST /shares](#operation/addShare) endpoint to set up your send, including password, recipients, expiration, etc. You must include **upload** among the permissions in the &#x60;accessMode&#x60; and set the &#x60;sendingLocalFiles&#x60; paramter to **true**. The response that is returned will include a \&quot;meta\&quot; attribute, which contains an **accessToken** attribute. This new access token is valid only for the send. 2. Use the [POST /resources/upload](#operation/uploadFile) endpoint to upload your files to the send you&#39;ve created. The \&quot;/\&quot; path represents the root of the share, not your home directory. **You must send the access token that you received from the first step in the &#x60;ev-access-token&#x60; header** 3. Use the [POST /shares/complete-send/{id}](#operation/completeDirectSend) endpoint to indicate that you have finished uploading files to your send. This will trigger the system to remove the **upload** permission from the share and send any invitation emails you set up in the first step of the process. **You must send YOUR access token in the &#x60;ev-access-token&#x60; header, not the temporary access token** 

    :param ev_api_key: API Key
    :type ev_api_key: str
    :param ev_access_token: Access Token
    :type ev_access_token: str
    :param id: ID of the share to trigger invitations for.
    :type id: int

    """
    return web.Response(status=200)


async def delete_share_by_id(request: web.Request, id, ev_api_key, ev_access_token) -> web.Response:
    """Deactivate a share

    Deactivate a share. Deactivating a share does not remove the underlying files for **shared_folder** and **receive** share types; it merely removes the access URL. Deleting a **send** share type does remove the associated files, as files that have been sent are only associated with the share, and aren&#39;t stored anywhere else in the account.  **Notes:**  - You must have [sharing permissons](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions) to use this. - You must have [admin-level access](/docs/account/04-users/01-admin-users), or you must be the owner of the specified share you wish to delete.

    :param id: ID of the share entry
    :type id: int
    :param ev_api_key: API Key required to make the API call.
    :type ev_api_key: str
    :param ev_access_token: Access token required to make the API call.
    :type ev_access_token: str

    """
    return web.Response(status=200)


async def get_share_by_id(request: web.Request, id, ev_api_key, ev_access_token, include=None) -> web.Response:
    """Get a share

    Get the details for a specific share entry. You can use the &#x60;include&#x60; parameter to also get the details of related records, such as the owning user or the resources involved in the share.  **Notes:**  - Authenticated user requires [share permission](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions). - To get share objects with type send, authenticated user&#39;s role must be admin or master.

    :param id: ID of the share entry
    :type id: int
    :param ev_api_key: API Key
    :type ev_api_key: str
    :param ev_access_token: Access Token
    :type ev_access_token: str
    :param include: Comma separated list of relationships to include in response. Possible values are **owner**, **resources**, **notifications**, **activity**.
    :type include: str

    """
    return web.Response(status=200)


async def list_shares(request: web.Request, ev_api_key, ev_access_token, offset=None, limit=None, scope=None, sort=None, type=None, include=None, name=None, recipient=None, message=None, username=None, search=None) -> web.Response:
    """Get a list of shares

    Get a list of shares that you would have access to view through the web interface. You can limit which results are returned by specifying specific types of shares you wish to view, finding things shared with a specific email address, as well as finding shares for specific folder names.   **Notes:**  - Authenticated user requires [share permission](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions). - To get share objects with type send, authenticated user&#39;s role must be admin or master.

    :param ev_api_key: API Key required to make the API call.
    :type ev_api_key: str
    :param ev_access_token: Access token required to make the API call.
    :type ev_access_token: str
    :param offset: Current offset of records (for pagination)
    :type offset: int
    :param limit: Limit of records to be returned (for pagination)
    :type limit: int
    :param scope: Set of shares to return. (**all**&#x3D;all of them, **active**&#x3D;shares that are currently active, **curentUser**&#x3D;shares created by you)
    :type scope: str
    :param sort: What order the list of matches should be in.
    :type sort: str
    :param type: Limit the list of matches to only certain types of shares.
    :type type: str
    :param include: Comma separated list of relationships to include in response. Possible values are **owner**, **resources**, **notifications**, **activity**.
    :type include: str
    :param name: When provided, only shares whose names include this value will be in the list. Supports wildcards, such as **send\\*** to return everything starting with \&quot;send\&quot;.  Use this parameter if you are searching for shares or receives for a specific folder name. For example **/Clients/ACME/To Be Processed**.
    :type name: str
    :param recipient: Filter the results to include only shares that invited a certain email address. Supports wildcard matching so that **\\*@example.com** will give back entries shared with addresses ending in \&quot;@example.com\&quot;. 
    :type recipient: str
    :param message: When provided, only shares with a message that contains the text will be included in the list of matches. Both the subject and the body of all messages will be checked for matches. This will always be a wildcard match, so that searching for **taxes** will return any shares with a message that contains the word \&quot;taxes\&quot;.
    :type message: str
    :param username: When provided, only shares created by the user with that &#x60;username&#x60; will be included in the list. Does not support wildcard searching.
    :type username: str
    :param search: Searches the share name, username, recipients, share messages fields for the provided value. Supports wildcard searches.
    :type search: str

    """
    return web.Response(status=200)


async def update_share_by_id(request: web.Request, id, ev_api_key, ev_access_token, body) -> web.Response:
    """Update a share

    Change the settings on an active share. Any changes made will affect all users that have access to the share.   When updating invitees, pass the &#x60;recipients&#x60; body paramater with the full list of people who should be included on the share. If you resend the list without an existing recipient, they will be removed from the share.  **Setting the Share Permissions**  Only 5 different combinations of permissions are valid for the &#x60;accessMode&#x60; object:  - **Upload Only**: This allows share visitors to upload to a share but do nothing else to the contained files. To use this mode, set &#x60;upload&#x60; to **true** and all other permissions to **false** - **Download Only**: This allows share visitors to download files from a share but do nothing else to the contained files. To use this mode, set &#x60;download&#x60; to **true** and all other permissions to **false** - **Upload and Download**: This allows share visitors to upload new files to the share or download files within the share, but not make any other changes to the share contents. To use this mode, set &#x60;upload&#x60; and &#x60;download&#x60; to **true** and set both &#x60;modify&#x60; and &#x60;delete&#x60; to **false** - **All but Delete**: This allows share visitors to make any changes to the contents of a share except deleting files. To use this mode, set &#x60;upload&#x60;, &#x60;download&#x60;, and &#x60;modify&#x60; to **true** and set &#x60;delete&#x60; to **false** - **Full Access**: This allows share visitors to make any changes to the contents of a share. To use this mode, set all 4 permissions &#x60;upload&#x60;, &#x60;download&#x60;, &#x60;modify&#x60;, and &#x60;delete&#x60; to **true**  Any other combination of permissions provided as the &#x60;accessMode&#x60; will be rejected as a bad request.  **Notes:**    - Authenticated user should be the owner of the specified share.

    :param id: ID of the share entry
    :type id: int
    :param ev_api_key: API Key
    :type ev_api_key: str
    :param ev_access_token: Access Token
    :type ev_access_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateShareRequestBody.from_dict(body)
    return web.Response(status=200)
