from typing import List, Dict
from aiohttp import web

from openapi_server.models.billing_aggregated_information_get_all200_response import BillingAggregatedInformationGetAll200Response
from openapi_server.models.billing_aggregated_information_get_by_app200_response import BillingAggregatedInformationGetByApp200Response
from openapi_server.models.billing_aggregated_information_get_by_app_default_response import BillingAggregatedInformationGetByAppDefaultResponse
from openapi_server import util


async def billing_aggregated_information_get_all(request: web.Request, service=None, period=None, show_original_plans=None) -> web.Response:
    """billing_aggregated_information_get_all

    Aggregated Billing Information for the requesting user and the organizations in which the user is an admin.

    :param service: Type of service that should be included in the Billing Information
    :type service: str
    :param period: Type of period that should be included in the Billing Information
    :type period: str
    :param show_original_plans: Controls whether the API should show the original plan when Azure Subscription is not enabled
    :type show_original_plans: bool

    """
    return web.Response(status=200)


async def billing_aggregated_information_get_by_app(request: web.Request, owner_name, app_name, service=None, period=None, show_original_plans=None) -> web.Response:
    """billing_aggregated_information_get_by_app

    Aggregated Billing Information for owner of a given app.

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param service: Type of service that should be included in the Billing Information
    :type service: str
    :param period: Type of period that should be included in the Billing Information
    :type period: str
    :param show_original_plans: Controls whether the API should show the original plan when Azure Subscription is not enabled
    :type show_original_plans: bool

    """
    return web.Response(status=200)


async def billing_aggregated_information_get_for_org(request: web.Request, org_name, service=None, period=None, show_original_plans=None) -> web.Response:
    """billing_aggregated_information_get_for_org

    Aggregated Billing Information for a given Organization.

    :param org_name: The name of the Organization
    :type org_name: str
    :param service: Type of service that should be included in the Billing Information
    :type service: str
    :param period: Type of period that should be included in the Billing Information
    :type period: str
    :param show_original_plans: Controls whether the API should show the original plan when Azure Subscription is not enabled
    :type show_original_plans: bool

    """
    return web.Response(status=200)
