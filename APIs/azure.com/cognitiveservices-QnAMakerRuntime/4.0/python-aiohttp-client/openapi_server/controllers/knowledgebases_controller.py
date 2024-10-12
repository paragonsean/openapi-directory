from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.feedback_records_dto import FeedbackRecordsDTO
from openapi_server.models.qn_a_search_result_list import QnASearchResultList
from openapi_server.models.query_dto import QueryDTO
from openapi_server import util


async def runtime_generate_answer(request: web.Request, kb_id, generate_answer_payload) -> web.Response:
    """GenerateAnswer call to query the knowledgebase.

    

    :param kb_id: Knowledgebase id.
    :type kb_id: str
    :param generate_answer_payload: Post body of the request.
    :type generate_answer_payload: dict | bytes

    """
    generate_answer_payload = QueryDTO.from_dict(generate_answer_payload)
    return web.Response(status=200)


async def runtime_train(request: web.Request, kb_id, train_payload) -> web.Response:
    """Train call to add suggestions to the knowledgebase.

    

    :param kb_id: Knowledgebase id.
    :type kb_id: str
    :param train_payload: Post body of the request.
    :type train_payload: dict | bytes

    """
    train_payload = FeedbackRecordsDTO.from_dict(train_payload)
    return web.Response(status=200)
