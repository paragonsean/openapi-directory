from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def create_secret(request: web.Request, account, kind, identifier, x_request_id=None, expirations=None, body=None) -> web.Response:
    """Creates a secret value within the specified variable.

    Creates a secret value within the specified Secret.   Note: Conjur will allow you to add a secret to any resource, but the best practice is to store and retrieve secret data only using Secret resources. 

    :param account: Organization account name
    :type account: str
    :param kind: Type of resource - in almost all cases this should be &#x60;variable&#x60;
    :type kind: str
    :param identifier: URL-encoded variable ID
    :type identifier: str
    :param x_request_id: Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
    :type x_request_id: str
    :param expirations: Tells the server to reset the variables expiration date
    :type expirations: str
    :param body: Secret data
    :type body: str

    """
    return web.Response(status=200)


async def get_secret(request: web.Request, account, kind, identifier, x_request_id=None, version=None) -> web.Response:
    """Fetches the value of a secret from the specified Secret.

    Fetches the value of a secret from the specified Secret. The latest version will be retrieved unless the version parameter is specified. The twenty most recent secret versions are retained.  The secret data is returned in the response body.  Note: Conjur will allow you to add a secret to any resource, but the best practice is to store and retrieve secret data only using Secret resources. 

    :param account: Organization account name
    :type account: str
    :param kind: Type of resource - in almost all cases this should be &#x60;variable&#x60;
    :type kind: str
    :param identifier: URL-encoded variable ID
    :type identifier: str
    :param x_request_id: Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
    :type x_request_id: str
    :param version: (**Optional**) Version you want to retrieve (Conjur keeps the last 20 versions of a secret)
    :type version: int

    """
    return web.Response(status=200)


async def get_secrets(request: web.Request, variable_ids, x_request_id=None, accept_encoding=None) -> web.Response:
    """Fetch multiple secrets

    Fetches multiple secret values in one invocation. It’s faster to fetch secrets in batches than to fetch them one at a time.

    :param variable_ids: Comma-delimited, URL-encoded resource IDs of the variables.
    :type variable_ids: str
    :param x_request_id: Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
    :type x_request_id: str
    :param accept_encoding: Set the encoding of the response object
    :type accept_encoding: str

    """
    return web.Response(status=200)
