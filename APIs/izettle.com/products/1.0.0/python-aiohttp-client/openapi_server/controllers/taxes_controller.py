from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.tax_rate import TaxRate
from openapi_server.models.tax_rate_product_count_response import TaxRateProductCountResponse
from openapi_server.models.tax_rate_update_request import TaxRateUpdateRequest
from openapi_server.models.tax_rates_create_request import TaxRatesCreateRequest
from openapi_server.models.tax_rates_response import TaxRatesResponse
from openapi_server.models.tax_settings_response import TaxSettingsResponse
from openapi_server.models.tax_settings_update_request import TaxSettingsUpdateRequest
from openapi_server import util


async def create_tax_rates(request: web.Request, body) -> web.Response:
    """Create new tax rates

    

    :param body: 
    :type body: dict | bytes

    """
    body = TaxRatesCreateRequest.from_dict(body)
    return web.Response(status=200)


async def delete_tax_rate(request: web.Request, tax_rate_uuid) -> web.Response:
    """Delete a single tax rate

    

    :param tax_rate_uuid: 
    :type tax_rate_uuid: str
    :type tax_rate_uuid: str

    """
    return web.Response(status=200)


async def get_product_count_for_all_taxes(request: web.Request, ) -> web.Response:
    """Get all tax rates and a count of products associated with each

    


    """
    return web.Response(status=200)


async def get_tax_rate(request: web.Request, tax_rate_uuid) -> web.Response:
    """Get a single tax rate

    

    :param tax_rate_uuid: 
    :type tax_rate_uuid: str
    :type tax_rate_uuid: str

    """
    return web.Response(status=200)


async def get_tax_rates(request: web.Request, ) -> web.Response:
    """Get all available tax rates

    


    """
    return web.Response(status=200)


async def get_tax_settings(request: web.Request, ) -> web.Response:
    """Get the organization tax settings 

    


    """
    return web.Response(status=200)


async def set_taxation_mode(request: web.Request, body) -> web.Response:
    """Update the organization tax settings

    

    :param body: 
    :type body: dict | bytes

    """
    body = TaxSettingsUpdateRequest.from_dict(body)
    return web.Response(status=200)


async def update_tax_rate(request: web.Request, tax_rate_uuid, body) -> web.Response:
    """Update a single tax rate

    

    :param tax_rate_uuid: 
    :type tax_rate_uuid: str
    :type tax_rate_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = TaxRateUpdateRequest.from_dict(body)
    return web.Response(status=200)
