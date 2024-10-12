from typing import List, Dict
from aiohttp import web

from openapi_server.models.billing_profile import BillingProfile
from openapi_server.models.billing_profile_creation_parameters import BillingProfileCreationParameters
from openapi_server.models.billing_profile_list_result import BillingProfileListResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def billing_profiles_create(request: web.Request, api_version, billing_account_name, parameters) -> web.Response:
    """billing_profiles_create

    The operation to create a BillingProfile.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    :type api_version: str
    :param billing_account_name: Billing Account Id.
    :type billing_account_name: str
    :param parameters: Parameters supplied to the Create BillingProfile operation.
    :type parameters: dict | bytes

    """
    parameters = BillingProfileCreationParameters.from_dict(parameters)
    return web.Response(status=200)


async def billing_profiles_get(request: web.Request, api_version, billing_account_name, billing_profile_name, expand=None) -> web.Response:
    """billing_profiles_get

    Get the billing profile by id.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    :type api_version: str
    :param billing_account_name: Billing Account Id.
    :type billing_account_name: str
    :param billing_profile_name: Billing Profile Id.
    :type billing_profile_name: str
    :param expand: May be used to expand the invoiceSections.
    :type expand: str

    """
    return web.Response(status=200)


async def billing_profiles_list_by_billing_account_name(request: web.Request, api_version, billing_account_name, expand=None) -> web.Response:
    """billing_profiles_list_by_billing_account_name

    Lists all billing profiles for a user which that user has access to.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    :type api_version: str
    :param billing_account_name: Billing Account Id.
    :type billing_account_name: str
    :param expand: May be used to expand the invoiceSections.
    :type expand: str

    """
    return web.Response(status=200)


async def billing_profiles_update(request: web.Request, api_version, billing_account_name, billing_profile_name, parameters) -> web.Response:
    """billing_profiles_update

    The operation to update a billing profile.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    :type api_version: str
    :param billing_account_name: Billing Account Id.
    :type billing_account_name: str
    :param billing_profile_name: Billing Profile Id.
    :type billing_profile_name: str
    :param parameters: Parameters supplied to the update billing profile operation.
    :type parameters: dict | bytes

    """
    parameters = BillingProfile.from_dict(parameters)
    return web.Response(status=200)
