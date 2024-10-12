from typing import List, Dict
from aiohttp import web

from openapi_server.models.transaction_metadata import TransactionMetadata
from openapi_server.models.transaction_metadata_list import TransactionMetadataList
from openapi_server import util


async def get_sync_transaction(request: web.Request, company_id, sync_id, transaction_id) -> web.Response:
    """Get Sync Transaction

    Gets the status of a transaction for a sync

    :param company_id: 
    :type company_id: str
    :type company_id: str
    :param sync_id: Unique identifier for a sync.
    :type sync_id: str
    :type sync_id: str
    :param transaction_id: The unique identifier for your SMB&#39;s transaction.
    :type transaction_id: str
    :type transaction_id: str

    """
    return web.Response(status=200)


async def list_sync_transactions(request: web.Request, company_id, sync_id, page, page_size=None) -> web.Response:
    """Get Sync transactions

    Get&#39;s the transactions and status for a sync

    :param company_id: 
    :type company_id: str
    :type company_id: str
    :param sync_id: Unique identifier for a sync.
    :type sync_id: str
    :type sync_id: str
    :param page: Page number. [Read more](https://docs.codat.io/using-the-api/paging).
    :type page: int
    :param page_size: Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging).
    :type page_size: int

    """
    return web.Response(status=200)
