from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_classifier_taxonomy_out import APIClassifierTaxonomyOut
from openapi_server.models.api_classifiers_status_out import APIClassifiersStatusOut
from openapi_server.models.api_key_out import APIKeyOut
from openapi_server.models.api_period_usage_out import APIPeriodUsageOut
from openapi_server.models.api_services_out import APIServicesOut
from openapi_server.models.api_usage_aggregated_out import APIUsageAggregatedOut
from openapi_server.models.api_usage_history_out import APIUsageHistoryOut
from openapi_server.models.region_out import RegionOut
from openapi_server.models.software_version_out import SoftwareVersionOut
from openapi_server import util


async def anonymize(request: web.Request, source, anonymized, token) -> web.Response:
    """Activate/deactivate anonymization for a source.

    

    :param source: 
    :type source: str
    :param anonymized: 
    :type anonymized: bool
    :param token: 
    :type token: str

    """
    return web.Response(status=200)


async def api_key_info(request: web.Request, ) -> web.Response:
    """Read API Key info.

    


    """
    return web.Response(status=200)


async def api_status(request: web.Request, ) -> web.Response:
    """Prints the current status of the classifiers. A classifier name in apiStatus corresponds to a service name in apiServices.

    


    """
    return web.Response(status=200)


async def api_usage(request: web.Request, ) -> web.Response:
    """Print current API usage.

    


    """
    return web.Response(status=200)


async def api_usage_history(request: web.Request, ) -> web.Response:
    """Print historical API usage.

    


    """
    return web.Response(status=200)


async def api_usage_history_aggregate(request: web.Request, ) -> web.Response:
    """Print historical API usage (in an aggregated view, by service, by day/hour/min).

    


    """
    return web.Response(status=200)


async def available_services(request: web.Request, ) -> web.Response:
    """List of classification services and usage cost in Units per classification (default is 1&#x3D;ONE Unit). Some API endpoints (ex. Corridor) combine multiple classifiers.

    


    """
    return web.Response(status=200)


async def learnable(request: web.Request, source, learnable, token) -> web.Response:
    """Activate/deactivate learning from a source.

    

    :param source: The API Key to set as learnable/non learnable.
    :type source: str
    :param learnable: 
    :type learnable: bool
    :param token: 
    :type token: str

    """
    return web.Response(status=200)


async def regions(request: web.Request, ) -> web.Response:
    """Print basic source statistics.

    


    """
    return web.Response(status=200)


async def software_version(request: web.Request, ) -> web.Response:
    """Get the current software version

    


    """
    return web.Response(status=200)


async def taxonomy_classes(request: web.Request, classifier_name) -> web.Response:
    """Print the taxonomy classes valid for the given classifier.

    

    :param classifier_name: 
    :type classifier_name: str

    """
    return web.Response(status=200)
