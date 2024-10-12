from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_kb_dto import CreateKbDTO
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.knowledgebase_dto import KnowledgebaseDTO
from openapi_server.models.knowledgebases_dto import KnowledgebasesDTO
from openapi_server.models.operation import Operation
from openapi_server.models.qn_a_documents_dto import QnADocumentsDTO
from openapi_server.models.replace_kb_dto import ReplaceKbDTO
from openapi_server.models.update_kb_operation_dto import UpdateKbOperationDTO
from openapi_server import util


async def knowledgebase_create(request: web.Request, create_kb_payload) -> web.Response:
    """Asynchronous operation to create a new knowledgebase.

    

    :param create_kb_payload: Post body of the request.
    :type create_kb_payload: dict | bytes

    """
    create_kb_payload = CreateKbDTO.from_dict(create_kb_payload)
    return web.Response(status=200)


async def knowledgebase_delete(request: web.Request, kb_id) -> web.Response:
    """Deletes the knowledgebase and all its data.

    

    :param kb_id: Knowledgebase id.
    :type kb_id: str

    """
    return web.Response(status=200)


async def knowledgebase_download(request: web.Request, kb_id, environment) -> web.Response:
    """Download the knowledgebase.

    

    :param kb_id: Knowledgebase id.
    :type kb_id: str
    :param environment: Specifies whether environment is Test or Prod.
    :type environment: str

    """
    return web.Response(status=200)


async def knowledgebase_get_details(request: web.Request, kb_id) -> web.Response:
    """Gets details of a specific knowledgebase.

    

    :param kb_id: Knowledgebase id.
    :type kb_id: str

    """
    return web.Response(status=200)


async def knowledgebase_list_all(request: web.Request, ) -> web.Response:
    """Gets all knowledgebases for a user.

    


    """
    return web.Response(status=200)


async def knowledgebase_publish(request: web.Request, kb_id) -> web.Response:
    """Publishes all changes in test index of a knowledgebase to its prod index.

    

    :param kb_id: Knowledgebase id.
    :type kb_id: str

    """
    return web.Response(status=200)


async def knowledgebase_replace(request: web.Request, kb_id, replace_kb) -> web.Response:
    """Replace knowledgebase contents.

    

    :param kb_id: Knowledgebase id.
    :type kb_id: str
    :param replace_kb: An instance of ReplaceKbDTO which contains list of qnas to be uploaded
    :type replace_kb: dict | bytes

    """
    replace_kb = ReplaceKbDTO.from_dict(replace_kb)
    return web.Response(status=200)


async def knowledgebase_update(request: web.Request, kb_id, update_kb) -> web.Response:
    """Asynchronous operation to modify a knowledgebase.

    

    :param kb_id: Knowledgebase id.
    :type kb_id: str
    :param update_kb: Post body of the request.
    :type update_kb: dict | bytes

    """
    update_kb = UpdateKbOperationDTO.from_dict(update_kb)
    return web.Response(status=200)
