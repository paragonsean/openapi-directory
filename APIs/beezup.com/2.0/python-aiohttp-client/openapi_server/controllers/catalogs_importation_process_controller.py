from typing import List, Dict
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.get_importation_products_report_request import GetImportationProductsReportRequest
from openapi_server.models.get_importation_products_report_response import GetImportationProductsReportResponse
from openapi_server.models.get_importation_report_response import GetImportationReportResponse
from openapi_server.models.import_already_in_progress_response import ImportAlreadyInProgressResponse
from openapi_server.models.importation_monitoring import ImportationMonitoring
from openapi_server.models.importation_technical_progression import ImportationTechnicalProgression
from openapi_server.models.importations_response import ImportationsResponse
from openapi_server.models.links_importation_get_importation_monitoring_link import LinksImportationGetImportationMonitoringLink
from openapi_server.models.start_manual_import_request import StartManualImportRequest
from openapi_server import util


async def importation_cancel(request: web.Request, store_id, execution_id) -> web.Response:
    """Cancel importation

    

    :param store_id: Your store identifier
    :type store_id: str
    :param execution_id: The execution identifier of you catalog importation
    :type execution_id: str

    """
    return web.Response(status=200)


async def importation_commit(request: web.Request, store_id, execution_id) -> web.Response:
    """Commit Importation

    

    :param store_id: Your store identifier
    :type store_id: str
    :param execution_id: The execution identifier of you catalog importation
    :type execution_id: str

    """
    return web.Response(status=200)


async def importation_commit_columns(request: web.Request, store_id, execution_id) -> web.Response:
    """Commit columns

    

    :param store_id: Your store identifier
    :type store_id: str
    :param execution_id: The execution identifier of you catalog importation
    :type execution_id: str

    """
    return web.Response(status=200)


async def importation_configure_remaining_catalog_columns(request: web.Request, store_id, execution_id) -> web.Response:
    """Configure remaining catalog columns

    This operation should be used after you have mapped the required BeezUP Columns

    :param store_id: Your store identifier
    :type store_id: str
    :param execution_id: The execution identifier of you catalog importation
    :type execution_id: str

    """
    return web.Response(status=200)


async def importation_get_importation_monitoring(request: web.Request, store_id, execution_id) -> web.Response:
    """Get the importation status

    

    :param store_id: Your store identifier
    :type store_id: str
    :param execution_id: The execution identifier of you catalog importation
    :type execution_id: str

    """
    return web.Response(status=200)


async def importation_get_products_report(request: web.Request, store_id, execution_id, body) -> web.Response:
    """Importation Get Products Report

    

    :param store_id: Your store identifier
    :type store_id: str
    :param execution_id: The execution identifier of you catalog importation
    :type execution_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = GetImportationProductsReportRequest.from_dict(body)
    return web.Response(status=200)


async def importation_get_report(request: web.Request, store_id, execution_id) -> web.Response:
    """Importation Get Report

    

    :param store_id: Your store identifier
    :type store_id: str
    :param execution_id: The execution identifier of you catalog importation
    :type execution_id: str

    """
    return web.Response(status=200)


async def importation_get_reportings(request: web.Request, store_id) -> web.Response:
    """Get the latest catalog importation reporting

    

    :param store_id: Your store identifier
    :type store_id: str

    """
    return web.Response(status=200)


async def importation_get_reportings_all_stores(request: web.Request, ) -> web.Response:
    """Get the latest catalog importation reporting for all your stores

    


    """
    return web.Response(status=200)


async def importation_start_manual_update(request: web.Request, store_id, body) -> web.Response:
    """Start Manual Import

    

    :param store_id: Your store identifier
    :type store_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = StartManualImportRequest.from_dict(body)
    return web.Response(status=200)


async def importation_technical_progression(request: web.Request, store_id, execution_id) -> web.Response:
    """Get technical progression

    

    :param store_id: Your store identifier
    :type store_id: str
    :param execution_id: The execution identifier of you catalog importation
    :type execution_id: str

    """
    return web.Response(status=200)
