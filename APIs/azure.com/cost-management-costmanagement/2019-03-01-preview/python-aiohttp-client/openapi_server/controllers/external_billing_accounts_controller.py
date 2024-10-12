from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.external_billing_account_definition import ExternalBillingAccountDefinition
from openapi_server.models.external_billing_account_definition_list_result import ExternalBillingAccountDefinitionListResult
from openapi_server import util


async def external_billing_account_get(request: web.Request, api_version, external_billing_account_name, expand=None) -> web.Response:
    """external_billing_account_get

    Get a ExternalBillingAccount definition

    :param api_version: Version of the API to be used with the client request. The current version is 2019-03-01-preview
    :type api_version: str
    :param external_billing_account_name: External Billing Account Name. (eg &#39;aws-{PayerAccountId}&#39;)
    :type external_billing_account_name: str
    :param expand: May be used to expand the collectionInfo property. By default, collectionInfo is not included.
    :type expand: str

    """
    return web.Response(status=200)


async def external_billing_account_list(request: web.Request, api_version) -> web.Response:
    """external_billing_account_list

    List all ExternalBillingAccount definitions

    :param api_version: Version of the API to be used with the client request. The current version is 2019-03-01-preview
    :type api_version: str

    """
    return web.Response(status=200)
