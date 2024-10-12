from typing import List, Dict
from aiohttp import web

from openapi_server.models.common_language_combination_dto import CommonLanguageCombinationDTO
from openapi_server.models.custom_field_dto import CustomFieldDTO
from openapi_server.models.finance_dto import FinanceDTO
from openapi_server.models.instructions_dto import InstructionsDTO
from openapi_server.models.payable_create_dto import PayableCreateDTO
from openapi_server.models.payable_dto import PayableDTO
from openapi_server.models.quote_dtov1 import QuoteDTOv1
from openapi_server.models.quote_dates_dto import QuoteDatesDTO
from openapi_server.models.receivable_create_dto import ReceivableCreateDTO
from openapi_server.models.receivable_dto import ReceivableDTO
from openapi_server.models.task_dto import TaskDTO
from openapi_server import util


async def create_language_combination1(request: web.Request, quote_id, body) -> web.Response:
    """Creates a new language combination for a given quote without creating a task.

    Creates a new language combination for a given quote without creating a task.

    :param quote_id: quote&#39;s internal identifier
    :type quote_id: str
    :param body: Created a new language combination for a given quote without creating a task.
    :type body: dict | bytes

    """
    body = CommonLanguageCombinationDTO.from_dict(body)
    return web.Response(status=200)


async def create_payable1(request: web.Request, quote_id, body) -> web.Response:
    """Adds a payable.

    Adds a payable.

    :param quote_id: quote&#39;s internal identifier
    :type quote_id: str
    :param body: Adds a payable.
    :type body: dict | bytes

    """
    body = PayableCreateDTO.from_dict(body)
    return web.Response(status=200)


async def create_receivable1(request: web.Request, quote_id, body) -> web.Response:
    """Adds a receivable.

    Adds a receivable.

    :param quote_id: quote&#39;s internal identifier
    :type quote_id: str
    :param body: Adds a receivable.
    :type body: dict | bytes

    """
    body = ReceivableCreateDTO.from_dict(body)
    return web.Response(status=200)


async def create_task1(request: web.Request, quote_id, body) -> web.Response:
    """Creates a new task for a given quote.

    Creates a new task for a given quote. Required fields are presented in the example.

    :param quote_id: quote&#39;s internal identifier
    :type quote_id: str
    :param body: Updated custom fields of a given quote.
    :type body: dict | bytes

    """
    body = TaskDTO.from_dict(body)
    return web.Response(status=200)


async def delete13(request: web.Request, quote_id) -> web.Response:
    """Removes a quote.

    Removes a quote.

    :param quote_id: quote&#39;s internal identifier
    :type quote_id: str

    """
    return web.Response(status=200)


async def delete_payable1(request: web.Request, quote_id, payable_id) -> web.Response:
    """Deletes a payable.

    Deletes a payable.

    :param quote_id: quoteId&#39;s internal identifier
    :type quote_id: str
    :param payable_id: payable&#39;s internal identifier
    :type payable_id: int

    """
    return web.Response(status=200)


async def delete_receivable1(request: web.Request, quote_id, receivable_id) -> web.Response:
    """Deletes a receivable.

    Deletes a receivable.

    :param quote_id: quoteId&#39;s internal identifier
    :type quote_id: str
    :param receivable_id: receivable&#39;s internal identifier
    :type receivable_id: int

    """
    return web.Response(status=200)


async def get_all_ids7(request: web.Request, updated_since=None) -> web.Response:
    """Returns quotes&#39; internal identifiers.

    Returns quotes&#39; internal identifiers.

    :param updated_since: only quotes modified since this timestamp
    :type updated_since: int

    """
    return web.Response(status=200)


async def get_by_id8(request: web.Request, quote_id, embed=None) -> web.Response:
    """Returns quote details.

    Returns quote details. If the specified quote ID refers to Smart Quote, 400 Bad Request is returned instead.

    :param quote_id: quote&#39;s internal identifier
    :type quote_id: str
    :param embed: list of adittional fields which should be embedded in the response (ie. tasks)
    :type embed: str

    """
    return web.Response(status=200)


async def get_custom_fields6(request: web.Request, quote_id) -> web.Response:
    """Returns custom fields of a given quote.

    Returns custom fields of a given quote.

    :param quote_id: quote&#39;s internal identifier
    :type quote_id: str

    """
    return web.Response(status=200)


async def get_dates2(request: web.Request, quote_id) -> web.Response:
    """Returns dates of a given quote.

    Returns dates of a given quote.

    :param quote_id: quote&#39;s internal identifier
    :type quote_id: str

    """
    return web.Response(status=200)


async def get_finance1(request: web.Request, quote_id) -> web.Response:
    """Returns finance of a given quote.

    Returns finance of a given quote.

    :param quote_id: quote&#39;s internal identifier
    :type quote_id: str

    """
    return web.Response(status=200)


async def get_instructions1(request: web.Request, quote_id) -> web.Response:
    """Returns instructions of a given quote.

    Returns instructions of a given quote.

    :param quote_id: quote&#39;s internal identifier
    :type quote_id: str

    """
    return web.Response(status=200)


async def send1(request: web.Request, quote_id) -> web.Response:
    """Sends a quote for customer confirmation.

    Sends a quote for customer confirmation. Quote status is changed to SENT and a document is sent to the customer.

    :param quote_id: quote&#39;s internal identifier
    :type quote_id: str

    """
    return web.Response(status=200)


async def start(request: web.Request, quote_id) -> web.Response:
    """Starts a quote.

    Starts a quote.

    :param quote_id: quote&#39;s internal identifier
    :type quote_id: str

    """
    return web.Response(status=200)


async def update_custom_fields4(request: web.Request, quote_id, body) -> web.Response:
    """Updates custom fields of a given quote.

    Updates custom fields of a given quote.

    :param quote_id: quote&#39;s internal identifier
    :type quote_id: str
    :param body: Updated custom fields of a given quote.

    """
    return web.Response(status=200)


async def update_instructions2(request: web.Request, quote_id, body) -> web.Response:
    """Updates instructions of a given quote.

    Updates instructions of a given quote.

    :param quote_id: quote&#39;s internal identifier
    :type quote_id: str
    :param body: Updated instructions of a given project.
    :type body: dict | bytes

    """
    body = InstructionsDTO.from_dict(body)
    return web.Response(status=200)


async def update_payable1(request: web.Request, quote_id, payable_id, body) -> web.Response:
    """Updates a payable.

    Updates a payable.

    :param quote_id: quote&#39;s internal identifier
    :type quote_id: str
    :param payable_id: payable&#39;s internal identifier
    :type payable_id: int
    :param body: Updates a payable.
    :type body: dict | bytes

    """
    body = PayableDTO.from_dict(body)
    return web.Response(status=200)


async def update_receivable1(request: web.Request, quote_id, receivable_id, body) -> web.Response:
    """Updates a receivable.

    Updates a receivable.

    :param quote_id: quote&#39;s internal identifier
    :type quote_id: str
    :param receivable_id: receivable&#39;s internal identifier
    :type receivable_id: int
    :param body: Updates a receivable.
    :type body: dict | bytes

    """
    body = ReceivableDTO.from_dict(body)
    return web.Response(status=200)
