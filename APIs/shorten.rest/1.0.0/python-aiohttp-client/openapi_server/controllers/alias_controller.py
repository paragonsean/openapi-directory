from typing import List, Dict
from aiohttp import web

from openapi_server.models.alias_model import AliasModel
from openapi_server.models.create_alias_model import CreateAliasModel
from openapi_server.models.create_alias_response_model import CreateAliasResponseModel
from openapi_server.models.get_aliases_model import GetAliasesModel
from openapi_server import util


async def create_alias(request: web.Request, body, domain_name=None, alias_name=None) -> web.Response:
    """Create alias

    This POST method creates a new alias under a specified domain. If no domain is specified in the request the alias will be attached to the default domain Short.fyi    **NOTE:** You can override the domain level Meta Tags and Tracking Snippets by specifying them for each URL. Any variables you add to a specific URL will always override domain level settings.

    :param body: alias properties
    :type body: dict | bytes
    :param domain_name: domain which alias will belong to (string without &#x60;http/https&#x60; or &#x60;/&#x60;)
    :type domain_name: str
    :param alias_name: alias (without &#x60;/&#x60; at the beginning)
    :type alias_name: str

    """
    body = CreateAliasModel.from_dict(body)
    return web.Response(status=200)


async def delete_alias(request: web.Request, alias_name, domain_name=None) -> web.Response:
    """Delete alias

    Deletes a single alias by providing alias and domain. If no domain is provided the API will search for the matching alias within the Short.fyi domain

    :param alias_name: alias (without &#x60;/&#x60; at the beginning)
    :type alias_name: str
    :param domain_name: domain which alias belongs to (string without &#x60;http/https&#x60; or &#x60;/&#x60;)
    :type domain_name: str

    """
    return web.Response(status=200)


async def get_alias(request: web.Request, alias_name, domain_name=None) -> web.Response:
    """Get alias

    Get detailed information for a single alias by providing its alias and domain name

    :param alias_name: alias value (without &#x60;/&#x60; at the beginning)
    :type alias_name: str
    :param domain_name: domain which alias belongs to (string without &#x60;http/https&#x60; or &#x60;/&#x60;)
    :type domain_name: str

    """
    return web.Response(status=200)


async def get_aliases(request: web.Request, domain_name=None, continue_from=None, limit=None) -> web.Response:
    """Get aliases by domain

    Obtain a list of all alias names associated with your account and given domain. Result array is in descending order by creation date.    If no domain is specified you will receive a list of all the alias names you have created using the Short.fyi domain.    If there are more results than the limit for the request the response will return you a value in lastId property you can specify it in the continueFrom query parameter to get the next batch of records.

    :param domain_name: The domain name to get the aliases for (string without &#x60;http/https&#x60; or &#x60;/&#x60;)
    :type domain_name: str
    :param continue_from: An ID returned by a previous query to continue aliases retrieval (see lastId in response)
    :type continue_from: str
    :param limit: Number of results to return per request
    :type limit: int

    """
    return web.Response(status=200)


async def update_alias(request: web.Request, alias_name, body, domain_name=None) -> web.Response:
    """Update alias

    Update a single short URL by providing its alias and domain as a parameter, and the data you wish to update in the body of the request. If no domain is provided you will receive the alias found attached to the Short.fyi domain (if it exists and is linked to your account!)   ### NOTE:    ( * )If you add a metatag or a snippet with a same name to an alias and the domain it&#39;s related to, the value will be taken from the alias and not the domain    ( ** ) When you update any array property (like destinations) the block is updated **completely** so you have to specify the old records to avoid deleting them   ( *** ) The method updates only the specified properties so if there was no change in one of them you don&#39;t have to send it.

    :param alias_name: alias (without &#x60;/&#x60; at the beginning)
    :type alias_name: str
    :param body: alias properties you wish to be updated
    :type body: dict | bytes
    :param domain_name: domain which alias belongs to (string without &#x60;http/https&#x60; or &#x60;/&#x60;)
    :type domain_name: str

    """
    body = CreateAliasModel.from_dict(body)
    return web.Response(status=200)
