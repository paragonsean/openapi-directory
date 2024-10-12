from typing import List, Dict
from aiohttp import web

from openapi_server.models.credit_note import CreditNote
from openapi_server.models.credit_note_list import CreditNoteList
from openapi_server import util


async def credit_note_get(request: web.Request, updated_after=None, page_size=None, page_number=None) -> web.Response:
    """Gets list of CreditNotes

    

    :param updated_after: 
    :type updated_after: str
    :param page_size: Number of items per page (max 1000)
    :type page_size: int
    :param page_number: Page to display. Starts from 1.
    :type page_number: int

    """
    updated_after = util.deserialize_datetime(updated_after)
    return web.Response(status=200)


async def credit_note_get_by_id(request: web.Request, id) -> web.Response:
    """Gets Credit Note by CreditNoteID

    

    :param id: Credit Note ID Number
    :type id: int

    """
    return web.Response(status=200)
