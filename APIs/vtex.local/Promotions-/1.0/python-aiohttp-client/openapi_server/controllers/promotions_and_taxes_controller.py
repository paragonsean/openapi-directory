from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_or_update_calculator_configuration200_response import CreateOrUpdateCalculatorConfiguration200Response
from openapi_server.models.create_or_update_calculator_configuration_request import CreateOrUpdateCalculatorConfigurationRequest
from openapi_server.models.get_all_benefits200_response import GetAllBenefits200Response
from openapi_server.models.get_all_taxes200_response import GetAllTaxes200Response
from openapi_server.models.get_archived_promotions200_response import GetArchivedPromotions200Response
from openapi_server.models.get_archived_taxes200_response import GetArchivedTaxes200Response
from openapi_server.models.get_calculator_configuration_by_id200_response import GetCalculatorConfigurationById200Response
from openapi_server.models.get_calculator_configuration_by_id200_response1 import GetCalculatorConfigurationById200Response1
from openapi_server import util


async def api_rnb_pvt_import_calculator_configuration_post(request: web.Request, content_type, accept, x_vtex_calculator_name, x_vtex_start_date, x_vtex_end_date, x_vtex_accumulate_with_manual_prices, x_vtex_cumulative=None, x_vtex_cluster_operator=None, x_vtex_cluster_expression=None, body=None) -> web.Response:
    """Create Multiple SKU Promotion

    Creates a Multiple SKU Promotion. This scenario allows to create a single promotion for multiples SKUs with the Percentage Effect.   &gt; ⚠️   &gt;  &gt; The limit of SKUs on a Multiple Effects promotion is 400.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param x_vtex_calculator_name: Promotion Name.
    :type x_vtex_calculator_name: str
    :param x_vtex_start_date: Promotion start date.
    :type x_vtex_start_date: str
    :param x_vtex_end_date: Promotion end date.
    :type x_vtex_end_date: str
    :param x_vtex_accumulate_with_manual_prices: Condition that will accumulate the Promotion with manual prices or not.
    :type x_vtex_accumulate_with_manual_prices: bool
    :param x_vtex_cumulative: Defines if the Promotion is cumulative with other promotions.
    :type x_vtex_cumulative: bool
    :param x_vtex_cluster_operator: This header allows implementing the Promotion in multiples client clusters. You can set the value as &#x60;all&#x60; - the Promotion will be valid to all the clusters - or &#x60;any&#x60; - the Promotion will be valid to any of the clusters.
    :type x_vtex_cluster_operator: str
    :param x_vtex_cluster_expression: Cluster that will be included in the Promotion. To add multiple clusters, create a header for each one of them.
    :type x_vtex_cluster_expression: str
    :param body: 
    :type body: str

    """
    return web.Response(status=200)


async def api_rnb_pvt_import_calculator_configuration_promotion_id_put(request: web.Request, content_type, accept, x_vtex_calculator_name, x_vtex_start_date, x_vtex_end_date, x_vtex_accumulate_with_manual_prices, promotion_id, x_vtex_cumulative=None, x_vtex_cluster_operator=None, x_vtex_cluster_expression=None, body=None) -> web.Response:
    """Update Multiple SKU Promotion

    Updates information from a Multiple SKU Promotion. This scenario allows to create a single promotion for multiples SKUs with the Percentage Effect.    &gt; ⚠️   &gt;  &gt; The limit of SKUs on a Multiple Effects promotion is 400.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param x_vtex_calculator_name: Promotion Name.
    :type x_vtex_calculator_name: str
    :param x_vtex_start_date: Promotion start date.
    :type x_vtex_start_date: str
    :param x_vtex_end_date: Promotion end date.
    :type x_vtex_end_date: str
    :param x_vtex_accumulate_with_manual_prices: Condition that will accumulate the Promotion with manual prices or not.
    :type x_vtex_accumulate_with_manual_prices: bool
    :param promotion_id: Promotion unique identifier.
    :type promotion_id: str
    :param x_vtex_cumulative: Defines if the Promotion is cumulative with other promotions.
    :type x_vtex_cumulative: bool
    :param x_vtex_cluster_operator: This header allows implementing the Promotion in multiples client clusters. You can set the value as &#x60;all&#x60; - the Promotion will be valid to all the clusters - or &#x60;any&#x60; - the Promotion will be valid to any of the clusters.
    :type x_vtex_cluster_operator: str
    :param x_vtex_cluster_expression: Cluster that will be included in the Promotion. To add multiple clusters, create a header for each one of them.
    :type x_vtex_cluster_expression: str
    :param body: 
    :type body: str

    """
    return web.Response(status=200)


async def archive_promotion(request: web.Request, content_type, accept, id_calculator_configuration) -> web.Response:
    """Archive Promotion or Tax

    Archives a Promotion or Tax by its ID.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param id_calculator_configuration: Promotion ID or tax ID.
    :type id_calculator_configuration: str

    """
    return web.Response(status=200)


async def create_or_update_calculator_configuration(request: web.Request, content_type, accept, body) -> web.Response:
    """Create or Update Promotion or Tax

    Creates or updates a specific Promotion by its Promotion ID or a specific Tax by its Tax ID.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrUpdateCalculatorConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def get_all_benefits(request: web.Request, content_type, accept) -> web.Response:
    """Get All Promotions

    Retrieves all promotions from an account.     &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Promotions onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/promotions-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about the Promotions and is organized by focusing on the developer&#39;s journey.    

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str

    """
    return web.Response(status=200)


async def get_all_taxes(request: web.Request, content_type, accept) -> web.Response:
    """Get All Taxes

    Retrieves all taxes from an account.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str

    """
    return web.Response(status=200)


async def get_archived_promotions(request: web.Request, content_type, accept) -> web.Response:
    """List Archived Promotions

    Lists all archived promotions.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str

    """
    return web.Response(status=200)


async def get_archived_taxes(request: web.Request, content_type, accept) -> web.Response:
    """List Archived Taxes

    Lists all archived taxes.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str

    """
    return web.Response(status=200)


async def get_calculator_configuration_by_id(request: web.Request, content_type, accept, id_calculator_configuration) -> web.Response:
    """Get Promotion or Tax by ID

    Retrieves a specific promotion by its Promotion ID or a specific tax by its Tax ID.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param id_calculator_configuration: Promotion ID or tax ID.
    :type id_calculator_configuration: str

    """
    return web.Response(status=200)


async def unarchive_promotion(request: web.Request, content_type, accept, id_calculator_configuration) -> web.Response:
    """Unarchive Promotion or Tax

    Unarchives a Promotion or Tax by its ID.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param id_calculator_configuration: Promotion ID or tax ID.
    :type id_calculator_configuration: str

    """
    return web.Response(status=200)
