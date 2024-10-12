from typing import List, Dict
from aiohttp import web

from openapi_server.models.document import Document
from openapi_server.models.document_analytic_data import DocumentAnalyticData
from openapi_server import util


async def cancel_document(request: web.Request, document_id, content_type, config_id=None) -> web.Response:
    """Cancel document analysis

    This method cancels document analysis by unique ID on Semantria side if it is waiting for analysis in queue.

    :param document_id: Document ID
    :type document_id: str
    :param content_type: 
    :type content_type: str
    :param config_id: Identifier of configuration used for analysis.
    :type config_id: str

    """
    return web.Response(status=200)


async def queue_batch_of_documents(request: web.Request, content_type, batch_of_documents, config_id=None) -> web.Response:
    """Queue batch of documents for analysis

    This method queues batch of documents for analysis. The rules are the same as for single document mode but here the documents ordered into the batch.

    :param content_type: 
    :type content_type: str
    :param batch_of_documents: List of parametrized JSON or XML objects.
    :type batch_of_documents: 
    :param config_id: Identifier of configuration used for analysis.
    :type config_id: str

    """
    return web.Response(status=200)


async def queue_document(request: web.Request, content_type, document, config_id=None) -> web.Response:
    """Queue document for analysis

    This method queues document onto the server for analysis. Queued document analyzes individually and will have its own set of results. If unique configuration ID provided, Semantria uses settings of that configuration during analysis, in opposite the primary configuration uses. Document IDs are unique in scope of configuration. If the same ID appears twice, Semantria overrides existing document with the new Data.

    :param content_type: 
    :type content_type: str
    :param document: Parametrized JSON or XML object.
    :type document: 
    :param config_id: Identifier of configuration used for analysis.
    :type config_id: str

    """
    return web.Response(status=200)


async def receive_document_analytic_data(request: web.Request, document_id, content_type, config_id=None) -> web.Response:
    """Retrieve document analysis or its status in queue

    This method retrieves analysis results for the single document by its unique ID or the document’s status in queue if it did not analyzed yet. Semantria guarantees delivering of all documents back to the client even if they FAILED on Semantria side due to some reason.

    :param document_id: Document ID
    :type document_id: str
    :param content_type: 
    :type content_type: str
    :param config_id: Identifier of configuration used for analysis.
    :type config_id: str

    """
    return web.Response(status=200)


async def retrieve_processed_documents(request: web.Request, content_type, config_id=None) -> web.Response:
    """Retrieve documents analysis

    This method retrieves analysis results for processed documents from Semantria. FAILED documents will have FAILED status in response. Semantria responds with limited amount of results per API call. If configuration ID provided, Semantria responds with the document, which were queued using the same configuration ID, in opposite Primary.

    :param content_type: 
    :type content_type: str
    :param config_id: Identifier of configuration used for analysis.
    :type config_id: str

    """
    return web.Response(status=200)
