from typing import List, Dict
from aiohttp import web

from openapi_server.models.web_service_account import WebServiceAccount
from openapi_server.models.web_service_account_statistics import WebServiceAccountStatistics
from openapi_server.models.web_service_transfer_credits_request import WebServiceTransferCreditsRequest
from openapi_server.models.web_service_user import WebServiceUser
from openapi_server.models.web_service_users import WebServiceUsers
from openapi_server import util


async def api_rest_v1_account_user_put(request: web.Request, body=None) -> web.Response:
    """create

    Creates a new sub-account in your team. The following fields are required &lt;i&gt;firstname, lastname, email address, contact number&lt;/i&gt; and &lt;i&gt;password.&lt;/i&gt;

    :param body: request
    :type body: dict | bytes

    """
    body = WebServiceUser.from_dict(body)
    return web.Response(status=200)


async def api_rest_v1_account_user_user_id_post(request: web.Request, user_id, body=None) -> web.Response:
    """update

    Updates a sub-account in your team. The following fields can be updated &lt;i&gt;firstname, lastname, contact number&lt;/i&gt; and &lt;i&gt;password.&lt;/i&gt;

    :param user_id: userId
    :type user_id: int
    :param body: request
    :type body: dict | bytes

    """
    body = WebServiceUser.from_dict(body)
    return web.Response(status=200)


async def get_balance(request: web.Request, ) -> web.Response:
    """balance

    Returns your account&#39;s credit balance


    """
    return web.Response(status=200)


async def get_statistics(request: web.Request, _from=None, to=None, user_email_address=None, campaign=None, include_refunded_and_optout=None, calculate_credit_value=None) -> web.Response:
    """statistics

    Returns data from the statistics report. Note that by default the statistics shown are based on the number of messages, use the calculateCreditValue should you wish to calculate the statistics based on credit value.

    :param _from: date format: dd-MM-yyyy
    :type _from: str
    :param to: date format: dd-MM-yyyy
    :type to: str
    :param user_email_address: optional email address of user to return statistics for a single user, default is to return statistics for all users if administrator, or statistics for your own account if not an administrator
    :type user_email_address: str
    :param campaign: optional campaign name
    :type campaign: str
    :param include_refunded_and_optout: optionally include refunded and optout counts, default is false
    :type include_refunded_and_optout: bool
    :param calculate_credit_value: optionally calculate using credit value rather than message count, default is false
    :type calculate_credit_value: bool

    """
    _from = util.deserialize_datetime(_from)
    to = util.deserialize_datetime(to)
    return web.Response(status=200)


async def get_user(request: web.Request, user_id) -> web.Response:
    """getUser

    Gets a user from a given user id

    :param user_id: userId
    :type user_id: int

    """
    return web.Response(status=200)


async def search(request: web.Request, search_email) -> web.Response:
    """search

    Find a user for a particular email address

    :param search_email: search by email address
    :type search_email: str

    """
    return web.Response(status=200)


async def transfer(request: web.Request, body=None) -> web.Response:
    """transfer

    Transfers credits between two users in the same team. The &lt;i&gt;account email address&lt;/i&gt; fields as well as the &lt;i&gt;number of credits to transfer&lt;/i&gt; are required. 

    :param body: request
    :type body: dict | bytes

    """
    body = WebServiceTransferCreditsRequest.from_dict(body)
    return web.Response(status=200)
