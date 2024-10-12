from typing import List, Dict
from aiohttp import web

from openapi_server.models.replace_policy201_response import ReplacePolicy201Response
from openapi_server import util


async def load_policy(request: web.Request, account, identifier, body, x_request_id=None) -> web.Response:
    """Adds data to the existing Conjur policy.

    Adds data to the existing Conjur policy. Deletions are not allowed. Any policy objects that exist on the server but are omitted from the policy file will not be deleted and any explicit deletions in the policy file will result in an error.  ##### Permissions required  &#x60;create&#x60; privilege on the policy.\&quot; 

    :param account: Organization account name
    :type account: str
    :param identifier: ID of the policy to update
    :type identifier: str
    :param body: Policy
    :type body: 
    :param x_request_id: Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
    :type x_request_id: str

    """
    return web.Response(status=200)


async def replace_policy(request: web.Request, account, identifier, body, x_request_id=None) -> web.Response:
    """Loads or replaces a Conjur policy document.

    Loads or replaces a Conjur policy document.  **Any policy data which already exists on the server but is not explicitly specified in the new policy file will be deleted!**. 

    :param account: Organization account name
    :type account: str
    :param identifier: ID of the policy to load (root if no root policy has been loaded yet)
    :type identifier: str
    :param body: Policy
    :type body: 
    :param x_request_id: Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
    :type x_request_id: str

    """
    return web.Response(status=200)


async def update_policy(request: web.Request, account, identifier, body, x_request_id=None) -> web.Response:
    """Modifies an existing Conjur policy.

    Modifies an existing Conjur policy. Data may be explicitly deleted using the &#x60;!delete&#x60;, &#x60;!revoke&#x60;, and &#x60;!deny&#x60; statements. Unlike &#x60;replace&#x60; mode, no data is ever implicitly deleted.  ##### Permissions required 

    :param account: Organization account name
    :type account: str
    :param identifier: ID of the policy to update
    :type identifier: str
    :param body: Policy
    :type body: 
    :param x_request_id: Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
    :type x_request_id: str

    """
    return web.Response(status=200)
