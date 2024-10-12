from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_email_list_request_body import AddEmailListRequestBody
from openapi_server.models.email_list_collection_response import EmailListCollectionResponse
from openapi_server.models.email_list_response import EmailListResponse
from openapi_server.models.empty_response import EmptyResponse
from openapi_server.models.update_email_list_request_body import UpdateEmailListRequestBody
from openapi_server import util


async def add_email_list(request: web.Request, ev_api_key, ev_access_token, body=None) -> web.Response:
    """Create new email list

    Create a new email list. Among other things, email lists can be used to send files or share folders with a group of email addresses at once.

    :param ev_api_key: API Key required to make the API call.
    :type ev_api_key: str
    :param ev_access_token: Access token required to make the API call.
    :type ev_access_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddEmailListRequestBody.from_dict(body)
    return web.Response(status=200)


async def delete_email_list_by_id(request: web.Request, ev_api_key, ev_access_token, id) -> web.Response:
    """Delete an email group with given id

    Permanently delete an email group. This action is not reversible. We recommend making a user confirm this action before sending the API call. 

    :param ev_api_key: API Key required to make the API call.
    :type ev_api_key: str
    :param ev_access_token: Access token required to make the API call.
    :type ev_access_token: str
    :param id: ID of the email list to delete
    :type id: int

    """
    return web.Response(status=200)


async def get_email_list_by_id(request: web.Request, ev_api_key, ev_access_token, id, include=None) -> web.Response:
    """Get individual email group

    Retrieve all the details of a specific email list including it&#39;s name, when it was created and all the email addresses that belong to the group.

    :param ev_api_key: API Key required to make the API call.
    :type ev_api_key: str
    :param ev_access_token: Access token required to make the API call.
    :type ev_access_token: str
    :param id: ID of the email list to return.
    :type id: int
    :param include: Related record types to include in the response. Valid option is &#x60;ownerUser&#x60;
    :type include: str

    """
    return web.Response(status=200)


async def get_email_lists(request: web.Request, ev_api_key, ev_access_token, include=None) -> web.Response:
    """Get all email groups

    List all email groups for authenticated user

    :param ev_api_key: API Key required to make the API call.
    :type ev_api_key: str
    :param ev_access_token: Access token required to make the API call.
    :type ev_access_token: str
    :param include: Related record types to include in the response. Valid option is &#x60;ownerUser&#x60;
    :type include: str

    """
    return web.Response(status=200)


async def update_email_list_by_id(request: web.Request, ev_api_key, ev_access_token, id, body=None) -> web.Response:
    """Update an email group

    Add or remove emails from an email list that can be used to send and share files with groups.   **Notes**  *This call will **replace** your current email list in its entirety.* If you want to keep any existing emails on the list, be sure to submit the call with any current emails you want to keep on the list.  

    :param ev_api_key: API Key required to make the API call.
    :type ev_api_key: str
    :param ev_access_token: Access token required to make the API call.
    :type ev_access_token: str
    :param id: ID of the email list to update.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateEmailListRequestBody.from_dict(body)
    return web.Response(status=200)
