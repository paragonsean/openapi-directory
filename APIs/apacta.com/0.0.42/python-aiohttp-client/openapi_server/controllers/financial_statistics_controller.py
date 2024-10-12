from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_expenses_sales_price200_response import GetExpensesSalesPrice200Response
from openapi_server.models.get_financial_statistics200_response import GetFinancialStatistics200Response
from openapi_server.models.get_financial_statistics_overview200_response import GetFinancialStatisticsOverview200Response
from openapi_server.models.get_invoiced_amount200_response import GetInvoicedAmount200Response
from openapi_server.models.get_margin200_response import GetMargin200Response
from openapi_server.models.get_material_rentals_cost_price200_response import GetMaterialRentalsCostPrice200Response
from openapi_server.models.get_products_cost_price200_response import GetProductsCostPrice200Response
from openapi_server import util


async def get_expenses_sales_price(request: web.Request, date_from=None, date_to=None, project_id=None) -> web.Response:
    """Get expenses sales price

    

    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param project_id: 
    :type project_id: str
    :type project_id: str

    """
    date_from = util.deserialize_date(date_from)
    date_to = util.deserialize_date(date_to)
    return web.Response(status=200)


async def get_financial_statistics(request: web.Request, date_from=None, date_to=None, project_id=None, project_status_ids=None, only_not_invoiced=None, details=None) -> web.Response:
    """Get general statistics

    

    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param project_id: 
    :type project_id: str
    :type project_id: str
    :param project_status_ids: 
    :type project_status_ids: str
    :type project_status_ids: str
    :param only_not_invoiced: 
    :type only_not_invoiced: bool
    :param details: 
    :type details: bool

    """
    date_from = util.deserialize_date(date_from)
    date_to = util.deserialize_date(date_to)
    return web.Response(status=200)


async def get_financial_statistics_overview(request: web.Request, date_from=None, date_to=None, project_id=None) -> web.Response:
    """Get statistics overview

    

    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param project_id: 
    :type project_id: str
    :type project_id: str

    """
    date_from = util.deserialize_date(date_from)
    date_to = util.deserialize_date(date_to)
    return web.Response(status=200)


async def get_invoiced_amount(request: web.Request, date_from=None, date_to=None, project_id=None) -> web.Response:
    """Get invoiced amount

    

    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param project_id: 
    :type project_id: str
    :type project_id: str

    """
    date_from = util.deserialize_date(date_from)
    date_to = util.deserialize_date(date_to)
    return web.Response(status=200)


async def get_margin(request: web.Request, date_from=None, date_to=None, project_id=None) -> web.Response:
    """Get margin

    

    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param project_id: 
    :type project_id: str
    :type project_id: str

    """
    date_from = util.deserialize_date(date_from)
    date_to = util.deserialize_date(date_to)
    return web.Response(status=200)


async def get_material_rentals_cost_price(request: web.Request, date_from=None, date_to=None, project_id=None) -> web.Response:
    """Get products material rentals cost price

    

    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param project_id: 
    :type project_id: str
    :type project_id: str

    """
    date_from = util.deserialize_date(date_from)
    date_to = util.deserialize_date(date_to)
    return web.Response(status=200)


async def get_products_cost_price(request: web.Request, date_from=None, date_to=None, project_id=None) -> web.Response:
    """Get products cost price

    

    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param project_id: 
    :type project_id: str
    :type project_id: str

    """
    date_from = util.deserialize_date(date_from)
    date_to = util.deserialize_date(date_to)
    return web.Response(status=200)
