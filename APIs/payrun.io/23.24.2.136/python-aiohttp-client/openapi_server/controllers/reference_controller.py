from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.journal_expression_data_table import JournalExpressionDataTable
from openapi_server import util


async def get_journal_expression_schema(request: web.Request, authorization, api_version) -> web.Response:
    """Gets the journal expression data schema

    Gets the data schema for all available journal expression values. Includes table names, column names and data types.

    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)
