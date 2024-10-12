from typing import List, Dict
from aiohttp import web

from openapi_server.models.collection import Collection
from openapi_server.models.collection_analytic_data import CollectionAnalyticData
from openapi_server import util


async def cancel_collection(request: web.Request, collection_id, content_type, config_id=None) -> web.Response:
    """Cancel collection analysis

    This method cancels collection analysis by unique ID on Semantria side if it is waiting for analysis in queue.

    :param collection_id: Collection ID
    :type collection_id: str
    :param content_type: 
    :type content_type: str
    :param config_id: Identifier of configuration used for analysis.
    :type config_id: str

    """
    return web.Response(status=200)


async def queue_collection(request: web.Request, content_type, collection, config_id=None) -> web.Response:
    """Queue collection for analysis

    This method queues collection of documents onto the server for analysis. Queued collection of documents analyzes in common context as entire thing. If unique configuration ID provided, Semantria uses settings of that configuration during analysis, in opposite the primary configuration uses. Collection IDs are unique in scope of configuration. If the same ID appears twice, Semantria overrides existing collection with the new Data

    :param content_type: 
    :type content_type: str
    :param collection: Parametrized JSON or XML object.
    :type collection: 
    :param config_id: Identifier of configuration used for analysis.
    :type config_id: str

    """
    return web.Response(status=200)


async def receive_collection_analytic_data(request: web.Request, collection_id, content_type, config_id=None) -> web.Response:
    """Retrieve collection analysis or its status in queue

    This method retrieves analysis results for documents collection by its unique ID or the collection’s status in queue if it did not analyzed yet. Semantria guarantees delivering of all collections back to the client even if they FAILED on Semantria side due to some reason.

    :param collection_id: Collection ID
    :type collection_id: str
    :param content_type: 
    :type content_type: str
    :param config_id: Identifier of configuration used for analysis.
    :type config_id: str

    """
    return web.Response(status=200)


async def retrieve_processed_collections(request: web.Request, content_type, config_id=None) -> web.Response:
    """Retrieve collections analysis

    This method retrieves analysis results for processed collections from Semantria. FAILED collections will have FAILED status in response. Semantria responds with limited amount of results per API call. If configuration ID provided, Semantria responds with the collections, which were queued using the same configuration ID, in opposite Primary configuration uses.

    :param content_type: 
    :type content_type: str
    :param config_id: Identifier of configuration used for analysis.
    :type config_id: str

    """
    return web.Response(status=200)
